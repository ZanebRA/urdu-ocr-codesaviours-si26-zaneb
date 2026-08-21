# Urdu Optical Character Recognition (OCR) Tool

An end-to-end Machine Learning pipeline and Streamlit web application designed to extract printed, synthetic, and complex Urdu text from images using Deep Learning models.

---

## 📌 Project Overview
OCR (Optical Character Recognition) converts text from images into editable digital format. Urdu OCR presents unique challenges compared to Latin scripts because Urdu is written right-to-left, letters dynamically change shape based on word position, and characters feature complex cursive ligatures. This tool aims to digitize Urdu books, newspapers, signboards, and educational materials.

---

## 🔗 Project Links & Demo

* 🚀 **Live Demo (Streamlit App):** [Urdu OCR Live Web Application](https://urdu-ocr-codesaviours-si26-zaneb-bjd6aedpdq3wbgufp74rul.streamlit.app/)
* 📹 **Video Demo (Loom):** [Watch Demo Video]()

---

## 📁 Dataset Structure
A dataset of 100+ annotated Urdu text images was organized across 5 distinct categories along with a mapped `labels.csv` file:

```text
data/
├── labels.csv
└── raw/
    ├── books/
    ├── newspaper/
    ├── signboards/
    ├── synthetic/
    └── other/
```
## 🛠️ Technologies Used
* **Languages & Frameworks:** Python, PyTorch, Streamlit
* **Libraries:** Transformers (TrOCR), Pillow, Arabic Reshaper, Python-Bidi, Pytesseract
* **Tools:** Google Colab, GitHub, VS Code

---

## 📊 Tesseract Performance vs. Model Motivation

Testing standard Tesseract OCR on sample category images highlighted key limitations:

| Category | Actual Urdu Text | Tesseract Output | Observation |
| :--- | :--- | :--- | :--- |
| **Signboard** | زمان اسٹیٹ پراپرٹی ایجنسی | *No text detected* | Failed due to complex background and stylized font. |
| **Book** | محضلہ برلاس کا اسی شہر سے دم گھٹتا تھا | *Partial text* | Some words detected, but character errors occurred. |
| **Newspaper** | پاکستان اور سعودی عرب کے درمیان... | *Partial text* | Key words missed due to newspaper layout/font. |
| **Other** | پاکستان کا نعرہ، پاکستان کا مطلب کیا... | *No text detected* | Failed on connected cursive script & noise. |
| **Synthetic** | پاکستان زندہ باد | *Incomplete text* | Partial detection with missing ligatures. |

**Conclusion:** Standard OCR engines struggle with cursive Urdu ligatures and complex backgrounds. This project utilizes Vision Encoder-Decoder architectures (Microsoft TrOCR) fine-tuned for better script-aware recognition.

---

## 💻 How to Run Locally

### 1. Install Dependencies
```bash
pip install torch transformers pillow streamlit arabic-reshaper python-bidi pytesseract
```

### 2. Run Streamlit App
```bash
streamlit run app.py
```
### 3. Run Standalone Inference Script
If you want to run text inference directly in Python without the Streamlit interface:

```python
import torch
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

# Load model and processor
model_name = "microsoft/trocr-base-stage1"  
processor = TrOCRProcessor.from_pretrained(model_name)
model = VisionEncoderDecoderModel.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Load image
image_path = "data/raw/signboards/13.jpg" 
image = Image.open(image_path).convert("RGB")

# Preprocess & generate output
pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)

with torch.no_grad():
    generated_ids = model.generate(pixel_values)

extracted_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

print("Extracted Text:", extracted_text)
```

## Limitations & Future Work

### Limitations
- The current model is trained on a small dataset (approximately 200 images).
- OCR accuracy is limited due to the small dataset size and limited diversity of Urdu text.
- The model may not perform well on complex backgrounds, different fonts, handwritten text, or low-quality images.

### Future Work
- Scale the dataset to **5,000+ Urdu images** to improve production-level accuracy.
- Include more fonts, layouts, newspapers, books, signboards, and handwritten Urdu samples.
- Fine-tune the TrOCR model on a larger and more diverse dataset.
- Deploy the application for real-world use with improved OCR performance.

---
## 👤 Built By
**Zaneb Rasool Ahmed**  
*Machine Learning Intern* | **Code Saviours SI-26** | 2026
