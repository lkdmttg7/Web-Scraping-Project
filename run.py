from multiprocessing import Pool
import csv
import datetime
import requests
from bs4 import BeautifulSoup




def get_headline(day):
	try:
		source_code = requests.get(day)
		plain_text = source_code.text
		date = day[37:46]
		print(date)
		soup = BeautifulSoup(plain_text,"lxml")
		for x in soup.find('div',{'style':'font-family:arial ;font-size:12;font-weight:bold; color: #006699'}):
			for i in x.findAll('a'):
				#print(i.get('href'))
				headline,link = i.string,i.get('href')

				if 'malnutrition' in headline:
					#headline_1.append(headline)
					csv_writer.writerow([date,headline,link])
	except:
		pass



csv_file = open('toi_headlines.csv','w',newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Date','Headline','link'])
begin_time = datetime.datetime.now()
day_url = []
with open("toi_day_urls.txt", "r") as f:
    for line in f:
        day_url.append((line.strip()))
p = Pool(50)
date_u = day_url[0:100]
records = p.map(get_headline, date_u)
p.terminate()
p.join()