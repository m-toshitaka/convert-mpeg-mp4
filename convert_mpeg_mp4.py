import subprocess
import tkinter as tk
from tkinter import filedialog

# 設定ファイルの読み込み
with open("config.txt") as f:
    config = dict(line.strip().split("=") for line in f)

# 変換に必要な情報を取得
video_encoder = config["video_encoder"]
video_bitrate = config["video_bitrate"]
video_resolution = config["video_resolution"]
video_framerate = config["video_framerate"]
audio_bitrate = config["audio_bitrate"]
audio_samplerate = config["audio_samplerate"]

# ファイルを選択
root = tk.Tk()
root.withdraw()
files = filedialog.askopenfilenames(title="Select Files")

# 変換後の保存先を選択
output_dir = filedialog.askdirectory(title="Select Output Directory")

# 変換処理
for file in files:
    output_file = f"{output_dir}/{file.split('/')[-1].split('.')[0]}.mp4"
    subprocess.run([
        "ffmpeg",
        "-i", file,
        "-c:v", video_encoder,
        "-b:v", video_bitrate,
        "-s", video_resolution,
        "-r", video_framerate,
        "-c:a", "aac",
        "-b:a", audio_bitrate,
        "-ar", audio_samplerate,
        output_file
    ])
