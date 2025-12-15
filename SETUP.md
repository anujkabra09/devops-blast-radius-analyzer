# Setup Guide - DevOps Blast Radius Analyzer

## 🚨 Security Notice

This project has been updated to use **environment variables** for API key management. Never commit API keys to version control!

## Prerequisites

- Python 3.7+
- BoB AI SDK (your company's AI service)
- BoB API key

## Installation Steps

### 1. Install Dependencies

```bash
pip install bob
```

If the `bob` package is not publicly available, contact your company's AI team for installation instructions.

### 2. Configure API Key

**Option A: Using Environment Variables (Recommended)**

Set the environment variable in your terminal:

```bash
# On macOS/Linux
export AI_API_KEY='your-actual-api-key-here'

# On Windows (Command Prompt)
set AI_API_KEY=your-actual-api-key-here

# On Windows (PowerShell)
$env:AI_API_KEY='your-actual-api-key-here'
```

**Option B: Using .env File (Alternative)**

1. Copy the example file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your API key:
   ```
   AI_API_KEY=your-actual-api-key-here
   ```

3. Install python-dotenv:
   ```bash
   pip install python-dotenv
   ```

4. Add this to the top of `analyze_change.py`:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

### 3. Run the Analyzer

```bash
python3 analyze_change.py
```

## 🔐 Security Best Practices

1. **Never commit API keys** - The `.gitignore` file is configured to exclude `.env` files
2. **Rotate keys regularly** - Change your API keys periodically
3. **Use different keys per environment** - Separate keys for dev, staging, and production
4. **Revoke exposed keys immediately** - If a key is accidentally committed, revoke it right away

## Customizing the AI Provider

The current implementation uses the BoB AI SDK. The code is already configured to work with your company's AI service.

## Troubleshooting

### "AI_API_KEY environment variable is not set"

Make sure you've set the environment variable in your current terminal session. Environment variables don't persist across terminal sessions unless added to your shell profile.

### "Import 'bob' could not be resolved"

Install the BoB AI SDK:
```bash
pip install bob
```

If the package is not publicly available, contact your company's AI team for installation instructions or access to the internal package repository.

### ModuleNotFoundError: No module named 'bob'

This means the BoB SDK is not installed. Follow the installation instructions above or contact your AI team for the correct installation method.