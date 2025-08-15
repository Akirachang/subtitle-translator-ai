import os
import re

from dotenv import load_dotenv

from src.api import SubtitleBlock

load_dotenv()


def bootstrap_input(input_path: str):
    with open(input_path, "r", encoding="utf-8") as file:
        input_content = file.read()
    blocks = re.split(r"\n\s*\n", input_content.strip())

    subtitles = []
    for block in blocks:
        subtitle_block = SubtitleBlock(block=block)
        print(f"Parsed block: {subtitle_block}")
        break


def translate_srt(input_path: str, output_path: str, target_language: str):
    model = os.getenv("OPENAI_MODEL", "gpt-4o")

    try:
        # Create translator and translate
        translator = bootstrap_input(input_path)
        # translator.translate_srt(input_path, output_path, target_language)

    except Exception as e:
        print(f"Error: {e}")
