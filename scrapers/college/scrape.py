import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://columbian.gwu.edu/2015-2016'
url2 = 'https://columbian.gwu.edu/2014-2015'
url3 = 'https://columbian.gwu.edu/2013-2014'
url4 = 'https://columbian.gwu.edu/2012-2013'
url5 = 'https://columbian.gwu.edu/2011-2012'
url6 = 'https://columbian.gwu.edu/2010-2011'
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
writer.writerow(["year", "dept", "faculty", "sponsor", "title"])
writer.writerows(list_of_rows)