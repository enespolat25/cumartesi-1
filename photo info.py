import exifread
from tkinter import *
from tkinter import filedialog

def select_photo():
    filepath = filedialog.askopenfilename()
    with open(filepath, 'rb') as f:
        tags = exifread.process_file(f)
        exif_data = ""
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                exif_data += f"{tag:25}: {tags[tag]}\n"
        text_widget.configure(state='normal')
        text_widget.delete('1.0', END)
        text_widget.insert(END, exif_data)
        text_widget.configure(state='disabled')

root = Tk()
root.configure(bg='gray')
root.attributes("-alpha", 0.9)
root.title("Photo info")
root.geometry("400x400")
root.maxsize(400,400)
root.minsize(400,400)

select_button = Button(root, text="Select Photo",background='White', command=select_photo)
select_button.pack()

text_widget = Text(root)
text_widget.pack()

root.mainloop()
