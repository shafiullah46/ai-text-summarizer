import os
from openai import OpenAI

# Initialize the OpenAI client with environment variables
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_API_BASE')
)

def summarize(text: str) -> str:
    """
    Summarizes the provided text paragraph into a single-line summary.
    """
    parameterized_prompt = (
        f"Summarize the following paragraph into exactly one single-line summary. "
        f"Keep it concise, direct, and under one line. Do not include any introductory text or markdown.\n\n"
        f"Paragraph:\n{text}"
    )
    
    response = client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[
            {"role": "user", "content": parameterized_prompt}
        ],
        max_tokens=80,
        temperature=0.5
    )
    
    try:
        summary_text = response.choices[0].message.content.strip()
    except (TypeError, AttributeError):
        try:
            choice = response['choices'] if isinstance(response, dict) else response.choices
            if isinstance(choice, list) and len(choice) > 0:
                item = choice[0]
                if isinstance(item, dict):
                    summary_text = item['message']['content'].strip()
                else:
                    summary_text = item.message.content.strip()
            elif isinstance(choice, dict):
                summary_text = choice['message']['content'].strip()
            else:
                summary_text = str(response)
        except Exception:
            summary_text = str(response)
            
    return summary_text

if __name__ == "__main__":
    input_text = "Artificial Intelligence enables machines to mimic human intelligence, performing tasks such as learning, problem-solving, and decision-making with increasing accuracy."
    
    response_summary = summarize(input_text)
    print("--- Generated One-Line Summary ---")
    print(response_summary)
