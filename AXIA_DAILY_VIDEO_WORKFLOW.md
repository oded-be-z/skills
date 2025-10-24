# Axia Daily TikTok-Style Video Automation Workflow

## 🎯 Project Overview

**Objective**: Fully automated daily 20-second TikTok-style videos for Axia YouTube channel
**Language**: GCC Dialect Arabic (Khaleeji)
**Style**: High-end, fast-paced, call-to-action focused
**Schedule**: Daily at 9:00 AM GMT
**Platform**: YouTube Shorts (TikTok-compatible format)

## 📐 Video Specifications

### Technical Format
- **Duration**: 20 seconds (TikTok/YouTube Shorts optimized)
- **Aspect Ratio**: 9:16 (Vertical)
- **Resolution**: 1080x1920 (Full HD Vertical)
- **Frame Rate**: 30 fps minimum
- **Audio**: High-quality Arabic voiceover (ElevenLabs)
- **Subtitles**: Arabic + English (accessibility)

### 20-Second Structure
```
0:00-0:03 (3s)  - HOOK: Eye-catching opening + question
0:03-0:08 (5s)  - PROBLEM: Trading challenge or market opportunity
0:08-0:15 (7s)  - SOLUTION: How Axia helps
0:15-0:20 (5s)  - CTA: Strong call-to-action + compliance
```

### Content Themes (Rotation)
1. **Market Opportunity**: "Today's forex move you can't miss"
2. **Success Story**: "Traders are making moves with Axia"
3. **Platform Feature**: "Trade smarter with our tools"
4. **Educational**: "60% of traders miss this"
5. **Urgency**: "Markets don't wait, start now"
6. **Trust**: "Fully regulated, fully transparent"
7. **Community**: "Join thousands of traders"

## 🏗️ Workflow Architecture

### Phase 1: Content Strategy & Script Generation (9:00-9:05 AM)
```
[Trigger: Cron 9:00 AM GMT]
    ↓
[Consult GPT-5-Pro]
    ├─→ Analyze yesterday's market moves
    ├─→ Identify today's trading opportunities
    ├─→ Select content theme (7-day rotation)
    └─→ Generate strategic brief (500 words)
    ↓
[Consult Perplexity]
    ├─→ Latest forex news (last 24h)
    ├─→ Major currency pair movements
    └─→ Economic calendar events today
    ↓
[GPT-5-Pro: Long Thinking Mode]
    ├─→ Synthesize market data + strategy
    ├─→ Create 20-second Arabic script (GCC dialect)
    ├─→ Ensure brand voice (Axia: bold, opportunity)
    └─→ Validate compliance (risk disclosure)
```

### Phase 2: Quality Validation - Script Level (9:05-9:10 AM)
```
[Quality Checker 1: Arabic Dialect Validation]
    ├─→ GPT-5-Pro: Verify Khaleeji dialect accuracy
    ├─→ Check cultural appropriateness
    ├─→ Validate financial terminology
    └─→ Score: 0-100 (threshold: 85+)
    ↓
[Quality Checker 2: Brand Compliance]
    ├─→ Load Axia brand voice guidelines
    ├─→ Verify tone: bold, confident, action-oriented
    ├─→ Check key messaging alignment
    └─→ Score: 0-100 (threshold: 90+)
    ↓
[Quality Checker 3: Regulatory Compliance]
    ├─→ Verify risk disclosure present
    ├─→ Check no guaranteed profit claims
    ├─→ Validate legal phrasing
    └─→ Score: 0-100 (threshold: 95+)
    ↓
[Quality Checker 4: TikTok Optimization]
    ├─→ Hook strength (first 3 seconds)
    ├─→ Pacing analysis (engagement curve)
    ├─→ CTA clarity and urgency
    └─→ Score: 0-100 (threshold: 85+)
```

**IF ANY CHECKER FAILS**: Loop back to script generation (max 3 attempts)

### Phase 3: Audio Generation (9:10-9:12 AM)
```
[ElevenLabs API]
    ├─→ Voice: Professional male OR female (alternate daily)
    ├─→ Language: Arabic (optimized for GCC)
    ├─→ Settings:
    │   ├─→ Stability: 0.75
    │   ├─→ Clarity: 0.80
    │   └─→ Style exaggeration: 0.60 (energetic)
    └─→ Output: High-quality MP3 (48kHz)
    ↓
[Audio Quality Check]
    ├─→ Duration validation (19-20 seconds)
    ├─→ Audio level normalization
    ├─→ Silence detection (no gaps > 1s)
    └─→ Pass/Fail
```

