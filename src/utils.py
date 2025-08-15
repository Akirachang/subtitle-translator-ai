import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI()


def query_llm(prompt: str, target_language: str, model: str = "gpt-4o"):
    system_prompt = """
        You are a professional subtitle translator. Translate subtitle text to 
        {target_language} while maintaining readability and proper subtitle timing. 
        Keep the [number] format intact. 
        """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,  # Lower temperature for more consistent translations
    )

    translated_text = response.choices[0].message.content.strip()
    return translated_text
