import sqlite3

def search_images(query):
    """Search images by label in the database."""
    conn = sqlite3.connect("image_labels.db")
    cursor = conn.cursor()

    # Perform a fuzzy search
    cursor.execute("SELECT image_name FROM labels WHERE label LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()

    conn.close()

    # Extract image names
    return [row[0] for row in results]


search_query = "dog" 
found_images = search_images(search_query)
print("Found images:", found_images)
