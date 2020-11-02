from pytube import YouTube
import tkinter as tk


def choose():
    if not var.get():
        return video_download()
    elif var.get():
        return audio_download()


def get_filters():
    try:
        URL = link_entry.get()
        yt_object = YouTube(URL)
    except Exception as e:
        print(e)
        textfield.delete(1.0, 'end')
        textfield.insert(1.0, "Not found")
    return yt_object.streams


def audio_download():
    textfield.delete(1.0, 'end')
    textfield.insert(1.0, "Downloading audio")
    get_filters().get_audio_only().download()


def video_download():
    textfield.delete(1.0, 'end')
    textfield.insert(1.0, "Downloading video")
    get_filters().get_highest_resolution().download()


# defining interface
win = tk.Tk()
win.title("YT downloader")
win.geometry("500x150+200+200")
win.resizable(False, False)

# widgets
label_link = tk.Label(win, text="YouTube link", padx=5, pady=5,
                      font=('Roboto', 12))
label_only_audio = tk.Label(win, text="Only audio", padx=5, pady=5,
                            font=('Roboto', 12))
link_entry = tk.Entry(win, font=('TimesNewRoman', 12))

var = tk.BooleanVar()
var.set(False)
check_audio = tk.Checkbutton(win, variable=var, offvalue=False, onvalue=True)

load = tk.Button(win, text="Download", padx=5, pady=5, command=choose)
textfield = tk.Text(win, font=('Roboto', 12), height=1, width=53, padx=5, pady=5, )

# placing
label_link.grid(row=0, column=0, stick='we')
label_only_audio.grid(row=1, column=0, stick='we')
link_entry.grid(row=0, column=1, stick='we')
check_audio.grid(row=1, column=1, stick='w')
load.grid(row=2, column=0)
textfield.grid(row=3, column=0, columnspan=2, stick='w')

win.grid_columnconfigure(1, minsize=390)

win.mainloop()
