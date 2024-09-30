from transformers import pipeline

pipe = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    img = image.open(uploaded_file)
    st.image(img)
    predictions = pipe(imge)
    st.write(predictions)

img = Image.open(uploaded_file)

predictions = pipe(img)
