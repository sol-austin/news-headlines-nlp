import requests
from bs4 import BeautifulSoup

url = ["https://www.dailymail.co.uk/home/sitemaparchive/day_", 20210216, ".html"]
res_arr = []

for year in range(2020, 2021):
    for month in range(1, 13):
        for day in range(1, 10):
            url[1] = str(year) + str(month).zfill(2) + str(day).zfill(2)
            res = requests.get(''.join(url))
            res_arr.append(res)
            print('done')
            print(year, month, day)

headlines_arr = []

for res in res_arr:
    soup = BeautifulSoup(res.content, 'html.parser')

    headlines_container = soup.find("ul", {"class": "archive-articles debate link-box"})
    headlines_tags = headlines_container.findChildren("a")

    for headline in headlines_tags:
        headlines_arr.append(headline.string)
    print(len(headlines_arr))

f = open("headlines.txt", "w")
f.write('\n'.join(headlines_arr))
