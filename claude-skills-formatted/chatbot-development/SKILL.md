---
name: chatbot-development
description: Develop and deploy intelligent chatbots for customer support, nurse matching, and client authentication using Azure Copilot Studio and AWS Bedrock.
---

# Chatbot Development Skill

## Active Projects

### 1. Wonder.care Nurse Matching Chatbot 🏥

**Objective**: Chat widget on website for matching nurses to clients based on criteria

**Technology Stack**:
- **Frontend**: Chat widget (web embed + WhatsApp)
- **Backend**: AWS Bedrock
- **Database**: PostgreSQL (AWS RDS)
- **Status**: In planning/development

**Matching Criteria**:
- Location (city/neighborhood)
- Language preferences (Arabic, English, Hebrew, etc.)
- Specialization (elderly care, post-op, pediatric, etc.)
- Availability (shifts, dates)
- Experience level
- Certifications
- Gender preference (if relevant culturally)
- Budget range

**Conversation Flow**:
```
Bot: Welcome to Wonder.care! I'll help you find the perfect nurse.

Bot: What's your location?
User: [City/Area]

Bot: What type of care do you need?
User: [Elderly care / Post-surgery / etc.]

Bot: What language should the nurse speak?
User: [Arabic / English / Hebrew]

Bot: When do you need care?
User: [Date range]

Bot: What's your budget range per hour?
User: [Amount]

Bot: Great! I found [N] nurses matching your criteria.
[Show top 3 matches with profiles]

Bot: Would you like to:
1. View more details
2. Book a consultation
3. Adjust criteria
```

**Technical Implementation**:
- **AWS Bedrock** (Claude or other LLM)
- **PostgreSQL** for nurse database + matching algorithm
- **WhatsApp Business API** for WhatsApp bot
- **Web Widget** for website integration

### 2. Seekapa & Axia Customer Support Chatbots 💬

**Objective**: Automated customer support using Azure Copilot Studio

**Phase 1**: Knowledge base chatbot (current)
- Answer common questions
- Explain policies
- Guide through platform features
- Multi-language support (4 languages)

**Phase 2**: Client database integration (future)
- Authenticate clients via email
- Check withdrawal status
- View account information
- Update personal details
- Submit support tickets

**Technology Stack**:
- **Platform**: Azure Copilot Studio
- **Knowledge Base**: 52 legal documents + FAQs
- **Authentication**: Email-based (link to Power BI preparing)
- **Languages**: English, Arabic, Portuguese, Spanish

**Key Features**:
1. **FAQ Answering**:
   - "How do I withdraw?"
   - "What are the fees?"
   - "Is this regulated?"
   - "Why can't I withdraw my full balance?"

2. **Policy Explanation**:
   - Reference specific legal documents
   - Explain margin requirements
   - Clarify fee structures
   - Detail complaint procedures

3. **Platform Guidance**:
   - How to open account
   - How to verify identity
   - How to make first deposit
   - How to place trades

4. **Multilingual Support**:
   - Detect user language
   - Respond in same language
   - Use appropriate terminology
   - Cultural sensitivity

**Knowledge Base Location**:
```
/home/odedbe/axia and seekapa documenation/
├── Axia Legal Documents (1)/
└── Seekapa Legal Documents New Version 26.05.2025/
```

**Authentication Flow** (Phase 2):
```
User: I want to check my withdrawal status
Bot: I'll need to verify your identity. Please enter your registered email.
User: client@example.com
Bot: I've sent a verification code to client@example.com. Please enter it.
User: [Code]
Bot: ✅ Verified! Your withdrawal status is: [Status from DB]
```

### 3. Validation Assistance Chatbot 📋

**Objective**: Help clients with ID verification documents

**Current Problem**:
- Many users struggle with document uploads
- Backoffice spends time calling clients
- Delays in verification process

