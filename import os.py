import os
from datetime import datetime
import whisper
from config import UPLOAD_FOLDER, TRANSCRIPT_FOLDER

# تحميل نموذج Whisper عند البداية
model = whisper.load_model("base")

def save_audio(file):
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    return filename, filepath

def transcribe_with_segments(filepath, language='ar'):
    result = model.transcribe(filepath, language=language, word_timestamps=True)
    segments = result.get("segments", [])
    return segments

def save_segments(segments, filename):
    name = filename.rsplit('.', 1)[0] + ".txt"
    path = os.path.join(TRANSCRIPT_FOLDER, name)
    full_text = ""
    for seg in segments:
        speaker = seg.get("speaker", "سبيكر ؟")
        text = seg.get("text", "").strip()
        full_text += f"[{seg['start']:.2f}-{seg['end']:.2f}] {speaker}: {text}\n"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    return name
