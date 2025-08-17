import argparse
from pathlib import Path

from .srt_translator import translate_srt


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="subtitle-translator",
        description="Translate .srt subtitle files using Transformers",
    )
    parser.add_argument("input", type=Path, help="Path to input .srt file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("outputs/translated.srt"),
        help="Path to write translated .srt file",
    )
    parser.add_argument(
        "--src-lang",
        default="fra_Latn",
        help="Source language code (default: fra_Latn)",
    )
    parser.add_argument(
        "--tgt-lang",
        default="eng_Latn",
        help="Target language code (default: eng_Latn)",
    )
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    translate_srt(
        str(args.input),
        str(args.output),
        src_lang=args.src_lang,
        tgt_lang=args.tgt_lang,
    )
    print(f"Translation complete! Output saved to: {args.output}")


if __name__ == "__main__":
    main()
