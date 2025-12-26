# VidText Pro

VidText Pro is a Flask-based web application that generates short videos from text input. The application uses a simple web interface where users can enter text, trigger a backend video generation request, track progress visually, and download or view the resulting video once ready. The backend integrates with the Pexels API to fetch video media, stores the generated file locally, and serves it back to the browser.

---

## Overview

The application works through the following flow:

1. User enters text in the browser UI.
2. The frontend sends the text to the backend `/generate-video` API.
3. The backend contacts the Pexels API, selects a suitable video, downloads it, and stores it with a unique filename.
4. The backend returns the generated video URL.
5. The frontend displays a progress animation while waiting and then renders the video in a player once available.

The UI includes a modern gradient design, central layout, loading/progress animation, and inline video output.

---

## Features

* Web interface for entering text
* Video generation endpoint powered by Flask
* Integration with Pexels video API
* Unique filename hashing for downloaded videos
* Local storage of generated video files
* Downloadable / streamable output video
* Progress bar animation during processing
* Inline video player display in the browser

---

## Tech Stack

* **Backend:** Python, Flask
* **HTTP Client:** requests
* **Frontend:** HTML, CSS, JavaScript
* **Video Source:** Pexels API
* **Deployment Support:** gunicorn

---

## Project Structure

```
VidText-Pro-main/
│
├── app.py                     # Flask backend and video processing logic
├── requirements.txt           # Dependencies
│
└── templates/
    └── index.html             # Web UI
```

---

## Installation

1. Ensure Python is installed.
2. Extract the project folder.
3. Open a terminal inside the project directory.
4. Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

The application requires a valid **Pexels API key**.

Set it as an environment variable:

**Linux / macOS**

```bash
export PEXELS_API_KEY="YOUR_API_KEY"
```

**Windows (PowerShell)**

```powershell
setx PEXELS_API_KEY "YOUR_API_KEY"
```

Internet access is required for API calls.

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The application runs in debug mode.
Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## Usage

1. Open the web application.
2. Enter your text in the provided text box.
3. Click the **Generate** button.
4. Wait while the progress animation runs.
5. Once ready, the generated video will appear in the player.
6. You can play or download the video from the interface.

---

## API Endpoint

### Generate Video

```
POST /generate-video
```

Request body:

```
JSON containing the text input
```

Response:

```
{
  "videoUrl": "/output_<hash>.mp4"
}
```

---

## Notes

* Generated video files are stored locally in the root directory.
* The video streaming/downloading route serves files directly via:

  ```
  /<filename>
  ```
* If Pexels API does not return content or network fails, the frontend displays an error alert.

---

## Dependencies

Defined in `requirements.txt`:

```
Flask
gunicorn
requests
requests-oauthlib
```

---

## License

No license file is included in this project.
