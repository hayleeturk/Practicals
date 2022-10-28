"""
CP1404 Practical
Read from file and display data
Estimated time:
Actual time:
"""

FILENAME = "wimbledon.csv"


def main():
    records = extract_data(FILENAME)
    name_to_occurrence, countries = calculate_occurrences(records)
    display_data(name_to_occurrence, countries)


def extract_data(filename):
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def calculate_occurrences(records):
    name_to_occurrence = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            name_to_occurrence[record[2]] += 1
        except KeyError:
            name_to_occurrence[record[2]] = 1
    return name_to_occurrence, countries


def display_data(name_to_occurrence, countries):
    print("Wimbledon Champions:")
    for name, occurrence in name_to_occurrence.items():
        print(name, occurrence)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


main()
