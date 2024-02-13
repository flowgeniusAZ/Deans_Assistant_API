#deanslist.py

#Imports
import openai
from openai import OpenAI
import time
import streamlit as st

#Initialize OpenAI Clinet
client = OpenAI(api_key='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')

#Streamlit App Title
st.title('Dean\'s Assistant API')

#Streamlit image for branding
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQroYsyWjvZmkyguxf2_XUKqcWTNLkZrRbPzPL8MU5I&s', caption='John F Kennedy Middle School')

#Streamlit user input for the prompt
user_prompt = st.text_area("Enter your question:", "Kid was vaping in the bathroom. what consequences should i give?")

#Button to submit question
if st.button('Submit'):
    with st.spinner('Fetching response...'):
        #Retrieve existing assistant
        my_assistant = client.beta.assistants.retrieve("asst_VS8FnRtUoE2P5YvZHQ7h8LzJ")
        st.write("Assistant Retrieved:", my_assistant)

        #create thread and messages
        thread = client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        #create and monitor the run
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=my_assistant.id
        )

        while run.status != 'completed':
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            time.sleep(5)

            #fetch and display messages
            thread_messages = client.beta.threads.messages.list(thread.id)
            for message in thread_messages.data:
                if message.role == 'assistant':
                    st.write("Assistant says:", message.content)
