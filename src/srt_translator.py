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


def translate_srt(
    input_path: str, output_path: str, src_lang="fra_Latn", tgt_lang="eng_Latn"
):
    load_nlp_model(
        model_name="facebook/nllb-200-distilled-600M",
        src_lang=src_lang,
        tgt_lang=tgt_lang,
    )

    try:
        structured_subtitles = bootstrap_input(input_path)
        texts = [subtitle.text for subtitle in structured_subtitles]
        translated_texts = run_translation(texts)

        for subtitle, translated_text in zip(structured_subtitles, translated_texts):
            subtitle.text = translated_text

        with open(output_path, "w", encoding="utf-8") as file:
            for subtitle in structured_subtitles:
                block = subtitle.serialize()
                file.write(block + "\n\n")

        print(f"Translation completed. Output saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")
