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

## Gap Analysis (Tesseract OCR)

The Tesseract OCR engine was tested on different categories of Urdu text images after preprocessing.

### Results
-  Newspaper images: Partial text detected.
-  Book images: Some Urdu text detected but with recognition errors.
-  Synthetic images: Short text recognized with minor mistakes.
-  Signboard images: No text detected.
-  Other images: No text detected.

### Limitations
- Struggles with low-quality and noisy images.
- Performance decreases on complex backgrounds (e.g., signboards).
- Cannot accurately recognize stylized Urdu fonts.
- Misses text in blurred or low-contrast images.
- Recognition accuracy is inconsistent across different image types.

### Conclusion
Tesseract OCR works reasonably well on clean printed Urdu text but performs poorly on challenging real-world images. A deep learning-based OCR model is needed for better Urdu text recognition.
