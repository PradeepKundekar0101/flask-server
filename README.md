# YouTube Transcript API Service

This Flask application provides a simple API to retrieve transcripts for YouTube videos using the YouTube Transcript API.

## Setup Instructions

Follow these steps to set up the project locally:

1. **Clone the Repository:**
   
   ```bash
   git clone https://github.com/SecondShorts/transcripts-server.git
2. **Install Dependencies:**
    Navigate to the project directory and install the required dependencies using pip:
    ```bash
    cd transcripts-server
    pip install -r requirements.txt
3. **Run the Application:**
   Run the Flask application using the following command:
    ```bash
    python app.py

****The application will start running locally on http://127.0.0.1:5000/****

# Endpoints
 - GET /get-transcripts/<video_id>:
 
 Returns transcripts for a YouTube video identified by its video_id.
 
 Example: http://127.0.0.1:5000/get-transcripts/<video_id>
