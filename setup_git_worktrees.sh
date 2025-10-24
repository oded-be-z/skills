#!/bin/bash
# Setup Git Worktrees for Axia Daily Video Automation
# Run this script to create the worktree structure

set -e  # Exit on error

echo "🌳 Setting up Git Worktrees for Axia Video Automation"
echo "=================================================="

# Configuration
BASE_DIR="/home/user"
PROJECT_NAME="axia-video-automation"
MAIN_REPO="${BASE_DIR}/${PROJECT_NAME}"

# Check if main repo exists
if [ -d "$MAIN_REPO" ]; then
    echo "⚠️  Main repository already exists at: $MAIN_REPO"
    read -p "Delete and recreate? (y/N): " confirm
    if [ "$confirm" != "y" ]; then
        echo "Exiting..."
        exit 1
    fi
    echo "🗑️  Removing existing repository..."
    cd "$BASE_DIR"
    # Remove existing worktrees first
    if [ -d "${MAIN_REPO}/.git" ]; then
        cd "$MAIN_REPO"
        git worktree remove ../axia-video-wt-development --force 2>/dev/null || true
        git worktree remove ../axia-video-wt-production --force 2>/dev/null || true
        git worktree remove ../axia-video-wt-testing --force 2>/dev/null || true
        cd "$BASE_DIR"
    fi
    rm -rf "$MAIN_REPO"
    rm -rf "${BASE_DIR}/axia-video-wt-development"
    rm -rf "${BASE_DIR}/axia-video-wt-production"
    rm -rf "${BASE_DIR}/axia-video-wt-testing"
fi

# Create main repository
echo "📁 Creating main repository..."
mkdir -p "$MAIN_REPO"
cd "$MAIN_REPO"
git init
git config user.name "Axia Automation"
git config user.email "automation@axia.trade"

# Create directory structure
echo "📂 Creating directory structure..."
mkdir -p workflows
mkdir -p scripts/{quality_checkers,video_generation,utils}
mkdir -p config
mkdir -p logs
mkdir -p artifacts/{videos,scripts,audio}
mkdir -p tests

# Create README
cat > README.md << 'EOF'
# Axia Daily Video Automation

Fully automated daily 20-second TikTok-style video generation for Axia YouTube channel.

## Features
- Daily automated execution at 9:00 AM GMT
- GCC dialect Arabic voiceovers (ElevenLabs)
- AI avatar videos (Synthesia/HeyGen)
- 8-stage quality validation pipeline
- Automatic YouTube upload
- Cross-platform distribution

## Worktrees Structure
- **main**: Core codebase (this directory)
- **development**: Active development and testing
- **production**: Deployed workflow (runs daily)
- **testing**: Isolated testing environment

## Quick Start
```bash
# Switch to development worktree
cd ../axia-video-wt-development

# Run workflow manually
python3 scripts/run_workflow.py

# Run tests
python3 -m pytest tests/
```

## Documentation
See `AXIA_DAILY_VIDEO_WORKFLOW.md` for comprehensive workflow documentation.
EOF

# Create .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# Logs
logs/*.log
*.log

# Artifacts (don't commit generated videos)
artifacts/videos/*.mp4
artifacts/audio/*.mp3
artifacts/scripts/*.txt

# Secrets
.env
config/secrets.json
*.key

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Database
*.db
*.sqlite
EOF

# Create initial config template
cat > config/config.template.json << 'EOF'
{
  "schedule": {
    "daily_time": "09:00",
    "timezone": "GMT"
  },
  "apis": {
    "azure_openai": {
      "endpoint": "https://models.inference.ai.azure.com",
      "model_gpt5": "gpt-4o",
      "model_gpt5_pro": "gpt-4o"
    },
    "elevenlabs": {
      "endpoint": "https://api.elevenlabs.io/v1",
      "voice_id_male": "VOICE_ID_MALE",
      "voice_id_female": "VOICE_ID_FEMALE"
    },
    "synthesia": {
      "endpoint": "https://api.synthesia.io/v2",
      "avatar_male": "AVATAR_ID_MALE",
      "avatar_female": "AVATAR_ID_FEMALE"
    },
    "heygen": {
      "endpoint": "https://api.heygen.com/v2"
    },
    "youtube": {
      "channel_id": "AXIA_CHANNEL_ID"
    }
  },
  "quality_thresholds": {
    "arabic_dialect": 85,
    "brand_compliance": 90,
    "regulatory_compliance": 95,
    "tiktok_optimization": 85,
    "visual_quality": 90,
    "brand_elements": 95,
    "av_sync": 90,
    "engagement_prediction": 80
  },
  "video": {
    "duration": 20,
    "resolution": "1080x1920",
    "fps": 30,
    "bitrate_mbps": 5
  },
  "retry": {
    "max_attempts": 3,
    "backoff_seconds": 5
  }
}
EOF

# Create requirements.txt
cat > requirements.txt << 'EOF'
# Core
openai>=1.0.0
requests>=2.31.0
python-dotenv>=1.0.0

# Video processing
opencv-python>=4.8.0
ffmpeg-python>=0.2.0
Pillow>=10.0.0

# Google APIs
google-api-python-client>=2.100.0
google-auth>=2.23.0
google-auth-oauthlib>=1.1.0

# Database
psycopg2-binary>=2.9.0
sqlalchemy>=2.0.0

# Utilities
schedule>=1.2.0
pytz>=2023.3
pyyaml>=6.0
jinja2>=3.1.2

# Testing
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-asyncio>=0.21.0

# Monitoring
sentry-sdk>=1.32.0
prometheus-client>=0.18.0
EOF

# Initial commit
echo "📝 Creating initial commit..."
git add .
git commit -m "Initial commit: Axia Daily Video Automation setup

- Directory structure created
- Configuration templates
- README and documentation
- Git worktrees ready for creation"

# Create worktrees
echo "🌿 Creating worktrees..."

echo "  - development branch..."
git worktree add ../axia-video-wt-development -b development
echo "  ✓ Development worktree created at: ../axia-video-wt-development"

echo "  - production branch..."
git worktree add ../axia-video-wt-production -b production
echo "  ✓ Production worktree created at: ../axia-video-wt-production"

echo "  - testing branch..."
git worktree add ../axia-video-wt-testing -b testing
echo "  ✓ Testing worktree created at: ../axia-video-wt-testing"

# Display worktrees
echo ""
echo "📋 Worktree Status:"
git worktree list

echo ""
echo "✅ Setup Complete!"
echo ""
echo "Worktrees created:"
echo "  📁 Main:        $MAIN_REPO"
echo "  🔧 Development: ${BASE_DIR}/axia-video-wt-development"
echo "  🚀 Production:  ${BASE_DIR}/axia-video-wt-production"
echo "  🧪 Testing:     ${BASE_DIR}/axia-video-wt-testing"
echo ""
echo "Next steps:"
echo "  1. cd ../axia-video-wt-development"
echo "  2. Copy .env file with API keys"
echo "  3. pip install -r requirements.txt"
echo "  4. Run tests: python -m pytest tests/"
echo "  5. Start development!"
