import csv
import pprint as pp

filename = "file_for_task2.csv"

users = [
    {"First name": "Oleksandr", "Last name": "Zheliazkov", "Telegram tag": "@pjotr98"},
    {"First name": "Ilya", "Last name": "Apestin", "Telegram tag": "@Ilya_UA"},
    {"First name": "Alexander", "Last name": "Kozhokar", "Telegram tag": "@hey_alex"},
    {"First name": "Rudikan", "Last name": "Rudikan", "Telegram tag": "@Rudikan"},
    {"First name": "Anastasiia", "Last name": "Kostenko", "Telegram tag": "@nastasiia_ko"}
]

with open(filename, "w", newline="") as file:
    columns = ["First name", "Last name", "Telegram tag"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(users)


with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        pp.pprint(row["First name"] + " " + row["Last name"] + " " + row["Telegram tag"])