# Wardrobe Picker

An AI-powered outfit generator that analyzes photos of your clothing and recommends outfit combinations using Google's Gemini API.

## Demo
Upload photos of your wardrobe and click "Get New Outfit" to get a styled outfit suggestion with images.

## Tech Stack
- Python, Flask
- Google Gemini API (gemini-2.5-flash-lite)
- JavaScript, HTML, CSS

## Features
- Sends clothing images to Gemini for AI analysis
- Parses AI response to display only the chosen outfit items
- Modal UI with regenerate functionality
- Secure API key management with .env

## Setup
1. Clone the repo
2. Install dependencies
```
   pip install flask google-genai python-dotenv Pillow
```
3. Create a `.env` file and add your Gemini API key
```
   GEMINI_API_KEY=your_key_here
```
4. Add your clothing images to the `Clothing/` folder
5. Run the app
```
   python app.py
```
6. Go to `http://127.0.0.1:5000`
