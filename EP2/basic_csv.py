#basic_csv.py
import csv

def Write(listdata):
	print("Writing...")
	# ( a = append , w = write)
	with open('data.csv', 'a', newline='', encoding='utf-8') as file:
		fw = csv.writer(file)
		fw.writerow(listdata)
		
Write(["inter",21,1999])  