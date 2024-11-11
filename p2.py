import sys
sys.path.append("C:/Users/admin/AppData/Local/Programs/Python/Python312/p1.py")
from p1 import*
print(responses[0])
print(responses[1])
while True:
    text = input("Please Ask:")
    for w in text.split():
        if w.upper() in operations.keys():
            try:
                l=extract_num(text)
                r=operations[w](l[0],l[1])
                print(r)
                break
            except:
                print("Please ask coorect questions")
                break
        elif w.upper() in commands.keys():
            commands[w.upper()]()
            break
    else:
        print(responses[4])
        print(responses[5])
                             
            
    
