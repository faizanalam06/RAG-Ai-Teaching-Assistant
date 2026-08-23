# RAG-Ai-Teaching-Assistant
RAG Ai Teaching Assistant that answers questions from course videos and provides relevant video timestamps using Whisper, embeddings, and semantic search
![(image)](https://github.com/faizanalam06/RAG-Ai-Teaching-Assistant/blob/7dfe77c84fd028ebd72daa2fa1bc8ee4c7a119ec/RAG.png)

How to use this RAG AI Teaching Assistant on your own data

Step 1 — Collect Your Videos
Move all your video files to the videos folder.

Step 2 — Convert to MP3
Convert all the video files to MP3 by running video_to_mp3.py.

Step 3 — Convert MP3 to JSON
Convert all the MP3 files to JSON by running mp3_to_text_to_chunk.py.

Step 4 — Convert JSON Files to Vectors
Use the creat_emmbedings.py file to convert the JSON files into a DataFrame with embeddings and save it as a Joblib pickle file.

Step 5 — Prompt Generation and Feeding to LLM
Read the Joblib file and load it into memory. Then create a relevant prompt according to the user's query and feed it to the LLM.
