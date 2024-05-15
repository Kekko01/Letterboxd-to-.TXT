import csv
with open('diary.csv', 'r') as file:
    reader = csv.reader(file)
    lines = 0
    for row in reader:
        if lines == 0:
            lines += 1
        else:
            with open('films.txt', 'a') as f:
                f.write(row[1] + "\n")
            print(row)
            lines += 1

print("Total number of films:", lines - 1)