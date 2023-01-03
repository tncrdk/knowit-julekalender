import string

def Formatting(link):
    with open(link) as f:
        txt = [i for i in f.read()]
    
    return txt


def FindNthOccurence(txt, alphabet):
    for i in alphabet:
        Index = alphabet.find(i)
        counter = 0
        x = 0
        while x < len(txt):
            if txt[x] == i:
                counter += 1
                if counter == Index:
                    x += 1
                else:
                    txt.pop(x)
            
            else:
                x += 1
        
    
    print("".join(txt))
    


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Python\\Knowit-Julekalender\\13-des\\Bokstavkluss.txt"

txt = Formatting(link)

alphabet = "1" + string.ascii_lowercase

FindNthOccurence(txt, alphabet)