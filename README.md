# 🚀 AI Video Generation Pipeline

An end-to-end automated AI-powered system that converts a single topic input into a YouTube-ready video.

This project demonstrates a modular Python-based pipeline integrating Generative AI, voice synthesis, stock media APIs, and video processing tools.

## 📌 Project Overview

This system takes a single topic as input and automatically:

- Generates a narration script using Google Gemini
- Creates AI voiceover using Edge-TTS
- Extracts cinematic scene prompts from the script
- Fetches high-quality stock images via Pexels API
- Builds a 16:9 video using MoviePy
- Generates subtitles (.srt) and embeds them into the video
- Creates SEO metadata (title, description, tags)
- Generates YouTube-ready thumbnail with title overlay

**Output:** A fully rendered YouTube-ready .mp4 file.

## 🏗 Architecture

```
User Topic
    ↓
Script Generation (Gemini)
    ↓
Scene Prompt Extraction
    ↓
Image Fetching (Pexels API)
    ↓
Voice Generation (Edge-TTS)
    ↓
Video Assembly (MoviePy + FFmpeg)
    ↓
Subtitle Embedding (ImageMagick)
    ↓
Thumbnail Generation (PIL)
    ↓
Final MP4 + Metadata + SRT + Thumbnail
```

The system is modular and fault-tolerant with retry logic and model fallback support.

## 🛠 Tools & Technologies Used

- **Google Gemini API** – Script and scene generation
- **Edge-TTS** – Neural voice synthesis
- **Pexels API** – High-quality stock images
- **MoviePy** – Video editing and composition
- **FFmpeg** – Video encoding backend
- **ImageMagick** – Subtitle rendering
- **PIL (Pillow)** – Thumbnail generation
- **Python 3.10+**

## 📂 Project Structure

```
ai_video_pipeline/
│
├── main.py
├── requirements.txt
├── .env.example
├── README.md
│
├── modules/
│   ├── script_generator.py
│   ├── voice_generator.py
│   ├── image_fetcher.py
│   ├── video_builder.py
│   ├── subtitle_generator.py
|   ├── thumbnail_generator.py
│   ├── moviepy_config.py
│   └── utils.py
│
├── assets/
│   ├── audio/
│   ├── images/
│   ├── thumbnails/
│   └── video/
│
└── output/
```

## ⚙ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd ai_video_pipeline
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install External Dependencies

#### FFmpeg
```bash
# Windows (using Chocolatey)
choco install ffmpeg

# macOS (using Homebrew)
brew install ffmpeg

# Linux (Ubuntu/Debian)
sudo apt-get install ffmpeg
```

Verify installation:
```bash
ffmpeg -version
```

#### ImageMagick
```bash
# Windows: Download from https://imagemagick.org/script/download.php/ImageMagick-Windows.exe
# Enable "Install legacy utilities"
# Add to system PATH

# macOS (using Homebrew)
brew install imagemagick

# Linux (Ubuntu/Debian)
sudo apt-get install imagemagick
```

Verify installation:
```bash
magick -version
```

### 5️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
PEXELS_API_KEY=your_pexels_api_key
```

## ▶ How to Run

```bash
python main.py
```

When prompted, enter a short conceptual topic:

```
Enter video topic: Future of AI in 2030
```

The script will:
1. Generate a narration script
2. Create AI voiceover
3. Fetch relevant images
4. Build the video with subtitles
5. Generate SEO metadata

## 📤 Output Files

After execution, the `output/` folder contains:

- `video_topic_timestamp.mp4` – Final rendered video with embedded subtitles
- `metadata.txt` – SEO title, description, and tags
- `subtitles.srt` – Subtitle file (standalone)
- `thumbnail.jpg` – YouTube-ready thumbnail (1280x720) with title overlay


The video includes:
- ✅ Embedded subtitles
- ✅ Synchronized narration
- ✅ Cinematic scene transitions
- ✅ 16:9 aspect ratio

## 🧠 Key Features

- 📸 **Scene-based visual matching** – Not generic slideshow
- 🔄 **Retry mechanism** – Multi-model fallback for API failures
- 🎬 **Cinematic scene prompt generation** – Detailed visual descriptions
- 📐 **Dynamic 16:9 video formatting** – YouTube standard
- 📝 **Automatic subtitle generation and embedding** – Synchronized with audio
- 🔍 **SEO metadata automation** – Title, description, tags
- 🎨 **Automatic thumbnail generation** – With topic text overlay
- ⏰ **Unique timestamp-based filenames** – No overwrites

## ⚠ Challenges Faced

- Handling Gemini API rate limits and model overload
- Resolving MoviePy and Pillow version conflicts
- Configuring FFmpeg and ImageMagick on Windows
- Managing subtitle rendering dependencies

## 🚀 Future Improvements

- Paragraph-level scene synchronization
- Background music integration
- Automatic YouTube upload via API
- Thumbnail generation
- Improved subtitle timing accuracy
- Multi-language support

## Author

S V Vishnu Vamsi


vishnuvamsi04@gmail.com
