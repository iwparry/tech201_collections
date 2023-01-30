# Collection Task - Hero Story

# Write a story, cut it into sections, store each section in a python dictionary

# Defining the dictionary

story1 = {
    "start" : """
    This is the story of Mouse Boy! A young boy named Howard was once bitten by a radioactive mouse and gained
    the powers of a mouse! He could run around undetected and scale rough surfaces impressively and had an incredibly
    appetite for cheese!
    """,
    "middle" : """
    One day Mouse Boy was walking to school and noticed a young gril screaming for help. "Help me! That cat is
    stuck in that tree!" Another onlooker rushed to help whilst Howard stayed back, the onlooker climbed steadily
    up the tree to rescue the cat only to find the mischievous Feline Felon! The villain attacked the innocent
    citizen and took his wallet and fled the scene. Howard however was not going to let him get away, so he chased
    the villain. Howard chased the Feline Felon to a dead end and revealed himself as Mouse Boy. The Feline Felon
    took one look, "You're the one who will stop me?" he said, chuckling at the young hero, to which Mouse Boy replied
    "Your thieving days are over Feline Felon!" Both hero and villain were now locked in a tense showdown with
    one inevitable end. "No mouse is gonna beat me!" the Feline Felon lunges at mouse boy with his claws! What will
    our hero do?
    """,
    "end":"""
    Mouse Boy is stood in a show down with the frightening Feline Felon with no way out, the Felon viciously attacks
    Mouse Boy, striking him with one of his claws! Mouse Boy falls to the ground scarred by the hit. The Feline prepares
    for a finishing blow but Mouse Boy takes advantage of the rough wall right next to him and scales the wall
    dodging his opponents attack and launches a counter flying kick! He catches the villain knocking him down
    and liberating the wallet he stole. "Remember this Felon! Any time you terrorise the people of this city,
    Mouse Boy will be here to take you down", the Feline Felon flees and Mouse Boy returns the wallet to its owner
    saving the day!
    """
}

print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())
print(story1["start"])
print(story1["middle"])
print(story1["end"])
story1["hero"] = "Mouse Boy"
print(story1["hero"])