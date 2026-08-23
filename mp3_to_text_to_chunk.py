import whisper
import os
import json

model = whisper.load_model("small")

audio_folder = "audios"
json_folder = "json"

os.makedirs(json_folder, exist_ok=True)

audios = os.listdir(audio_folder)

for audio in audios:

    audio_path = os.path.join(audio_folder, audio)

    # Example:
    # "1 How to Create Array in Numpy in Hindi.mp3"

    filename = os.path.splitext(audio)[0]

    # Get video number
    video_number = filename.split(" ", 1)[0]

    # Get video title
    video_title = filename.split(" ", 1)[1]

    print(f"Processing Video {video_number}: {video_title}")

    result = model.transcribe(
        audio_path,
        language="hi",
        task="translate",
        fp16=False
    )

    chunks = []

    for chunk_id, segment in enumerate(result["segments"]):

        chunk = {
            "video_number": int(video_number),
            "video_title": video_title,
            "chunk_id": chunk_id,
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"].strip()
        }

        chunks.append(chunk)

    data = {
        "chunks": chunks
    }

    json_file = os.path.join(
        json_folder,
        f"{video_number}_{video_title}.json"
    )

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Saved: {json_file}")