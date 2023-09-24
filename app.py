import streamlit as st

def main():
    st.title('Codebase Explainer')
    user_input = st.text_area("Paste your code here:")

    if st.button('Explain'):
        if user_input:
            st.subheader('Explanation will appear here...')
        else:
            st.warning('Please input some code or documentation first.')

if __name__ == '__main__':
    main()
