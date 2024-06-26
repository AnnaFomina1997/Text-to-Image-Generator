
# Text to Image Generator

The project aims to create images from text using a pre-trained ML learning model.

This project contains two main components:
1. A FastAPI backend serving HTML, CSS, and JavaScript.
2. A machine learning service using the `stabilityai/sdxl-turbo` model to generate images from text.

## Project Structure

### Fastapi Backend
The FastApi backend serves the frontend application, which includes HTML, CSS, and JavaScript files. It provides the user interface where users can input their text and view the generated image.

### ML Learning Service
The ML learning service utilizes the stabilityai/sdxl-turbo model. This service accepts text as input, processes them using the model, and returns image.


### Backend
The FastApi backend will be accessible at http://localhost:8000. It serves the front end application where users can input their text and receive the image..


## Features
FastApi Backend: Serves the frontend and handles user interactions.
ML Service: Uses a state-of-the-art language model to provide answers based on the provided text.
Docker Support: Both components can be easily deployed using Docker and Docker Compose.
CORS Handling: Ensures smooth interaction between the backend and the ML service.


### FastApi Backend: 
Serves the frontend and handles user interactions.
### ML Service: 
Uses a state-of-the-art language model to provide answers based on the provided documents.
### Docker Support: 
Both components can be easily deployed using Docker and Docker Compose.
CORS Handling: Ensures smooth interaction between the backend and the ML service

## Running the project


### Using Docker Compose

To build and run the project with Docker Compose, use the following command:

```bash
docker-compose up --build
```
