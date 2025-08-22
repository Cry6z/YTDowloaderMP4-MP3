import os
from yt_dlp import YoutubeDL

DEFAULT_PATH = os.path.join(os.path.expanduser("~"), "Downloads")

def download_video(url, path=DEFAULT_PATH):
    if not os.path.exists(path):
        os.makedirs(path)

    ydl_opts = {
        'outtmpl': f'{path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',  
        'merge_output_format': 'mp4'
    }

    with YoutubeDL(ydl_opts) as ydl:
        print("🔽 Sedang mendownload video (MP4)...")
        ydl.download([url])
        print(f"✅ Video berhasil didownload ke folder: {path}")


def download_audio(url, path=DEFAULT_PATH):
    if not os.path.exists(path):
        os.makedirs(path)
    ydl_opts = {
        'outtmpl': f'{path}/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{ 
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with YoutubeDL(ydl_opts) as ydl:
        print("🔽 Sedang mendownload audio (MP3)...")
        ydl.download([url])
        print(f"✅ Audio berhasil didownload ke folder: {path}")


if __name__ == "__main__":
    print("=== 🎬 YouTube Downloader ===")
    link = input("Masukkan link YouTube: ")
    mode = input("Pilih mode (1 = Video MP4, 2 = Audio MP3): ")

    if mode == "1":
        download_video(link)
    elif mode == "2":
        download_audio(link)
    else:
        print("❌ Pilihan tidak valid!")