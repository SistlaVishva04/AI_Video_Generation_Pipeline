import os

def ensure_directories():
    os.makedirs("assets/images", exist_ok=True)
    os.makedirs("assets/audio", exist_ok=True)
    os.makedirs("output", exist_ok=True)