from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import sqlite3

from generate_labels import generate_labels 

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to the images folder
image_dir = r"C:\Users\lovey\OneDrive\Documents\imageRetrieval\test_data_v2"
database_path = "image_labels.db"


if not os.path.exists(database_path):
    generate_labels(image_dir)


app.mount("/images", StaticFiles(directory=image_dir), name="images")

def search_database(query):
    """Search images based on query using SQLite database."""
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT image_name FROM labels WHERE label LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    
    conn.close()
    return [f"/images/{row[0]}" for row in results]

@app.get("/search/")
async def search(query: str):
    """Search for images based on the query."""
    image_paths = search_database(query)
    
    if not image_paths:
        return {"message": f"No results found for '{query}', try searching something else."}

    description = f"We found {len(image_paths)} result" + ("s" if len(image_paths) > 1 else "")
    return {"images": image_paths, "description": description}
