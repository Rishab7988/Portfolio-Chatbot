import streamlit as st


from langchain_helper import get_qa_chain, create_vector_db

st.title("RiBo 😎 The personal assistant of Rishab")
btn = st.button("Create Knowledgebase")
if btn:
    create_vector_db()

if "messages" not in st.session_state:
    st.session_state.messages = []

#Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Take user input
question = st.chat_input("Question: ")

if question:
    # displaying user message in chat-bot container
    with  st.chat_message("user"):
        st.markdown(question)

    # Add user message to chat history
    st.session_state.messages.append({"role":"user","content":question})

    if (question=="What is your name?"):
        response="Rishab Mahato"
    else:
        chain = get_qa_chain()
        response = chain.run(question)

    # display bot response in chat container
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role":"bot","content":response})