import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

def create_brand_design():
    # Create the main application window
    root = tk.Tk()
    root.title("Zorodo Brand Design")
    root.geometry("800x600")
    root.configure(bg="black")

    # Set up fonts
    header_font = Font(family="Lexend", size=36, weight="bold")
    subheader_font = Font(family="Lexend", size=18)
    text_font = Font(family="Lexend", size=14)

    # Add a title
    title = tk.Label(root, text="Zorodo", font=header_font, bg="black", fg="blue")
    title.pack(pady=20)

    # Add a tagline
    tagline = tk.Label(root, text="Quality and comfort lies in us", font=subheader_font, bg="black", fg="white")
    tagline.pack(pady=10)

    # Add an icon (a simple globe representation)
    canvas = tk.Canvas(root, width=200, height=200, bg="black", highlightthickness=0)
    canvas.pack(pady=20)

    # Draw a globe
    canvas.create_oval(20, 20, 180, 180, outline="blue", width=3)  # Outer circle
    canvas.create_line(100, 20, 100, 180, fill="blue", width=2)    # Longitude line
    canvas.create_line(20, 100, 180, 100, fill="blue", width=2)    # Latitude line
    canvas.create_oval(60, 40, 140, 160, outline="blue", width=2)  # Inner ellipse

    # Add a description
    description = tk.Label(root, \
        text="Funky, youthful clothing for the modern generation. Inspired by global trends.", \
        font=text_font, bg="black", fg="white", wraplength=600, justify="center")
    description.pack(pady=20)

    # Add a footer (example usage on a website)
    footer = tk.Label(root, \
        text="", \
        font=text_font, bg="black", fg="blue", wraplength=700, justify="center")
    footer.pack(pady=20)

    # Run the application
    root.mainloop()

# Call the function to create the brand design
create_brand_design()