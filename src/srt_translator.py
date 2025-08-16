import re

from dotenv import load_dotenv

from src.api import SubtitleBlock
from src.utils import load_nlp_model, run_translation

load_dotenv()


def bootstrap_input(input_path: str):
    with open(input_path, "r", encoding="utf-8") as file:
        input_content = file.read()
    blocks = re.split(r"\n\s*\n", input_content.strip())

    subtitles = []
    for block in blocks:
        subtitle_block = SubtitleBlock(block=block)
        subtitles.append(subtitle_block)

    return subtitles


def translate_srt(input_path: str, output_path: str, target_language: str):
    load_nlp_model(model_name="facebook/nllb-200-distilled-600M")

    try:
        # Create translator and translate
        structured_subtitles = bootstrap_input(input_path)
        texts = [subtitle.text for subtitle in structured_subtitles]
        translated_texts = run_translation(texts)
        print(translated_texts)

    except Exception as e:
        print(f"Error: {e}")
