# Person Detection API
![Uploading image.png…]()

## Description
This project is a simple API for detecting persons in images. It uses the YOLO (You Only Look Once) model for object detection. The API can process images from local files, URLs, or directly uploaded by the user.

## Features
- Detects persons in images.
- Supports images from local files, URLs, and uploads.
- Saves processed images with detected persons highlighted.
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/person-detection-api.git
   cd person_detecion_with_FastAPI

 ## USAGE
 1. Run the FastAPI server:
 ```bash
 uvicorn main:app --reload
 ```
## API Endpoints:
 
```bash
GET /detect_local_image?file_path=path/to/your/image.jpg
GET /detect_online_image?url=http://example.com/image.jpg
POST /detect_uploaded_image
