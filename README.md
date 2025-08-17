<p align="center">
  <img src="assets/logo.svg" alt="subtitle-translator-ai" width="260">
</p>

## subtitle-translator-ai

Translate .srt subtitle files using Hugging Face Transformers (NLLB-200). Provides a simple Python API and a CLI.

### Features

- Parses SRT blocks with Pydantic and preserves index/timing
- Keeps basic HTML tags like <b> during round-trip
- Uses NLLB-200 for many language pairs (fra_Latn → eng_Latn by default)
- CLI and Python API

## Install

Editable install for local development:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
# Optional (recommended): install PyTorch for your platform
# pip install torch
```

The first run will download the model; expect a large download and some warm-up time.

## CLI

```bash
subtitle-translator sample.srt -o outputs/translated.srt --src-lang fra_Latn --tgt-lang eng_Latn
```

Options:

- --src-lang: source language code (default: fra_Latn)
- --tgt-lang: target language code (default: eng_Latn)

NLLB examples: spa_Latn (Spanish), deu_Latn (German), jpn_Jpan (Japanese), kor_Hang (Korean), zho_Hans (Chinese Simplified).

## Python API

```python
from subtitle_translator_ai import translate_srt, SubtitleBlock

# Translate a file
translate_srt(
   "sample.srt",
   "outputs/translated.srt",
   src_lang="fra_Latn",
   tgt_lang="eng_Latn",
)

# Parse and serialize a single block
block_text = """1
00:00:01,234 --> 00:00:03,456
Hello <b>world</b>!"""
sb = SubtitleBlock(block=block_text)
print(sb.index, sb.start_time, sb.end_time, sb.text)
print(sb.serialize())  # back to SRT block (with <b> tags)
```

## Notes

- Default model: facebook/nllb-200-distilled-600M
- For better performance, install a GPU-enabled torch for your platform.
- Output preserves the original timing/index and wraps text in <b>…</b> when writing.

## Development

```bash
pip install -e .
python run.py  # uses sample.srt → outputs/translated.srt
```

## License

MIT
