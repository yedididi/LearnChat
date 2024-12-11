import pytest
import resolve_path

from chatbot.generator import Generator

generator = Generator()


def test_generator() -> None:
    sentence_part = "hello from"
    text = generator.generate(sentence_part)
    assert text.startswith(sentence_part)
    assert len(text) > len(sentence_part)
