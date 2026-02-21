import streamlit as st
from PIL import Image, ImageDraw
from streamlit_image_coordinates import streamlit_image_coordinates

st.title("Image Coordinate Picker")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.write("Click on the point you want to select:")

    coordinates = streamlit_image_coordinates(image, key="image")
    st.subheader("Image After Selection")

    if coordinates:
        x = coordinates["x"]
        y = coordinates["y"]

        image_copy = image.copy()
        draw = ImageDraw.Draw(image_copy)

        radius = 10
        draw.ellipse(
            (x - radius, y - radius, x + radius, y + radius),
            fill="red",
            outline="white",
            width=3
        )

        st.image(image_copy, caption=f"Selected Point: ({x}, {y})", use_container_width=True)
        st.write(f"Coordinates: X = {x}, Y = {y}")
    else:
        st.write("No point selected yet.")
