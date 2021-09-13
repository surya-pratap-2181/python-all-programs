from bs4 import BeautifulSoup
import requests
url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

response = requests.get(url)
# print(response)
# print(response.status_code)
# print(response.content)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())
# print(soup.title.string)
# print(soup.find_all('a'))
# print(soup.find(id="productRating_LSTCOMFVW9TGFYZZGFQWAXP94_COMFVW9TGFYZZGFQ_"))
# for link in soup.find_all('a'):
#     print(link.get('href'))

# for image in soup.find_all('img'):
#     print(image.get('src'))

# product = soup.find_all('div', class_='_2kHMtA')
# print(product)

# product = soup.find('div', attrs={'class': '_2kHMtA'})
# print(product)

titles = []
prices = []
images = []
description = []
links = []
for data in soup.find_all('div', attrs={'class': '_2kHMtA'}):
    title = data.find('div', attrs={'class': '_4rR01T'})
    price = data.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    image = data.find('img', attrs={'class': '_396cs4 _3exPp9'})
    desc = data.find('ul', attrs={'class': '_1xgFaf'})
    lk = data.find('a', attrs={'class': '_1fQZEK'})
    # print(lk.get('href'))
    links.append(lk.get('href'))
    print(links)
    # _1fQZEK
    # print(title.string)
    # print(price.string)
    # print(image.get('src'))
    # lst = []
    # for li in desc:
    # print(li.string)
    # lst.append(li.string)
    # print("****************************")
    # print(lst)
    # description.append(lst)
#     titles.append(title.string)
#     prices.append(price.string)
#     images.append(image.get('src'))
# with open('Alldata.txt', 'w') as f:
#     for title, image, price in zip(titles, images, prices):
#         print(title, file=f)
#         print(image, file=f)
#         print(price, file=f)
    # f.write(title, end='\n')
print(description)
