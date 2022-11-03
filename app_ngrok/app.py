import streamlit as st
from pyngrok import ngrok

# ---- LAYOUT PAGE ----
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Streamlit with ngrok Demo", page_icon=":rocket:", layout="wide")

# ---- MAINPAGE ----
# Make a title for this demo using emojis
st.title('Streamlit with ngrok :rocket:')
st.header('(to show session_state)')

# Put your Python+Streamlit code here ...
# you can modify it by double cliking on the folder icon at the left

# @title This last cell would keep the app running. If stoped, the app would be disconnected.

public_url = ngrok.connect(port='80')
print('Link to web app:')
print(public_url)
# streamlit run --server.port 80 app.py >/dev/null
