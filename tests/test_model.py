import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import sentiment_classification


def test_sentiment_classification():
    text = "I love you"
    out = sentiment_classification(text)
    assert out == "5 stars"
    assert type(out) == str

    text = "I hate you"
    out = sentiment_classification(text)
    assert out == "1 star"
