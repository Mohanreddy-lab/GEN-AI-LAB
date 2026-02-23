# 🧠 Text Similarity Checker using Sentence Transformers

A simple Python project that calculates **semantic similarity** between
two texts using pre-trained transformer models.

This project uses the `all-MiniLM-L6-v2` model from the Sentence
Transformers library to compute cosine similarity between two input
sentences.

------------------------------------------------------------------------

## 🚀 Features

-   Takes two text inputs from the user
-   Converts text into embeddings using a pre-trained transformer model
-   Calculates cosine similarity
-   Classifies similarity level as:
    -   🔴 Low
    -   🟡 Medium
    -   🟢 Max

------------------------------------------------------------------------

## 📌 Technologies Used

-   Python
-   Sentence-Transformers
-   HuggingFace Transformers
-   Cosine Similarity

------------------------------------------------------------------------

## 📦 Installation

Install the required library:

    pip install sentence-transformers

------------------------------------------------------------------------

## ▶️ How to Run

1.  Clone the repository:

    git clone
    https://github.com/your-username/text-similarity-checker.git

2.  Navigate to the project folder:

    cd text-similarity-checker

3.  Run the Python file:

    python similarity_check-gen_ai.py

4.  Enter two texts when prompted.

------------------------------------------------------------------------

## 🧠 How It Works

### Step 1: Load Pretrained Model

The project uses the `all-MiniLM-L6-v2` model.

### Step 2: Convert Text to Embeddings

Each sentence is converted into a numerical vector (embedding).

### Step 3: Compute Cosine Similarity

Cosine similarity measures how similar two vectors are.

Formula:

    similarity = (A · B) / (||A|| ||B||)

### Step 4: Classify Similarity

  Similarity Score   Level
  ------------------ --------
  \> 0.75            Max
  0.4 -- 0.75        Medium
  \< 0.4             Low

------------------------------------------------------------------------

## 📊 Example

Input: Text 1: Machine learning is amazing Text 2: AI is fascinating

Output: Similarity between the 2 texts is: 0.82 The similarity level is:
Max

------------------------------------------------------------------------

## 📁 Project Structure

    text-similarity-checker/
    │
    ├── similarity_check-gen_ai.py
    └── README.md

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Add GUI using Tkinter or Streamlit
-   Add plagiarism percentage output
-   Add file input support (.txt, .pdf)
-   Deploy as a web app
-   Add multi-language support

------------------------------------------------------------------------

## 👨‍💻 Author

Mohan Reddy\
B.Tech CSE (AI & ML)

------------------------------------------------------------------------

## ⭐ If You Like This Project

Give it a ⭐ on GitHub!
