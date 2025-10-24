---
name: youtube-automation
description: Create and automate daily 1-minute Arabic market update videos for Seekapa and Axia using Synthesia AI avatars, ElevenLabs voice, and YouTube API.
---

# YouTube Channel Automation Skill

## Project Goals
1. **2 AI Avatars** (Male & Female, Arabic-speaking)
2. **Daily Videos** (1 minute each)
3. **High-Value Content** (Real market insights, not fluff)
4. **Fully Automated** (Minimal manual intervention)
5. **GCC/UAE/Saudi Audience** (Khaleeji Arabic dialect)

## Video Production Tools

### Primary Option: Synthesia ⭐
- **140+ languages** including Arabic
- **240+ AI avatars** (professional quality)
- **Enterprise-grade** output
- **API available**: https://api.synthesia.io/v2
- **API Key**: `85d7cd90cba47b874cd5051af33e1e9e`

### Secondary Option: HeyGen (For Comparison)
- **Current tool**: Already have API key
- **For comparison**: Test alongside Synthesia
- **API**: https://api.heygen.com/v2
- **Key**: `sk_V2_hgu_kKAIZMefpfr_Vjz49zIdtGr110JxPiRmLMpCgKArb1Mnelevnlabs`

### Audio: ElevenLabs
- **High-quality Arabic TTS**
- **Voice cloning capable**
- **API Key**: `37db551f376697b8fcbb1b3b86088d51c9f0d7e415cba8545ed10297d770d701`
- **Endpoint**: https://api.elevenlabs.io/v1

## Video Structure (1-Minute Format)

### Template (60 seconds):
```
0:00-0:05 (5s)  - Hook: "Today's forex market in 60 seconds"
0:05-0:15 (10s) - Major currency pairs update (EUR/USD, GBP/USD, USD/JPY)
0:15-0:30 (15s) - Key market event or news impact
0:30-0:50 (20s) - Trading insight or tip (actionable)
0:50-1:00 (10s) - CTA: "Trade with [Brand]" + disclosure
```

### Content Requirements:
✅ **Real market data** (use live APIs)
✅ **Valuable insights** (not generic fluff)
✅ **Arabic Khaleeji dialect**
✅ **Professional tone** yet approachable
✅ **Compliance**: Risk disclosure
✅ **Brand consistent** (Seekapa or Axia voice)

## Automation Pipeline

### Step 1: Market Data Collection
**Sources**:
- **Azure AI models** (GPT-5-Pro for analysis)
- **Perplexity API** (latest market news)
- **Financial APIs**: Alpha Vantage, Forex API, etc.

**Process**:
1. Fetch current forex prices (major pairs)
2. Get last 24h news (Perplexity deep research)
3. Analyze trends (GPT-5-Pro consultation)
4. Generate insights (GPT-5 content creation)

### Step 2: Script Generation
**Script Formula**:
```
Hook → Data → Insight → Action → Disclosure
```

**Arabic Script Template**:
```arabic
[Hook]
السلام عليكم، أسواق الفوركس اليوم في ٦٠ ثانية

[Data]
اليورو/دولار عند [price]، [change]%
الإسترليني/دولار عند [price]، [change]%

[Insight]
[Key market event explanation]

[Action]
[Trading tip or observation]

[Disclosure]
تداول بحذر - المخاطر موجودة دائماً
ابدأ التداول مع [Brand]
```

### Step 3: Voice Generation
**Using ElevenLabs**:
1. Convert Arabic script to speech
2. Generate male OR female voice (alternate daily)
3. High-quality, natural Arabic pronunciation
4. Save audio file

### Step 4: Video Generation
**Using Synthesia/HeyGen**:
1. Select avatar (male/female)
2. Upload audio or use text-to-speech
3. Select background template
4. Add brand overlay (logo, colors)
5. Generate video
6. Download final MP4

### Step 5: Post to YouTube
**Automation**:
- Use YouTube Data API
- Upload video
- Set title, description, tags
- Schedule if needed
- Add to appropriate playlist

## n8n Workflow Design

```
[Daily Trigger 6:00 AM GMT]
    ↓
[Fetch Market Data]
    ↓
[Consult Perplexity (Market News)]
    ↓
[Consult GPT-5-Pro (Analysis)]
    ↓
[Generate Arabic Script]
    ↓
[Generate Audio (ElevenLabs)]
    ↓
[Create Video (Synthesia/HeyGen)]
    ↓
[Upload to YouTube]
    ↓
[Notify Success/Failure]
```

## Brand-Specific Variations

### Seekapa Videos:
- **Tone**: Professional excellence
- **Color Scheme**: Seekapa brand colors
- **Logo**: Seekapa logo (corner overlay)
- **CTA**: "Trade with confidence at Seekapa.com"

### Axia Videos:
- **Tone**: Bold opportunities
- **Color Scheme**: Axia brand colors
- **Logo**: Axia logo (corner overlay)
- **CTA**: "Endless opportunities at Axia.trade"

## SEO & Distribution

### YouTube Optimization:
**Title Format** (Arabic):
```
أسواق الفوركس اليوم - [Date] | تحليل يومي سريع
```

**Description Template**:
```
تحليل سريع لأسواق الفوركس ليوم [Date]

📊 أزواج العملات المتداولة:
- EUR/USD: [price]
- GBP/USD: [price]
- USD/JPY: [price]

💡 نصيحة اليوم:
[Insight from video]

⚠️ تنويه المخاطر:
تداول الفوركس يحمل مخاطر عالية. يمكن أن تخسر رأس مالك.

🔗 ابدأ التداول مع [Brand]:
https://[domain]

#فوركس #تداول #تحليل_فوركس #[Brand]
```

**Tags**:
- فوركس (Forex)
- تداول (Trading)
- تحليل فني (Technical Analysis)
- سوق المال (Financial Market)
- [Brand name]

### Cross-Platform:
- Share on X (Twitter)
- Post on LinkedIn
- Embed in blog posts
- Share in Telegram/WhatsApp groups

## Quality Control

### Daily Checks:
✅ Market data is accurate
✅ Arabic script is natural (not machine-translated)
✅ Audio quality is clear
✅ Video renders correctly
✅ Brand elements present
✅ Compliance disclosure included
✅ Upload successful

### Weekly Reviews:
- Viewer analytics
- Engagement metrics
- Comments moderation
- Feedback incorporation
- Content quality assessment

## Integration with Other Skills
- **Combine with**: `seekapa-brand` or `axia-brand` for brand consistency
- **Combine with**: `multilingual-content` for Arabic script quality
- **Combine with**: `forex-regulations` for compliance
- **Combine with**: `aeo-optimization` for SEO strategy

## Tools & APIs

### Required Access:
1. **Synthesia API** (have key: 85d7cd90cba47b874cd5051af33e1e9e)
2. **HeyGen API** (have key)
3. **ElevenLabs API** (have key)
4. **YouTube Data API** (need to enable)
5. **Financial Data API** (Alpha Vantage or similar)
6. **n8n Workflows** (have access)

### Consultation Tools:
- **Azure OpenAI (GPT-5-Pro)**: Market analysis
- **Perplexity MCP**: Latest news
- **GPT-5**: Script writing

## Notes
- Start with manual testing before full automation
- Compare Synthesia vs HeyGen quality
- Monitor viewer feedback closely
- Adjust format based on analytics
- Consider expanding to 2-3 minutes if engagement is high
