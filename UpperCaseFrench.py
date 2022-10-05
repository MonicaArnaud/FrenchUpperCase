import pandas as pd
import docx
from docx import Document
import streamlit as st

st.title('法语大写转换')

uploaded_file = st.file_uploader("Choose a file")

# To read file as string:

if uploaded_file:
   st.write("Filename: ", uploaded_file.name)

#documentWord = "F:\我的量化\DingDingDowload\frenchNews_upperTest.docx"

def uppercaseFrench(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
      fullText.append(para.text)
    result = '\n'.join(fullText)
    #print(result.upper())
    return result.upper()

UpperFile = uppercaseFrench(uploaded_file)

st.button('转换', on_click=UpperFile)

raw_text = str(UpperFile)
st.write(raw_text)



