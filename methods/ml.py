from summarizer import TransformerSummarizer


def abstract(text: str) -> str:
    model = TransformerSummarizer(transformer_type="XLNet", transformer_model_key="xlnet-base-cased")
    summary = ''.join(model(text.replace('\n', ' ')))
    return summary
