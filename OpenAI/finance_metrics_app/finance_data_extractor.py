import json
import os

import pandas as pd
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_prompt(text):
    prompt = f"""
    You are an expert in finance and accounting. You are given a text  from a news article that contains financial data.
    Your task is to extract the some relevant data and return it in a structured format.
    The fields you have to extract are:
    Company Name, Revenue, Net Income, Earnings Per Share (EPS), Stock Symbol.
    You may not find the Stock Symbol in the text. You have to apply your general knowledge to find it and
    if you cannot find it, you can leave it blank (and return empty string for Stock Symbol).
    Return the answer in json. Dont provide any extra text/explanation.
    Example:
    "Company Name": "Walmart",
    "Stock Symbol": "WMT",
    "Revenue": "12.34 million",
    "Net Income": "34.78 million",
    "EPS": "2.1 $"
    Here is the text:
    {text}
    """
    return prompt


def extract_data(text):
    frame = pd.DataFrame()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": generate_prompt(text=text)}],
        response_format={"type": "json_object"},
    )
    content = response.choices[0].message.content
    try:
        json_content = json.loads(content)
        frame = pd.DataFrame(json_content.items(), columns=["Measure", "Values"])
    except (json.JSONDecodeError, IndexError) as err:
        print(err)
    finally:
        return frame


if __name__ == "__main__":
    text = """
    The company reported a 10% increase in revenue for the quarter, driven by strong sales of its flagship product, the iPhone.
    The company also announced a new product, the iPhone 15, which is expected to be a hit with consumers.
    """
    print(extract_data(text=text))
