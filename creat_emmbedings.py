import requests
import joblib
import os
import json
import pandas as pd

#create embeddings using ollama
def creat_embbeding(text_list):
    r = requests.post("http://localhost:11434/api/embed",json ={
        "model":"bge-m3",
        "input":text_list
    })

    embedding = r.json()['embeddings']
    return embedding


jsons = os.listdir("newjson")

chunk_id = 0
my_dict = []

for json_file in jsons:
    with open(f"newjson/{json_file}") as f:
       content = json.load(f)
    print(f"create Embeddings for {json_file}")
    embeddings = creat_embbeding( [c['text'] for c in content["chunks"]]) 


    for i , chunk in enumerate(content["chunks"]):
        
        
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dict.append(chunk)


    

#create  datafrme
df = pd.DataFrame.from_records(my_dict)



# Save all files
joblib.dump(df,'embeddings.joblib')

