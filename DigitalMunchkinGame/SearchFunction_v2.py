from Cards_Samlet import *


def print_card():
    # input part of name you want to search for
    search_input = input('Enter part of name to find\n')

    # read csv, and split on "," the line
    with open('MunchkinTreasureCards.csv', "r") as csv_file:
        reader = csv.reader(csv_file)

        # result of search list variables
        search_result = []

        # loop through the csv list
        for row in reader:
            if len(row) > 1:  # checking for empty rows
                # if input is equel to anything in the file, then it is returned.
                # lower() makes sure it does not distinguish between lower and uppercase.
                if any(search_input.lower() in cell.lower() for cell in row):
                    search_result.append(row)  # adding row to result
        # Throws a message when nothing is found.
        if len(search_result) == 0:
            print("No hits!")
        else:  # printing each result on a new line
            for row in search_result:
                print(row)

            print(f"\n {len(search_result)} results found")  # counting the results
        return search_result


print_card()  # Search for potion!


def return_card():
    file = 'MunchkinTreasureCards.csv'
    with open(file, "r") as csv_file:
        reader = csv.DictReader(csv_file)

        # loop through the csv list
        for row in reader:
            # checking for empty rows
            if len(row) > 1:
                if row["card_type"] == "Weapon":
                    card = WeaponCards(
                        row["card_number"],
                        row["name"],
                        row["card_description"],
                        row["battle_modifier"],
                        row["price"],
                        row["big"])
                    return card
