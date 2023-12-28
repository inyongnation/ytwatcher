import webbrowser
import time

def open_youtube_video(video_id):
    try:
        # Tambahkan parameter --mute untuk membuka video tanpa suara
        youtube_url = f"https://www.youtube.com/watch?v=HLYPvtaCRcU&list=PLwjFKs8GCaKwZAZDHFciG0foxJPSZxFNk&index=1"
        webbrowser.open(youtube_url)
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