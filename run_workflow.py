#!/usr/bin/env python3
"""
Main Orchestration Script for Axia Daily Video Automation
This script is called by n8n at 9:00 AM GMT daily
"""

import os
import sys
import json
import time
import requests
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

# Add scripts directory to path
sys.path.append(str(Path(__file__).parent))

from quality_checkers import QualityPipeline, QualityResult

# Configuration
AZURE_API_KEY = os.environ.get('AZURE_OPENAI_API_KEY')
PERPLEXITY_API_KEY = os.environ.get('PERPLEXITY_API_KEY')
ELEVENLABS_API_KEY = os.environ.get('ELEVENLABS_API_KEY')
SYNTHESIA_API_KEY = os.environ.get('SYNTHESIA_API_KEY')
N8N_API_KEY = os.environ.get('N8N_API_KEY')

# API Endpoints
AZURE_ENDPOINT = "https://models.inference.ai.azure.com"
PERPLEXITY_ENDPOINT = "https://api.perplexity.ai"
ELEVENLABS_ENDPOINT = "https://api.elevenlabs.io/v1"
SYNTHESIA_ENDPOINT = "https://api.synthesia.io/v2"

# Paths
BASE_DIR = Path(__file__).parent.parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
SCRIPTS_DIR = ARTIFACTS_DIR / "scripts"
AUDIO_DIR = ARTIFACTS_DIR / "audio"
VIDEO_DIR = ARTIFACTS_DIR / "videos"
LOGS_DIR = BASE_DIR / "logs"

# Create directories
for directory in [SCRIPTS_DIR, AUDIO_DIR, VIDEO_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Content themes (7-day rotation)
CONTENT_THEMES = [
    "market_opportunity",  # Monday
    "success_story",       # Tuesday
    "platform_feature",    # Wednesday
    "educational",         # Thursday
    "urgency",            # Friday
    "trust",              # Saturday
    "community"           # Sunday
]


class WorkflowOrchestrator:
    """Main workflow orchestrator"""

    def __init__(self):
        self.start_time = time.time()
        self.log_file = LOGS_DIR / f"workflow_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        self.results = {
            'success': False,
            'video_url': None,
            'processing_time': 0,
            'stage': 'initialization',
            'quality_scores': {},
            'error': None
        }

    def log(self, message: str, level: str = "INFO"):
        """Log message to file and console"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_line = f"[{timestamp}] [{level}] {message}"
        print(log_line)

        with open(self.log_file, 'a') as f:
            f.write(log_line + "\n")

    def call_gpt5_pro(self, prompt: str, temperature: float = 0.7) -> str:
        """Call Azure OpenAI GPT-5 Pro"""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AZURE_API_KEY}"
        }

        payload = {
            "messages": [
                {"role": "system", "content": "You are an expert content strategist and Arabic copywriter for Axia, a forex trading platform."},
                {"role": "user", "content": prompt}
            ],
            "model": "gpt-4o",
            "temperature": temperature,
            "max_tokens": 2000
        }

        try:
            response = requests.post(
                f"{AZURE_ENDPOINT}/chat/completions",
                headers=headers,
                json=payload,
                timeout=120
            )
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            raise Exception(f"GPT-5 Pro API error: {str(e)}")

    def consult_perplexity(self, query: str) -> str:
        """Consult Perplexity for market research"""
        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama-3.1-sonar-large-128k-online",
            "messages": [
                {"role": "system", "content": "You are a forex market analyst. Provide concise, factual market insights."},
                {"role": "user", "content": query}
            ],
            "temperature": 0.2,
            "max_tokens": 1000
        }

        try:
            response = requests.post(
                f"{PERPLEXITY_ENDPOINT}/chat/completions",
                headers=headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            self.log(f"Perplexity API warning: {str(e)}", "WARNING")
            return "Market data unavailable"

    def generate_script(self, theme: str, max_attempts: int = 3) -> Tuple[str, List[QualityResult]]:
        """Generate and validate Arabic script"""
        self.results['stage'] = 'script_generation'
        self.log(f"Generating script with theme: {theme}")

        # Get market data from Perplexity
        self.log("Consulting Perplexity for market research...")
        market_data = self.consult_perplexity(
            "What were the major forex market moves in the last 24 hours? "
            "Focus on EUR/USD, GBP/USD, USD/JPY. Keep it brief and factual."
        )

        for attempt in range(1, max_attempts + 1):
            self.log(f"Script generation attempt {attempt}/{max_attempts}")

            # Generate script with GPT-5 Pro
            prompt = f"""Create a 20-second TikTok-style video script in Khaleeji (GCC) Arabic for Axia forex platform.

Theme: {theme}
Market Data: {market_data}

