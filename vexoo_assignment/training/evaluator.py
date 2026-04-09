def evaluate_model(model, tokenizer, test_data):
    model.eval()

    correct = 0
    total = 0

    for i in range(20):  # test on 100 samples (fast)
        sample = test_data[i]

        inputs = tokenizer(sample["question"], return_tensors="pt")
        inputs.pop("token_type_ids", None)

        outputs = model.generate(**inputs, max_length=50)

        prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
        answer = sample["answer"]

        # simple match check
        if prediction.strip() in answer:
            correct += 1

        total += 1

    accuracy = correct / total
    print(f"\nAccuracy: {accuracy:.2f}")