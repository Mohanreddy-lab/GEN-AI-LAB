# GEN-AI-LAB
Text Addon Functionalities
This section details the text-focused capabilities implemented in this Colab notebook.

1. Text Similarity Calculation
This script utilizes the sentence-transformers library to calculate the cosine similarity between two input texts. It loads a pre-trained model (all-MiniLM-L6-v2) to encode the texts into embeddings, which are then used to determine their semantic similarity. The script prompts the user for two texts and outputs a similarity score, classifying it as Max, Medium, or Low based on predefined thresholds.

2. Text Generation with GPT-2
This script leverages the transformers library to perform text generation using a pre-trained GPT-2 model. It takes an initial prompt from the user and then generates a coherent continuation of that text, demonstrating generative AI capabilities.

3. Sentiment Analysis and Pros/Cons Extraction
This script performs sentiment analysis on a block of review-like text using the transformers library. It processes the input text sentence by sentence, identifies whether each sentence expresses a positive or negative sentiment, and then categorizes them into 'Pros' and 'Cons'. Finally, it presents a summary of the identified pros and cons, typically showing the top few from each category in a structured format.
