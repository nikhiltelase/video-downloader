import tkinter
import customtkinter
from plyer import notification
from pytube import YouTube


def download():
    video_resolution = resolutions_box.get()
    send_notification("Your video is downloading")
    try:
        youtube_link = link.get()
        youtube_object = YouTube(youtube_link)
        if video_resolution == "Lowest Quality":
            video = youtube_object.streams.get_lowest_resolution()
        else:
            video = youtube_object.streams.get_highest_resolution()
        title.configure(text=youtube_object.title)
        video.download("C:/Users/Lenovo/Videos/python downloader/")
        finished_label.configure(text="Download Completed", text_color="green")
        send_notification("Download Successful")
    except:
        finished_label.configure(text="Download Error", text_color="red")


def send_notification(message):
    print("ram ram ")
    notification.notify(
        title='Python Downloader',
        app_name='python',
        message=message,
        app_icon='icon.ico',
        timeout=5  # seconds
    )


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# Our apa frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Video Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link", font=('Times', 20, "bold"))
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# create a resolution combo box
resolutions = ["Highest Quality", "Lowest Quality"]
resolutions_box = customtkinter.CTkComboBox(app, values=resolutions)
resolutions_box.pack(padx=20, pady=20)
resolutions_box.set("Highest Quality")

# Finished DownLoading
finished_label = customtkinter.CTkLabel(app, text="")
finished_label.pack()

# Download Button
download_button = customtkinter.CTkButton(app, text="Download", command=download)
download_button.pack(padx=20, pady=20)

# run app
app.mainloop()
