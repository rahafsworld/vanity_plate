# Generate numbers list programmatically
numbers = [str(i) for i in range(10)]
letters = [chr(i) for i in range(65, 91)]  # Capital letters A-Z

plate = input("Please input vanity plate: ")

is_valid = True

if len(plate) < 2 or len(plate) > 6:
    is_valid = False

user_letters = 0

def letter_in_plate(plate):
    global user_letters
    for char in plate:
        if char in letters:
            user_letters += 1
    return user_letters

letter_in_plate(plate)
if user_letters < 2:
    is_valid = False

for char in plate:
    if char not in numbers and char not in letters:
        is_valid = False

has_num = False

for index, char in enumerate(plate):
    if char in numbers:
        if index > 0:
            has_num = True
        elif index == 0 and char == '0':
            is_valid = False
    elif has_num:
        is_valid = False

if is_valid:
    print("Valid.")
else:
    print("Invalid.")
