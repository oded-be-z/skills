---
name: n8n-workflows
description: Create and manage n8n workflows for content automation, API integrations, and process optimization with workarounds for MCP integration issues.
---

# n8n Workflow Automation Skill

## Current Status
**User feedback**: "I have [n8n workflows] but they are not really good ones, claude-code tend to have issues to create them properly with n8n mcp or something."

**Challenge**: Claude Code struggles with n8n MCP integration

## n8n Access
**API Key**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3YjM5MjE0MS0wNmNkLTQ0ZDktYjZmZS1mMzJhOGVmMDkxMjIiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzYwOTQyNDg3fQ.053e7Mh63ZgrMSP6Hc3lcskDfhJGop1FBSc1iR9XETw`

**Project Location**: `/home/odedbe/n8n-seekapa-content/`

## Known Issues with n8n MCP

### Problem 1: MCP Integration Failures
- Claude Code has trouble creating workflows via n8n MCP
- Workflows may not execute properly
- Node connections fail

### Solution Approaches:
1. **Manual JSON Export/Import**: Create workflow JSON manually, import via UI
2. **n8n API Direct**: Use n8n REST API instead of MCP
3. **Template-Based**: Start with working templates, modify
4. **Hybrid**: Use Claude Code for logic, manual for n8n setup

## Priority Workflows

### 1. Seekapa/Axia Content Automation 📝

**Objective**: Automate blog and web content creation

**Current Status**: `/home/odedbe/n8n-seekapa-content/` exists but needs improvement

**Workflow**:
```
[Trigger: Daily Schedule]
    ↓
[Perplexity: Market Research] → Get latest forex news
    ↓
[GPT-5-Pro: Content Strategy] → Plan article topics
    ↓
[GPT-5: Write English Article]
    ↓
[GPT-5: Translate to Arabic]
    ↓
[GPT-5: Translate to Portuguese]
    ↓
[GPT-5: Translate to Spanish]
    ↓
[Store in Database / Send to CMS]
    ↓
[Notify: Content Ready]
```

**Improvements Needed**:
- Better API error handling
- Quality validation before publishing
- SEO optimization checks
- Brand voice consistency validation

### 2. YouTube Video Automation 🎥

**Objective**: Daily 1-minute market videos

**Workflow**:
```
[Trigger: Daily 6:00 AM GMT]
    ↓
[Fetch Market Data] → Forex prices
    ↓
[Perplexity: Latest News]
    ↓
[GPT-5-Pro: Analyze Market]
    ↓
[GPT-5: Write Arabic Script]
    ↓
[ElevenLabs: Generate Audio]
    ↓
[Synthesia/HeyGen: Create Video]
    ↓
[YouTube API: Upload]
    ↓
[Cross-post: Social Media]
```

### 3. Customer Support Automation 💬

**Objective**: Route and respond to support queries

**Workflow**:
```
[Trigger: New Support Email/Chat]
    ↓
[Detect Language] → English/Arabic/Portuguese/Spanish
    ↓
[Classify Intent] → Withdrawal/Technical/Account/General
    ↓
[Check Knowledge Base] → Azure Copilot Studio
    ↓
[If Solved] → Send Response
    ↓
[If Not Solved] → Create Ticket for Human
    ↓
[Log Conversation]
```

### 4. Voice Agent Call Processing 📞

**Objective**: Process and analyze sales calls

**Workflow**:
```
[Trigger: Call Ends]
    ↓
[Azure Speech: Transcribe]
    ↓
[Detect Language]
    ↓
[GPT-5-Pro: Analyze Conversation]
    ↓
[Extract: Objections, Outcomes, Sentiment]
    ↓
[Store in Database]
    ↓
[If Successful] → Add to Training Data
    ↓
[If Follow-up Needed] → Create Task
```

### 5. Document Validation Workflow 📋

**Objective**: Assist with ID verification

**Workflow**:
```
[Trigger: Document Uploaded]
    ↓
[Azure Computer Vision: Analyze Image]
    ↓
[Check: Quality, Type, Readability]
    ↓
[If Pass] → Azure Form Recognizer (OCR)
    ↓
[Extract: Name, ID Number, Expiry]
    ↓
[Validate Against Client Data]
    ↓
