from . import moviepy_config

from moviepy.editor import (
    AudioFileClip,
    ImageClip,
    concatenate_videoclips,
    TextClip,
    CompositeVideoClip,
)
def create_video(image_paths, audio_path):

    if not image_paths:
        raise ValueError("No images fetched. Cannot build video.")

    audio = AudioFileClip(audio_path)
    duration_per_image = audio.duration / len(image_paths)

    clips = []

    for img in image_paths:
        clip = (
            ImageClip(img)
            .set_duration(duration_per_image)
            .resize(height=720)
            .fadein(0.5)
            .fadeout(0.5)
        )
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")

    # IMPORTANT: Do NOT write here
    return video, audio


def add_subtitles(video, script, audio_duration):

    sentences = [s.strip() for s in script.split(". ") if s.strip()]
    segment_duration = audio_duration / len(sentences)

    subtitles = []
    current_time = 0

    for sentence in sentences:
        txt = (
            TextClip(
                sentence,
                fontsize=40,
                color="white",
                size=(1000, None),
                method="caption",
            )
            .set_position(("center", "bottom"))
            .set_duration(segment_duration)
            .set_start(current_time)
        )

        subtitles.append(txt)
        current_time += segment_duration

    return CompositeVideoClip([video, *subtitles])