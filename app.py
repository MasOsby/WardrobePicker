from flask import Flask, jsonify, send_from_directory
import os
from dotenv import load_dotenv
from google import genai
import PIL.Image

app = Flask(__name__)

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/Clothing/<filename>")
def clothing(filename):
    return send_from_directory("Clothing", filename)

@app.route("/api/outfits/generate", methods=["POST"])
def generate_outfit():
    print("Request received for PIO")
    images = [
    PIL.Image.open("Clothing/Tee_1.jpg"),
    PIL.Image.open("Clothing/Tee_2.jpg"),
    PIL.Image.open("Clothing/Pants_1.jpg"),
    PIL.Image.open("Clothing/Pants_2.jpg"),
    PIL.Image.open("Clothing/Pants_3.jpg"),
    PIL.Image.open("Clothing/clog.jpg"),
    PIL.Image.open("Clothing/Jacket_1.png"),
    PIL.Image.open("Clothing/Jacket_3.jpg")
    ]

    filenames = [
    "Tee_1.jpg",
    "Tee_2.jpg",
    "Pants_1.jpg",
    "Pants_2.jpg",
    "Pants_3.jpg",
    "clog.jpg", 
    "Jacket_1.png",
    "Jacket_3.jpg"
    ]


    image_list = ""
    for i, filename in enumerate(filenames):
        image_list += f"Image {i+1}: {filename}\n"

    print("Calling Gemini...")

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=images + [f"""Here are the images:\n{image_list}
        Pick an outfit and refer to each item by its exact filename.
        At the end of your response, add a line that says exactly:
        CHOSEN: filename1.jpg, filename2.jpg, filename3.jpg
        Only include the filenames you actually picked."""]
        )
    
    print("Gemini response received.")

    text = response.text
    chosen_line = [line for line in text.split("\n") if line.startswith("CHOSEN:")][0]
    chosen_files = [f.strip() for f in chosen_line.replace("CHOSEN:", "").split(",")]
    clean_description = text.replace(chosen_line, "").strip()

    return jsonify({
        "outfit_description": clean_description,
        "images": chosen_files
    })

if __name__ == "__main__":
    app.run(debug=True)