from bs4 import BeautifulSoup
import requests

url = "https://www.islamicfinder.org/world/algeria/2498611/chlef-prayer-times/"
html_text = requests.get(url)
soup = BeautifulSoup(html_text.content, "lxml")
prayername = soup.find_all('span', "prayername")
prayertime = soup.find_all('span', "prayertime")

dic = {}
for i in range(len(prayername)):
    dic[prayername[i].text] = prayertime[i].text

print(dic)
