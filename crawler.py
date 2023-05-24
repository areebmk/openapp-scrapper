import requests
from bs4 import BeautifulSoup
import json


num_results = 10000

query = "site:youtube.com openinapp.co"


url = f"https://www.google.com/search?q={query}&num={num_results}"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

links = soup.find_all("a")

youtube_channel_links = []
for link in links:
    href = link.get("href")
    if href.startswith("/url?q=https://www.youtube.com/channel/"):
        channel_link = href.split("/url?q=")[1].split("&sa=")[0]
        youtube_channel_links.append(channel_link)
    elif href.startswith("/url?q=https://www.youtube.com/watch"):
        video_link = href.split("/url?q=")[1].split("&sa=")[0]
        youtube_channel_links.append(video_link)

with open("youtube_channels.json", "w") as json_file:
    json.dump(youtube_channel_links, json_file, indent=4)

print("Scraping completed. Results saved in JSON formats.")