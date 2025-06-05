import csv #csv.writer() .reader()
max_sales = 0
max_sales_book =None

csv_file = 'Bestseller - Sheet1.csv'
with open(csv_file, 'r', encoding='utf-8') as file:
    csv_read = csv.reader(file)
    file.readline()
    for row in csv_read:
        #print(row)
        sales = float(row[4]) #column 5
        print(sales)
        
        if sales > max_sales:
            max_sales = sales
            max_sales_book =row
        print(max_sales) #find  highest sell value
    
with open('bestsellerfile.csv', 'w', newline='') as newfile:
    csv_write = csv.writer(newfile)
    csv_write.writerow(['book', 'author', 'sales in millions'])
    csv_write.writerow([max_sales_book[0], max_sales_book[1], max_sales_book[4]])
