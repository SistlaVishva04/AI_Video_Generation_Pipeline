from datetime import datetime
from modules.script_generator import generate_script
from modules.voice_generator import generate_voice
from modules.image_fetcher import fetch_images
from modules.video_builder import create_video
from modules.utils import ensure_directories
from modules.script_generator import generate_scene_prompts
from modules.subtitle_generator import generate_srt
from moviepy.editor import AudioFileClip
from modules.video_builder import add_subtitles
from modules.script_generator import generate_seo_metadata

def main():
    ensure_directories()

    topic = input("Enter video topic (short conceptual idea only): ")
    safe_topic = topic.replace(" ", "_").lower()
    print("Generating script...")
    script = generate_script(topic)
   
    print("Generating voice...")
    audio_path = generate_voice(script)


    audio = AudioFileClip(audio_path)
    generate_srt(script, audio.duration)
    print("Fetching images...")
    scenes = generate_scene_prompts(script)
    images = []
    for scene in scenes:
        scene_images = fetch_images(scene, count=1)
        if scene_images:
            images.extend(scene_images)

    print("Building video...")

    video_clip, audio = create_video(images, audio_path)

    video_with_subs = add_subtitles(video_clip, script, audio.duration)
    final_video = video_with_subs.set_audio(audio)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"output/{safe_topic}_{timestamp}.mp4"

    final_video.write_videofile(output_path, fps=24)

    print(f"\nVideo created successfully at: {output_path}")

    print("Generating SEO metadata...")
    metadata = generate_seo_metadata(script)

    with open("output/metadata.txt", "w", encoding="utf-8") as f:
        f.write(metadata)
   
    output_path = f"output/{safe_topic}_{timestamp}.mp4"

if __name__ == "__main__":
    main()