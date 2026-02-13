from google import genai
import os
from dotenv import load_dotenv
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_seo_metadata(script):
    prompt = f"""
    Based on the following YouTube script generate:

    1. A catchy YouTube title under 60 characters
    2. A 150-word SEO optimized description
    3. 10 comma-separated tags

    Plain text only.
    
    Script:
    {script}
    """

    return generate_with_retry(prompt)


def generate_with_retry(prompt, max_retries=3):
    models_to_try = [
        "gemini-flash-latest",
        "gemini-2.5-flash"
    ]

    for model_name in models_to_try:
        for attempt in range(max_retries):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )
                return response.text.strip()

            except Exception as e:
                print(f"Model {model_name} failed (attempt {attempt+1}): {e}")
                time.sleep(2)

    raise Exception("All Gemini models failed.")


def generate_script(topic):
    prompt = f"""
    Write a 2-minute YouTube narration script about: {topic}

    Requirements:
    - Plain text only
    - No markdown
    - No emojis
    - No special characters
    - Around 250-300 words
    - Hook in first 2 sentences
    - Storytelling style
    """

    return generate_with_retry(prompt)


def generate_scene_prompts(script):
    prompt = f"""
    You are a visual director for a YouTube documentary video.

    Based on the following narration script, generate 6 highly detailed visual scene descriptions.

    Each scene must:
    - Be one sentence only
    - Describe people, environment, action, and mood
    - Include time of day or lighting if possible
    - Include camera style like wide shot, close up, cinematic, documentary style
    - Be realistic photography (not cartoon or illustration)
    - Be suitable for stock footage search

    Do NOT:
    - Use numbering
    - Add explanations
    - Use special characters
    - Add emojis

    Script:
    {script}
    """

    response_text = generate_with_retry(prompt)

    scenes = [line.strip() for line in response_text.split("\n") if line.strip()]
    scenes = [s for s in scenes if len(s) > 40]
    return scenes[:6]