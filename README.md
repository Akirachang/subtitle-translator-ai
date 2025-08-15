# SRT Translator

A Python script that translates SRT (SubRip) subtitle files using OpenAI's ChatGPT API. The script processes subtitles in chunks of 50 entries to avoid context length limitations while maintaining the original SRT formatting.

## Features

- ✅ Parses SRT files correctly with proper timing and formatting
- ✅ **HTML Tag Support**: Preserves formatting tags like `<b>`, `<i>`, `<u>` during translation
- ✅ Translates subtitle text using OpenAI's ChatGPT API
- ✅ Processes subtitles in chunks of 50 to avoid token limits
- ✅ Maintains original SRT format for DaVinci Resolve compatibility
- ✅ Supports multiple languages
- ✅ Handles multi-line subtitles properly
- ✅ Auto-generates output filenames
- ✅ Error handling and fallback encoding support

## Installation

1. Clone or download this repository
2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   TARGET_LANGUAGE=Spanish
   OPENAI_MODEL=gpt-3.5-turbo
   ```

## Usage

### Basic Usage

Translate an SRT file to Spanish (default):

```bash
python srt_translator.py input.srt
```

This will create a file named `input_spanish.srt` in the same directory.

### Specify Output File

```bash
python srt_translator.py input.srt output_translated.srt
```

### Specify Target Language

```bash
python srt_translator.py input.srt --language French
python srt_translator.py input.srt -l German
```

### Use Different OpenAI Model

```bash
python srt_translator.py input.srt --model gpt-4
```

### Complete Example

```bash
python srt_translator.py movie_subtitles.srt movie_subtitles_french.srt --language French --model gpt-4
```

## Configuration

You can configure default settings in the `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `TARGET_LANGUAGE`: Default target language (default: Spanish)
- `OPENAI_MODEL`: OpenAI model to use (default: gpt-3.5-turbo)

## Supported Languages

The script can translate to any language supported by ChatGPT. Common examples:

- Spanish
- French
- German
- Italian
- Portuguese
- Japanese
- Korean
- Chinese
- Russian
- Arabic

## How It Works

1. **Parse SRT**: The script reads and parses the input SRT file, extracting subtitle entries with their timing and text.

2. **Chunk Processing**: Subtitles are processed in chunks of 50 entries to stay within ChatGPT's context limits.

3. **Translation**: Each chunk is sent to the OpenAI API with a specialized prompt for subtitle translation.

4. **Format Preservation**: The original SRT format (timing, indexing) is preserved while only the text content is translated.

5. **Output**: A new SRT file is created with translated text, ready for import into video editing software like DaVinci Resolve.

## SRT Format Example

Input:

```
1
00:00:01,000 --> 00:00:03,000
Hello, how are you?

2
00:00:04,000 --> 00:00:06,000
I'm fine, thank you.
```

Output (Spanish):

```
1
00:00:01,000 --> 00:00:03,000
Hola, ¿cómo estás?

2
00:00:04,000 --> 00:00:06,000
Estoy bien, gracias.
```

### HTML Formatting Support

The script preserves HTML formatting tags during translation:

Input with formatting:

```
161
01:03:47,740 --> 01:03:49,125
<b>Good bread and a good baguette.</b>
```

Output (Spanish):

```
161
01:03:47,740 --> 01:03:49,125
<b>Buen pan y una buena baguette.</b>
```

Supported HTML tags: `<b>`, `<i>`, `<u>`, and other common formatting tags.

## Error Handling

The script includes robust error handling for:

- Malformed SRT files
- Encoding issues (tries UTF-8, falls back to Latin-1)
- API failures (returns original text for failed chunks)
- Missing or incorrect subtitle entries

## Requirements

- Python 3.7+
- OpenAI API key
- Internet connection for API calls
- Required packages (see `requirements.txt`)

## Cost Considerations

Translation costs depend on:

- Number of subtitles
- Length of subtitle text
- OpenAI model used (gpt-3.5-turbo is more cost-effective than gpt-4)

Estimate: A typical 2-hour movie with ~1000 subtitle entries costs approximately $0.50-$2.00 USD with gpt-3.5-turbo.

## Troubleshooting

### "Import openai could not be resolved"

Install the required packages:

```bash
pip install -r requirements.txt
```

### "OPENAI_API_KEY not found"

Make sure you've created a `.env` file with your API key:

```bash
cp .env.example .env
# Edit .env and add your API key
```

### "No subtitles found"

Check that your SRT file is properly formatted and contains valid subtitle entries.

### Poor translation quality

Try using a different model (gpt-4) or adjust the target language specification to be more specific (e.g., "Mexican Spanish" instead of "Spanish").

## License

This project is open source and available under the MIT License.
