# image-super-resolution
A deep learning-powered Python app for upscaling low-resolution images using the RRDBNet architecture.


# Image Super Resolution

This project implements an **Image Super-Resolution** system using a deep learning architecture, specifically **RRDBNet**. It enhances the resolution of low-quality images to produce sharper, high-definition outputs. It can be applied to tasks like photo restoration, video upscaling, satellite image enhancement, and medical imaging.

## 📁 Project Structure  
- `app.py` – Flask web interface for uploading and displaying super-resolved images  
- `test.py` – Script to test and visualize the model on sample images  
- `RRDBNet_arch.py` – Contains the RRDBNet deep learning model architecture  
- `static/` – Folder for storing uploaded and output images  
- `templates/` – HTML files for frontend display  

## 🔍 Model  
- **RRDBNet (Residual-in-Residual Dense Block Network)**  
- Architecture inspired by ESRGAN  
- Capable of 4x super-resolution or more  
- Uses residual learning and dense connections to retain image details  

## 💡 Key Features  
- Upload image via browser and get an enhanced version  
- Built using PyTorch for model inference  
- Flask for lightweight web app interface  
- Works on JPG, PNG, and other common formats  

## 🧪 Technologies Used  
- Python  
- PyTorch  
- Flask  
- NumPy / PIL  
- RRDBNet / ESRGAN  

## 🖼️ Sample Use Case  
Upload a blurry or pixelated image and get a super-resolved output using deep learning.

## 👨‍💻 Author  
**Akiti Sri Kalyan Reddy**  
B.Tech – Data Science and Artificial Intelligence  
ICFAI University, Hyderabad  
