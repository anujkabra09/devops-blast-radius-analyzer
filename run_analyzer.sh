#!/bin/bash

# DevOps Blast Radius Analyzer Runner
# This script sets the API key and runs the analyzer

# Set your API key here (or it will prompt you)
API_KEY="${AI_API_KEY:-xxx}"

# Export the API key
export AI_API_KEY="$API_KEY"

echo "=== Running DevOps Blast Radius Analyzer ==="
echo "API Key set: ${API_KEY:0:10}..."
echo ""

# Run the analyzer
python3 analyze_change.py

# Made with Bob
