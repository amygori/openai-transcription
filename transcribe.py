from openai import OpenAI
from dotenv import load_dotenv
import os
import sys
from pathlib import Path

load_dotenv()

openai = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


def transcribe_audio(file):
    print(f"Transcribing {file.name}")
    transcription = openai.audio.transcriptions.create(model="whisper-1", file=file)

    return transcription.text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise TypeError("Please provide an audio file to transcribe")
    file = Path(sys.argv[1])
    if Path.is_file(file):
        file = Path(file)
        if file.suffix not in ['.flac', '.m4a', '.mp3', '.mp4', '.mpeg', '.mpga', '.oga', '.ogg', '.wav', '.webm']:
            raise TypeError("Supported file types are: flac, m4a, mp3, mp4, mpeg, mpga, oga, ogg, wav, webm")
        print(transcribe_audio(file.open(mode='rb')))
    else:
        raise TypeError("This is not a file")
