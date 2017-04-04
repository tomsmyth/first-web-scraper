import csv
import requests
from BeautifulSoup import BeautifulSoup

years = ['2017/04', '2017/03', '2017/02', '2017/01', '2016/12', '2016/11', '2016/10', '2016/09', '2016/08', '2016/07', '2016/06', '2016/05', '2016/04', '2016/03', '2016/02', '2016/01', '2015/12', '2015/11', '2015/10', '2015/09', '2015/08', '2015/07', '2015/06', '2015/05', '2015/04', '2015/03', '2015/02', '2015/01', '2014/12']
list_of_rows = []

for year in years:
	print year
	response = requests.get("http://m.mlb.com/was/roster/transactions/" + year)
	html = response.content

	soup = BeautifulSoup(html)
	table = soup.find('table')

	for row in table.findAll('tr')[1:]:
		list_of_cells = []
		list_of_cells.append(year)
		for cell in row.findAll('td'):
			list_of_cells.append(cell.text.encode('utf-8'))
		list_of_rows.append(list_of_cells)

outfile = open("transactions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["date", "url", "text"])
writer.writerows(list_of_rows)
