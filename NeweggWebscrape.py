from bs4 import BeautifulSoup as Soup
import re
import requests

newEggUrl = "https://www.newegg.com/p/pl?d=macbook"

page = requests.get(newEggUrl)
soup = Soup(page.content, "html.parser")


""" Getting Block Info """

items = soup.find_all('div', {"item-cell"})
price = soup.find_all('div', {})

models = []
price = []
cpus = []
rams = []


""" Looping through and ordering data """


for item in items:
	title = item.find('a', {"item-title"}).text
	if title[0:5] == "Apple":
		#print(title)

		""" Finding the model"""	

		model = re.search("Pro|Air", title)
		if model == None:
			models.append('NA')
		else:
			models.append(model.group())

		""" Finding Cpu """

		cpu = re.search("[i][5/7].+GHz.", title)
		if cpu == None:
			cpus.append('NA')
		else:
			cpus.append(cpu.group())

		""" Finding RAM """

		ram = re.search("\d.GB.Memory|\d\d.GB.Memory|[4|8].GB|[4|8]GB", title)
		if ram == None:
			rams.append('NA')
		else:
			rawRam = ram.group()
			raw = re.search("\d+", rawRam)
			rams.append(raw.group() + " GB Ram")

		""" Finding Price """

		cost = item.find('li', {"price-current"}).text
		costs = cost.split('.')
		if len(costs) == 0:
		 	price.append("NA")
		else:
			price.append(costs[0])


""" Displaying Data """

itemNumber = 1
for w,x,y,z in zip(models, price, cpus, rams):

	print(f"{'('+str(itemNumber)+')':<5}  {'Macbook '+ w:<15}   {str(x):<7}   {str(y):<35}  {str(z):<10}")
	print(' ')
	itemNumber += 1






