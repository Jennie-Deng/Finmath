import warnings
warnings.filterwarnings("ignore")
import os
from openai import OpenAI
import base64
from IPython.display import Markdown,Image,Latex, display
import requests
import json


file_path = "/Volumes/Jennie/Reasoning/FinMath/dataset/multiDemo.json"
with open(file_path, 'r') as file:
    data = json.load(file)
data=data[-1]

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
image_path='/Volumes/Jennie/Reasoning/FinMath/dataset/'+data.get("Image")
base64_image=encode_image(image_path)


display(Image(filename=image_path))

# api_key="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"
# url="https://api.openai.com/v1/chat/completions"
api_key = "sk-VUQOgoxNjtiPxFDo895535A3635847B7A903688099089385"
url = "https://api.xi-ai.cn/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization":f"Bearer {api_key}"
}

task_instruction = f"""
You are a financial expert. You are supposed to answer the given question. First, think through the problem step by step, documenting each necessary step clearly. Then, conclude your response with the final answer in your last sentence as “Therefore, the answer is \\boxed{{}}”.

Here is the question:
Share context: {data.get('Share Context')}

Question: {data.get('Question Text')}

Options: {data.get('Options')}

Let's think through the problem step by step to answer the given question. The reasoning steps should include math symbols, formulas, and equations properly formatted using Markdown. Ensure that any math symbols or equations are enclosed in inline `\( \)` for smaller formulas or in block `\[ \]` for larger equations. 

### Example output format:
- Use Markdown headers for numbering the steps (e.g., "### step 1. Step Title").
- For inline math symbols or expressions, use `\( \)` (e.g., `\( x = y \)`).
- For block math expressions, use `\[ \]` (e.g., `\[ x = \\frac{{a}}{{b}} \]`).
- The final answer should be placed in `\\boxed{{}}` format, allowing only a single letter for the final answer (e.g., `\\boxed{{A}}`).

Now, answer the question, ensuring that all reasoning steps and equations follow the format above.
Put your final answer in \\boxed{{}} and ensure only one letter (such as "A", "B", or "C") is inside the \\boxed{{}} (e.g., \\boxed{{A}}).
"""

payload = {
  "model":"gpt-4o",
  "messages":[
    {
      "role":"user",
      "content":[
        {
          "type":"text",
          "text": task_instruction
        },
        {
          "type":"image_url",
          "image_url":{"url": f"data:image/jpeg;base64,{base64_image}"}
        },
       {
          "type": "text",
          "text": "This image above is associated with the question text."
        }, 

      ]
    }
  ],
  "max_tokens":1000,
}
respon = requests.post(url, headers=headers, json=payload)
respon.json()
