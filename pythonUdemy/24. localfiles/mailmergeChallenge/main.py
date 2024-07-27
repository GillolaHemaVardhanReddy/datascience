#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

with open('./Input/Names/invited_names.txt','r') as Names:
    with open('./Input/Letters/starting_letter.txt','r+') as Letter:
        for name in Names:
            letter = Letter.read()
            name = name.replace("\n","")
            letter = letter.replace("[name]",name)
            path = f"./Output/ReadyToSend/{name}.txt"
            newletter = open(path,'w')
            newletter.write(letter)
            Letter.seek(0)
        