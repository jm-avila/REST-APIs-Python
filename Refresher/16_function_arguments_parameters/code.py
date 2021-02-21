def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

# Positional parameters, values are determined by the position
say_hello("Bob", "Smith")

# Nameds parameters, values are determined by their name
say_hello(surname="Smith", name="Bob")

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")

divide(dividend=15, divisor=0)