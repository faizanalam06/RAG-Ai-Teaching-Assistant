import os
import json
import math

n = 3

for filename in os.listdir("json"):
    if filename.endswith("json"):
        file_path = os.path.join("json", filename)
        print(file_path)

        with open(file_path, "r" , encoding="utf-8") as f:
            data = json.load(f) 
            #print(data.get('text'))
            
            new_chunks = []
            num_chunks = len(data['chunks'])
            num_groups = math.ceil(num_chunks / n)
            #print(num_groups)

            for i in range(num_groups):
                start_idx = i*n
                end_idx = min((i+1)*n, num_chunks)


                chunks_group = data['chunks'][start_idx:end_idx]

                new_chunks.append({
                   "video_number":data['chunks'][0]['video_number'],
                   "video_title":chunks_group[0]['video_title'],
                   "start": chunks_group[0]['start'],
                   "end":chunks_group[-1]['end'],
                   "text": " ".join(c['text'] for c in chunks_group)
                })



            # Save the file 
            os.makedirs("newjson", exist_ok=True)
            with open(os.path.join("newjson", filename), "w" , encoding="utf-8") as json_file:
                json.dump({"chunks": new_chunks}, json_file, indent=4  )
                #json.dump({"chunks": new_chunks, "text": data.get('text', "")}, json_file, indent=4)


