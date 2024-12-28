from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