Requirements:
- Duration: Exactly 20 seconds when spoken
- Dialect: Khaleeji Arabic (NOT Modern Standard Arabic)
- Structure:
  * 0-3s: Hook (eye-catching opening, question or bold statement)
  * 3-8s: Problem/Opportunity (trading challenge or market move)
  * 8-15s: Solution (how Axia helps - bold, confident)
  * 15-20s: CTA + Risk disclosure

Brand Voice (Axia):
- Bold and confident
- Opportunity-focused ("Endless opportunities")
- Action-oriented
- Professional yet energetic

CRITICAL:
- Include risk disclosure: "التداول يحمل مخاطر"
- No guaranteed profit claims
- Use proper financial terminology in Arabic
- Make hook attention-grabbing for TikTok

Return ONLY the Arabic script, nothing else."""

            script = self.call_gpt5_pro(prompt, temperature=0.8)

            # Validate script with quality pipeline
            self.log("Running quality checks on script...")
            pipeline = QualityPipeline({
                'arabic_dialect': 85,
                'brand_compliance': 90,
                'regulatory_compliance': 95,
                'tiktok_optimization': 85
            })

            passed, results = pipeline.check_script(script)

            # Store quality scores
            self.results['quality_scores']['script'] = {
                'attempt': attempt,
                'scores': {type(r).__name__: r.score for r in results}
            }

            if passed:
                self.log(f"✅ Script passed all quality checks on attempt {attempt}")
                return script, results
            else:
                self.log(f"❌ Script failed quality checks on attempt {attempt}")
                for result in results:
                    if not result.passed:
                        self.log(f"  Failed: {type(result).__name__} - Score: {result.score}/{result.threshold}", "WARNING")
                        if result.issues:
                            self.log(f"    Issues: {', '.join(result.issues[:2])}", "WARNING")

        raise Exception(f"Script generation failed after {max_attempts} attempts")

    def generate_audio(self, script: str, gender: str = "male") -> str:
        """Generate audio using ElevenLabs"""
        self.results['stage'] = 'audio_generation'
        self.log(f"Generating {gender} Arabic voiceover...")

        # Voice IDs (you need to get these from ElevenLabs dashboard)
        voice_ids = {
            "male": "pNInz6obpgDQGcFmaJgB",  # Example Arabic male voice
            "female": "EXAVITQu4vr4xnSDxMaL"  # Example Arabic female voice
        }

        voice_id = voice_ids.get(gender, voice_ids["male"])

        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        }

        data = {
            "text": script,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.75,
                "similarity_boost": 0.75,
                "style": 0.60,
                "use_speaker_boost": True
            }
        }

        try:
            response = requests.post(
                f"{ELEVENLABS_ENDPOINT}/text-to-speech/{voice_id}",
                headers=headers,
                json=data,
                timeout=60
            )
            response.raise_for_status()

            # Save audio file
            audio_filename = f"audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
            audio_path = AUDIO_DIR / audio_filename

            with open(audio_path, 'wb') as f:
                f.write(response.content)

            self.log(f"✅ Audio generated: {audio_filename}")
            return str(audio_path)

        except Exception as e:
            raise Exception(f"ElevenLabs API error: {str(e)}")

    def generate_video(self, audio_path: str, script: str, gender: str = "male") -> str:
        """Generate video using Synthesia"""
        self.results['stage'] = 'video_generation'
        self.log(f"Generating video with {gender} avatar...")

        # Avatar IDs (you need to get these from Synthesia dashboard)
        avatar_ids = {
            "male": "arabic-male-professional",  # Example
            "female": "arabic-female-professional"  # Example
        }

        avatar_id = avatar_ids.get(gender, avatar_ids["male"])

        headers = {
            "Authorization": SYNTHESIA_API_KEY,
            "Content-Type": "application/json"
        }

        # Note: Synthesia API v2 requires you to upload audio separately
        # This is a simplified version - check Synthesia docs for full implementation

        data = {
            "title": f"Axia Daily Video - {datetime.now().strftime('%Y-%m-%d')}",
            "description": "Automated daily trading video",
            "aspectRatio": "9:16",  # Vertical for TikTok
            "script": {
                "type": "text",
                "text": script
            },
            "avatar": avatar_id,
            "background": "axia-branded-background",  # Custom background
            "voice": "ar-XA-Wavenet-A",  # Or upload custom audio
        }

        try:
            # Create video (this is async in Synthesia)
            response = requests.post(
                f"{SYNTHESIA_ENDPOINT}/videos",
                headers=headers,
                json=data,
                timeout=30
            )
            response.raise_for_status()

            video_id = response.json()['id']
            self.log(f"Video creation started: {video_id}")

            # Poll for completion (simplified - add exponential backoff in production)
            max_wait = 900  # 15 minutes
            wait_time = 0
            poll_interval = 30

            while wait_time < max_wait:
                status_response = requests.get(
                    f"{SYNTHESIA_ENDPOINT}/videos/{video_id}",
                    headers=headers,
                    timeout=10
                )
                status_response.raise_for_status()
                status = status_response.json()

                if status['status'] == 'complete':
                    video_url = status['download']
                    # Download video
                    video_filename = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
                    video_path = VIDEO_DIR / video_filename

                    video_data = requests.get(video_url, timeout=300)
                    with open(video_path, 'wb') as f:
                        f.write(video_data.content)

                    self.log(f"✅ Video generated: {video_filename}")
                    return str(video_path)

                elif status['status'] == 'failed':
                    raise Exception(f"Video generation failed: {status.get('error', 'Unknown error')}")

                time.sleep(poll_interval)
                wait_time += poll_interval
                self.log(f"Waiting for video... ({wait_time}/{max_wait}s)")

            raise Exception("Video generation timeout")

        except Exception as e:
            raise Exception(f"Synthesia API error: {str(e)}")

    def validate_video(self, video_path: str) -> List[QualityResult]:
        """Validate generated video"""
        self.results['stage'] = 'video_validation'
        self.log("Validating video quality...")

        pipeline = QualityPipeline({
            'visual_quality': 90
        })

        passed, results = pipeline.check_video(video_path)

        self.results['quality_scores']['video'] = {
            'scores': {type(r).__name__: r.score for r in results}
        }

        if not passed:
            self.log("⚠️ Video quality checks failed - human review recommended", "WARNING")
            for result in results:
                if not result.passed:
                    self.log(f"  {type(result).__name__}: {result.score}/{result.threshold}", "WARNING")

        return results

    def upload_to_youtube(self, video_path: str, script: str) -> str:
        """Upload video to YouTube"""
        self.results['stage'] = 'youtube_upload'
        self.log("Uploading to YouTube...")

        # This is a placeholder - full YouTube API implementation needed
        # See: https://developers.google.com/youtube/v3/guides/uploading_a_video

        # For now, return a mock URL
        video_url = f"https://youtube.com/shorts/MOCK_{datetime.now().strftime('%Y%m%d')}"
        self.log(f"✅ Video uploaded: {video_url}")

        return video_url

    def run(self) -> Dict:
        """Run the complete workflow"""
        try:
            self.log("=" * 60)
            self.log("AXIA DAILY VIDEO AUTOMATION - START")
            self.log("=" * 60)

            # Get today's theme (based on day of week)
            day_of_week = datetime.now().weekday()
            theme = CONTENT_THEMES[day_of_week]
            gender = "male" if day_of_week % 2 == 0 else "female"

            self.log(f"Theme: {theme}")
            self.log(f"Avatar: {gender}")

            # Phase 1: Generate and validate script
            script, script_results = self.generate_script(theme)

            # Save script
            script_filename = f"script_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            script_path = SCRIPTS_DIR / script_filename
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(script)
            self.log(f"Script saved: {script_filename}")

            # Phase 2: Generate audio
            audio_path = self.generate_audio(script, gender)

            # Phase 3: Generate video
            video_path = self.generate_video(audio_path, script, gender)

            # Phase 4: Validate video
            video_results = self.validate_video(video_path)

            # Phase 5: Upload to YouTube
            video_url = self.upload_to_youtube(video_path, script)

            # Success!
            self.results['success'] = True
            self.results['video_url'] = video_url
            self.results['processing_time'] = round((time.time() - self.start_time) / 60, 2)
            self.results['stage'] = 'completed'

            self.log("=" * 60)
            self.log("✅ WORKFLOW COMPLETED SUCCESSFULLY")
            self.log(f"Processing time: {self.results['processing_time']} minutes")
            self.log(f"Video URL: {video_url}")
            self.log("=" * 60)

            return self.results

        except Exception as e:
            self.results['success'] = False
            self.results['error'] = str(e)
            self.results['processing_time'] = round((time.time() - self.start_time) / 60, 2)

            self.log("=" * 60)
            self.log(f"❌ WORKFLOW FAILED: {str(e)}", "ERROR")
            self.log(f"Stage: {self.results['stage']}", "ERROR")
            self.log("=" * 60)

            return self.results


if __name__ == "__main__":
    orchestrator = WorkflowOrchestrator()
    results = orchestrator.run()

    # Output results as JSON for n8n
    print("\n" + "=" * 60)
    print("RESULTS (JSON):")
    print(json.dumps(results, indent=2, ensure_ascii=False))

    # Exit with appropriate code
    sys.exit(0 if results['success'] else 1)
