def parse_bool(value):
    normalized = value.strip().lower()
    true_values = {"true", "1", "yes", "y", "t"}
    false_values = {"false", "0", "no", "n", "f"}

    if normalized in true_values:
        return True
    if normalized in false_values:
        return False
    raise ValueError("Please enter true/false, yes/no, 1/0")


def read_value(prompt, parse_func):
    while True:
        text = input(prompt)
        try:
            return parse_func(text)
        except ValueError as exc:
            print("Invalid input:", exc)
            print("Please try again.")


def main():
    a = read_value("Enter an integer value for a: ", int)
    b = read_value("Enter a number for b: ", float)
    c = read_value("Enter a complex number for c (e.g. 1+2j): ", complex)
    i = read_value("Enter another complex number for i (e.g. 3-4j): ", complex)
    d = read_value("Enter a boolean value for d (true/false): ", parse_bool)
    j = read_value("Enter a boolean value for j (true/false): ", parse_bool)
    e = input("Enter a string value for e: ")
    f = list(input("Enter a value for f (each character becomes a list element): "))
    g = tuple(input("Enter a value for g (each character becomes a tuple element): "))
    h = set(input("Enter a value for h (each character becomes a set element): "))

    Addition = a + b
    Substraction = a - b
    Multiplication = a * b
    Division = a / b
    floor_division = a // b
    power = a ** b

    complex_number_Addition = c + i
    complex_number_Substraction = c - i
    complex_number_Multiplication = c * i
    complex_number_Division = c / i

    bool_And = d and j
    bool_Or = d or j
    bool_Not = not d
    bool_Xor = d ^ j
    bool_Nand = not (d and j)
    bool_Nor = not (d or j)
    bool_Xnor = not (d ^ j)

    str_Concatenation = e + e
    str_Replication = e * 3
    str_Slicing = e[0:3]
    str_Reverse = e[::-1]
    str_Length = len(e)
    str_Uppercase = e.upper()
    str_Lowercase = e.lower()
    str_Capitalize = e.capitalize()
    str_Title = e.title()
    str_Strip = e.strip()
    str_Replace = e.replace("a", "b")
    str_Split = e.split()
    str_Join = "-".join(e)
    str_Find = e.find("a")
    str_Count = e.count("a")
    str_Isalnum = e.isalnum()
    str_Isalpha = e.isalpha()
    str_Isdigit = e.isdigit()
    str_Islower = e.islower()
    str_Isupper = e.isupper()
    str_Istitle = e.istitle()

    print(a)
    print(type(a))
    print(b)
    print(type(b))
    print(c)
    print(type(c))
    print(d)
    print(type(d))
    print(e)
    print(type(e))
    print(f)
    print(type(f))
    print(g)
    print(type(g))
    print(h)
    print(type(h))
    print("Addition of a and b is:", Addition)
    print(type(Addition))
    print("Substraction of a and b is:", Substraction)
    print(type(Substraction))
    print("Multiplication of a and b is:", Multiplication)
    print(type(Multiplication))
    print("Division of a and b is:", Division)
    print(type(Division))
    print("Floor Division of a and b is:", floor_division)
    print(type(floor_division))
    print("Power of a and b is:", power)
    print(type(power))
    print("Addition of c and i is:", complex_number_Addition)
    print(type(complex_number_Addition))
    print("Substraction of c and i is:", complex_number_Substraction)
    print(type(complex_number_Substraction))
    print("Multiplication of c and i is:", complex_number_Multiplication)
    print(type(complex_number_Multiplication))
    print("Division of c and i is:", complex_number_Division)
    print(type(complex_number_Division))
    print("And of d and j is:", bool_And)
    print(type(bool_And))
    print("Or of d and j is:", bool_Or)
    print(type(bool_Or))
    print("Not of d is:", bool_Not)
    print(type(bool_Not))
    print("Xor of d and j is:", bool_Xor)
    print(type(bool_Xor))
    print("Nand of d and j is:", bool_Nand)
    print(type(bool_Nand))
    print("Nor of d and j is:", bool_Nor)
    print(type(bool_Nor))
    print("Xnor of d and j is:", bool_Xnor)
    print(type(bool_Xnor))


if __name__ == "__main__":
    main()