[If Match] → Approve
    ↓
[If Issues] → Chatbot Notify User
```

## n8n Best Practices

### Node Connection Strategy
✅ **Do**:
- Use error handling nodes
- Add wait/delay nodes for rate limits
- Include conditional branches
- Log workflow execution
- Use environment variables for API keys

❌ **Don't**:
- Hardcode credentials
- Skip error handling
- Create overly complex single workflows
- Ignore rate limits
- Mix staging and production workflows

### Workflow Organization
```
workflows/
├── production/
│   ├── seekapa-content-daily.json
│   ├── axia-content-daily.json
│   ├── youtube-automation.json
│   └── support-routing.json
├── staging/
│   └── [test versions]
└── templates/
    ├── api-call-template.json
    ├── translation-template.json
    └── social-media-template.json
```

### Version Control
- Export workflows as JSON
- Commit to git repository
- Tag production releases
- Document changes in README

## Alternative: Direct n8n API Usage

If MCP continues to fail, use n8n REST API directly:

### Create Workflow via API:
```bash
curl -X POST https://your-n8n-instance.com/api/v1/workflows \
  -H "X-N8N-API-KEY: eyJhbGciOiJIUzI1NiIs..." \
  -H "Content-Type: application/json" \
  -d @workflow.json
```

### Execute Workflow:
```bash
curl -X POST https://your-n8n-instance.com/api/v1/workflows/{id}/execute \
  -H "X-N8N-API-KEY: eyJhbGciOiJIUzI1NiIs..." \
  -d '{"data": {...}}'
```

### Get Workflow Status:
```bash
curl -X GET https://your-n8n-instance.com/api/v1/executions/{executionId} \
  -H "X-N8N-API-KEY: eyJhbGciOiJIUzI1NiIs..."
```

## Workflow Templates

### Template: API Call with Retry Logic
```json
{
  "nodes": [
    {
      "type": "n8n-nodes-base.httpRequest",
      "name": "API Call",
      "retryOnFail": true,
      "maxTries": 3,
      "waitBetweenTries": 5000
    },
    {
      "type": "n8n-nodes-base.if",
      "name": "Check Success"
    },
    {
      "type": "n8n-nodes-base.errorTrigger",
      "name": "Handle Error"
    }
  ]
}
```

## Integration with Other Systems

### Azure OpenAI
- Use HTTP Request node
- Authentication: API key in header
- Handle rate limits (100K-150K TPM)

### Perplexity API
- Endpoint: https://api.perplexity.ai
- For deep research tasks
- Parse JSON responses

### ElevenLabs
- Text-to-speech generation
- Handle audio file downloads
- Store audio for later use

### Synthesia/HeyGen
- Video generation APIs
- Webhook-based responses
- Handle video file URLs

## Monitoring & Debugging

### Execution Logs
- Review failed executions
- Check error messages
- Monitor execution times
- Track API rate limits

### Alerting
- Email on workflow failures
- Slack notifications for critical workflows
- Daily summary reports

### Performance
- Optimize slow workflows
- Reduce unnecessary API calls
- Use webhook triggers instead of polling
- Cache repeated requests

## Development Workflow

### 1. Design Phase
- Map out workflow logic
- Identify API dependencies
- Plan error handling
- Document expected inputs/outputs

### 2. Build Phase
- Start with n8n UI (manual)
- Test each node individually
- Connect nodes gradually
- Add error handlers

### 3. Test Phase
- Run with test data
- Verify all branches work
- Check error scenarios
- Validate output format

### 4. Deploy Phase
- Export workflow JSON
- Commit to git
- Import to production n8n
- Monitor first executions

### 5. Maintain Phase
- Review execution logs weekly
- Update on API changes
- Optimize based on performance
- Document improvements

## Integration with Other Skills
- **Combine with**: `youtube-automation` for video workflows
- **Combine with**: `chatbot-development` for support automation
- **Combine with**: `multilingual-content` for translation workflows
- **Combine with**: `voice-agents` for call processing

## Notes
- MCP integration issues confirmed
- Focus on n8n API or manual JSON export/import
- Keep workflows simple and modular
- Test extensively before production
- Document all workflows thoroughly
- Consider hiring n8n expert if issues persist
