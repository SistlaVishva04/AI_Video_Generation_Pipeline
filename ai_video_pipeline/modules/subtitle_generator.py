def format_time(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)

    return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"


def generate_srt(script, audio_duration):
    sentences = [s.strip() for s in script.split(". ") if s.strip()]
    segment_duration = audio_duration / len(sentences)

    srt_content = ""
    current_time = 0

    for i, sentence in enumerate(sentences):
        start = current_time
        end = current_time + segment_duration

        srt_content += f"{i+1}\n"
        srt_content += f"{format_time(start)} --> {format_time(end)}\n"
        srt_content += sentence + "\n\n"

        current_time = end

    with open("output/subtitles.srt", "w", encoding="utf-8") as f:
        f.write(srt_content)