#!/usr/bin/env python3
"""
Manual Test Run - Generate ONE video to check quality
Run this to see the video output before automation
"""

import os
import sys
import json
import time
import requests
from datetime import datetime
from pathlib import Path

# Import quality checkers
from quality_checkers import QualityPipeline

# Configuration from environment
AZURE_API_KEY = os.environ.get('AZURE_OPENAI_API_KEY')
PERPLEXITY_API_KEY = os.environ.get('PERPLEXITY_API_KEY')
ELEVENLABS_API_KEY = os.environ.get('ELEVENLABS_API_KEY')
SYNTHESIA_API_KEY = os.environ.get('SYNTHESIA_API_KEY')

print("=" * 80)
print("AXIA VIDEO - MANUAL TEST RUN")
print("=" * 80)
print()

# Create output directories
output_dir = Path("test_output")
output_dir.mkdir(exist_ok=True)

def call_gpt(prompt: str) -> str:
    """Call GPT for script generation"""
    print("📝 Consulting GPT-5 Pro for script generation...")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AZURE_API_KEY}"
    }

    payload = {
        "messages": [
            {
                "role": "system",
                "content": "You are an expert Arabic copywriter for Axia forex platform. Write in authentic Khaleeji (GCC) dialect."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "model": "gpt-4o",
        "temperature": 0.8,
        "max_tokens": 500
    }

    try:
        response = requests.post(
            "https://models.inference.ai.azure.com/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"❌ Error calling GPT: {e}")
        sys.exit(1)

def get_market_insights() -> str:
    """Get latest market insights from Perplexity"""
    print("📊 Getting market insights from Perplexity...")

    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-sonar-large-128k-online",
        "messages": [
            {
                "role": "user",
                "content": "What are the major forex market moves today? EUR/USD, GBP/USD, USD/JPY. Keep it very brief - 2-3 sentences."
            }
        ]
    }

    try:
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"⚠️  Perplexity unavailable, using fallback: {e}")
        return "Markets showing typical volatility today with major pairs seeing moderate movement."

# Step 1: Get market data
market_data = get_market_insights()
print(f"✅ Market data retrieved")
print(f"   {market_data[:100]}...")
print()

# Step 2: Generate script
print("=" * 80)
print("STEP 1: SCRIPT GENERATION")
print("=" * 80)
print()

script_prompt = f"""Create a 20-second TikTok-style video script in Khaleeji (GCC) Arabic for Axia forex platform.

Today's theme: MARKET OPPORTUNITY
Market context: {market_data}

Requirements:
- Duration: Exactly 20 seconds when spoken (about 50-60 words in Arabic)
- Dialect: Khaleeji Arabic (Gulf dialect) - NOT Modern Standard Arabic
- Structure:
  * 0-3s: HOOK - Bold opening question or statement
  * 3-8s: PROBLEM - Trading challenge or missed opportunity
  * 8-15s: SOLUTION - How Axia helps (bold, action-oriented)
  * 15-20s: CTA + Risk disclosure

Brand Voice (Axia):
- Bold and confident
- Opportunity-focused
- "Endless market opportunities" messaging
- Professional yet energetic

CRITICAL:
- Use authentic Khaleeji dialect (how people speak in UAE/Saudi, not formal Arabic)
- Include risk disclosure: "التداول يحمل مخاطر" or similar
- No guaranteed profit claims
- Make hook attention-grabbing for TikTok

Return ONLY the Arabic script, nothing else. No English translation."""

script = call_gpt(script_prompt)

print("📄 Generated Script:")
print("-" * 80)
print(script)
print("-" * 80)
print()

# Save script
script_file = output_dir / f"script_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(script_file, 'w', encoding='utf-8') as f:
    f.write(script)
print(f"💾 Script saved to: {script_file}")
print()

# Step 3: Quality checks
print("=" * 80)
print("STEP 2: QUALITY VALIDATION")
print("=" * 80)
print()

pipeline = QualityPipeline({
    'arabic_dialect': 85,
    'brand_compliance': 90,
    'regulatory_compliance': 95,
    'tiktok_optimization': 85
})

passed, results = pipeline.check_script(script)

print("\n📊 Quality Scores:")
print("-" * 80)
for i, result in enumerate(results, 1):
    checker_name = type(result).__name__.replace('Checker', '')
    status = "✅ PASS" if result.passed else "❌ FAIL"
    print(f"{i}. {checker_name}: {result.score}/100 (threshold: {result.threshold}) - {status}")

    if not result.passed and result.issues:
        print(f"   Issues: {', '.join(result.issues[:2])}")
    if result.suggestions:
        print(f"   Suggestions: {result.suggestions[0]}")

print("-" * 80)

if passed:
    print("\n✅ All quality checks PASSED!")
else:
    print("\n⚠️  Some quality checks failed - review above")
    print("   This is a test run, so we'll continue anyway")

print()

# Step 4: Generate audio with ElevenLabs
print("=" * 80)
print("STEP 3: AUDIO GENERATION (ElevenLabs)")
print("=" * 80)
print()

print("🎤 Generating Arabic voiceover...")

# Use a pre-configured Arabic voice
# You can get voice IDs from https://elevenlabs.io/app/voice-library
arabic_voice_id = "pNInz6obpgDQGcFmaJgB"  # Example male Arabic voice

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
        "style": 0.60
    }
}

