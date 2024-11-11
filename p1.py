responses = ["Hello, My name is Robot","What may I help you","Thank You","Bye-Bye","Sorry, I dont know this", "But Next time surely I will do for you"]
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def end():
    print(responses[2])
    print(responses[3])
def extract_num(text):
    l1=[]
    for w in text_split():
        try:
            l1.append(float(w))
        except:
            pass
    return l1
def ajay():
    print("Ajay is student of Coding Seekho,He is in 2nd year of engineering")
operations = {"ADDITION":add, "SUM":add, "PLUS":add, "SUB":sub, "MINUS":sub}
commands = {"AJAY":ajay, "BYE":end, "BYE BYE":end , "EXIT":end}   
