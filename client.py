import streamlit as st
from backend import *

def main() :
    st.set_page_config(page_title = 'PDF Summarizer')

    st.title('PDF Summarizer App')
    st.write('Summarize your PDF in just few Seconds')
    st.divider()


    pdf = st.file_uploader('Upload Your PDF', type='pdf')

    submit = st.button('Generate Summary')

    if submit :
        response = summarizer(pdf)
        st.subheader('Summary of File:')
        st.write(response)


if __name__ == '__main__' :
    main()



