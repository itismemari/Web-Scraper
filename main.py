import streamlit as st
from Scrape import scrape_website , split_dom_content , clean_body_content , extract_content_from_html
from llm import parse_with_ollama

st.title("URL Scraper")

url = st.text_input("Enter a website URL :")

if st.button("Scrape"):
    st.write("Scraping the website ...")
    result = scrape_website(url)
    body_content = extract_content_from_html(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("veiw DOM content"):
        st.text_area("DOM Content", cleaned_content , height = 300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Descripe what you want to pares :")

    if st.button("Parse content"):
        if parse_description:
            st.write("parsing the content ...")

            chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(chunks , parse_description)
            st.write(result)
            

