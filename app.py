import streamlit as st
import uuid
from medisearch_client import MediSearchClient
import os

# Set the API key if not already set in the environment
if "api_key" not in os.environ:
    os.environ["api_key"] = "31dce06e-a531-4c8a-9bfc-65d1bbf0003d"  # Replace "your_api_key_here" with your actual API key

def get_advice(question):
    conversation_id = str(uuid.uuid4())
    client = MediSearchClient(api_key=os.environ["api_key"])
    responses = client.send_user_message(conversation=[f"{question}"], 
                                         conversation_id=conversation_id,
                                         should_stream_response=False,
                                         language="English")
    return responses


st.title("HealthCare Informatics MediSearch System 🧬")

api_key = os.environ["api_key"] 
text_input = st.text_input("Enter Your HealthCare Informatics MediSearch Key Here:")

if st.button("Submit"):
  with st.spinner("Loading..."):
    output = get_advice(text_input)
    print(output)
    for response in output:
      if response["event"] == "llm_response":
        st.write(response["text"])
      elif response["event"] == "articles":
        for article in response["articles"]:
          st.write(f"[{article['title']}]({article['url']})")
    with st.expander("All Article Details"):
        st.write(response["articles"])

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>

"""
st.markdown(footer,unsafe_allow_html=True)