from datetime import datetime
import random
import os

# Optional: Integrate OpenAI later if you want real AI-generated text
# from openai import OpenAI
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Daily AI insights examples
insights = [
    "AI Fact: Neural networks can recognize handwritten digits with >99% accuracy.",
    "AI Tip: Normalizing input data improves training speed and performance.",
    "Mini Example: In NLP, tokenization splits text into words or subwords..",
    "AI Fun Fact: GANs can generate realistic human faces that don't exist!",
    "Quick Tip: Dropout layers help prevent overfitting in neural networks.",
    "AI Fact: Transformers allow models to focus on relevant parts of sequences."
    "AI Fact : The Healthcare AI Imaging Market to Exceed $7 Billion by 2026."
    "AI Fact:AI in the Insurance Sector to Trim Claims Processing time by 70%."
    "AI Fact:AI literacy programs are now part of national curriculam in more than 20 countries."
]

# Pick a random insight
daily_insight = random.choice(insighs)

# Optional: Fetch from OpenAI API (uncomment to use real AI-generated content)
# response = client.responses.create(
#     model="gpt-4.1-mini",
#     input="Give me a short AI insight or tip for today."
# )
# daily_insight = response.output_text.strip()

# Log file
log_file = "daily_ai_log.md"

# Append today's insight with timestamp
with open(log_file, "a", encoding="utf-8") as f:
    f.write(f"### {datetime.now().strftime('%Y-%m-%d')}\n")
    f.write(f"- {daily_insight}\n\n")

print(f"✅ Logged today's AI insight: {daily_insight}")
