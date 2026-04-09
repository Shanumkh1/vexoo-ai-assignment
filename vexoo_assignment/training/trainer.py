import torch
from torch.utils.data import DataLoader


def train_model(model, tokenizer, train_data):

    model.train()

    dataloader = DataLoader(train_data, batch_size=4, shuffle=True)

    optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

    for epoch in range(1):  # keep 1 epoch (fast)
        print(f"\nEpoch {epoch+1}")

        for i, batch in enumerate(dataloader):

            # 🔥 stop early to save time
            if i > 100:
                break

            inputs = tokenizer(
                batch["question"],
                text_target=batch["answer"],
                padding=True,
                truncation=True,
                return_tensors="pt"
            )

            # remove unsupported field
            inputs.pop("token_type_ids", None)

            outputs = model(**inputs)

            loss = outputs.loss

            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            if i % 10 == 0:
                print(f"Step {i}, Loss: {loss.item():.4f}")