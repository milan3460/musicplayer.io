import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x150")

        mixer.init()

        self.track = tk.StringVar()
        self.status = tk.StringVar()

        track_frame = tk.LabelFrame(self.root, text="Song Track", font=("times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=tk.GROOVE)
        track_frame.place(x=0, y=0, width=400, height=50)

        track_label = tk.Label(track_frame, textvariable=self.track, width=20, font=("times new roman", 10, "bold"), bg="grey", fg="white")
        track_label.grid(row=0, column=0)

        status_label = tk.Label(track_frame, textvariable=self.status, font=("times new roman", 10, "bold"), bg="grey", fg="white")
        status_label.grid(row=0, column=1)

        button_frame = tk.LabelFrame(self.root, text="Control Panel", font=("times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=tk.GROOVE)
        button_frame.place(x=0, y=50, width=400, height=100)

        play_button = tk.Button(button_frame, text="PLAY", command=self.play_song, width=6, height=1, font=("times new roman", 12, "bold"), bg="grey", fg="white")
        play_button.grid(row=0, column=0, padx=10, pady=5)

        pause_button = tk.Button(button_frame, text="PAUSE", command=self.pause_song, width=8, height=1, font=("times new roman", 12, "bold"), bg="grey", fg="white")
        pause_button.grid(row=0, column=1, padx=10, pady=5)

        stop_button = tk.Button(button_frame, text="STOP", command=self.stop_song, width=6, height=1, font=("times new roman", 12, "bold"), bg="grey", fg="white")
        stop_button.grid(row=0, column=2, padx=10, pady=5)

        select_button = tk.Button(button_frame, text="SELECT SONG", command=self.select_song, width=15, height=1, font=("times new roman", 12, "bold"), bg="grey", fg="white")
        select_button.grid(row=1, column=1, padx=10, pady=5)

    def select_song(self):
        self.song = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Song", filetypes=(("MP3 files", "*.mp3"), ("WAV files", "*.wav")))
        self.track.set(self.song)

    def play_song(self):
        try:
            mixer.music.load(self.song)
            mixer.music.play()
            self.status.set("Playing")

        except:
            tk.messagebox.showerror("Error", "No Song Found")

    def pause_song(self):
        mixer.music.pause()
        self.status.set("Paused")

    def stop_song(self):
        mixer.music.stop()
        self.status.set("Stopped")

root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
