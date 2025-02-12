Multi-Modal Image Retrieval System

This project allows users to search for images based on **text** and **voice commands**.  
It utilizes **FastAPI for the backend** and **React.js for the frontend**.  

---

Features
✅ Assigns **random labels** to images from a predefined set.  
✅ Stores image labels in an **SQLite database**.  
✅ Provides an API to **search for images by labels**.  
✅ React-based UI with **voice search functionality**.  

---

Installation & Setup

Backend Setup (FastAPI)
1. Navigate to the backend folder:
   ```bash
   cd backend

2.Create a virtual environment:
python -m venv venv

3.Activate the virtual environment:
venv\Scripts\activate

4.pip install -r requirements.txt
pip install -r requirements.txt

5.uvicorn main:app --reload
uvicorn main:app --reload
The server will start at: http://127.0.0.1:8000

Frontend Setup (React)
1.Navigate to the frontend folder:
cd frontend

2.Install dependencies:
npm install

3.Run the frontend server:
npm start
The React app will be available at: http://localhost:3000

-Upload images to the /test_data_v2/ folder.https://www.kaggle.com/datasets/alessandrasala79/ai-vs-human-generated-dataset/data?select=test_data_v2
-Run the backend to generate labels.
-Access the frontend and enter a search term or use voice search.
-The system will retrieve and display matching images.


Running Tests
1.Backend Tests
python -m unittest test_backend.py


Assumptions
Voice search requires a browser supporting Web Speech API









