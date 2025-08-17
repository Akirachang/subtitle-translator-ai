<p align="center">
  <img src="assets/logo.png" alt="subtitle-translator-ai" width="1600">
</p>

## Overview

Translate .srt subtitle files using Hugging Face Transformers (NLLB-200). Provides a simple Python API and a CLI.

### Features

This project keeps the SRT file as the source of truth:

- Parses SRT blocks with Pydantic and preserves index/timing
- Keeps basic HTML tags that is comprehensible by softwares (e.g. Davinci Resolve)
- Uses hugging face nlp model for many language pairs (fra_Latn → eng_Latn by default) - [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M)
- CLI and Python API

The result is a reliable, repeatable translation pipeline that works well on long files without drifting context or breaking your editor workflow (e.g., DaVinci Resolve).

## Motivation

I use DaVinci Resolve to automatically generate subtitles. It does a great job with timing and segmentation, but it doesn’t translate between languages. I tried ChatGPT and other LLMs, but long videos create extremely long contexts; chunking them naïvely often leads to hallucinations, mixed languages, or lost formatting.

This tool uses smaller, specialized translation models that run entirely on your local machine. Unlike general-purpose LLMs, these models are purpose-built for translation tasks, resulting in more consistent and reliable outputs without the unpredictability of LLMs.

## Install

Editable install for local development:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

The first run will download the model; expect a large download and some warm-up time.

## CLI

```bash
subtitle-translator sample.srt -o outputs/translated.srt --src-lang fra_Latn --tgt-lang eng_Latn
```

Options:

- --src-lang: source language (default: fra_Latn)
- --tgt-lang: target language (default: eng_Latn)

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
00:00:01,000 --> 00:00:03,500
<b>Bonjour! Bienvenue á Paris</b>
"""
sb = SubtitleBlock(block=block_text)
print(sb.index, sb.start_time, sb.end_time, sb.text)
print(sb.serialize())  # back to SRT block (with <b> tags)
```

## Notes

- Default model: facebook/nllb-200-distilled-600M
- Output preserves the original timing/index and wraps with tags.