**Solution**:
Chatbot to guide clients through:
1. Photo quality requirements
2. Document types accepted
3. Common rejection reasons
4. Step-by-step photo guide
5. Real-time validation feedback

**Features**:
- **Image Analysis**: Check if photo meets requirements
- **OCR**: Extract text for quick validation
- **Instant Feedback**: "Photo too blurry, please retake"
- **Multi-language**: Instructions in all 4 languages
- **App Push Integration**: Notify when docs received

**Technology**:
- Azure Computer Vision API
- Azure Form Recognizer (OCR)
- Copilot Studio for conversation
- Integration with existing verification system

## Chatbot Best Practices

### Conversation Design
✅ **Short responses** (2-3 sentences max)
✅ **Clear options** (buttons, quick replies)
✅ **Empathetic tone** ("I understand your concern...")
✅ **Transparency** (set expectations: "This may take 1-2 minutes...")
✅ **Fallback to human** (easy escalation path)

### Knowledge Management
- **Update regularly** when policies change
- **Version control** for knowledge bases
- **Track unanswered questions** for improvement
- **A/B test** responses for effectiveness

### Multilingual Considerations
- **Consistent terminology** across languages
- **Cultural sensitivity** in responses
- **Right-to-left** support for Arabic
- **Local examples** (currency, locations)

### Compliance & Security
- **Data privacy**: GDPR, local regulations
- **Authentication**: Secure verification methods
- **Audit logs**: Track all conversations
- **PII protection**: Mask sensitive data in logs

## Integration with Other Systems

### For Seekapa/Axia:
- **CRM**: Log conversations
- **Power BI**: Display data to authenticated users
- **Email**: Send verification codes
- **SMS**: Alternative 2FA method
- **Support Tickets**: Create tickets for human escalation

### For Wonder.care:
- **PostgreSQL**: Query nurse database
- **Matching Algorithm**: Score and rank nurses
- **Booking System**: Schedule appointments
- **WhatsApp**: Send confirmations and updates

## Development Workflow

### 1. Requirements Gathering
- Define use cases
- Map conversation flows
- Identify data sources
- Determine integrations

### 2. Design
- Create flow diagrams
- Write sample dialogues
- Design UI/UX
- Plan multilingual approach

### 3. Implementation
- Build conversation logic
- Connect data sources
- Implement authentication
- Add multilingual support

### 4. Testing
- Unit tests for logic
- Integration tests for APIs
- User acceptance testing
- Load testing

### 5. Deployment
- Gradual rollout
- Monitor performance
- Collect feedback
- Iterate and improve

## Tools & Technologies

### Azure Copilot Studio
- **Visual bot builder**
- **Integration with Azure services**
- **Multi-channel deployment** (web, Teams, etc.)
- **Analytics dashboard**

### AWS Bedrock
- **Multiple LLM options** (Claude, etc.)
- **Scalable infrastructure**
- **Pay-per-use pricing**
- **API access**

### n8n Integration
- **Workflow automation**
- **Connect multiple services**
- **Data transformation**
- **Scheduled tasks**

## Integration with Other Skills
- **Combine with**: `seekapa-brand` or `axia-brand` for brand voice
- **Combine with**: `multilingual-content` for translations
- **Combine with**: `forex-regulations` for compliance accuracy

## Metrics & KPIs

### User Satisfaction
- **CSAT Score**: Post-conversation rating
- **Resolution Rate**: Questions answered successfully
- **Escalation Rate**: How often human needed

### Performance
- **Response Time**: Average time to respond
- **Uptime**: Bot availability %
- **Accuracy**: Correct answers %

### Business Impact
- **Support Ticket Reduction**: % decrease
- **Conversion Rate**: Chat to sign-up
- **Cost Savings**: vs human support

## Notes
- Start simple, iterate based on real usage
- Monitor Arabic performance closely (dialect challenges)
- Plan for human handoff from day 1
- Keep knowledge base synchronized with legal doc updates
- Test authentication flows thoroughly before launch
