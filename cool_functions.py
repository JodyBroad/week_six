# define some useful functions
def cool_func1(name):
    return "Hello " + name + " from cool func 1"

def cool_fun2(name):
    return "Hola " + name + " from cool func 2"

# wrap all of the code that is not a function in this extra function main so that it does run when you import it

# invoking my own useful functions
def main():
    message = cool_func1("Everyone")
    greeting = cool_fun2("Team")

    print(message, "\n", greeting)

    # __name__ causes __main__ string in place of filename - main indicates it is the launching script; knowing that means we can use the "main trick" when importing files. This allows us to seperate our function and class definitions away from the code that actually uses them
    print("Cool Functions", __name__)

# so if this file is the __main__ one it will run all the executable code, but if it is imported elsewhere it won't run this code
if __name__ == "__main__":
    main()