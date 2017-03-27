import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://columbian.gwu.edu/2015-2016'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
    	if cell.text[0] == '(':
    		party, state = cell.text.split(',')
    		list_of_cells.append(party)
    		list_of_cells.append(state)
    	else:
    		list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)

outfile = open("college.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["dept", "faculty", "sponsor", "title"])
writer.writerows(list_of_rows)