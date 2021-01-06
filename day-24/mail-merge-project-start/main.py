#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open('./Input/Names/invited_names.txt') as names:
    for name in names:
        stripped_name = name.strip()
        with open('./Input/Letters/starting_letter.docx') as f2:
            content = f2.read()

            with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode='w') as letter:
                letter.write(content.replace('[name]',stripped_name))
            
