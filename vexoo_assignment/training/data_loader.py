from datasets import load_dataset


def load_gsm8k():
    dataset = load_dataset("openai/gsm8k", "main")

    train_data = dataset["train"].select(range(300))
    test_data = dataset["test"].select(range(100))

    return train_data, test_data