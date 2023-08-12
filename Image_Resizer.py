import streamlit as st
from PIL import Image
import io
import matplotlib.pyplot as plt

# Function to resize the image (High quality resampling)
def resize_image(image, size):
    resized_image = image.resize(size, Image.LANCZOS)
    return resized_image

def main():
    st.title("Image_Resizer")
    st.subheader("Just a Simple Image Resizer and Cropper")

main()

# Upload image file
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
        # Read the image file
    image = Image.open(uploaded_file)

    # Displaying the image with axes using matplotlib
    st.subheader("Original Image")
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.axis('on')  # Display axes
    st.pyplot(fig)

    # Cropping the image
    st.subheader("Crop Image")
    crop = st.checkbox("Do you want to crop the image?")

    if crop:
            left = st.number_input("Left", min_value=0, max_value=image.width, value=0)
            upper = st.number_input("Upper", min_value=0, max_value=image.height, value=0)
            right = st.number_input("Right", min_value=0, max_value=image.width, value=image.width)
            lower = st.number_input("Lower", min_value=0, max_value=image.height, value=image.height)

            image = image.crop((left, upper, right, lower))
            st.image(image, caption="Cropped Image")


    # Choose the resize option        
    resize_option = st.selectbox("Choose Resize Option", ("Original", "Large", "Medium", "Small", "Custom"))

    if resize_option == "Original":
        size = image.size
    elif resize_option == "Large":
                size = (1920, 2560)
    elif resize_option == "Medium":
                size = (1280, 1707)
    elif resize_option == "Small":
                size = (640, 853)
    else:
        custom_width = st.number_input("Enter custom width", min_value=1)
        custom_height = st.number_input("Enter custom height", min_value=1)
        size = (custom_width, custom_height)

    # Resize the image
    resized_image = resize_image(image, size)

    # Display the resized image
    st.subheader("Resized Image")
    st.image(resized_image, caption="Resized Image")

    # Choose the output format
    output_format = st.selectbox("Choose Output Format", ("JPG", "PNG"))

    # Input field for file name
    file_name = st.text_input("Enter file name", value="resized_image")

    # Download button
    download_button = st.button("Download Resized Image")


    if download_button:
        with st.spinner("Processing..."):
            # Save the resized image to BytesIO
            image_stream = io.BytesIO()
            if output_format.lower() == "jpg":
                resized_image.save(image_stream, format="JPEG", quality=95)
            else:
                resized_image.save(image_stream, format=output_format)
                image_stream.seek(0)

            # Prepare data for download
            data = image_stream.getvalue()

            # Create a download button with pop-up file save dialog
            st.download_button(
                    label="Click to Download",
                    data=data,
                    file_name=file_name + "." + output_format.lower(),
                    mime=output_format.lower(),
            )

