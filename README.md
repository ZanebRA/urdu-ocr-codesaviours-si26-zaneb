# Urdu OCR Internship Project
## Intern Information
- **Name:** Zaneb Rasool Ahmed
- **Department:** ML/AI

## Objective
To develop an Urdu Optical Character Recognition (OCR) system using Machine Learning and Deep Learning techniques.

## Research Summary
OCR (Optical Character Recognition) is a technology that converts text from images into editable digital text. Urdu OCR is more challenging than English OCR because it is written from right to left, letters change shape depending on their position in a word, and many characters have similar appearances. Urdu OCR can be used to digitize books, newspapers, government documents, and educational materials.

## Week 1 Tasks Completed
- Created GitHub and Google Colab environment.
- Studied the basics of Urdu OCR.
- Collected and organized **100 Urdu text images**.
- Generated **20 synthetic Urdu text images** using Python.
- Collected images from books, newspapers, signboards, and other sources.
- Organized the dataset into separate folders.
- Created **labels.csv** containing image paths and corresponding Urdu text.
- Uploaded the Week 1 notebook and project files to GitHub.

## Dataset Structure
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

## Technologies Used
- Python
- Google Colab
- GitHub
- Pillow
- Arabic Reshaper
- Python-Bidi

## Project Status
 Week 1 Completed

## Why We Need a Better Model

Tesseract OCR was tested on five different categories of Urdu images, including signboards, books, newspapers, other text images, and synthetic images.

### Image 1 – Signboard
- **Actual Urdu Text:** زمان اسٹیٹ پراپرٹی ایجنسی
- **Tesseract Output:** No text detected
- **Observation:** Tesseract failed to detect any Urdu text from the signboard image. The complex background and stylized Urdu font made recognition unsuccessful.

### Image 2 – Book
- **Actual Urdu Text:** محضلہ برلاس کا اسی شہر سے دم گھٹتا تھا
- **Tesseract Output:** Partial Urdu text with recognition errors.
- **Observation:** Some words were detected, but many characters were incorrect or missing.

### Image 3 – Newspaper
- **Actual Urdu Text:** پاکستان اور سعودی عرب کے درمیان سیکیورٹی کے شعبے میں مفاہمتی یادداشت پر دستخط
- **Tesseract Output:** Partial Urdu text with several errors.
- **Observation:** Some words were recognized correctly, but many characters and words were incorrect or omitted.

### Image 4 – Other
- **Actual Urdu Text:** پاکستان کا نعرہ، پاکستان کا مطلب کیا؟ لا الٰہ الا اللہ۔ میں مرگ بدنامہ ہے
- **Tesseract Output:** No text detected.
- **Observation:** Tesseract failed to recognize the Urdu text because of the image complexity and connected Urdu script.

### Image 5 – Synthetic
- **Actual Urdu Text:** پاکستان زندہ باد
- **Tesseract Output:** Partial text detected.
- **Observation:** Tesseract recognized part of the text, but the output was incomplete and contained recognition mistakes.

### Conclusion

**Tesseract fails on Urdu because** it struggles to recognize connected Urdu characters, ligatures, different writing styles, and complex backgrounds. Although it performs slightly better on clean printed text, it often produces incomplete, incorrect, or empty results. These limitations highlight the need for a dedicated deep learning–based Urdu OCR model.
