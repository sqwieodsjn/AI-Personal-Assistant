BLOCKED_WORDS = [
    "hack",
    "malware",
    "virus",
    "steal passwords",
    "phishing",
    "ddos"
]


def safety_check(prompt):

    prompt = prompt.lower()

    for word in BLOCKED_WORDS:

        if word in prompt:

            return (
                "🚫 I cannot assist with harmful, illegal, or unsafe activities."
            )

    return None