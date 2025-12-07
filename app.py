import streamlit as st
from google import genai
 
client = genai.Client(api_key="AIzaSyByxAvghwrrjTBczinskJvm1BOrAM7iNi8")
st.title("MadhuGPT")
def answers(question):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""You are an export summarizing,
        So given me a meaningfully and simply words explai in this, {question}"""
    )
    return response

content = st.file_uploader("Pleas Uploade your file")

if st.button('Generat answer'):
    if content:
        with st.spinner('Pleas whit.....'):
            question = content.read()
            result = answers(question)
            st.write(result.text)
            st.balloons()
    else:
        st.warning('Pleas Uploade the file first')
