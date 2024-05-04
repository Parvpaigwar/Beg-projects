

import os
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import threading

def download_video(url, save_path, frame):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        os.makedirs(save_path, exist_ok=True)
        highest_res_stream.download(output_path=save_path)
        messagebox.showinfo('Success', 'Download completed successfully!')
    except Exception as e:
        messagebox.showinfo('Error', f'Failed to download: {e}')
    finally:
        frame.button.config(state=tk.NORMAL)  # Re-enable the button after download completes

def open_file_dialog(frame):
    folder = filedialog.askdirectory()
    if folder:
        frame.label.config(text=f"Selected folder: {folder}")
    return folder

class DownloaderApp:
    def __init__(self, master):
        self.master = master
        master.geometry('500x350')
        master.title("YouTube Downloader")

        self.frame = tk.Frame(master)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = tk.Label(self.frame, text="YouTube Downloader", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)

        image_ = Image.open('luffy_image.png')
        resized_image = image_.resize((120, 120))
        self.img = ImageTk.PhotoImage(resized_image)
        self.image_label = tk.Label(self.frame, image=self.img)
        self.image_label.image = self.img
        self.image_label.pack()

        self.entry1 = tk.Entry(self.frame, width=160)
        self.entry1.insert(tk.END, "Enter YouTube video URL")
        self.entry1.pack(pady=12, padx=10)

        self.button = tk.Button(self.frame, text="Get video!", width=150, height=50, command=self.get_video)
        self.button.pack(pady=12, padx=10)

    def get_video(self):
        self.button.config(state=tk.DISABLED)  # Disable the button during download
        url = self.entry1.get()
        save_dir = open_file_dialog(self)
        if save_dir:
            self.label1 = tk.Label(self.frame, text="Started download...", font=("Roboto", 10))
            self.label1.pack(pady=12, padx=10)
            threading.Thread(target=download_video, args=(url, save_dir, self.frame)).start()
        else:
            messagebox.showinfo('Error', 'Invalid save location!')

if __name__ == "__main__":
    root = tk.Tk()
    app = DownloaderApp(root)
    root.mainloop()
