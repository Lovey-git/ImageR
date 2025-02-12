import os
import sqlite3
import random

# Predefined possible labels
possible_labels = [
    "cat", "dog", "car", "tree", "person", "house", "building", "nature", "sky", "road",
    "water", "food", "furniture", "fish", "chicken", "vegetables", "fruits", "cake", "sugar",
    "soda", "computer", "horse", "AI", "doctor", "baby", "time", "rabbit", "breakfast", "machine",
    "sick", "wedding", "phone", "love", "peace", "clown", "gym", "skeleton", "clothes", "tv",
    "cow", "construction", "office", "chair", "sunflower", "honey", "books", "presentation",
    "stones", "shopping", "team", "family", "joy", "laugh", "balloons", "cargo", "ship", "ocean",
    "beach", "mountain", "hiking", "coffee", "exercise", "yoga", "walk", "travel", "river", "pumpkin",
    "sleep", "pawpaw", "beef", "cube", "circle", "factory", "shoes", "work"
]

# Path to the image
image_dir =  r"C:\Users\lovey\OneDrive\Documents\imageRetrieval\test_data_v2" 

# database 
def create_database():
    conn = sqlite3.connect('image_labels.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS labels (
            image_name TEXT PRIMARY KEY,
            labels TEXT
        )
    """)
    conn.commit()
    conn.close()

# generate labels for images
def generate_labels(image_dir):
    labels = {}
    for image_name in os.listdir(image_dir):
        if image_name.endswith((".jpg", ".jpeg", ".png")):
            
            labels[image_name] = random.sample(possible_labels, k=1) 
    return labels

# generated labels to the database
def save_labels_to_database(labels):
    conn = sqlite3.connect('image_labels.db')
    cursor = conn.cursor()

    for image_name, label_list in labels.items():
        labels_str = ", ".join(label_list)  
        cursor.execute("INSERT OR REPLACE INTO labels (image_name, labels) VALUES (?, ?)", (image_name, labels_str))

    conn.commit()
    conn.close()

# Main 
def main():
    # database and table
    create_database()

    # Generate labels for images
    generated_labels = generate_labels(image_dir)

    # generated labels to the database
    save_labels_to_database(generated_labels)

    # Print the generated labels 
    for image_name, label in generated_labels.items():
        print(f"{image_name} → {', '.join(label)}")

if __name__ == "__main__":
    main()
