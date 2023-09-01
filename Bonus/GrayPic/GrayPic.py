import streamlit as st
from PIL import Image
from io import BytesIO


st.set_page_config(page_title="GrayPic")
st.title("Camera Picture to Grayscale")

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input(label="Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)
    # Convert the pillow image to grayscale
    gray_img = img.convert("L")
    # Render the grayscale image on the webpage
    st.image(gray_img, use_column_width="always")
    # Prepare the image for downloading
    buf = BytesIO()
    gray_img.save(buf, format="png")
    byte_img = buf.getvalue()
    # Create button for downloading the picture
    st.download_button(
        label="Download Picture Here!", 
        data=byte_img, 
        use_container_width=True, 
        file_name="grayscale.png"
    )
    