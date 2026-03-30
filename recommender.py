from groq import Groq
import os

client = Groq(api_key="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")

def get_remedy(selected_symptoms):
    symptoms_text = ",".join(selected_symptoms)

    output = f"""A person is experiencing the following symptoms: {symptoms_text}.

    I only suggest home-remedy / desi-nuskhe for counter relief.
    Keep it:
    - Simple and Practical
    - Safe
    - Clearly state this is NOT a substitute for professional medical advice\
    """

    response = client.chat.completions.create(
    model="llama-3.1-8b-instant", 
    messages=[
        {"role": "user", "content": output}
    ],
    max_tokens=300
)

    return response.choices[0].message.content