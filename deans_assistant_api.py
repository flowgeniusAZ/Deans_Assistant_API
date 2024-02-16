#deanslist.py

#Imports
import openai
from openai import OpenAI
import time
import streamlit as st

#Initialize OpenAI Clinet
client = OpenAI(api_key= st.secrets.openai.api_key)

#Streamlit App Title
st.title('Dean\'s Assistant')

#Streamlit image for branding
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQroYsyWjvZmkyguxf2_XUKqcWTNLkZrRbPzPL8MU5I&s', caption='Plainfield School District 202')

#Streamlit user input for the prompt
user_prompt = st.text_area("Enter your question:", "Example: A student just had his third tardy. What consequences should I consider?")

#Button to submit question
if st.button('Submit'):
    with st.spinner('Fetching response...'):
        #Retrieve existing assistant
        my_assistant = client.beta.assistants.retrieve("asst_VS8FnRtUoE2P5YvZHQ7h8LzJ")
        #st.write("Assistant Retrieved:", my_assistant)

        #create thread and messages
        thread = client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

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
                    for content_part in message.content:
                        message_text = content_part.text.value
                        st.markdown(f"**Assistant's Response:** {message_text}")
                    
 
    

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
