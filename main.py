from bs4 import BeautifulSoup
import requests

video_mapping = {
	"name": "title",
	"interactionCount": "views",
	"description": "description",
	"datePublished": "datePublished",
	"channelId": "channelId",
	"genre": "genre"
}


def yt_info(link):

	source = requests.get(link, headers={"User-Agent": "Mozilla/5.0"}, verify=False).text
	soup = BeautifulSoup(source, 'html.parser')
	video_info = dict()
	for key in video_mapping.keys():
		meta = soup.find("meta", itemprop=key)
		video_info[video_mapping.get(key)] = meta.get("content", None) if meta else None

	return video_info


if __name__ == "__main__":
	url = "https://www.youtube.com/watch?v=aSnrbKU4kuY"
	print(yt_info(url))
