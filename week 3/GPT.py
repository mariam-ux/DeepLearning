from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='openai-gpt')
set_seed(42)
generator("Hello, I'm a professor,", max_length=30, num_return_sequences=5)