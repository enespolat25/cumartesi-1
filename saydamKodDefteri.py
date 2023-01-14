from tkinter import *
from tkinter import filedialog

def save_notes(event):
    notes = text_widget.get("1.0", "end-1c")  # 
    file_path = filedialog.asksaveasfilename(defaultextension="*.*", title = "Kayit Turu", filetypes = (("Hersey","*.*"),("text","*.txt"),("python","*.py")))
    with open(file_path, "w") as f:
        f.write(notes)
    print(f"Kod Kaydedildi {file_path}")

def on_key_press(event):
    if event.keysym == 's' and event.state == 4:
        save_notes()

root = Tk()
root.attributes("-alpha", 0.5)
root.title("Kod Defteri")

text_widget = Text(root)
text_widget.config(width=root.winfo_screenwidth(), height=(root.winfo_screenheight()))
text_widget.pack()
text_widget.bind("<Control-s>", save_notes)
root.mainloop()
