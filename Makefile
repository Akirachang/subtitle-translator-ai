.PHONY: install translate gradio clean

install:
	pip install -e .

translate:
	subtitle-translator $(INPUT) -o $(or $(OUTPUT),outputs/translated.srt)

gradio:
	python -m subtitle_translator_ai.gradio_app

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf build dist *.egg-info src/*.egg-info
