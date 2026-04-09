from transformers import AutoModelForSeq2SeqLM

def get_model():
    model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")
    return model