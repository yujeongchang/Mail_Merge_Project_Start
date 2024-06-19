PLACE_HOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as name_file:
    names_list = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter_content = starting_letter.read()
    for name in names_list:
        stripped_name = name.strip()   #str data type
        personalized_letter = letter_content.replace(PLACE_HOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as data:
            data.write(personalized_letter)