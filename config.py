import os
from dotenv import load_dotenv

import google.generativeai as genai
from openai import OpenAI

# ==========================
# LOAD ENVIRONMENT VARIABLES
# ==========================

load_dotenv()

# ==========================
# GEMINI CONFIG
# ==========================

genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

gemini_model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# ==========================
# OPENROUTER CONFIG
# ==========================

openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv(
        "OPENROUTER_API_KEY"
    )
)

# ==========================
# RESPONSE GENERATOR
# ==========================

def generate_response(
    prompt,
    provider="Auto"
):

    try:

        # ======================
        # GEMINI ONLY
        # ======================

        if provider == "Gemini":

            response = (
                gemini_model.generate_content(
                    prompt
                )
            )

            return response.text

        # ======================
        # OPENROUTER ONLY
        # ======================

        elif provider == "OpenRouter":

            completion = (
                openrouter_client.chat.completions.create(
                    model="meta-llama/llama-3.3-70b-instruct",

                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )
            )

            return (
                completion
                .choices[0]
                .message
                .content
            )

        # ======================
        # AUTO MODE
        # ======================

        else:

            try:

                completion = (
                    openrouter_client.chat.completions.create(
                        model="meta-llama/llama-3.3-70b-instruct",

                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )
                )

                return (
                    completion
                    .choices[0]
                    .message
                    .content
                )

            except Exception as e:

                print(
                    "OpenRouter Failed:",
                    e
                )

                response = (
                    gemini_model.generate_content(
                        prompt
                    )
                )

                return response.text

    except Exception as e:

        return (
            f"⚠️ AI Error\n\n{str(e)}"
        )