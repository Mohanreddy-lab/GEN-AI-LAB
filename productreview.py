!pip install transformers torch pandas
from transformers import pipeline
import pandas as pd
sentiment = pipeline("sentiment-analysis")
reviews="""The laptop starts quickly and works smoothly for daily tasks.
The screen quality is clear and good for watching videos.
Battery backup is average and needs charging often.
The fan makes noise when many apps are running.
Overall, it is a good laptop for students but not for gaming.
"""

sentences = reviews.split(".")
pros=[]
cons=[]
for s in sentences:
  s=s.strip()
  if s=="":
    continue
  result = sentiment(s)[0]
  if result['label'] == 'POSITIVE':
    pros.append(s)
  else:
    cons.append(s)
#Take only 2 pros and 2 cons
pros=pros[:2]
cons=cons[:2]
#create table
df = pd.DataFrame({'Pros': pros, 'Cons': cons})
