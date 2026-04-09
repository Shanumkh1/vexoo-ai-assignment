# -------- PART 1: DOCUMENT INGESTION --------
from ingestion.loader import load_text
from ingestion.chunker import create_chunks
from ingestion.pyramid import build_pyramid
from retrieval.search import search_pyramid

# -------- PART 2: TRAINING --------
from training.data_loader import load_gsm8k
from training.tokenizer import get_tokenizer
from training.model import get_model
from training.trainer import train_model
from training.evaluator import evaluate_model


def run_part1():
    print("\n========== PART 1: DOCUMENT QA ==========")

    text = load_text("sample.txt")
    chunks = create_chunks(text, chunk_size=50, overlap=10)
    pyramid = build_pyramid(chunks)

    query = input("\nAsk something: ").strip().lower()
    result = search_pyramid(pyramid, query)

    print("\n--- Answer ---")

    if result:
        print(f"""
This is what I found:

👉 {result["summary"]}

Category: {result["category"]}
Key ideas: {", ".join(result["keywords"])}
""")
    else:
        print("No relevant answer found.")


def run_part2():
    print("\n========== PART 2: MODEL TRAINING ==========")

    train_data, test_data = load_gsm8k()
    tokenizer = get_tokenizer()
    model = get_model()

    train_model(model, tokenizer, train_data)
    evaluate_model(model, tokenizer, test_data)


def main():
    # Run both parts
    run_part1()
    run_part2()


if __name__ == "__main__":
    main()