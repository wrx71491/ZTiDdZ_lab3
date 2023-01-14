import random, string

def Generator():
    password = ''
    for x in range (0,3):
        password = password + random.choice(string.ascii_uppercase) 
    for x in range (4,7):
        password = password + random.choice(string.ascii_lowercase)  
    for x in range (8,11):     
        password = password + random.choice(string.digits) 
    for x in range (12,15):
        password = password + random.choice(string.punctuation)
    return password
    
    
if __name__ == '__main__':
    print(Generator())
