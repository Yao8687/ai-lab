import os
from openai import OpenAI

key = os.environ.get("DEEPSEEK_API_KEY")
if not key:
    print("没读到 DEEPSEEK_API_KEY")
    raise SystemExit(1)

client = OpenAI(api_key=key, base_url="https://api.deepseek.com")

resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "用一句话解释 SQL 注入里 OR 1=1 为什么永真"}],
    temperature=0.3,
)
print(type(resp.choices))
print(len(resp.choices))
print(type(resp.choices[0]))
print(resp.choices[0].finish_reason)
print(resp.usage)
print(resp.choices[0].message.content)