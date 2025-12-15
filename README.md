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
1. Configure company AI credentials
2. Update sample change file
3. Run:
   ```bash
   python analyze_change.py