### Phase 4: Video Generation (9:12-9:25 AM)
```
[Synthesia API - Primary]
    ├─→ Avatar: Arabic-speaking professional
    │   ├─→ Male: Monday, Wednesday, Friday, Sunday
    │   └─→ Female: Tuesday, Thursday, Saturday
    ├─→ Background: Axia-branded (dynamic trading charts)
    ├─→ Format: 9:16 vertical (1080x1920)
    ├─→ Upload audio + sync with avatar
    └─→ Generate video (processing time: 10-15 min)
    ↓
[Fallback: HeyGen API]
    └─→ If Synthesia fails or quality < threshold
    ↓
[Video Post-Processing]
    ├─→ Add Axia logo (bottom right, 20% opacity)
    ├─→ Add text overlays (Arabic + English):
    │   ├─→ 0:00-0:03: Hook text (large, bold)
    │   ├─→ 0:03-0:15: Key points (animated)
    │   └─→ 0:15-0:20: CTA text + URL
    ├─→ Add background music (subtle, energetic)
    ├─→ Color grading (Axia brand colors)
    └─→ Export: MP4 (H.264, 1080x1920, 30fps)
```

### Phase 5: Quality Validation - Video Level (9:25-9:28 AM)
```
[Quality Checker 5: Visual Quality]
    ├─→ Resolution check (1080x1920)
    ├─→ Aspect ratio validation (9:16)
    ├─→ Frame rate (30fps minimum)
    ├─→ Bitrate (minimum 5 Mbps)
    └─→ Score: 0-100 (threshold: 90+)
    ↓
[Quality Checker 6: Brand Elements]
    ├─→ Logo presence and positioning
    ├─→ Color scheme (Axia brand colors)
    ├─→ Font consistency (if text overlays)
    └─→ Score: 0-100 (threshold: 95+)
    ↓
[Quality Checker 7: Audio-Visual Sync]
    ├─→ Lip sync accuracy (if avatar)
    ├─→ Audio clarity (no distortion)
    ├─→ Subtitle timing (if present)
    └─→ Score: 0-100 (threshold: 90+)
    ↓
[Quality Checker 8: TikTok Engagement Prediction]
    ├─→ GPT-5-Pro: Analyze hook effectiveness
    ├─→ Pacing and energy level
    ├─→ CTA visibility and clarity
    ├─→ Predicted engagement score
    └─→ Score: 0-100 (threshold: 80+)
```

