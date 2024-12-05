#age counter, erroe then 
#only 6-18 allowed
#age = even or odd
try:
    park = int(input("Enter your age:"))
    if park < 18 and park > 6:
        print("Valid")
    else:
        raise ValueError
except ValueError as ex:
    print("Oops age ins't in a given range")