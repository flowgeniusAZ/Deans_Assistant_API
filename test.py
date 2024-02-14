#test.py

import streamlit as st
from openai import OpenAI
import time
 
assistant_key = st.secrets.openai.assistant_key
client = OpenAI(st.secrets.openai.api_key)
thread = client.beta.threads.create()
threadid = thread.id
messages = []
 
def get_run(varAsstId, varThreadId):
    run = client.beta.threads.runs.create(
        thread_id=varThreadId,
        assistant_id=varAsstId
    )
 
    while run.status == "in_progress" or run.status=="queued":
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            run_id=run.id,
            thread_id=varThreadId
        )
 
        if run.status == "completed":
            message_list = reversed(client.beta.threads.messages.list(
                thread_id=varThreadId
            ))
 
            message_data = message_list.data
            for thread_message in message_data.content:
                for message_content in thread_message.content:
                    message_text = message_content.text.value
 
                    st.chat_message(thread_message.role).markdown(message_text)
