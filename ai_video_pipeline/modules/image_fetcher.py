import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def fetch_images(query, count=1):
    if not PEXELS_API_KEY:
        raise ValueError("PEXELS_API_KEY not found in environment.")

    headers = {"Authorization": PEXELS_API_KEY}
    enhanced_query = f"{query}, realistic photography, cinematic lighting, 16:9, documentary style"

    url = "https://api.pexels.com/v1/search"
    params = {
        "query": enhanced_query,
        "per_page": count,
        "orientation": "landscape"
    }

    response = requests.get(url, headers=headers, params=params, timeout=10)

    if response.status_code != 200:
        raise Exception(f"Pexels API Error: {response.status_code}")

    data = response.json()
    photos = data.get("photos", [])

    if not photos:
        print(f"No images found for query: {query}")
        return []

    image_paths = []
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    for i, photo in enumerate(photos):
        img_url = photo["src"]["large2x"]  # higher resolution
        img_data = requests.get(img_url, timeout=10).content

        path = f"assets/images/{timestamp}_{i}.jpg"

        with open(path, "wb") as f:
            f.write(img_data)

        image_paths.append(path)

    return image_paths