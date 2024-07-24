import tkinter as tk
from tkVideoPlayer import TkinterVideo


HEIGHT = 700
WIDTH = 800



root = tk.Tk()

#Canvas
canvas = tk.Canvas(root, height = HEIGHT, width=WIDTH)
canvas.pack()

#Background Picture
background_img = tk.PhotoImage(file = "GundamNarrative2.png")
background_label = tk.Label(root, image=background_img)
background_label.place(relwidth=1, relheight=1)

#Background
background = tk.Frame(root, bg = "blue")
background.place(relx=.5, rely=.1, relwidth=0.75, relheight=0.1, anchor="n")

# Buttons
record_button = tk.Button(background, text = "Record", bg = "green")
record_button.place(relx = 0, rely = .5, relwidth = 0.15, relheight = .5)

skeleton_button = tk.Button(background, text = "Skeleton", bg = "red")
skeleton_button.place(relx = .4, rely = .5, relwidth = 0.15, relheight = .5)

frame_button = tk.Button(background, text = "Frame", bg = "yellow")
frame_button.place(relx = .85, rely = .5, relwidth = 0.15, relheight = .5)

#Label
video_label = tk.Label(background, text = "Enter video name below")
video_label.place(relx = 0.4, rely=0, relwidth=.25, relheight=.15)

#Entry Area
entry = tk.Entry(background, bg = 'gray')
entry.place(relx = 0.4, rely=.15, relwidth=.25, relheight=.35)

#Bottom Frame
bottom_frame = tk.Frame(root, bg = "blue", bd=10)
bottom_frame.place(relx = .5, rely=0.25, relwidth=.75, relheight=.65, anchor = "n")

#Screen
screen = tk.Label(bottom_frame, text = "I want video to play here", bg = "gray")
screen.place(relx=0, rely=0, relwidth=1, relheight=1)

#Error in line below
videoplayer = TkinterVideo(screen, scaled=True, pre_load=False)
videoplayer.load("D:\project - 4 ( AI Assistent )\Brain.mp4")
videoplayer.place(relx=0, rely=0, relwidth=1, relheight=1)

videoplayer.play()


root.mainloop()