try:
    print(f"   Using voice ID: {arabic_voice_id}")
    response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{arabic_voice_id}",
        headers=headers,
        json=data,
        timeout=120
    )
    response.raise_for_status()

    audio_file = output_dir / f"audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
    with open(audio_file, 'wb') as f:
        f.write(response.content)

    print(f"✅ Audio generated: {audio_file}")

    # Get audio duration
    import subprocess
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
             '-of', 'default=noprint_wrappers=1:nokey=1', str(audio_file)],
            capture_output=True,
            text=True,
            timeout=10
        )
        duration = float(result.stdout.strip())
        print(f"   Duration: {duration:.1f} seconds")

        if duration < 18 or duration > 22:
            print(f"   ⚠️  Duration outside target range (19-21s)")
    except:
        pass

except Exception as e:
    print(f"❌ Audio generation failed: {e}")
    sys.exit(1)

print()

# Step 5: Video generation (Synthesia)
print("=" * 80)
print("STEP 4: VIDEO GENERATION (Synthesia)")
print("=" * 80)
print()

print("🎬 Generating AI avatar video...")
print("   This will take 10-15 minutes...")
print()

headers = {
    "Authorization": SYNTHESIA_API_KEY,
    "Content-Type": "application/json"
}

# Simplified Synthesia request (check actual API docs for exact format)
data = {
    "title": f"Axia Test Video - {datetime.now().strftime('%Y-%m-%d %H:%M')}",
    "description": "Test video for quality review",
    "visibility": "private",
    "aspectRatio": "9:16",  # Vertical for TikTok
    "input": [
        {
            "scriptText": script,
            "avatar": "anna_costume1_cameraA",  # Replace with Arabic avatar ID
            "background": "white",  # Or custom branded background
        }
    ]
}

try:
    # Create video
    print("   Submitting video generation request...")
    response = requests.post(
        "https://api.synthesia.io/v2/videos",
        headers=headers,
        json=data,
        timeout=30
    )
    response.raise_for_status()

    video_id = response.json()['id']
    print(f"   Video ID: {video_id}")
    print(f"   Status: Processing...")

    # Poll for completion
    max_wait = 1200  # 20 minutes
    poll_interval = 30  # Check every 30 seconds
    waited = 0

    while waited < max_wait:
        time.sleep(poll_interval)
        waited += poll_interval

        status_response = requests.get(
            f"https://api.synthesia.io/v2/videos/{video_id}",
            headers=headers,
            timeout=10
        )
        status_response.raise_for_status()
        status = status_response.json()

        current_status = status.get('status', 'unknown')
        print(f"   [{waited//60}min {waited%60}s] Status: {current_status}")

        if current_status == 'complete':
            download_url = status['download']
            print(f"\n✅ Video generation complete!")

            # Download video
            print("   Downloading video...")
            video_response = requests.get(download_url, timeout=300)
            video_response.raise_for_status()

            video_file = output_dir / f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
            with open(video_file, 'wb') as f:
                f.write(video_response.content)

            print(f"✅ Video saved: {video_file}")
            print()

            # Final results
            print("=" * 80)
            print("🎉 VIDEO GENERATION COMPLETE!")
            print("=" * 80)
            print()
            print("📁 Output Files:")
            print(f"   Script: {script_file}")
            print(f"   Audio:  {audio_file}")
            print(f"   Video:  {video_file}")
            print()
            print("👀 NEXT STEPS:")
            print("   1. Watch the video to review quality")
            print("   2. Check Arabic dialect authenticity")
            print("   3. Verify brand voice and compliance")
            print("   4. Provide feedback for improvements")
            print()
            print(f"To play video:")
            print(f"   vlc {video_file}")
            print(f"   # or")
            print(f"   mpv {video_file}")
            print()

            # Quality report
            print("📊 Quality Report:")
            print("-" * 80)
            for result in results:
                checker_name = type(result).__name__.replace('Checker', '')
                print(f"   {checker_name}: {result.score}/100")
            print("-" * 80)
            print()

            sys.exit(0)

        elif current_status == 'failed':
            error_msg = status.get('error', 'Unknown error')
            print(f"\n❌ Video generation failed: {error_msg}")
            sys.exit(1)

    print("\n❌ Video generation timeout (20 minutes)")
    print(f"   Video ID: {video_id}")
    print("   Check Synthesia dashboard for status")
    sys.exit(1)

except Exception as e:
    print(f"\n❌ Video generation error: {e}")
    print("\nNote: This may fail if:")
    print("   - Synthesia API key is invalid")
    print("   - Avatar ID doesn't exist")
    print("   - API format has changed")
    print("\nCheck Synthesia API docs: https://docs.synthesia.io/")
    sys.exit(1)
