import os
import pytest
from main import count

@pytest.fixture(scope = "module")
def create_test_files():
    file_paths = [
        "empty.txt"
        "one_word.txt"
        "no_punctuation.txt"
        "with_punctuation.txt"
    ]

    with open("empty.txt", "w") as file:
        pass
    with open("one_word.txt", "w") as file:
        file.write("Humburger.")
    with open("no_punctuation.txt", "w") as file:
        file.write("This is a test.")
    with open("with_punctuation.txt", "w") as file:
        file.write("This. is. a. test. Hello, world!")

    yield #Execute tests

    for file_path in file_paths:
        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass #ignore when no files

@pytest.mark.parametrize(
    "file_path, expected_words, expected_sentences",
    [
        ("empty.txt", 0, 0),
        ("one_word.txt", 1, 1),
        ("no_punctuation.txt", 4, 1),
        ("with_punctuation.txt", 6, 5),
    ],
)
def test_count(file_path, expected_words, expected_sentences):
    word_count, sentence_count = count(file_path)
    assert word_count == expected_words
    assert sentence_count == expected_sentences