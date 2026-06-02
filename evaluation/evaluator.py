import sys
import os
import time
import pandas as pd

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from test_prompt import (
    BIAS_PROMPTS,
    FACTUAL_PROMPTS,
    JAILBREAK_PROMPTS,
    SAFETY_PROMPTS
)

from assistants.gemini_assistant import (
    get_gemini_response
)

from assistants.oss_assistant import (
    get_oss_response
)

results = []


def evaluate_category(
    prompts,
    category
):

    for prompt in prompts:

        print(
            f"\nTesting: {prompt}"
        )

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        # Gemini Response
        try:

            gemini_response = (
                get_gemini_response(
                    messages
                )
            )

        except Exception as e:

            gemini_response = (
                f"ERROR: {e}"
            )

        # OSS Response
        try:

            oss_response = (
                get_oss_response(
                    messages
                )
            )

        except Exception as e:

            oss_response = (
                f"ERROR: {e}"
            )

        results.append(
            {
                "Category": category,
                "Prompt": prompt,
                "Gemini": gemini_response,
                "OSS": oss_response
            }
        )

        print("✓ Completed")

        # Prevent Gemini rate limit
        time.sleep(15)


# Run Evaluations

print("\n===== FACTUAL TESTS =====")

evaluate_category(
    FACTUAL_PROMPTS,
    "Factual"
)

print("\n===== BIAS TESTS =====")

evaluate_category(
    BIAS_PROMPTS,
    "Bias"
)

print("\n===== SAFETY TESTS =====")

evaluate_category(
    SAFETY_PROMPTS,
    "Safety"
)

print("\n===== JAILBREAK TESTS =====")

evaluate_category(
    JAILBREAK_PROMPTS,
    "Jailbreak"
)

# Save Results

df = pd.DataFrame(results)

output_file = "evaluation_results.csv"

df.to_csv(

    output_file,
    index=False
)

print(
    f"\nResults saved to {output_file}"
)

print(
    "\nEvaluation Complete!"
)