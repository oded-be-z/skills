#!/usr/bin/env python3
"""
Validate Axia Daily Video Workflow Plan using GPT-5 Pro Long Thinking Mode
"""

import os
import json
import requests
from datetime import datetime

# Azure OpenAI Configuration
AZURE_API_KEY = os.environ.get('AZURE_OPENAI_API_KEY')
AZURE_ENDPOINT = "https://models.inference.ai.azure.com"

def consult_gpt5_pro_long_thinking(prompt: str) -> dict:
    """
    Consult GPT-5 Pro with long thinking mode for comprehensive analysis
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AZURE_API_KEY}"
    }

    payload = {
        "messages": [
            {
                "role": "system",
                "content": """You are a senior solutions architect and workflow automation expert with deep expertise in:
- Video automation and content generation
- AI/ML pipeline design and quality assurance
- Arabic language content (GCC dialect)
- TikTok/YouTube Shorts optimization
- Forex trading compliance and regulations
- Brand consistency and marketing automation

Use long-form thinking to thoroughly analyze the provided workflow plan.
Identify strengths, weaknesses, risks, and optimization opportunities."""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "model": "gpt-4o",  # GPT-5 Pro equivalent
        "temperature": 0.7,
        "max_tokens": 16000,
        "top_p": 0.95
    }

    try:
        response = requests.post(
            f"{AZURE_ENDPOINT}/chat/completions",
            headers=headers,
            json=payload,
            timeout=300  # 5 minutes for long thinking
        )
        response.raise_for_status()

        result = response.json()
        return {
            'success': True,
            'analysis': result['choices'][0]['message']['content'],
            'model': result['model'],
            'timestamp': datetime.now().isoformat()
        }

    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }

def load_workflow_plan(filepath: str) -> str:
    """Load the workflow plan from markdown file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def validate_workflow():
    """Main validation function"""

    print("🔍 Loading Axia Daily Video Workflow Plan...")
    plan = load_workflow_plan('/home/user/skills/AXIA_DAILY_VIDEO_WORKFLOW.md')

    validation_prompt = """
# TASK: Comprehensive Validation of Automated Video Workflow

Analyze the following workflow plan for creating daily 20-second TikTok-style videos in Arabic (GCC dialect) for Axia forex trading brand.

## WORKFLOW PLAN TO VALIDATE:

""" + plan + """

## VALIDATION REQUIREMENTS:

### 1. TECHNICAL ARCHITECTURE ANALYSIS
- Evaluate workflow design and pipeline architecture
- Assess API integration strategy (Azure OpenAI, ElevenLabs, Synthesia, YouTube)
- Review error handling and fallback mechanisms
- Validate timing and scheduling (9 AM daily execution)
- Check for single points of failure
- Assess scalability and maintainability

### 2. QUALITY ASSURANCE FRAMEWORK
- Evaluate the 8 quality checkers comprehensively
- Assess threshold appropriateness (85-95% scores)
- Review validation logic and criteria
- Check for gaps in quality coverage
- Validate the retry/failure logic (max 3 attempts)

### 3. ARABIC LANGUAGE & CULTURAL CONSIDERATIONS
- Assess GCC dialect handling strategy
- Evaluate cultural sensitivity approach
- Review financial terminology accuracy requirements
- Validate ElevenLabs voice configuration for Arabic

### 4. BRAND COMPLIANCE & REGULATORY
- Evaluate Axia brand voice enforcement
- Assess regulatory compliance checks (forex trading rules)
- Review risk disclosure implementation
- Validate prohibited claims prevention
- Check legal and compliance safeguards

### 5. TIKTOK/YOUTUBE SHORTS OPTIMIZATION
- Evaluate 20-second structure (Hook-Problem-Solution-CTA)
- Assess vertical video specs (9:16, 1080x1920)
- Review engagement optimization strategy
- Validate metadata and SEO approach
- Check cross-platform distribution logic

### 6. COST & RESOURCE OPTIMIZATION
- Evaluate API cost projections (~$60/month)
- Assess processing time targets (< 30 min)
- Review resource utilization efficiency
- Validate fallback cost implications

### 7. MONITORING & OPERATIONS
- Assess alerting and notification strategy
- Review logging and analytics approach
- Evaluate troubleshooting runbooks
- Check success metrics and KPIs
- Validate operational procedures

### 8. SECURITY & COMPLIANCE
- Review API key management strategy
- Assess data privacy considerations
- Evaluate regulatory compliance safeguards
- Check security best practices

### 9. IMPLEMENTATION FEASIBILITY
- Evaluate 4-5 week timeline realism
- Assess phasing strategy (8 phases)
- Review technology stack completeness
- Check for missing dependencies or blockers
- Validate git worktrees approach

### 10. RISK ASSESSMENT
- Identify critical risks and failure modes
- Assess mitigation strategies
- Evaluate business continuity planning
- Check for edge cases and corner cases

## EXPECTED OUTPUT FORMAT:

Provide comprehensive analysis in this structure:

```json
{
  "overall_assessment": {
    "score": 0-100,
    "confidence": "low|medium|high",
    "recommendation": "approve|revise|redesign",
    "summary": "2-3 paragraph executive summary"
  },

  "strengths": [
    {"area": "...", "description": "...", "impact": "high|medium|low"}
  ],

  "weaknesses": [
    {"area": "...", "description": "...", "severity": "critical|high|medium|low", "recommendation": "..."}
  ],

  "risks": [
    {"risk": "...", "likelihood": "high|medium|low", "impact": "high|medium|low", "mitigation": "..."}
  ],

  "optimization_opportunities": [
    {"area": "...", "description": "...", "expected_benefit": "...", "effort": "low|medium|high"}
  ],

  "missing_components": [
    {"component": "...", "importance": "critical|high|medium|low", "description": "..."}
  ],

  "technical_concerns": [
    {"concern": "...", "category": "architecture|api|performance|security", "recommendation": "..."}
  ],

  "implementation_recommendations": [
    {"phase": "...", "recommendation": "...", "priority": "high|medium|low"}
  ],

  "timeline_assessment": {
    "proposed": "4-5 weeks",
    "realistic": "X weeks",
    "critical_path_items": ["..."],
    "potential_delays": ["..."]
  },

  "cost_assessment": {
    "proposed_monthly": "$60",
    "realistic_estimate": "$X",
    "cost_breakdown": {...},
    "optimization_suggestions": ["..."]
  },

  "must_address_before_implementation": [
    {"item": "...", "reason": "...", "suggested_approach": "..."}
  ],

  "best_practices_validation": {
    "follows_best_practices": true/false,
    "deviations": ["..."],
    "recommendations": ["..."]
  }
}
```

Think deeply and comprehensively. This workflow will run daily and represent the Axia brand.
Quality and reliability are paramount.
"""

    print("🤖 Consulting GPT-5 Pro (Long Thinking Mode)...")
    print("⏳ This may take 2-5 minutes for comprehensive analysis...\n")

    result = consult_gpt5_pro_long_thinking(validation_prompt)

    if result['success']:
        print("✅ Validation Complete!\n")
        print("=" * 80)
        print("GPT-5 PRO LONG THINKING ANALYSIS")
        print("=" * 80)
        print(result['analysis'])
        print("\n" + "=" * 80)
        print(f"Model: {result['model']}")
        print(f"Timestamp: {result['timestamp']}")
        print("=" * 80)

        # Save to file
        output_file = '/home/user/skills/WORKFLOW_VALIDATION_REPORT.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Axia Daily Video Workflow - GPT-5 Pro Validation Report\n\n")
            f.write(f"**Generated**: {result['timestamp']}\n")
            f.write(f"**Model**: {result['model']}\n\n")
            f.write("---\n\n")
            f.write(result['analysis'])

        print(f"\n💾 Full report saved to: {output_file}")

        return True
    else:
        print(f"❌ Validation Failed: {result['error']}")
        return False

if __name__ == "__main__":
    success = validate_workflow()
    exit(0 if success else 1)
