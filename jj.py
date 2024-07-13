import requests
import pandas
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=iphone+13&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=iphone+13%7CMobiles&requestId=ff4f0054-7da3-462b-9f4d-22a68a69e7e6")
#print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
names=soup.find_all('div',class_="_4rR01T")
#print(names)
name=[]
for i in names[0:12]:
    d=i.get_text()
    name.append(d)
#print(name)

prices=soup.find_all('div',class_="_30jeq3 _1_WHN1")
#print(names)
price=[]
for i in prices[0:12]:
    d=i.get_text()
    price.append(d)
#print(price)


ratings=soup.find_all('div',class_="_3LWZlK")
#print(names)
rate=[]
for i in ratings[0:12]:
    d=i.get_text()
    rate.append(float(d))
#print(rate)



reviews=soup.find_all('span',class_="_2_R_DZ")
#print(names)
review=[]
for i in reviews[0:12]:
    d=i.get_text()
    review.append(d)
#print(review)


features=soup.find_all('li', class_="rgWa7D")
#print(names)
feature=[]
for i in features[0:12]:
    d=i.get_text()
    feature.append(d)
#print(feature)



links=soup.find_all('a',class_="_1fQZEK")
#print(names)
link=[]
for i in links[0:12]:
    d="https://www.flipkart.com"+i['href']
    link.append(d)
#print(link)




images=soup.find_all('img',class_="_396cs4" )
#print(names)
image=[]
for i in images[0:12]:
    d=i['src']
    image.append(d)
#print(image)

df=pandas.DataFrame()
#print(df)
data={'Names':name,"Price":price,"Ratings":rate,"Features":feature,"Reviews":review,"Images":image,"Links":link}
#print(data)
df=pandas.DataFrame(data)
#print(df)
df.to_csv("mobiles_data.csv")
