def encrypt(text,s):
    result = ""
 
    
    for i in range(len(text)):
        char = text[i]
 
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
 

text = "RUNNINGCLASS"
s = 6
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("encrypt Cipher: " + encrypt(text,s))
print ("decrypt Cipher: " + encrypt(text,26-s))