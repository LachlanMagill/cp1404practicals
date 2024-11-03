import csv

filename = "wimbledon.csv"
champion_counts = {}
countries = set()

with open(filename, "r", encoding="utf-8-sig") as in_file:
    reader = csv.reader(in_file)
    next(reader)
    for row in reader:
        champion = row[0]
        country = row[1]


        if champion not in champion_counts:
            champion_counts[champion] = 0
        champion_counts[champion] += 1

        countries.add(country)

print("Wimbledon Champions:")
for champion in sorted(champion_counts):
    print(f"{champion} {champion_counts[champion]}")

sorted_countries = sorted(countries)
print(f"\nThese {len(sorted_countries)} countries have won Wimbledon: ")
print(", ".join(sorted_countries))
