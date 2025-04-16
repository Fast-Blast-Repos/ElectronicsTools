import random as rd
import time as t

tips = ["Try saying \"hello\" to start the conversation.", "Try telling me what you are working on."]

def prind(text):
    """Prints text with a delay."""
    for char in text:
        print(char, end='', flush=True)
        t.sleep(0.01)
    print()

prind("\33[1;49;34mWelcome to Rubber Duck Chat! Chat as usual, but type \"bye\" to quit the chat.")
prind("TIP: Type \"tip\" for tips.")
exit = False
while not exit:
    In = input("\33[1;49;31mYou: \033[m")
    In = In.lower()
    IN = In.split()
    output = ""
    if "bye" in IN or "goodbye" in IN or "farewell" in IN or "bye!" in IN or "goodbye!" in IN or "farewell!" in IN or "x" in IN:
        exit = True
        possableA = ["Bye!", "Goodbye!", "Farewell!"]
        output = rd.choice(possableA)
    elif "hello" in IN or "hi" in IN or "hey" in IN or "howdy" in IN or "greetings" in IN or "sup" in IN or "yo" in IN:
        possableA  = ["Hello!", "Hi!", "Hey!", "Howdy!", "Greetings!"]
        possableB  = ["How are you?", "How's it going?", "How are you doing?", "How's everything?"]
        output = rd.choice(possableA) + " " + rd.choice(possableB)
    elif "good" in IN or "fine" in IN or "great" in IN or "ok" in IN:
        possableA  = ["That's good to hear!", "I'm glad to hear that!", "That's awesome!", "That's great!"]
        possableB  = ["What are you working on?", "What are you up to?", "What are you doing?"]
        output = rd.choice(possableA) + " " + rd.choice(possableB)
    elif "bad" in IN or "sad" in IN or "angry" in IN or "mad" in IN or "upset" in IN or "frustrated" in IN or "disappointed" in IN or "depressed" in IN or "stressed" in IN or "anxious" in IN or "worried" in IN or "nervous" in IN or "fearful" in IN or "scared" in IN or "lonely" in IN or "tired" in IN:
        possableA  = ["I'm sorry to hear that.", "That sucks.", "I understand how you feel.", "I can relate to that."]
        output = rd.choice(possableA)
    elif "im" in IN or "i'm" in IN or "i am" in IN:
        if "making" in IN or "creating" in IN or "designing" in IN or "working" in IN or "building" in IN or "developing" in IN or "coding" in IN or "programming" in IN: 
            possableA = ["That's great!", "That's awesome!", "That's cool!", "That's interesting!"]
            output = rd.choice(possableA)
    elif IN == "tip":
        output = rd.choice(tips)
    elif "skill" in IN and "issue" in IN or "fuck" in IN and "you" in IN:
        possableA = ["That isn't nice!", "How dare you?!"]
        output = rd.choice(possableA)
    elif "how" in IN and "to" in IN or "what" in IN and "is" in IN or "how" in IN and "many" in IN or "how" in IN and "much" in IN or "how" in IN and "do" in IN or "what" in IN and "are" in IN or "where" in IN and "is" in IN or "when" in IN and "is" in IN or "how" in IN and "does" in IN or "what" in IN:
        if "chatgpt" in IN or "chat" in IN and "gpt" in IN or "gemini" in IN:
            possableA = ["I have no idea.", "I don't know.", "I have no clue.", "I wouldn't know."]
            output = rd.choice(possableA) + " Maybe ask ChatGPT?"
        else:
            possableA = ["I have no idea.", "I don't know.", "I have no clue.", "I wouldn't know."]
            possableB = ["Why don't you try looking it up?", "Maybe try asking someone else?", "Have you tried searching for it?", "Maybe ask ChatGPT?"]
            output = rd.choice(possableA) + " " + rd.choice(possableB)
    elif "puck" in IN:
        output = "That's not a nice thing to say!"
    else:
        output = "I don't understand what you're saying. " + rd.choice(tips)
    t.sleep(1)
    prind("\33[1;49;33mRubber Duck: \033[m" + output)