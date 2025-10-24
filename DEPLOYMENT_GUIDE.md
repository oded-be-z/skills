# Axia Daily Video Automation - Deployment Guide

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- FFmpeg installed (`apt install ffmpeg` or `brew install ffmpeg`)
- PostgreSQL database (optional, for logging)
- Git
- Access to all required APIs (see API Keys section)

### 1. Initial Setup

```bash
# Navigate to the skills directory
cd /home/user/skills

# Run the git worktrees setup script
chmod +x setup_git_worktrees.sh
./setup_git_worktrees.sh

# Switch to development worktree
cd ../axia-video-wt-development
```

### 2. Configure API Keys

Create a `.env` file in the development worktree:

```bash
cat > .env << 'EOF'
# Azure OpenAI
AZURE_OPENAI_API_KEY=your_azure_api_key_here

# Perplexity
PERPLEXITY_API_KEY=your_perplexity_api_key_here

# ElevenLabs
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here

# Synthesia
SYNTHESIA_API_KEY=your_synthesia_api_key_here

# n8n
N8N_API_KEY=your_n8n_api_key_here

# YouTube (configure after OAuth setup)
YOUTUBE_CLIENT_ID=your_client_id
YOUTUBE_CLIENT_SECRET=your_client_secret

# Notifications (optional)
SLACK_WEBHOOK_URL=your_slack_webhook
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
EOF

# Note: All API keys are available in your environment variables
# You can copy them from: env | grep -E "AZURE|PERPLEXITY|ELEVENLABS|SYNTHESIA|N8N"
```

### 3. Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Install system dependencies
sudo apt-get install -y ffmpeg libsm6 libxext6
```

### 4. Configure Settings

Copy the configuration template:

```bash
cp config/config.template.json config/config.json
```

Edit `config/config.json` with your specific settings:
- Update voice IDs from ElevenLabs dashboard
- Update avatar IDs from Synthesia dashboard
- Update YouTube channel ID
- Adjust quality thresholds if needed

### 5. Test the Workflow

Run a test execution:

```bash
# Load environment variables
export $(cat .env | xargs)

# Run workflow
python3 scripts/run_workflow.py
```

Check the logs in `logs/` directory for any issues.

### 6. Deploy to Production

Once testing is successful:

```bash
# Merge to production branch
cd ../axia-video-automation
git checkout production
git merge development

# Switch to production worktree
cd ../axia-video-wt-production

# Copy .env file
cp ../axia-video-wt-development/.env .

# Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 7. Set Up n8n Workflow

#### Option A: Using n8n UI (Recommended due to MCP issues)

1. Log in to your n8n instance
2. Click "Import from File"
3. Upload `workflows/n8n_workflow_axia_daily_video.json`
4. Configure credentials:
   - PostgreSQL connection (if using)
   - Email SMTP settings
   - Slack webhook (optional)
   - Telegram bot (optional)
5. Test the workflow manually
6. Activate the workflow

#### Option B: Using n8n API

```bash
# Import workflow via API
curl -X POST https://your-n8n-instance.com/api/v1/workflows \
  -H "X-N8N-API-KEY: ${N8N_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @workflows/n8n_workflow_axia_daily_video.json

# Activate workflow
curl -X PATCH https://your-n8n-instance.com/api/v1/workflows/{workflow_id} \
  -H "X-N8N-API-KEY: ${N8N_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"active": true}'
```

### 8. Set Up Monitoring

#### Database Logging (Optional)

Create PostgreSQL database and table:

```sql
CREATE DATABASE axia_video_logs;

\c axia_video_logs

CREATE TABLE video_logs (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP DEFAULT NOW(),
    video_url TEXT,
    processing_time FLOAT,
    quality_scores JSONB,
    status VARCHAR(50),
    error_message TEXT
);

CREATE INDEX idx_date ON video_logs(date);
CREATE INDEX idx_status ON video_logs(status);
```

#### Email Notifications

Configure SMTP settings in n8n or use a service like SendGrid.

#### Slack Notifications

1. Create a Slack app
2. Enable Incoming Webhooks
3. Copy webhook URL to `.env`

#### Telegram Notifications

1. Create a bot via @BotFather
2. Get bot token
3. Get chat ID (send message to bot, then call getUpdates)
4. Add to `.env`

## 🔧 Configuration

