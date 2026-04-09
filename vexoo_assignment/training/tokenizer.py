from transformers import AutoTokenizer

def get_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    return tokenizer


def tokenize_data(example, tokenizer):
    return tokenizer(
        example["question"],
        text_target=example["answer"],
        truncation=True,
        padding="max_length",
        max_length=128
    )