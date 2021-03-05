# sequence of dna
# sequence
# open files
# read them to memomry
# [] - list
# () - tuple
# {} - dict
def get_files():
    while True:
        try:
            database = open(input("Database: "))
            sequence = open(input("Sequences: "))
            return database, sequence
        except FileNotFoundError:
            print("Please give a available file")


def open_database(database):
    first_line = ""
    names_values = []
    sequence_was = False
    for x in database:
        if sequence_was == False:
            sequence_was = True
            first_line = x
            continue
        names_values.append(x)
    dna_parts = first_line.split(",")
    dna_parts.pop(0)

    return dna_parts, names_values


def analyse_sequence(sequence_string, dna_parts):
    list = []
    for x in dna_parts:
        list.append(sequence_string.count(x))
    return list


def person_from_dna(list_of_sequence_values, names_value):
    people_with_similar_dna = {}
    for x in names_value:
        parts_of_names = x.split(",")
        name = parts_of_names.pop(0)
        count = 0
        similarities = 0
        for parts in parts_of_names:
            if parts == str(list_of_sequence_values[count]):
                similarities += 1
            count += 1
        people_with_similar_dna.update({name: similarities})
    return max(people_with_similar_dna, key=lambda x: people_with_similar_dna[x])


#database, sequence = get_files()
database = open("dna/databases/large.csv")
sequence = open("dna/sequences/9.txt")

sequence_string = sequence.readline()

dna_parts, names_value = open_database(database)

list = analyse_sequence(sequence_string, dna_parts)

print(person_from_dna(list, names_value))
