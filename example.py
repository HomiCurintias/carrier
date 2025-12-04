import carrier
import hashlib as hash

def hasher(string):
    sha = hash.sha256(string.encode()).hexdigest()
    
    return sha
    
def armazen(name, password):
    carrier.ncar(f"{name}.carrier", "password", hasher(password))

def checker(name, password):
    hashed = hasher(password)
    
    userPass = carrier.body(f"{name}.carrier", "password")
    
    if hashed == userPass:
        print("Loged in")
    else:
        print("wrong password")

prompt = input("Name: ")
prompt2 = input("Password: ")

if prompt != "login":
    armazen(prompt, prompt2)
else:
    name = input("Username: ")
    password = input("Password: ")
    
    checker(name, password)
