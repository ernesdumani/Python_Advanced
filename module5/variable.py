#greeting="Hello"


#def greet(name):
   # message=f"{greeting}, {name}"
   #print(message)

#greet("ernes")

#greet(message)
def greet():
    global greeting
    greeting= "goodbye"
    global name
    name="Alice"
    message=f"{greeting}, {name}"
    print(message)

greet()
print(greeting)
print(name)