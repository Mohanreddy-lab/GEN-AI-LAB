!pip install sentence-transformers -q
from transformers import pipeline
#Load text generation model (GenAI)
generator = pipeline(
    "text-generation",
    model="gpt2"
    )
#input code
prompt = "Artificial Intelligence in finance will"
#generate text
result=generator(prompt,max_length=50,num_return_sequences=1)

print("AI Generated Text")
print(result[0]['generated_text'])