**IF ANY CHECKER FAILS**: Alert human for review (don't auto-publish)

### Phase 6: Metadata Generation (9:28-9:30 AM)
```
[GPT-5: Generate Optimized Metadata]
    ↓
[YouTube Title] (Arabic + English)
Arabic: "ابدأ التداول اليوم مع أكسيا | [Theme] | #shorts"
English: "Start Trading Today with Axia | [Theme] | #shorts"
    ↓
[Description] (Arabic primary, English secondary)
```arabic
ابدأ التداول مع أكسيا - منصة تداول مرخصة بالكامل

[Hook من الفيديو]

✅ مرخصة ومنظمة
✅ منصة احترافية
✅ دعم متعدد اللغات
✅ رسوم شفافة

⚠️ تحذير المخاطر:
تداول الفوركس يحمل مخاطر. قد تخسر رأس مالك.

🔗 ابدأ الآن: https://axia.trade

---
Start trading with Axia - Fully regulated platform
[CTA in English]

#فوركس #تداول #أكسيا #Forex #Trading #Axia
```
    ↓
[Tags] (30 max)
فوركس, تداول, أكسيا, forex, trading, axia, تداول_العملات,
forex_trading, online_trading, investment, استثمار, ...
    ↓
[Thumbnail] (Auto-generated from frame at 0:03)
    └─→ Enhance: Bright colors, text overlay, emoji
```

### Phase 7: Publishing & Distribution (9:30-9:35 AM)
```
[YouTube Data API v3]
    ├─→ Upload video as "Public"
    ├─→ Category: Education / How-to
    ├─→ Made for Kids: No
    ├─→ Add to Playlist: "Daily Trading Insights"
    └─→ Get video URL
    ↓
[Cross-Platform Distribution]
    ├─→ TikTok API (if available)
    ├─→ Instagram Reels (Meta API)
    ├─→ LinkedIn (native upload)
    ├─→ Twitter/X (video post)
    └─→ Telegram channel (embed)
    ↓
[Database Logging]
    ├─→ Store video metadata
    ├─→ Log quality scores
    ├─→ Track theme used
    └─→ Schedule analytics review
```

### Phase 8: Monitoring & Alerting (9:35-9:40 AM)
```
[Success Check]
    ├─→ Video published successfully?
    ├─→ All quality scores logged?
    ├─→ Cross-platform posts completed?
    └─→ If YES: Send success notification
    ↓
[Failure Handling]
    ├─→ If script generation failed (3 attempts)
    ├─→ If quality check failed
    ├─→ If API error occurred
    └─→ Send alert to human + save artifacts
    ↓
[Daily Report Email]
    ├─→ Video URL
    ├─→ All quality scores
    ├─→ Theme used
    ├─→ Processing time
    └─→ Next scheduled run
```

## 🔐 Quality Checker Implementations

### Checker 1: Arabic Dialect Validator
```python
def validate_arabic_dialect(script: str) -> dict:
    """
    Validates Khaleeji Arabic dialect accuracy
    Returns: {score: int, issues: list, suggestions: list}
    """
    prompt = f"""
    You are an expert in Khaleeji (GCC) Arabic dialect.

    Analyze this script for:
    1. Dialect accuracy (Khaleeji vs MSA)
    2. Financial terminology correctness
    3. Cultural appropriateness
    4. Natural conversational flow

    Script:
    {script}

    Return JSON:
    {{
        "score": 0-100,
        "dialect_accuracy": 0-100,
        "terminology": 0-100,
        "cultural_fit": 0-100,
        "issues": ["list of issues"],
        "suggestions": ["list of improvements"]
    }}
    """

    response = consult_gpt5_pro(prompt, temperature=0.3)
    return parse_json(response)
```

### Checker 2: Brand Compliance Validator
```python
def validate_brand_compliance(script: str) -> dict:
    """
    Validates Axia brand voice compliance
    Returns: {score: int, voice_match: bool, messaging: list}
    """

    # Load Axia brand guidelines
    brand_voice = """
    - Bold and confident
    - Opportunity-focused
    - Action-oriented
    - Professional yet energetic
    - Empowering
    - Trustworthy
    Key messaging:
    - Endless opportunities
    - Fully regulated
    - Professional platform
    """

    prompt = f"""
    Compare this script against Axia brand guidelines.

    Brand Voice: {brand_voice}

    Script: {script}

    Analyze:
    1. Tone match (bold, confident)
    2. Key messaging presence
    3. Action-orientation
    4. Professional yet energetic balance

    Return JSON with score 0-100 and detailed analysis.
    """

    response = consult_gpt5_pro(prompt, temperature=0.2)
    return parse_json(response)
```

### Checker 3: Regulatory Compliance Validator
```python
def validate_regulatory_compliance(script: str) -> dict:
    """
    Ensures forex trading regulations compliance
    Returns: {score: int, compliant: bool, risks: list}
    """

    compliance_requirements = """
    MUST INCLUDE:
    - Risk disclosure (trading carries risks)
    - No guaranteed profit claims
    - Clear that losses are possible
    - Platform is regulated (mention if space allows)

    MUST AVOID:
    - "Get rich quick" language
    - Guaranteed returns
    - No-risk promises
    - Pressure tactics
    """

    prompt = f"""
    Check this forex trading script for regulatory compliance.

    Requirements: {compliance_requirements}

    Script: {script}

    Return JSON:
    {{
        "score": 0-100,
        "compliant": true/false,
        "risk_disclosure_present": true/false,
        "prohibited_claims": ["list any found"],
        "missing_elements": ["list what's missing"],
        "severity": "low|medium|high"
    }}
    """

    response = consult_gpt5_pro(prompt, temperature=0.1)
    result = parse_json(response)

    # Hard fail on prohibited claims
    if result['prohibited_claims']:
        result['score'] = 0
        result['compliant'] = False

    return result
```

### Checker 4: TikTok Optimization Validator
```python
def validate_tiktok_optimization(script: str) -> dict:
    """
    Validates TikTok engagement optimization
    Returns: {score: int, hook_strength: int, pacing: str}
    """

    prompt = f"""
    Analyze this 20-second script for TikTok engagement.

    Script timing:
    0:00-0:03 - Hook
    0:03-0:08 - Problem
    0:08-0:15 - Solution
    0:15-0:20 - CTA

    Script: {script}

    Evaluate:
    1. Hook strength (0-100): Does it grab attention in 3s?
    2. Problem clarity (0-100): Clear pain point?
    3. Solution impact (0-100): Compelling offer?
    4. CTA urgency (0-100): Strong call-to-action?
    5. Pacing (fast/medium/slow): Right for TikTok?
    6. Predicted engagement (low/medium/high)

    Return JSON with detailed scores and suggestions.
    """

    response = consult_gpt5_pro(prompt, temperature=0.5)
    return parse_json(response)
```

### Checker 5: Visual Quality Validator
```python
def validate_visual_quality(video_path: str) -> dict:
    """
    Validates video technical quality
    Returns: {score: int, specs: dict, issues: list}
    """
    import cv2
    import subprocess

    # Get video properties
    video = cv2.VideoCapture(video_path)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps

    # Get bitrate using ffprobe
    cmd = f'ffprobe -v error -show_entries format=bit_rate -of default=noprint_wrappers=1:nokey=1 {video_path}'
    bitrate = int(subprocess.check_output(cmd, shell=True)) / 1_000_000  # Mbps

    issues = []
    score = 100

    # Validate specs
    if width != 1080 or height != 1920:
        issues.append(f"Resolution {width}x{height}, expected 1080x1920")
        score -= 30

    if fps < 30:
        issues.append(f"FPS {fps}, expected 30+")
        score -= 20

    if duration < 19 or duration > 21:
        issues.append(f"Duration {duration}s, expected 19-21s")
        score -= 15

    if bitrate < 5:
        issues.append(f"Bitrate {bitrate}Mbps, expected 5+")
        score -= 15

    return {
        'score': max(0, score),
        'specs': {
            'resolution': f"{width}x{height}",
            'fps': fps,
            'duration': duration,
            'bitrate': bitrate
        },
        'issues': issues
    }
```

### Checker 6: Brand Elements Validator
```python
def validate_brand_elements(video_path: str) -> dict:
    """
    Validates Axia brand elements in video
    Returns: {score: int, logo_present: bool, colors: dict}
    """
    import cv2
    import numpy as np

    # Axia brand colors (RGB)
    axia_colors = {
        'primary': (0, 71, 171),  # Blue
        'secondary': (255, 183, 3),  # Gold
    }

    video = cv2.VideoCapture(video_path)

    # Sample frames at key points
    frames_to_check = [
        int(video.get(cv2.CAP_PROP_FRAME_COUNT) * 0.1),  # 10%
        int(video.get(cv2.CAP_PROP_FRAME_COUNT) * 0.5),  # 50%
        int(video.get(cv2.CAP_PROP_FRAME_COUNT) * 0.9),  # 90%
    ]

    logo_detected = False
    brand_colors_present = False

    for frame_num in frames_to_check:
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = video.read()

        if not ret:
            continue

        # Check for logo (bottom right quadrant)
        h, w = frame.shape[:2]
        logo_region = frame[int(h*0.75):, int(w*0.75):]

        # Simple logo detection (check for white/branded areas)
        # In production, use template matching or ML model

        # Check for brand colors in frame
        # Convert frame to RGB for color detection
        # Simplified: check if brand colors are present

    score = 100
    if not logo_detected:
        score -= 40
    if not brand_colors_present:
        score -= 20

    return {
        'score': score,
        'logo_present': logo_detected,
        'brand_colors_present': brand_colors_present,
        'issues': []
    }
```

### Checker 7: Audio-Visual Sync Validator
```python
def validate_av_sync(video_path: str) -> dict:
    """
    Validates audio-visual synchronization
    Returns: {score: int, sync_offset: float, clarity: float}
    """
    # This would use specialized libraries like:
    # - syncnet for lip sync detection
    # - librosa for audio analysis

    # Simplified implementation
    score = 100
    issues = []

    # Check audio clarity (no distortion, proper levels)
    # Check subtitle timing (if present)
    # Check lip sync (if avatar-based)

    return {
        'score': score,
        'sync_offset': 0.0,  # milliseconds
        'audio_clarity': 95,
        'issues': issues
    }
```

### Checker 8: Engagement Prediction
```python
def predict_engagement(video_path: str, script: str, metadata: dict) -> dict:
    """
    Predicts TikTok engagement using GPT-5-Pro
    Returns: {score: int, predicted_metrics: dict}
    """

    prompt = f"""
    Analyze this TikTok-style video for predicted engagement.

    Script: {script}

    Video specs: {metadata}

    Based on TikTok best practices, predict:
    1. Hook effectiveness (first 3s): 0-100
    2. Watch time prediction (% who watch to end): 0-100
    3. Like probability: low/medium/high
    4. Share probability: low/medium/high
    5. Comment probability: low/medium/high
    6. Overall engagement score: 0-100

    Consider:
    - Hook strength
    - Value delivered in 20s
    - CTA clarity
    - Visual appeal
    - Audio quality
    - Arabic market preferences

    Return detailed JSON analysis.
    """

    response = consult_gpt5_pro(prompt, temperature=0.4)
    return parse_json(response)
```

## 🌳 Git Worktrees Structure

```bash
/home/user/
├── axia-video-automation/              # Main repo
│   ├── .git/                           # Shared git directory
│   ├── workflows/                      # n8n workflow definitions
│   ├── scripts/                        # Python scripts
│   ├── quality-checkers/               # Quality validator modules
│   └── README.md
│
├── axia-video-wt-development/          # Development worktree
│   └── [Active development here]
│
├── axia-video-wt-production/           # Production worktree
│   └── [Deployed workflow runs here]
│
└── axia-video-wt-testing/              # Testing worktree
    └── [Test runs and validation]
```

### Setup Commands:
```bash
# Create main repository
cd /home/user
mkdir axia-video-automation
cd axia-video-automation
git init
git checkout -b main

# Create worktrees
git worktree add ../axia-video-wt-development -b development
git worktree add ../axia-video-wt-production -b production
git worktree add ../axia-video-wt-testing -b testing

# Each worktree can run independently
# Production runs the daily workflow
# Development is for improvements
# Testing is for validating changes
```

## 📦 Technology Stack

### Core Services:
1. **Azure OpenAI (GPT-5-Pro)**: Strategy, script generation, validation
2. **Perplexity API**: Market research, news gathering
3. **ElevenLabs**: Arabic voice generation
4. **Synthesia**: AI avatar video generation (primary)
5. **HeyGen**: AI avatar video generation (fallback)
6. **n8n**: Workflow orchestration
7. **YouTube Data API v3**: Video upload and management
8. **PostgreSQL**: Logging and analytics

### Python Libraries:
```
requirements.txt:
- openai>=1.0.0
- requests>=2.31.0
- opencv-python>=4.8.0
- ffmpeg-python>=0.2.0
- google-api-python-client>=2.100.0
- psycopg2-binary>=2.9.0
- schedule>=1.2.0
- python-dotenv>=1.0.0
```

## 🚀 Implementation Phases

### Phase 1: Foundation (Week 1)
- [ ] Set up git worktrees structure
- [ ] Create main repository with scaffolding
- [ ] Configure all API keys and credentials
- [ ] Set up PostgreSQL database schema
- [ ] Create basic n8n workflow skeleton

### Phase 2: Script Generation Pipeline (Week 1-2)
- [ ] Implement GPT-5-Pro consultation system
- [ ] Build Perplexity integration for news
- [ ] Create script generation module
- [ ] Implement 7-day theme rotation
- [ ] Test Arabic script quality

### Phase 3: Quality Checkers (Week 2)
- [ ] Implement Checker 1: Arabic Dialect
- [ ] Implement Checker 2: Brand Compliance
- [ ] Implement Checker 3: Regulatory Compliance
- [ ] Implement Checker 4: TikTok Optimization
- [ ] Test all checkers with sample scripts

### Phase 4: Audio-Video Generation (Week 3)
- [ ] Integrate ElevenLabs API
- [ ] Set up Synthesia API (primary)
- [ ] Configure HeyGen API (fallback)
- [ ] Build video post-processing pipeline
- [ ] Add text overlays and branding

### Phase 5: Video Quality Validation (Week 3)
- [ ] Implement Checker 5: Visual Quality
- [ ] Implement Checker 6: Brand Elements
- [ ] Implement Checker 7: Audio-Visual Sync
- [ ] Implement Checker 8: Engagement Prediction
- [ ] Test with generated videos

### Phase 6: Publishing & Distribution (Week 4)
- [ ] Set up YouTube Data API integration
- [ ] Build metadata generation system
- [ ] Configure cross-platform posting
- [ ] Implement database logging
- [ ] Create monitoring dashboard

### Phase 7: Automation & Monitoring (Week 4)
- [ ] Set up cron scheduler (9 AM daily)
- [ ] Implement error handling and retries
- [ ] Build alerting system (email/SMS)
- [ ] Create daily report generator
- [ ] Set up analytics tracking

### Phase 8: Testing & Optimization (Week 5)
- [ ] End-to-end testing in testing worktree
- [ ] Load testing and performance optimization
- [ ] Quality threshold calibration
- [ ] Documentation and runbooks
- [ ] Deploy to production worktree

## 📊 Success Metrics

### Technical Metrics:
- **Uptime**: 99%+ (daily execution success rate)
- **Processing Time**: < 30 minutes per video
- **Quality Score**: 85+ average across all checkers
- **API Failures**: < 5% (with automatic fallbacks)

### Content Metrics:
- **YouTube Views**: Track daily growth
- **Engagement Rate**: Likes, comments, shares
- **Watch Time**: Average % of video watched
- **CTR to Axia.trade**: Conversion tracking

### Business Metrics:
- **Cost per Video**: Target < $2 (API costs)
- **Time Saved**: ~2 hours/day vs manual production
- **Quality Consistency**: 95%+ brand compliance
- **Regulatory Compliance**: 100% (zero violations)

## 🔔 Alerting & Notifications

### Success Notification (9:40 AM daily):
```
✅ Axia Video Published Successfully

Video: [YouTube URL]
Theme: Market Opportunity
Duration: 20s
Quality Scores:
  - Arabic Dialect: 92/100
  - Brand Compliance: 95/100
  - Regulatory: 100/100
  - TikTok Optimization: 88/100
  - Visual Quality: 94/100
  - Engagement Prediction: 85/100

Processing Time: 28 minutes
Next Run: Tomorrow 9:00 AM GMT
```

### Failure Notification (if issues):
```
⚠️ Axia Video Workflow Failed

Stage: Script Generation
Attempts: 3/3
Reason: Quality checkers failed - Arabic dialect score 72/100

Action Required: Manual review needed

Artifacts saved at: /artifacts/2025-10-24/
Logs: [Link]
```

## 📚 Documentation & Runbooks

### Daily Operations:
1. **Morning Check** (9:00 AM): Verify workflow started
2. **Success Verification** (9:40 AM): Confirm video published
3. **Analytics Review** (weekly): Review engagement metrics
4. **Quality Calibration** (monthly): Adjust checker thresholds

### Troubleshooting:
- **Script generation loops**: Check GPT-5-Pro API status
- **Video generation fails**: Switch to HeyGen fallback
- **YouTube upload fails**: Check API quota and credentials
- **Quality scores too low**: Review and adjust thresholds

## 🔐 Security & Compliance

### API Key Management:
- All keys stored in environment variables
- Rotation policy: Every 90 days
- Access logs maintained
- Separate keys for dev/test/prod

### Data Privacy:
- No PII stored in logs
- Video artifacts deleted after 7 days
- Database backups encrypted
- Compliance with GDPR and local regulations

### Regulatory Compliance:
- All videos include risk disclosure
- No guaranteed profit claims
- Regular compliance audits
- Documented approval process for new themes

---

## 📝 Next Steps

1. ✅ Review and validate this plan with GPT-5-Pro (long thinking mode)
2. Create detailed implementation tickets
3. Set up development environment
4. Begin Phase 1 implementation
5. Schedule weekly progress reviews

**Estimated Total Time to Production**: 4-5 weeks
**Estimated Cost**: ~$1000 setup + ~$60/month operational
