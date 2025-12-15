# DevOps Blast Radius Analyzer

This project demonstrates the use of the company AI tool to analyze
DevOps changes and predict potential blast radius before production rollout.

## What it does
- Accepts a DevOps change (YAML/config)
- Sends it to the company AI model using a constrained DevOps prompt
- Receives structured risk analysis, checks, and rollback strategy

## Why AI is used
DevOps change risk assessment depends on experience.
This tool uses AI as a virtual senior DevOps reviewer to standardize
and automate that analysis.

## How to run

### Quick Start

1. **Activate virtual environment** (if using one):
   ```bash
   source venv/bin/activate
   ```

2. **Set your API key**:
   ```bash
   export AI_API_KEY='your-api-key-here'
   ```

3. **Run the analyzer**:
   ```bash
   ./run_analyzer.sh
   # OR
   python3 analyze_change.py
   ```

### Setup Instructions

See [`SETUP.md`](SETUP.md) for detailed installation and configuration instructions.

## Security

⚠️ **Important**: This project uses environment variables for API key management. Never commit API keys to version control.

- API keys are loaded from the `AI_API_KEY` environment variable
- The `.gitignore` file is configured to exclude sensitive files
- See [`SECURITY_INCIDENT.md`](SECURITY_INCIDENT.md) for security best practices

## Supported AI Providers

The analyzer automatically detects and uses available AI SDKs in this order:
1. **BoB AI** (company's AI service) - Priority
2. **IBM watsonx**
3. **OpenAI**
4. **Anthropic Claude**

Install the SDK for your preferred provider and set the appropriate API key.

## Testing

A mock BoB module (`bob.py`) is included for testing purposes. Replace it with the actual BoB SDK when available from your AI team.
