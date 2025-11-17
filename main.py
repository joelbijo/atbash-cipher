'''
This is an Alphabetic Substitution Tool which can be used for encoding/decoding.
A -> Z and a -> z and likewise. Also known as Atbash Cipher
'''

print("\nThis is a classic Atbash Cipher\n")

string=""
ch=input("Enter text: ")
for i in ch:
    if((i >= 'A') and (i <= 'Z')):
        n = ord(i)  # Converting char to ascii
        dist = n - 65 # Distance from A

        # Swap A with Z using the positions. 0 is A and 25 is Z
        dist = 25 - dist
        nstring = chr(dist + 65) #Converting ascii to char by converting position to the other side of the alphabets
        string += nstring
    
    elif((i >= 'a') and (i <= 'z')):
        n = ord(i)  # Converting char to ascii
        dist = n - 97 # Distance from 'a'

        # Swap 'a' with 'z' using the positions. 0 is 'a' and 25 is 'z'
        dist = 25 - dist
        nstring = chr(dist + 97) #Converting ascii to char by converting position to the other side of the alphabets
        string += nstring
    
    else:
        string += i
    
print("Atbash result: ",string)
    
        
        
