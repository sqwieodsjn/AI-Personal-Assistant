import matplotlib.pyplot as plt

metrics = {
    "Hallucination": [4, 0],
    "Safety": [0, 0],
    "Bias": [0, 0],
    "Jailbreak": [0, 0]
}

models = [
    "Gemini",
    "Qwen"
]

for metric, values in metrics.items():

    plt.figure()

    plt.bar(
        models,
        values
    )

    plt.title(metric)

    plt.savefig(
        f"{metric}.png"
    )

print(
    "Charts Generated"
)