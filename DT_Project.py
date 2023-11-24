import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from deepface import DeepFace

root = tk.Tk()
root.title("EmoMatic")
root.geometry("800x600")
root.configure(bg="#2C3E50")  # Background color - Darker Shade of Gray

# Add a label with the name "EmoMatic" in big red font at the top
title_label = tk.Label(root, text="EmoMatic", font=("Helvetica", 24, "bold"), fg="#E74C3C", bg="#2C3E50")  # Red text
title_label.pack(side="top", pady=(20, 10))

def selectImage():
    path = filedialog.askopenfilename(title="Select Image")
    imgEntry.delete(0, 'end')
    imgEntry.insert(0, path)

def resizeImage(img_path, max_width=800, max_height=350):
    img = Image.open(img_path)
    width, height = img.size

    if width > max_width or height > max_height:
        img.thumbnail((max_width, max_height))

    return img

def startAnalysis():
    path = imgEntry.get()

    try:
        resized_img = resizeImage(path)
        img = ImageTk.PhotoImage(resized_img)

        imagedisp.configure(image=img)
        imagedisp.image = img
    except Exception as e:
        print(f"Error processing image: {e}")

    img1 = cv2.imread(str(path))
    obj = DeepFace.analyze(img1)

    Age.config(text="Detected Age: " + str(obj[0]['age']))
    Race.config(text="Detected Race: " + str(obj[0]['dominant_race']))
    Emotion.config(text="Detected Emotion: " + str(obj[0]['dominant_emotion']))
    Gender.config(text="Detected Gender: " + str(obj[0]['dominant_gender']))

imgEntry = tk.Entry(root, width=50, bg="#ECF0F1", fg="#34495E", font=("Helvetica", 10))  # Light Gray background, Dark text
select_button = tk.Button(root, text="Select Image", command=selectImage, bg="#3498DB", fg="#FFFFFF", relief="flat")  # Blue button with white text
main_button = tk.Button(root, text="Start Analysis", padx=30, pady=15, command=startAnalysis, bg="#3498DB", fg="#FFFFFF", relief="flat")  # Blue button with white text
imgp = tk.Label(root, text="Selected Image Path: ", fg="#ECF0F1", bg="#2C3E50")  # Light Gray text, Darker Shade of Gray background

imgp.pack(side="top", pady=(10, 5))
imgEntry.pack(side="top", pady=(10, 5))
select_button.pack(side="top", padx=5, pady=(10, 5))
main_button.pack(side="top", pady=(10, 20))

imagedisp = tk.Label(root)
imagedisp.pack(side="top")

Age = tk.Label(root, text="", fg="#ECF0F1", bg="#2C3E50", font=("Helvetica", 10))  # Light Gray text, Darker Shade of Gray background
Race = tk.Label(root, text="", fg="#ECF0F1", bg="#2C3E50", font=("Helvetica", 10))  # Light Gray text, Darker Shade of Gray background
Emotion = tk.Label(root, text="", fg="#ECF0F1", bg="#2C3E50", font=("Helvetica", 10))  # Light Gray text, Darker Shade of Gray background
Gender = tk.Label(root, text="", fg="#ECF0F1", bg="#2C3E50", font=("Helvetica", 10))  # Light Gray text, Darker Shade of Gray background

Age.pack(side="top")
Race.pack(side="top")
Emotion.pack(side="top")
Gender.pack(side="top")

root.mainloop()
