#!/usr/bin/env python3
"""
Launch the Subtitle Translator AI Gradio web interface.

Usage:
    python run_gradio.py                    # Launch locally
    python run_gradio.py --share            # Create a public link
    python run_gradio.py --port 8080        # Custom port
"""

import argparse

from src.subtitle_translator_ai.gradio_app import launch_app


def main():
    parser = argparse.ArgumentParser(
        description="Launch the Subtitle Translator AI Gradio interface"
    )
    parser.add_argument(
        "--share",
        action="store_true",
        help="Create a public shareable link",
    )
    parser.add_argument(
        "--server-name",
        default="127.0.0.1",
        help="Server hostname (default: 127.0.0.1)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=7860,
        help="Server port (default: 7860)",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode",
    )

    args = parser.parse_args()

    print("Starting Subtitle Translator AI Gradio interface...")
    print(f"Server: http://{args.server_name}:{args.port}")
    if args.share:
        print("Creating public share link...")

    launch_app(
        share=args.share,
        server_name=args.server_name,
        server_port=args.port,
        debug=args.debug,
    )


if __name__ == "__main__":
    main()
