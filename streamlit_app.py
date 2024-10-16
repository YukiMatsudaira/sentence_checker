import streamlit as st
from collections import Counter

# StreamlitのUIを作成
st.title("共起語出現回数カウントツール")

input_text = st.text_area("共起語を入力してください", "")
document_text = st.text_area("文章を入力してください", "")

if st.button("カウント"):
    keyword_list = input_text.replace("\n", ",").split(',')
    text_frequency = Counter()
    for keyword in keyword_list:
        text_frequency[keyword] = document_text.count(keyword)

    sorted_text_frequency = sorted(text_frequency.items(), key=lambda x: x[1], reverse=True)
    document_length = len(document_text)

    st.write(f"文章の総文字数: {document_length}")
    st.write("共起語の出現回数:")
    for rank, (keyword, count) in enumerate(sorted_text_frequency, start=1):
        st.write(f"{rank}. {keyword}: {count}")

