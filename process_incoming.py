import requests
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib




def creat_embbeding(text_list):
    r = requests.post("http://localhost:11434/api/embed",json ={
        "model":"bge-m3",
        "input":text_list
    })

    embedding = r.json()['embeddings']
    return embedding


def inference(prompt):
     r = requests.post("http://localhost:11434/api/generate",json ={
        "model":"llama3.2",
        "prompt":prompt,
        "stream":False

     })

     response = r.json()
     print(response)
     return response
    




# Load all files
df = joblib.load('embeddings.joblib')


incoming_query = input("Ask a Question: ")
queston_embedding = creat_embbeding([incoming_query])[0]


#find similarity of question_embedding
similarities = cosine_similarity(np.vstack(df['embedding']),[queston_embedding]).flatten()
#print(similarities)
top_result = 5
max_indx =  similarities.argsort()[::-1][0:top_result]
##print(max_indx)
new_df = df.loc[max_indx]




prompt = f''' i am teaching the numpy course , here are video subtaitals chunks containing video title,
video number, and video strat time in second  and end time in second and the text at the time

{new_df[["video_number","video_title","start","end","text"]].to_json(orient='records')}
------------------------------
{incoming_query}
User asked this questions related to this video chunks you have to answer in human way (don't mention format it's for you) then where and how much content is 
taught in which video file (in which video and at the timestamp) and guide the user to go to that particular
information. if user asks unrelated questions , tell him that you can only answer queston in realted in file
'''
with open("prompt.txt", "w") as f:
    f.write(prompt)

response = inference(prompt)['response']
print(response)

with open("response.txt","w") as f:
    f.write(response)

# print(new_df[['video_number','video_title',"text"]])

# for index , item in new_df.iterrows():
#     print(index,item['video_number'],item['video_title'],item['text'],item['start'],item['end'])