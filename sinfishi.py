from datetime import datetime

def register():
    
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    print("Registering")
    today = datetime.now()
    
    def save():
        
        with open("user_data.txt", "a") as file:
            file.write(f"{name} {last_name} {today}\n")
            print("Registration successful")
            
    return save

res = register()
print(res())


def clculate(a,b):
    def command():
        pass
    
    def plus():
        return a + b
    
    def minus():
        return a - b
    
    def multiply():
        return a * b
    
    def divide():
        if b == 0:
            return "Error: Division by zero"
        return a / b
    
    command.plus = plus
    command.minus = minus
    command.multiply = multiply
    command.divide = divide
    
    return command
calculator = calcu