#deanslist.py

#Imports
import openai
from openai import OpenAI
import time
import streamlit as st

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
 
    

# Add a spacer
st.write("")  # Adjust the number of these based on needed spacing
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

# Add a Streamlit footer
footer_html = """
<div style='position: absolute; bottom: 0; left: 0; width: 100%; text-align: right; padding: 10px;'>
    <p style='margin: 0;'>Powered by FlowGenius</p>
    <img src='https://media.licdn.com/dms/image/D5603AQGzpMfnqrHpvA/profile-displayphoto-shrink_800_800/0/1691028781928?e=2147483647&v=beta&t=DR35TiCIcWT711AOyjHTsWIf2E2L0t_ktfGDqrqSYiE' style='height: 50px; margin-top: 5px;'/>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
