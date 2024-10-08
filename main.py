import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from fastapi import FastAPI

app = FastAPI()


# Create a function to do sentiment classification
@app.get("/sentiment_classification/{text}")
def sentiment_classification(text: str) -> str:
    """
    This function takes a text input and returns the sentiment classification logits.

    Args:
        text (str): The input text.

    Returns:
        str: The sentiment classification class.
    """
    tokenizer = AutoTokenizer.from_pretrained(
        "nlptown/bert-base-multilingual-uncased-sentiment"
    )
    model = AutoModelForSequenceClassification.from_pretrained(
        "nlptown/bert-base-multilingual-uncased-sentiment"
    )
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    logits = torch.softmax(logits, dim=1)
    out = torch.argmax(logits)
    idx2class = model.config.id2label
    out = idx2class[out.item()]
    return out


# # Test the function
# text = "I love you"
# out = sentiment_classification(text)
# print(out)
