import streamlit as st
import yaml

# Read config yaml file
with open('./streamlit_app/config.yaml', 'r') as file:
    config = yaml.safe_load(file)
#print(config)
title = config['streamlit']['title']
avatar = {
    'user': None,
    'assistant': config['streamlit']['avatar']
}

# Set page config
st.set_page_config(
    page_title=config['streamlit']['tab_title'], 
    page_icon=config['streamlit']['page_icon'], 
    )

# Set sidebar
st.sidebar.title("About")
st.sidebar.info(config['streamlit']['about'])

# Set logo
st.image(config['streamlit']['logo'], width=50)

# Set page title
st.title(title)



    