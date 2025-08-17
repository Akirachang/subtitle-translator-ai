from tqdm import tqdm
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

_translator = None


def load_nlp_model(
    model_name="facebook/nllb-200-distilled-600M",
    src_lang="fra_Latn",
    tgt_lang="eng_Latn",
):
    global _translator
    if _translator is not None:
        return _translator

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    _translator = pipeline(
        "translation",
        model=model,
        tokenizer=tokenizer,
        src_lang=src_lang,
        tgt_lang=tgt_lang,
    )


def run_translation(texts, batch_size=16, max_length=128):
    if _translator is None:
        load_nlp_model()

    out = []
    for i in tqdm(range(0, len(texts), batch_size), desc="Translating"):
        batch = texts[i : i + batch_size]
        batch_out = _translator(batch, batch_size=batch_size, max_length=max_length)
        out.extend(batch_out)

    return [o["translation_text"] for o in out]
