# analyze_change.py

# 1. Read prompt template
with open("prompts/blast_radius_prompt.txt", "r") as f:
    prompt_template = f.read()

# 2. Read DevOps change
with open("examples/sample_change.yaml", "r") as f:
    devops_change = f.read()

# 3. Inject change into prompt
final_prompt = prompt_template.replace("{{USER_INPUT}}", devops_change)

# 4. Call AI tool
# Using environment variable for secure API key management
import os
import sys

# Get API key from environment variable
api_key = os.environ.get("AI_API_KEY")
if not api_key:
    raise ValueError(
        "AI_API_KEY environment variable is not set.\n"
        "Please set it using: export AI_API_KEY='your-api-key-here'"
    )

# Try multiple AI SDK options
response_text = None

# Option 1: Try BoB AI (company's AI service)
try:
    from bob import Client
    
    client = Client(api_key=api_key)
    response = client.generate(prompt=final_prompt)
    response_text = response.text
    print("✓ Using BoB AI")
    
except ImportError:
    pass

# Option 2: Try IBM watsonx (if available)
if not response_text:
    try:
        from ibm_watson_machine_learning.foundation_models import Model
        from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
        
        # Configure watsonx
        model = Model(
            model_id="ibm/granite-13b-chat-v2",
            credentials={"apikey": api_key, "url": "https://us-south.ml.cloud.ibm.com"},
            project_id=os.environ.get("IBM_PROJECT_ID", "")
        )
        
        response_text = model.generate_text(prompt=final_prompt)
        print("✓ Using IBM watsonx")
        
    except ImportError:
        pass

# Option 3: Try OpenAI (if available)
if not response_text:
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a DevOps expert analyzing infrastructure changes."},
                {"role": "user", "content": final_prompt}
            ]
        )
        response_text = response.choices[0].message.content
        print("✓ Using OpenAI")
        
    except ImportError:
        pass

# Option 4: Try Anthropic Claude (if available)
if not response_text:
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            messages=[
                {"role": "user", "content": final_prompt}
            ]
        )
        response_text = message.content[0].text
        print("✓ Using Anthropic Claude")
        
    except ImportError:
        pass

# If no AI SDK is available, show error
if not response_text:
    print("\n❌ ERROR: No AI SDK found.")
    print("\nPlease install one of the following:")
    print("  • BoB AI: Contact your AI team for installation")
    print("  • IBM watsonx: pip install ibm-watson-machine-learning")
    print("  • OpenAI: pip install openai")
    print("  • Anthropic: pip install anthropic")
    sys.exit(1)

# 5. Print result
print("=== DevOps Blast Radius Analysis ===")
print(response_text)
