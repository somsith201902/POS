#basic_csv.py
import csv

def Write(listdata):
	print("Writing...")
	with open('EP2/data.csv', 'a', newline='', encoding='UTF-8') as file:
		fw = csv.writer(file)
		fw.writerow(listdata)

Write(['inter', 22, 1999])