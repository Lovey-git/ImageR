import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [images, setImages] = useState([]);
  const [message, setMessage] = useState("Enter a search word"); // Default message

  // handles search
  const handleSearch = async () => {
    if (!query.trim()) {
      setMessage("Please enter a search term.");
      setImages([]);
      return;
    }

    try {
      const response = await fetch(`http://127.0.0.1:8000/search/?query=${query}`);
      const data = await response.json();

      if (data.message) {
        setMessage(data.message);
        setImages([]);
      } else {
        setImages(data.images);
        setMessage(`We found ${data.images.length} result${data.images.length > 1 ? "s" : ""}`);
      }
    } catch (error) {
      console.error("❌ Error fetching images:", error);
      setMessage("Error retrieving images. Try again.");
    }
  };

  // handles voice search
  const handleVoiceSearch = () => {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";

    recognition.onstart = () => {
      setMessage("Listening...");
    };

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setQuery(transcript);
      setMessage(`Searching for: "${transcript}"`);
      handleSearch(); //Automatically search after voice input
    };

    recognition.onerror = (event) => {
      setMessage("Voice search failed. Try again.");
      console.error("Speech recognition error:", event.error);
    };

    recognition.start();
  };

  return (
    <div className="App" style={{ backgroundColor: "lightblue" }}>
      <h1>Multi-Modal Image Retrieval System</h1>

      <div className="search-container">
        <input
          type="text"
          placeholder="Search for images"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
        <button onClick={handleVoiceSearch}>🎤 Voice Search</button> {/*MIC BUTTON */}
      </div>

      <div className="image-results">
        <p>{message}</p>

        {images.length > 0 && (
          <div className="images">
            {images.map((image, index) => (
              <div key={index} className="image-item">
                <img src={`http://127.0.0.1:8000${image}`} alt={`Result ${index + 1}`} />
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
