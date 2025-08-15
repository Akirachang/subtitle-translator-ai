import argparse
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv


def bootstrap_input(input_path: str):
    with open(input_path, "r", encoding="utf-8") as file:
        input_content = file.read()
    blocks = re.split(r"\n\s*\n", input_content.strip())

    subtitles = []
    for block in blocks:
        lines = block.strip().split("\n")

        if len(lines) < 3:
            continue

        index = int(lines[0])
        start_time, end_time = lines[1].split(" --> ")


def main():
    parser = argparse.ArgumentParser(
        description="Translate SRT subtitle files using LLMs"
    )
    parser.add_argument("input", help="Input SRT file path")
    parser.add_argument("output", nargs="?", help="Output SRT file path (optional)")
    parser.add_argument(
        "--language",
        "-l",
        default=None,
        help="Target language for translation (e.g., 'Spanish', 'French', 'German')",
    )
    parser.add_argument(
        "--model",
        "-m",
        default=None,
        help="OpenAI model to use (default: gpt-4o)",
    )

    args = parser.parse_args()

    load_dotenv()

    target_language = args.language or os.getenv("TARGET_LANGUAGE", "Spanish")

    model = args.model or os.getenv("OPENAI_MODEL", "gpt-4o")

    input_path = args.input
    if args.output:
        output_path = args.output
    else:
        input_path_obj = Path(input_path)
        output_path = str(
            input_path_obj.parent
            / f"{input_path_obj.stem}_{target_language.lower()}{input_path_obj.suffix}"
        )

    try:
        # Create translator and translate
        translator = bootstrap_input(input_path)
        # translator.translate_srt(input_path, output_path, target_language)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
