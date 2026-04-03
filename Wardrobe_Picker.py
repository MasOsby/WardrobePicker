import os 
from dotenv import load_dotenv
from google import genai
import PIL.Image
import json

#"Suggest an outfit for a male for a casual spring day. Include a shirt, pants, and shoes."

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in the .env file.")

client = genai.Client(api_key=GEMINI_API_KEY)
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
    "Jacket_1.jpg",
    "Jacket_3.jpg"
]

image_list = ""
for i, filename in enumerate(filenames):
    image_list += f"Image {i+1}: {filename}\n"


response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents =images + [f"Here are the images: \n{image_list}\n\nSuggest an outfit and refer to each image by its exact file name"]
)

result = {
    "outfit_description": response.text,
    "images": ["Tee_2.jpg", "Pants_2.jpg", "Jacket_3.jpg", "clog.jpg"]
}

with open("outfit_suggestion.json", "w") as f:
    json.dump(result, f)

print("Outfit suggestion saved to outfit_suggestion.json")