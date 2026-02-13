import asyncio
import edge_tts
import os

async def text_to_speech(text, output_path):
    communicate = edge_tts.Communicate(text, "en-US-AriaNeural")
    await communicate.save(output_path)

def generate_voice(script):
    output_path = "assets/audio/voice.mp3"
    asyncio.run(text_to_speech(script, output_path))
    return output_path