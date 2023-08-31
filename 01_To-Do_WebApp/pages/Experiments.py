import streamlit as st


st.title("Experiments")

st.code(
    """
    # This is a comment
    print("Hello")

    for i in range(5):
        print("Streamlit is amazing!")
    """
)

st.color_picker(label="Choose a color")

with st.expander(label="This is an expander for the Camera"):
    picture = st.camera_input(label="Is this my webcam?!")

if picture:
    st.image(picture, use_column_width="always")

with st.chat_message("user"):
    st.write("This is a message!")

with st.chat_message("user"):
    st.write("This is another message!")

st.chat_input()

st.file_uploader(label="Upload here!")

st.markdown(
    """
    # This is Markdown

    ## Getting Started

    Before you begin...

    1.  **Number One:** BLABLA
    2.  **Number Two:** BLABLA

    Markdown is amazing, right?
    """
)

st.divider()

st.success("Success!")
st.info("Informative!")
st.warning("Warning!")
st.error("Error!")

st.video(data="https://youtu.be/4sPnOqeUDmk")

st.caption(body="Is this a caption?")

st.audio(data="https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3")

st.header("This is a Header")

st.tabs(["Tab1", "Tab2", "Tab3"])

st.snow()
st.balloons()