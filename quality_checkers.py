#!/usr/bin/env python3
"""
Quality Checkers for Axia Daily Video Automation
Comprehensive validation pipeline for scripts and videos
"""

import os
import json
import cv2
import subprocess
from typing import Dict, List, Tuple
from dataclasses import dataclass
import requests

# API Configuration
AZURE_API_KEY = os.environ.get('AZURE_OPENAI_API_KEY')
AZURE_ENDPOINT = "https://models.inference.ai.azure.com"


@dataclass
class QualityResult:
    """Result from a quality checker"""
    score: int  # 0-100
    passed: bool
    threshold: int
    issues: List[str]
    suggestions: List[str]
    metadata: Dict


class QualityChecker:
    """Base class for all quality checkers"""

    def __init__(self, threshold: int = 85):
        self.threshold = threshold

    def check(self, *args, **kwargs) -> QualityResult:
        """Run the quality check"""
        raise NotImplementedError

    def _call_gpt5_pro(self, prompt: str, temperature: float = 0.3) -> str:
        """Call Azure OpenAI GPT-5 Pro"""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AZURE_API_KEY}"
        }

        payload = {
            "messages": [
                {"role": "system", "content": "You are an expert analyst. Provide detailed, JSON-formatted responses."},
                {"role": "user", "content": prompt}
            ],
            "model": "gpt-4o",
            "temperature": temperature,
            "max_tokens": 4000
        }

        try:
            response = requests.post(
                f"{AZURE_ENDPOINT}/chat/completions",
                headers=headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            raise Exception(f"GPT-5 Pro API error: {str(e)}")


class ArabicDialectChecker(QualityChecker):
    """Checker 1: Validates Khaleeji Arabic dialect accuracy"""

    def __init__(self, threshold: int = 85):
        super().__init__(threshold)
        self.name = "Arabic Dialect Validator"

    def check(self, script: str) -> QualityResult:
        """
        Validates Khaleeji (GCC) Arabic dialect accuracy
        """
        prompt = f"""You are an expert in Khaleeji (GCC) Arabic dialect, spoken in UAE, Saudi Arabia, Kuwait, Qatar, Bahrain, and Oman.

Analyze this Arabic script for a 20-second forex trading video:

{script}

Evaluate:
1. **Dialect Accuracy** (0-100): Is this authentic Khaleeji dialect or Modern Standard Arabic?
2. **Financial Terminology** (0-100): Are financial terms correct in Gulf Arabic?
3. **Cultural Appropriateness** (0-100): Suitable for GCC audience?
4. **Natural Flow** (0-100): Does it sound natural when spoken?

Return ONLY valid JSON:
{{
  "score": <overall 0-100>,
  "dialect_accuracy": <0-100>,
  "terminology": <0-100>,
  "cultural_fit": <0-100>,
  "natural_flow": <0-100>,
  "issues": ["list specific dialect issues"],
  "suggestions": ["specific improvements for Khaleeji dialect"]
}}"""

        try:
            response = self._call_gpt5_pro(prompt, temperature=0.2)
            # Extract JSON from response
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            if json_start >= 0 and json_end > json_start:
                data = json.loads(response[json_start:json_end])
            else:
                data = json.loads(response)

            return QualityResult(
                score=data['score'],
                passed=data['score'] >= self.threshold,
                threshold=self.threshold,
                issues=data.get('issues', []),
                suggestions=data.get('suggestions', []),
                metadata={
                    'dialect_accuracy': data.get('dialect_accuracy', 0),
                    'terminology': data.get('terminology', 0),
                    'cultural_fit': data.get('cultural_fit', 0),
                    'natural_flow': data.get('natural_flow', 0)
                }
            )
        except Exception as e:
            return QualityResult(
                score=0,
                passed=False,
                threshold=self.threshold,
                issues=[f"Checker failed: {str(e)}"],
                suggestions=["Manual review required"],
                metadata={}
            )


class BrandComplianceChecker(QualityChecker):
    """Checker 2: Validates Axia brand voice compliance"""

    def __init__(self, threshold: int = 90):
        super().__init__(threshold)
        self.name = "Brand Compliance Validator"
        self.brand_guidelines = """
Axia Brand Voice:
- Bold and confident
- Opportunity-focused: "Endless market opportunities"
- Action-oriented: Motivate traders to act
- Professional yet energetic
- Empowering: Help traders seize opportunities
- Trustworthy: Emphasize regulation and security

Key Messaging:
1. Endless opportunities
2. Fully regulated
3. Advanced trading tools
4. Global market access
5. Professional support

Tone for Arabic (GCC):
- Formal and respectful
- Emphasize trust and tradition
- Use proper financial terminology
- Avoid gambling references
"""

    def check(self, script: str) -> QualityResult:
        """Validates script against Axia brand guidelines"""

        prompt = f"""You are a brand compliance expert for Axia, a forex trading platform.

Brand Guidelines:
{self.brand_guidelines}

Analyze this script:
{script}

Evaluate:
1. **Voice Match** (0-100): Does it match Axia's bold, opportunity-focused voice?
2. **Key Messaging** (0-100): Are core messages present?
3. **Tone Appropriateness** (0-100): Right balance of professional and energetic?
4. **Action Orientation** (0-100): Does it motivate traders to act?

Return ONLY valid JSON:
{{
  "score": <overall 0-100>,
  "voice_match": <0-100>,
  "messaging": <0-100>,
  "tone": <0-100>,
  "action_orientation": <0-100>,
  "issues": ["specific brand voice mismatches"],
  "suggestions": ["how to better align with Axia brand"]
}}"""

        try:
            response = self._call_gpt5_pro(prompt, temperature=0.2)
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            data = json.loads(response[json_start:json_end])

            return QualityResult(
                score=data['score'],
                passed=data['score'] >= self.threshold,
                threshold=self.threshold,
                issues=data.get('issues', []),
                suggestions=data.get('suggestions', []),
                metadata={
                    'voice_match': data.get('voice_match', 0),
                    'messaging': data.get('messaging', 0),
                    'tone': data.get('tone', 0),
                    'action_orientation': data.get('action_orientation', 0)
                }
            )
        except Exception as e:
            return QualityResult(
                score=0,
                passed=False,
                threshold=self.threshold,
                issues=[f"Checker failed: {str(e)}"],
                suggestions=["Manual review required"],
                metadata={}
            )


class RegulatoryComplianceChecker(QualityChecker):
    """Checker 3: Ensures forex trading regulatory compliance"""

    def __init__(self, threshold: int = 95):
        super().__init__(threshold)
        self.name = "Regulatory Compliance Validator"

    def check(self, script: str) -> QualityResult:
        """Validates regulatory compliance for forex trading"""

        prompt = f"""You are a forex trading compliance expert.

Analyze this script for regulatory compliance:
{script}

REQUIREMENTS (MUST INCLUDE):
- Risk disclosure: Trading carries risks
- No guaranteed profit claims
- Acknowledge possible losses
- Platform is regulated (if space allows)

PROHIBITED (MUST NOT INCLUDE):
- "Get rich quick" language
- Guaranteed returns or profits
- No-risk promises
- Excessive pressure tactics
- Misleading claims

Evaluate:
1. **Risk Disclosure** (present/absent): Is risk mentioned?
2. **Prohibited Claims** (list any): Any forbidden statements?
3. **Overall Compliance** (0-100): Meets regulatory standards?

Return ONLY valid JSON:
{{
  "score": <0-100, use 0 if prohibited claims found>,
  "compliant": <true/false>,
  "risk_disclosure_present": <true/false>,
  "prohibited_claims": ["list exact phrases that violate regulations"],
  "missing_elements": ["required elements not present"],
  "severity": "none|low|medium|high|critical"
}}"""

        try:
            response = self._call_gpt5_pro(prompt, temperature=0.1)
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            data = json.loads(response[json_start:json_end])

            # Hard fail on prohibited claims
            if data.get('prohibited_claims') and len(data['prohibited_claims']) > 0:
                data['score'] = 0
                data['compliant'] = False
                data['severity'] = 'critical'

            return QualityResult(
                score=data['score'],
                passed=data['score'] >= self.threshold and data['compliant'],
                threshold=self.threshold,
                issues=data.get('prohibited_claims', []) + data.get('missing_elements', []),
                suggestions=["Ensure risk disclosure is clear and present", "Remove any guaranteed profit language"],
                metadata={
                    'compliant': data.get('compliant', False),
                    'risk_disclosure_present': data.get('risk_disclosure_present', False),
                    'severity': data.get('severity', 'unknown')
                }
            )
        except Exception as e:
            return QualityResult(
                score=0,
                passed=False,
                threshold=self.threshold,
                issues=[f"Checker failed: {str(e)}"],
                suggestions=["Manual compliance review required"],
                metadata={'compliant': False, 'severity': 'unknown'}
            )


class TikTokOptimizationChecker(QualityChecker):
    """Checker 4: Validates TikTok/YouTube Shorts optimization"""

    def __init__(self, threshold: int = 85):
        super().__init__(threshold)
        self.name = "TikTok Optimization Validator"

    def check(self, script: str) -> QualityResult:
        """Validates TikTok engagement optimization"""

        prompt = f"""You are a TikTok content optimization expert.

Analyze this 20-second video script for TikTok/YouTube Shorts:

{script}

Expected Structure:
- 0:00-0:03 (3s): HOOK - Eye-catching opening
- 0:03-0:08 (5s): PROBLEM - Challenge or opportunity
- 0:08-0:15 (7s): SOLUTION - How Axia helps
- 0:15-0:20 (5s): CTA - Call to action

Evaluate:
1. **Hook Strength** (0-100): Does first 3s grab attention?
2. **Problem Clarity** (0-100): Clear pain point or opportunity?
3. **Solution Impact** (0-100): Compelling solution presentation?
4. **CTA Urgency** (0-100): Strong, clear call-to-action?
5. **Pacing** (fast/medium/slow): Appropriate for TikTok?
6. **Predicted Engagement** (0-100): Likely to perform well?

Return ONLY valid JSON:
{{
  "score": <overall 0-100>,
  "hook_strength": <0-100>,
  "problem_clarity": <0-100>,
  "solution_impact": <0-100>,
  "cta_urgency": <0-100>,
  "pacing": "fast|medium|slow",
  "predicted_engagement": <0-100>,
  "issues": ["specific optimization issues"],
  "suggestions": ["improvements for better engagement"]
}}"""

        try:
            response = self._call_gpt5_pro(prompt, temperature=0.5)
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            data = json.loads(response[json_start:json_end])

            return QualityResult(
                score=data['score'],
                passed=data['score'] >= self.threshold,
                threshold=self.threshold,
                issues=data.get('issues', []),
                suggestions=data.get('suggestions', []),
                metadata={
                    'hook_strength': data.get('hook_strength', 0),
                    'problem_clarity': data.get('problem_clarity', 0),
                    'solution_impact': data.get('solution_impact', 0),
                    'cta_urgency': data.get('cta_urgency', 0),
                    'pacing': data.get('pacing', 'unknown'),
                    'predicted_engagement': data.get('predicted_engagement', 0)
                }
            )
        except Exception as e:
            return QualityResult(
                score=0,
                passed=False,
                threshold=self.threshold,
                issues=[f"Checker failed: {str(e)}"],
                suggestions=["Manual optimization review required"],
                metadata={}
            )


class VisualQualityChecker(QualityChecker):
    """Checker 5: Validates video technical quality"""

    def __init__(self, threshold: int = 90):
        super().__init__(threshold)
        self.name = "Visual Quality Validator"

    def check(self, video_path: str) -> QualityResult:
        """Validates video technical specifications"""

        if not os.path.exists(video_path):
            return QualityResult(
                score=0,
                passed=False,
                threshold=self.threshold,
                issues=[f"Video file not found: {video_path}"],
                suggestions=["Ensure video generation completed successfully"],
                metadata={}
            )

        try:
            # Get video properties using OpenCV
            video = cv2.VideoCapture(video_path)

            width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(video.get(cv2.CAP_PROP_FPS))
            frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            duration = frame_count / fps if fps > 0 else 0

            video.release()

            # Get bitrate using ffprobe
            try:
                cmd = [
                    'ffprobe', '-v', 'error',
                    '-show_entries', 'format=bit_rate',
                    '-of', 'default=noprint_wrappers=1:nokey=1',
                    video_path
                ]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                bitrate = float(result.stdout.strip()) / 1_000_000  # Convert to Mbps
            except:
                bitrate = 0

            # Validate specs
            issues = []
            score = 100

            # Resolution check (1080x1920 for vertical)
            if width != 1080 or height != 1920:
                issues.append(f"Resolution {width}x{height}, expected 1080x1920")
                score -= 30

            # FPS check (minimum 30)
            if fps < 30:
                issues.append(f"FPS {fps}, expected 30+")
                score -= 20

            # Duration check (19-21 seconds)
            if duration < 19 or duration > 21:
                issues.append(f"Duration {duration:.1f}s, expected 19-21s")
                score -= 15

            # Bitrate check (minimum 5 Mbps)
            if bitrate > 0 and bitrate < 5:
                issues.append(f"Bitrate {bitrate:.1f}Mbps, expected 5+")
                score -= 15

            suggestions = []
            if score < self.threshold:
                suggestions.append("Re-generate video with correct specifications")
                if width != 1080 or height != 1920:
                    suggestions.append("Ensure video generation uses 1080x1920 resolution")
                if fps < 30:
                    suggestions.append("Increase frame rate to 30fps minimum")

            return QualityResult(
                score=max(0, score),
                passed=score >= self.threshold,
                threshold=self.threshold,
                issues=issues,
                suggestions=suggestions,
                metadata={
                    'resolution': f"{width}x{height}",
                    'fps': fps,
                    'duration': round(duration, 2),
                    'bitrate_mbps': round(bitrate, 2) if bitrate > 0 else 'unknown'
                }
            )

        except Exception as e:
            return QualityResult(
                score=0,
                passed=False,
                threshold=self.threshold,
                issues=[f"Video analysis failed: {str(e)}"],
                suggestions=["Ensure video file is valid and accessible"],
                metadata={}
            )


class QualityPipeline:
    """Orchestrates all quality checkers"""

    def __init__(self, config: Dict = None):
        if config is None:
            config = {}

        # Initialize all checkers with thresholds from config
        self.script_checkers = [
            ArabicDialectChecker(threshold=config.get('arabic_dialect', 85)),
            BrandComplianceChecker(threshold=config.get('brand_compliance', 90)),
            RegulatoryComplianceChecker(threshold=config.get('regulatory_compliance', 95)),
            TikTokOptimizationChecker(threshold=config.get('tiktok_optimization', 85))
        ]

        self.video_checkers = [
            VisualQualityChecker(threshold=config.get('visual_quality', 90))
        ]

    def check_script(self, script: str) -> Tuple[bool, List[QualityResult]]:
        """
        Run all script-level quality checks
        Returns: (all_passed, list_of_results)
        """
        results = []
        all_passed = True

        for checker in self.script_checkers:
            print(f"  Running {checker.name}...")
            result = checker.check(script)
            results.append(result)

            if not result.passed:
                all_passed = False
                print(f"    ❌ Failed: {result.score}/{result.threshold}")
            else:
                print(f"    ✅ Passed: {result.score}/{result.threshold}")

        return all_passed, results

    def check_video(self, video_path: str) -> Tuple[bool, List[QualityResult]]:
        """
        Run all video-level quality checks
        Returns: (all_passed, list_of_results)
        """
        results = []
        all_passed = True

        for checker in self.video_checkers:
            print(f"  Running {checker.name}...")
            result = checker.check(video_path)
            results.append(result)

            if not result.passed:
                all_passed = False
                print(f"    ❌ Failed: {result.score}/{result.threshold}")
            else:
                print(f"    ✅ Passed: {result.score}/{result.threshold}")

        return all_passed, results


# Test function
if __name__ == "__main__":
    print("Testing Quality Checkers...")
    print("=" * 60)

    # Test Arabic script
    test_script_arabic = """
السلام عليكم! هل تفوتك فرص التداول؟

الأسواق تتحرك كل يوم، والفرص لا تنتظر أحد.

مع أكسيا، تداول بثقة على منصة مرخصة ومنظمة.

ابدأ اليوم - axia.trade

⚠️ التداول يحمل مخاطر
"""

    pipeline = QualityPipeline()

    print("\n📝 Testing Script Quality Checks...")
    print("-" * 60)
    passed, results = pipeline.check_script(test_script_arabic)

    print("\n" + "=" * 60)
    print(f"Overall Result: {'✅ PASSED' if passed else '❌ FAILED'}")
    print("=" * 60)

    for i, result in enumerate(results, 1):
        print(f"\nChecker {i}: Score {result.score}/100 (threshold: {result.threshold})")
        if result.issues:
            print("  Issues:", result.issues)
        if result.suggestions:
            print("  Suggestions:", result.suggestions)
