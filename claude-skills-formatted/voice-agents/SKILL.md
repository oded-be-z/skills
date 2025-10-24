---
name: voice-agents
description: Develop and train AI voice agents for sales training and Arabic-speaking sales automation using ElevenLabs and Azure OpenAI.
---

# Voice Agents Development Skill

## Project Overview

### Part 1: Sales Training Voice Agents ⚠️ 80% Complete
**Status**: Working but needs improvements

**Objective**: Train sales reps by simulating customer conversations

**How It Works**:
1. Sales rep calls AI "customer"
2. AI responds with realistic objections/questions
3. System records and analyzes conversation
4. Provides feedback on performance

**Technology**:
- **Voice Recognition**: (TBD - specify current tool)
- **LLM Backend**: Azure OpenAI GPT-5
- **Text-to-Speech**: ElevenLabs
- **Language**: Arabic (Khaleeji dialect) + English

**Current Issues**:
- Needs improvement (user mentioned "needs improvements")
- Arabic dialect accuracy
- Response timing
- Realism of objections

### Part 2: Real Sales Voice Agents 🛑 STUCK
**Status**: Development blocked

**Objective**: Replace human sales agents with AI voice agents

**Technology Stack** (Proposed):
- **Voice Platform**: Twilio, Vonage, or similar
- **Speech-to-Text**: Azure Speech Services (Arabic support)
- **LLM**: Azure OpenAI GPT-5-Pro (for sales strategy)
- **Text-to-Speech**: ElevenLabs (Arabic voices)
- **CRM Integration**: Log calls, update status

### Part 3: Call Transcription System 📝 WAITING
**Status**: Sys admin to build, not started yet

**Objective**: Transcribe all sales calls for analysis and learning

**Why It's Needed**:
- Learn from successful sales calls
- Identify common objections
- Train AI voice agents with real data
- Quality assurance
- Compliance documentation

**Technology**:
- **Speech-to-Text**: Azure Speech Services
- **Language Detection**: Auto-detect Arabic vs English
- **Speaker Diarization**: Identify who's speaking
- **Storage**: Secure database
- **Analysis**: GPT-5 for insights

## Arabic Voice Agent Considerations

### Dialect Challenges
**Khaleeji (Gulf) Arabic** is different from:
- Modern Standard Arabic (MSA)
- Egyptian Arabic
- Levantine Arabic

**Key Differences**:
- Pronunciation
- Vocabulary
- Phrases and expressions
- Formality levels

### Cultural Sensitivity
✅ **Do**:
- Use respectful greetings
- Be patient and listen
- Acknowledge concerns seriously
- Emphasize trust and security
- Use proper titles (Ustadh, Hajj, etc.)

❌ **Don't**:
- Rush or pressure
- Use aggressive sales tactics
- Disrespect family/cultural values
- Ignore religious considerations
- Make unrealistic promises

### Sales Script Adaptation

**English vs Arabic Approach**:
- **English**: Direct, features-focused
- **Arabic**: Relationship-first, trust-building

**Example Opening**:
```
English: "Hi, I'm calling about Seekapa's trading platform..."

Arabic (Khaleeji):
"السلام عليكم، كيف حالك؟ [pause for response]
أنا أتصل من سيكابا، منصة التداول المرخصة..."
(Peace be upon you, how are you? I'm calling from Seekapa, the licensed trading platform...)
```

## Voice Agent Architecture

```
[Incoming Call]
    ↓
[Voice Recognition] → Detect language (Arabic/English)
    ↓
[Speech-to-Text] → Convert to text
    ↓
[LLM Processing] → GPT-5-Pro analyzes intent, formulates response
    ↓
[Response Generation] → Create culturally appropriate response
    ↓
[Text-to-Speech] → ElevenLabs Arabic voice
    ↓
[Audio Playback] → Respond to caller
    ↓
[Loop] → Continue conversation
    ↓
[Call End] → Log, transcribe, analyze
```

## Sales Training Scenarios

