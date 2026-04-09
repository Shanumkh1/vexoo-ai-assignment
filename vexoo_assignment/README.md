# Vexoo AI Engineer Assignment

## Overview

This project implements an end-to-end AI system combining:

1. Document Ingestion & Knowledge Representation
2. Retrieval-based Question Answering
3. Reasoning Model Training (GSM8K)

The focus is on **system design, modularity, and scalability**, rather than raw model performance.

---

## Project Structure

```
vexoo_assignment/
│
├── ingestion/        # Document processing pipeline
├── retrieval/        # Query + search system
├── training/         # Model training + evaluation
├── utils/            # Helper functions
│
├── main.py           # Runs full system
├── sample.txt        # Input document
├── README.md
└── report.docx
```

---

## Part 1: Document Ingestion + Knowledge Pyramid

### Pipeline

Load Document → Chunk (Sliding Window) → Build Knowledge Pyramid → Retrieval

### Key Features

* Sliding window chunking with overlap
* 4-layer Knowledge Pyramid:

  * Raw Text
  * Summary
  * Category
  * Keywords
* Multi-layer retrieval (raw + summary + keywords)

### Example

Input:

```
What is AI?
```

Output:

```
Artificial Intelligence is changing the world
```

---

## Part 2: GSM8K Reasoning Model

### Components

* Dataset: GSM8K (via Hugging Face)
* Model: T5-small (lightweight simulation of LLM)
* Tokenization: Transformer tokenizer
* Training: Basic supervised fine-tuning loop
* Evaluation: Approximate accuracy matching

### Optimizations

* Reduced dataset size (for faster execution)
* Early stopping in training loop
* Lightweight configuration for CPU execution

---

## How to Run

### 1. Install Dependencies

```
python -m pip install torch transformers datasets
```

---

### 2. Run the System

```
python main.py
```

---

### 3. Flow

* Part 1: Ask a question based on document
* Part 2: Model trains and evaluates automatically

---

## Design Philosophy

* Modular architecture (each component isolated)
* Replaceable components (easy to swap models or logic)
* Scalable pipeline (can extend to large datasets / real LLMs)
* Focus on reasoning + structure over brute-force performance

---

## Notes

* Training is intentionally lightweight due to compute constraints
* Accuracy is not the primary goal—pipeline correctness is
* System simulates real-world RAG + fine-tuning workflow

---

## Future Improvements

* Replace keyword matching with embeddings (FAISS)
* Use real summarization models instead of placeholders
* Add LoRA-based fine-tuning
* Introduce reasoning-aware routing layer

---

## Conclusion

This project demonstrates the ability to design and implement a complete AI pipeline:

Document → Knowledge → Retrieval → Reasoning Model

The emphasis is on **thinking like a systems architect**, not just writing code.
