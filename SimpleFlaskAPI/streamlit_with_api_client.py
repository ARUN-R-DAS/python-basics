import requests
import streamlit as st

def main():
    st.title('API enabled page')
    # widgets
    input1 = st.text_input("Input 1","")
    okay_button = st.button('okay')

    if okay_button:
        response = requests.post(
            "http://127.0.0.1:5000/page",
            json={"input1": input1}
        )

        print(response.json())
        output = response.json()
        st.write(output['result'])

main()