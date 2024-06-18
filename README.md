# Webcam_motion_detector
This repository contains the source code for a webcam detection application. The application is written in Python and uses OpenCV for image processing. The application is designed to detect objects in an image and draw a bounding box around them.
The repository contains the following files: - main.py: The main application file. This file contains the code for the detection algorithm. - images: A folder where images are saved. -emaili# Motion Detection App

This application detects motion using a webcam, captures images when motion is detected, and sends an email with the captured image. It uses Flask for the backend, OpenCV for motion detection, and smtplib for sending emails.

## Demo

You can see a live demo of this application [here](https://chatbot-hzyv.onrender.com).

## Requirements

- Python 3.6 or higher
- Flask
- OpenCV
- smtplib
- imghdr

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/motion-detection-app.git
    cd motion-detection-app
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```sh
    python app.py
    ```

2. Open a web browser and go to `http://127.0.0.1:5000/`.

3. Click the "Start" button to start the video stream. Motion detection will be performed, and emails will be sent if motion is detected.

## Email Configuration

Edit the `emailing.py` file to configure the sender and receiver email addresses:

```python
SENDER = "your_email@gmail.com"
PASSWORD = "your_password"
RECEIVER = "receiver_email@gmail.com"
ng.py: for sending email when the object is detected. 
