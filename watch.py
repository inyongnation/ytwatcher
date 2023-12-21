import webbrowser
import time
import pyautogui

def open_youtube_video(video_id):
    try:
        youtube_url = f"https://www.youtube.com/watch?v=XvkEiIwt-UU&autoplay=1&mute=1"
        webbrowser.open(youtube_url)
        # Tunggu sejenak agar video dimuat sebelum mengatur volume
        time.sleep(5)
        # Nonaktifkan suara dengan mengatur volume menjadi 0
        pyautogui.press('volumemute')
    except webbrowser.Error:
        print("Gagal membuka video YouTube. Pastikan koneksi internet Anda terhubung.")

# Ganti 'VIDEO_ID' dengan ID video YouTube yang ingin Anda buka
video_id = 'VIDEO_ID'

# Loop membuka video YouTube sebanyak 5 kali
for _ in range(5):
    open_youtube_video(video_id)
    # Tambahkan delay sejenak sebelum membuka video berikutnya
    time.sleep(10)

# Tambahkan delay sejenak sebelum menutup aplikasi
time.sleep(5)