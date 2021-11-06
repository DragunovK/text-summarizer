from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.luhn import LuhnSummarizer

from utils.language import recognize


def abstract(text: str):
    language = recognize(text)

    parser = PlaintextParser.from_string(text, Tokenizer(language))

    summarizer = LuhnSummarizer()
    summary = summarizer(parser.document, 10)

    return summary
