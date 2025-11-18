from PIL import Image
import pytesseract

# If Tesseract is not in PATH, specify its full path:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load your image
image_path = "./sample1.png"
img = Image.open(image_path)

# Run OCR
text = pytesseract.image_to_string(img)
if "Haris" in text:
    print("Correct")
else:
    print("Incorrect")

# Print the result
# print("Detected text:")
# print(text)

# # Optionally, save the text to a file
# with open("output_text.txt", "w", encoding="utf-8") as f:
#     f.write(text)
