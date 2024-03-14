import csv

details = []
with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    details = [line.strip().split(',') for line in in_file.readlines()]

score = {}
for champion in details:
    name = champion[2]
    score[name] = score.get(name, 0) + 1

countries = sorted(set(champion[1] for champion in details))

print("Wimbledon Champions:")
for champion, count in score.items():
    print(f"{champion} {count}")

print("These", len(countries), "countries have won Wimbledon:")
print(", ".join(countries))