import streamlit as st
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

MODEL_PATH = "zaneb-217/trocr-urdu-model-si26-zaneb"

st.title("Urdu OCR - Code Saviours SI-26")
st.write("Upload an Urdu image to extract text.")

@st.cache_resource
def load_model():
    processor = TrOCRProcessor.from_pretrained(MODEL_PATH)
    model = VisionEncoderDecoderModel.from_pretrained(MODEL_PATH)
    model.eval()
    return processor, model

processor, model = load_model()

uploaded_file = st.file_uploader(
    "Choose an Urdu image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    pixel_values = processor(
        images=image,
        return_tensors="pt"
    ).pixel_values

    with torch.no_grad():
        generated_ids = model.generate(
            pixel_values,
            max_length=128,
            no_repeat_ngram_size=3,
            repetition_penalty=2.0,
            num_beams=4
        )

    text = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

    st.subheader("Extracted Text")
    st.write(text)
