
def Formatting(link):
    with open(link) as f:
        txt = f.read()
        
    txt = [int(i) for i in txt if i != "\n"]
    
    return txt
    

def Travel(reiserute):
    Energy = 10
    pos = 0
    
    while Energy > 0:
        Energy -= 1
        
        if pos >= len(reiserute):
            break
        
        if reiserute[pos] == 1:
            Energy += 2
        
        pos += 1
        
    print(pos)


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Knowit-Julekalender\\24-des\\Julereisen.txt"

reiserute = Formatting(link)

Travel(reiserute)



