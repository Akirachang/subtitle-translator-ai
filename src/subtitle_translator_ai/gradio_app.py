import tempfile

import gradio as gr

from .srt_translator import translate_srt

# Common language codes for the dropdown
LANGUAGES = {
    "English": "eng_Latn",
    "Spanish": "spa_Latn",
    "French": "fra_Latn",
    "German": "deu_Latn",
    "Italian": "ita_Latn",
    "Portuguese": "por_Latn",
    "Japanese": "jpn_Jpan",
    "Korean": "kor_Hang",
    "Chinese (Simplified)": "zho_Hans",
    "Chinese (Traditional)": "zho_Hant",
    "Arabic": "arb_Arab",
    "Russian": "rus_Cyrl",
    "Hindi": "hin_Deva",
    "Turkish": "tur_Latn",
    "Vietnamese": "vie_Latn",
    "Thai": "tha_Thai",
    "Polish": "pol_Latn",
    "Dutch": "nld_Latn",
    "Swedish": "swe_Latn",
    "Greek": "ell_Grek",
}


def process_translation(
    input_file,
    src_lang,
    tgt_lang,
    batch_size,
    progress=gr.Progress(),
):
    """
    Process the SRT file translation.

    Args:
        input_file: Uploaded SRT file
        src_lang: Source language name
        tgt_lang: Target language name
        batch_size: Batch size for translation
        progress: Gradio progress tracker

    Returns:
        Path to the translated file and status message
    """
    if input_file is None:
        return None, "Please upload an SRT file first!"

    if src_lang == tgt_lang:
        return None, "Source and target languages must be different!"

    try:
        progress(0, desc="Loading model...")

        # Get language codes
        src_code = LANGUAGES[src_lang]
        tgt_code = LANGUAGES[tgt_lang]

        # Create temporary output file
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".srt", delete=False, encoding="utf-8"
        ) as tmp_output:
            output_path = tmp_output.name

        progress(0.2, desc="Starting translation...")

        # Run translation
        translate_srt(
            input_path=input_file.name,
            output_path=output_path,
            src_lang=src_code,
            tgt_lang=tgt_code,
            batch_size=batch_size,
        )

        progress(1.0, desc="Translation complete!")

        success_msg = f"Translation complete! Translated from {src_lang} to {tgt_lang}"
        return output_path, success_msg

    except Exception as e:
        error_msg = f"Error during translation: {str(e)}"
        return None, error_msg


# Create custom orange theme
orange_theme = gr.themes.Soft(
    primary_hue="orange",
    secondary_hue="amber",
    neutral_hue="stone",
).set(
    button_primary_background_fill="*primary_500",
    button_primary_background_fill_hover="*primary_600",
    button_primary_text_color="white",
    slider_color="*primary_500",
)


def create_gradio_interface():
    """Create and configure the Gradio interface."""

    with gr.Blocks(
        theme=orange_theme,
        title="Subtitle Translator AI",
        css="""
        .gradio-container {
            font-family: 'Inter', sans-serif;
        }
        footer {
            visibility: hidden;
        }
        """,
    ) as demo:
        gr.Markdown(
            """
            # Subtitle Translator AI

            Translate SRT subtitle files while preserving timing and formatting.
            Powered by Meta's NLLB-200 model (200+ languages supported).
            """
        )

        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### Input")

                input_file = gr.File(
                    label="Upload SRT File",
                    file_types=[".srt"],
                    type="filepath",
                )

                with gr.Row():
                    src_lang = gr.Dropdown(
                        choices=list(LANGUAGES.keys()),
                        value="French",
                        label="Source Language",
                    )

                    tgt_lang = gr.Dropdown(
                        choices=list(LANGUAGES.keys()),
                        value="English",
                        label="Target Language",
                    )

                batch_size = gr.Slider(
                    minimum=1,
                    maximum=32,
                    value=16,
                    step=1,
                    label="Batch Size",
                    info="Higher values = faster but more memory usage",
                )

                translate_btn = gr.Button(
                    "Translate",
                    variant="primary",
                    size="lg",
                )

            with gr.Column(scale=1):
                gr.Markdown("### Output")

                status_msg = gr.Textbox(
                    label="Status",
                    interactive=False,
                    placeholder="Upload a file and click Translate to begin...",
                )

                output_file = gr.File(
                    label="Translated SRT File",
                    interactive=False,
                )

        gr.Markdown(
            """
            ---
            ### About

            This tool uses specialized translation models that run entirely on your local machine.
            The first run will download the NLLB-200 model (~2.5GB).

            **Features:**
            - Preserves timing and structure
            - Maintains HTML formatting tags
            - Supports 200+ languages
            - Runs completely offline
            - No API keys required

            [View Full Language List](https://github.com/facebookresearch/flores/blob/main/flores200/README.md#languages-in-flores-200) |
            [GitHub Repository](https://github.com/Akirachang/subtitle-translator-ai)
            """
        )

        # Wire up the translation button
        translate_btn.click(
            fn=process_translation,
            inputs=[input_file, src_lang, tgt_lang, batch_size],
            outputs=[output_file, status_msg],
        )

    return demo


def launch_app(share=False, server_name="127.0.0.1", server_port=7860, **kwargs):
    """
    Launch the Gradio app.

    Args:
        share: Whether to create a public link (default: False)
        server_name: Server hostname (default: "127.0.0.1")
        server_port: Server port (default: 7860)
        **kwargs: Additional arguments to pass to gr.Blocks.launch()
    """
    demo = create_gradio_interface()
    demo.launch(share=share, server_name=server_name, server_port=server_port, **kwargs)


if __name__ == "__main__":
    launch_app()
