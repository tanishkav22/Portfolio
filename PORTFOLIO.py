import tkinter as tk
import time

# Main window
root = tk.Tk()
root.title("My Digital Portfolio!")
root.geometry("700x450")
root.resizable(False, False)

# Theme colors
light_bg = "#f5f5f5"
dark_bg = "#1e1e1e"
accent = "#E9697E"

current_bg = light_bg
root.configure(bg=current_bg)

# Header
header = tk.Label(
    root,
    text="",
    font=("Helvetica", 24, "bold"),
    bg=current_bg,
    fg=accent
)
header.pack(pady=15)

# Typing animation
def typing_effect(text):
    header.config(text="")
    for i in range(len(text) + 1):
        header.config(text=text[:i])
        root.update()
        time.sleep(0.05)

typing_effect("Hello, I'm a Python Developer 🚀")

# Content area
content = tk.Label(
    root,
    text="",
    font=("Helvetica", 13),
    bg=current_bg,
    fg="#333",
    justify="left"
)
content.pack(pady=10)

# Sections
def show_about():
    content.config(
        text="👤 About Me\n\n"
            "Hello This is me Tanishka Vardam\n"
             "I am a passionate student developer who loves\n"
             "creating creative Python applications.\n"
             "I enjoy learning new technologies and\n"
             "building real-world projects."
    )

def show_skills():
    content.config(
        text="🛠 Skills\n\n"
             "• Python\n"
             "• Tkinter (GUI)\n"
             "• HTML & CSS\n"
             "• Basic Cybersecurity"
             
    )

def show_projects():
    content.config(
        text="📂 Projects\n\n"
             "• Digital Clock with Themes\n"
             "• GUI Calculator\n"
             "• Password Generator\n"
             "• Quiz App\n"
             "• To-Do List Application"
    )

def show_contact():
    content.config(
        text="📧 Contact\n\n"
             "Email: tanv22@gmail.com\n"
             "GitHub: github.com/tanishkav22\n"
             "LinkedIn: linkedin.com/in/tanishka-vardam"
    )

# Theme toggle
def toggle_theme():
    global current_bg
    if current_bg == light_bg:
        current_bg = dark_bg
        fg_color = "#ffffff"
    else:
        current_bg = light_bg
        fg_color = "#333"

    root.configure(bg=current_bg)
    header.configure(bg=current_bg)
    content.configure(bg=current_bg, fg=fg_color)
    btn_frame.configure(bg=current_bg)

# Buttons frame
btn_frame = tk.Frame(root, bg=current_bg)
btn_frame.pack(pady=10)

# Buttons
btn_style = {
    "width": 12,
    "bg": accent,
    "fg": "white",
    "font": ("Helvetica", 10, "bold"),
    "bd": 0
}

tk.Button(btn_frame, text="About", command=show_about, **btn_style).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Skills", command=show_skills, **btn_style).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Projects", command=show_projects, **btn_style).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Contact", command=show_contact, **btn_style).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Theme", command=toggle_theme, **btn_style).grid(row=0, column=4, padx=5)

# Footer
footer = tk.Label(
    root,
    text="© 2026 | Python GUI Portfolio",
    font=("Helvetica", 9),
    bg=current_bg,
    fg="#888"
)
footer.pack(side="bottom", pady=10)

# Default section
show_about()

# Run app
root.mainloop()