### Scenario 1: Interested but Cautious
```
Rep: مرحباً، أريد أن أحدثك عن فرص التداول
Customer (AI): هل المنصة مرخصة؟ سمعت عن نصب كثير

(Rep: Hello, I want to talk to you about trading opportunities)
(AI: Is the platform licensed? I heard about many scams)
```
**Training Goal**: Handle scam concerns professionally

### Scenario 2: Budget Concerns
```
Rep: يمكنك البدء بمبلغ صغير
Customer (AI): كم الحد الأدنى؟ ماذا لو خسرت؟

(Rep: You can start with a small amount)
(AI: What's the minimum? What if I lose?)
```
**Training Goal**: Explain risk management

### Scenario 3: Competition Comparison
```
Rep: نحن أفضل من المنافسين
Customer (AI): أستخدم [Competitor] already، لماذا أغير؟

(Rep: We're better than competitors)
(AI: I use [Competitor] already, why change?)
```
**Training Goal**: Differentiate without bashing competitors

## ElevenLabs Arabic Voice Setup

**API Endpoint**: `https://api.elevenlabs.io/v1`
**API Key**: `37db551f376697b8fcbb1b3b86088d51c9f0d7e415cba8545ed10297d770d701`

### Voice Selection:
- **Male voices**: Professional, trustworthy tone
- **Female voices**: Warm, approachable tone
- **Language**: Arabic (multiple dialect options)
- **Settings**: Clarity, stability, style exaggeration

### API Call Example:
```python
import requests

url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
headers = {
    "xi-api-key": "37db551f376697b8fcbb1b3b86088d51c9f0d7e415cba8545ed10297d770d701",
    "Content-Type": "application/json"
}
data = {
    "text": "السلام عليكم، كيف يمكنني مساعدتك اليوم؟",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.75,
        "similarity_boost": 0.75
    }
}
response = requests.post(url, json=data, headers=headers)
audio_data = response.content
```

## Performance Analytics

### Metrics to Track:
1. **Conversation Duration**: Average call length
2. **Conversion Rate**: Training calls → real sales readiness
3. **Objection Handling**: Success rate per objection type
4. **Language Quality**: Arabic fluency score
5. **Response Time**: Latency between speech and response

### Improvement Loop:
```
[Conversation Recorded]
    ↓
[GPT-5-Pro Analyzes]
    ↓
[Identifies Weaknesses]
    ↓
[Suggests Improvements]
    ↓
[Update Training Scenarios]
    ↓
[Re-train Sales Rep]
```

## Integration with Transcription System

### When Transcripts Become Available:
1. **Analyze Successful Calls**:
   - What phrases worked?
   - Which objections were handled well?
   - What tone/pace was effective?

2. **Train AI from Real Data**:
   - Feed transcripts to GPT-5-Pro
   - Extract successful patterns
   - Build response library
   - Refine voice agent scripts

3. **Quality Assurance**:
   - Compare AI vs human performance
   - Identify gaps
   - Continuous improvement

## Roadmap

### Phase 1: Improve Training Agents (Now)
- [ ] Fix Arabic dialect accuracy
- [ ] Improve response realism
- [ ] Add more training scenarios
- [ ] Enhance feedback system

### Phase 2: Call Transcription (Waiting)
- [ ] Sys admin builds transcription system
- [ ] Test transcription accuracy
- [ ] Build analysis pipeline
- [ ] Extract training data

### Phase 3: Real Sales Agents (Future)
- [ ] Identify current blockers
- [ ] Test in controlled environment
- [ ] Pilot with low-risk calls
- [ ] Monitor and improve
- [ ] Scale to production

## Integration with Other Skills
- **Combine with**: `multilingual-content` for Arabic quality
- **Combine with**: `seekapa-brand` or `axia-brand` for sales messaging
- **Combine with**: `forex-regulations` for compliance

## Notes
- Part 1 needs improvement - specifics TBD
- Part 2 is stuck - need to identify blockers
- Part 3 waiting on sys admin - then analyze for improvements
- Arabic dialect accuracy is critical
- Cultural sensitivity paramount
- Start with training, move to real sales only when proven
