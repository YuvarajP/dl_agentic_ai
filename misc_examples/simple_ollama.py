import ollama

# Simple chat interaction
response = ollama.chat(model='gemma3', messages=[
  {
    'role': 'user',
    'content': 'Explain how quantum entanglement works in one sentence.',
  },
])

print(response['message']['content'])