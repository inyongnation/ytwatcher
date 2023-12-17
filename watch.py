from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
import time

# Set up Firefox options
firefox_options = Options()
firefox_options.add_argument("--headless")  # Run in headless mode (silent)
firefox_options.add_argument("--autoplay-policy=no-user-gesture-required")  # Autoplay
firefox_options.add_argument("--loop")  # Looping

# Path to geckodriver executable, download from: https://github.com/mozilla/geckodriver/releases
geckodriver_path = "/data/data/com.termux/files/usr/bin/"

# Set up Firefox driver with options
driver = webdriver.Firefox(executable_path=geckodriver_path, options=firefox_options)

# YouTube video URL
youtube_video_url = "https://www.youtube.com/watch?v=5sb9fhJzCP0"

# Open YouTube video in the browser
driver.get(youtube_video_url)

# Wait for the video to load (adjust the time based on your internet speed)
time.sleep(5)

# Close the browser
driver.quit()