### Quality Thresholds

Edit `config/config.json` to adjust quality thresholds:

```json
{
  "quality_thresholds": {
    "arabic_dialect": 85,        // Khaleeji dialect accuracy
    "brand_compliance": 90,      // Axia brand voice match
    "regulatory_compliance": 95, // Forex regulations (strict!)
    "tiktok_optimization": 85,   // Engagement optimization
    "visual_quality": 90,        // Video specs compliance
    "brand_elements": 95,        // Logo/branding presence
    "av_sync": 90,               // Audio-visual sync
    "engagement_prediction": 80  // Predicted engagement
  }
}
```

**Important**: Don't lower `regulatory_compliance` below 95. Legal compliance is critical.

### Video Specifications

Default specifications (don't change unless needed):

```json
{
  "video": {
    "duration": 20,           // seconds
    "resolution": "1080x1920", // vertical (9:16)
    "fps": 30,
    "bitrate_mbps": 5
  }
}
```

### Content Themes

Themes rotate by day of week (defined in `scripts/run_workflow.py`):

- Monday: Market Opportunity
- Tuesday: Success Story
- Wednesday: Platform Feature
- Thursday: Educational
- Friday: Urgency
- Saturday: Trust
- Sunday: Community

To customize, edit the `CONTENT_THEMES` list in the script.

## 🎨 ElevenLabs Voice Configuration

Get your Arabic voice IDs from ElevenLabs:

1. Log in to https://elevenlabs.io
2. Go to Voice Library
3. Search for "Arabic" voices
4. Preview and select professional male and female voices
5. Copy Voice IDs to `config/config.json`

Recommended voices:
- **Male**: Look for "Professional", "News Anchor", or "Business" styles
- **Female**: Same criteria

Test voices with a sample script before going live.

## 🎭 Synthesia Avatar Configuration

Get your avatar IDs from Synthesia:

1. Log in to https://synthesia.io
2. Go to Avatars section
3. Filter by "Arabic" or "Middle Eastern" avatars
4. Select professional, business-appropriate avatars
5. Copy Avatar IDs to `config/config.json`

**Note**: Ensure avatars are appropriate for financial services content.

## 📺 YouTube Setup

### 1. Create YouTube Data API Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project: "Axia Video Automation"
3. Enable "YouTube Data API v3"
4. Create OAuth 2.0 credentials:
   - Application type: Web application
   - Authorized redirect URIs: `http://localhost:8080/`
5. Download credentials JSON

### 2. Authenticate

Run the authentication script (create this):

```bash
python3 scripts/youtube_auth.py
```

This will open a browser for OAuth flow and save the token.

### 3. Configure Channel

Update `config/config.json` with your Axia YouTube channel ID.

## 🧪 Testing

### Unit Tests

```bash
# Run all tests
python3 -m pytest tests/ -v

# Run specific test
python3 -m pytest tests/test_quality_checkers.py -v

# Run with coverage
python3 -m pytest tests/ --cov=scripts --cov-report=html
```

### Manual Testing

```bash
# Test script generation only
python3 scripts/test_script_generation.py

# Test quality checkers
python3 scripts/quality_checkers.py

# Test full workflow (dry run)
DRY_RUN=true python3 scripts/run_workflow.py
```

## 📊 Monitoring

### Check Logs

```bash
# View today's logs
tail -f logs/workflow_$(date +%Y%m%d)_*.log

# Search for errors
grep -i error logs/*.log

# View quality scores
grep -i "quality" logs/*.log
```

### Review Generated Content

```bash
# View generated scripts
ls -lht artifacts/scripts/

# View generated videos
ls -lht artifacts/videos/

# Play latest video
vlc $(ls -t artifacts/videos/*.mp4 | head -1)
```

### Database Queries

```sql
-- View recent executions
SELECT date, status, processing_time, video_url
FROM video_logs
ORDER BY date DESC
LIMIT 10;

-- Calculate success rate
SELECT
    status,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) as percentage
FROM video_logs
WHERE date > NOW() - INTERVAL '30 days'
GROUP BY status;

-- Average processing time
SELECT AVG(processing_time) as avg_minutes
FROM video_logs
WHERE status = 'success'
AND date > NOW() - INTERVAL '30 days';
```

## 🚨 Troubleshooting

### Script Generation Fails

**Issue**: Quality checkers failing repeatedly

**Solutions**:
1. Check GPT-5 Pro API key and quota
2. Review quality thresholds - may be too strict
3. Check Perplexity API for market data
4. Manually review failed scripts in `artifacts/scripts/`

### Audio Generation Fails

**Issue**: ElevenLabs API errors

**Solutions**:
1. Verify API key and quota
2. Check voice IDs are correct
3. Ensure script is valid UTF-8 Arabic text
4. Try a different voice ID

### Video Generation Takes Too Long

**Issue**: Synthesia processing > 15 minutes

**Solutions**:
1. This is normal for first-time renders
2. Check Synthesia dashboard for status
3. Ensure avatar IDs are correct
4. Consider switching to HeyGen as fallback

### YouTube Upload Fails

**Issue**: Upload errors or authentication issues

**Solutions**:
1. Re-run OAuth authentication
2. Check API quota (50 uploads/day default)
3. Verify video file is valid
4. Check file size < 256GB
5. Ensure channel ownership

### Quality Scores Too Low

**Issue**: Legitimate content failing checks

**Solutions**:
1. Review checker logic in `scripts/quality_checkers.py`
2. Adjust thresholds in `config/config.json`
3. Provide feedback to GPT-5 Pro via prompt engineering
4. Consider manual review bypass for edge cases

## 📈 Optimization

### Reduce API Costs

1. **Cache Perplexity results**: Market data doesn't change every second
2. **Batch operations**: Generate multiple scripts/videos if needed
3. **Use cheaper models**: Test with GPT-4 instead of GPT-5 Pro
4. **Optimize prompts**: Shorter prompts = lower costs

### Improve Quality

1. **Fine-tune prompts**: Iterate based on failed checks
2. **A/B test themes**: Track which themes perform best
3. **Analyze engagement**: Use YouTube Analytics to optimize
4. **Update knowledge**: Retrain checkers with successful examples

### Speed Up Processing

1. **Parallel API calls**: Where possible (audio + metadata)
2. **Pre-warm avatars**: Keep Synthesia avatars "hot"
3. **Local caching**: Cache voice/avatar configs
4. **Optimize video encoding**: Use hardware acceleration

## 🔒 Security

### API Key Rotation

Rotate API keys every 90 days:

```bash
# Script to rotate keys
./scripts/rotate_api_keys.sh
```

### Audit Logs

All workflow executions are logged:
- Script generation attempts
- Quality check results
- API calls
- Video uploads
- Errors and failures

Logs are stored in `logs/` and optionally in PostgreSQL.

### Compliance

- All videos include risk disclosure
- No guaranteed profit claims
- Regulatory compliance score: 95+ required
- Manual review for failed compliance checks

## 📞 Support

### Getting Help

1. Check logs: `logs/workflow_*.log`
2. Review this guide
3. Check n8n workflow execution logs
4. Review API documentation:
   - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
   - [ElevenLabs](https://elevenlabs.io/docs)
   - [Synthesia](https://docs.synthesia.io/)
   - [YouTube](https://developers.google.com/youtube/v3)

### Common Issues

See Troubleshooting section above.

## 📝 Changelog

### Version 1.0.0 (2025-10-24)
- Initial release
- 8-stage quality validation pipeline
- Daily automated execution at 9 AM GMT
- Support for Khaleeji Arabic
- TikTok-style vertical videos (9:16)
- Git worktrees for isolated development

## 🎯 Roadmap

### Phase 2 (Future)
- [ ] HeyGen integration as primary (if better results)
- [ ] Automated thumbnail generation
- [ ] Cross-platform posting (TikTok, Instagram Reels)
- [ ] A/B testing framework
- [ ] Voice cloning for consistency
- [ ] Multilingual support (English, Portuguese, Spanish)
- [ ] Analytics dashboard
- [ ] ML-based engagement prediction
- [ ] Automated content calendar

### Phase 3 (Future)
- [ ] Multi-brand support (Seekapa + Axia)
- [ ] Dynamic duration (30s, 60s options)
- [ ] Live market data integration
- [ ] Real-time trend detection
- [ ] Automated hashtag generation
- [ ] Community interaction analysis
- [ ] A/B test winner auto-promotion

---

**Last Updated**: 2025-10-24
**Maintainer**: Axia Automation Team
**License**: Proprietary
