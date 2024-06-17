import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageOps

def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image_path.set(file_path)

def select_color():
    color_code = colorchooser.askcolor(title="Choose fill color")[1]
    if color_code:
        fill_color.set(color_code)

def resize_image():
    try:
        img_path = image_path.get()
        new_width = int(width_entry.get())
        color = fill_color.get()

        image = Image.open(img_path)
        current_width, current_height = image.size
        border_width = (new_width - current_width) // 2

        new_image = ImageOps.expand(image, border=(border_width, 0), fill=color)
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            new_image.save(save_path)
            tk.messagebox.showinfo("Success", f"Image saved as {save_path}")
    except Exception as e:
        tk.messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Image Resizer")

image_path = tk.StringVar()
fill_color = tk.StringVar(value="black")

tk.Label(app, text="Select Image:").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(app, textvariable=image_path, width=40).grid(row=0, column=1, padx=10, pady=5)
tk.Button(app, text="Browse", command=select_image).grid(row=0, column=2, padx=10, pady=5)

tk.Label(app, text="Current Width:").grid(row=1, column=0, padx=10, pady=5)
current_width_label = tk.Label(app, text="", width=20)
current_width_label.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="New Width:").grid(row=2, column=0, padx=10, pady=5)
width_entry = tk.Entry(app)
width_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(app, text="Fill Color:").grid(row=3, column=0, padx=10, pady=5)
tk.Entry(app, textvariable=fill_color, width=20).grid(row=3, column=1, padx=10, pady=5)
tk.Button(app, text="Choose Color", command=select_color).grid(row=3, column=2, padx=10, pady=5)

tk.Button(app, text="Resize Image", command=resize_image).grid(row=4, column=1, pady=20)

app.mainloop()
