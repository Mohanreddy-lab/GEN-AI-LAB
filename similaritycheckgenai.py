!pip install sentence-transformers -q
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')
#take input from user
text1=input("Enter the text 1: ")
text2=input("Enter the text 2: ")
#convert text to embeddingsing1,embedding2)
embedding1=model.encode(text1)
embedding2=model.encode(text2)
#calculate similarity
similarity=util.cos_sim(embedding1,embedding2)
print("Similarity between the 2 texts is: ", round(float(similarity),2))
if(similarity>0.75):
   print("the similarity level is: Max")
elif(similarity>0.4):
     print("the similarity level is: Medium")
else:
   print("the similarity level is: Low")
