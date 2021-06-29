person = {
    "name": "Mickey",
    "surname": "Mouse",
    "gender": "M",
    "dob": "1/12/1961",
}
f_code = ''
name, surname, gender, dob = person["name"].upper(), person["surname"].upper(), person["gender"], person["dob"]
vowels = ['A', 'E', 'I', 'O', 'U']

if len(surname) < 3:
    f_code += surname + ('X' * (3 - len(surname)))
else:
    unvoweled = ''
    ordered_vowels = ''
    for x in surname:
        if x in vowels:
            ordered_vowels += x
        else:
            unvoweled += x
    if len(unvoweled) >= 3:
        f_code += unvoweled[:3]
    else:
        f_code += unvoweled + ordered_vowels[:len(unvoweled) * -1 + 3]

n_consonants = ''
n_vowels = ''
for x in name:
    if x in vowels:
        n_vowels += x
    else:
        n_consonants += x
if len(name) < 3:
    f_code += n_consonants + n_vowels + ('X' * (3 - len(n_consonants) + len(n_vowels)))
elif len(n_consonants) == 3:
    f_code += n_consonants
elif len(n_consonants) > 3:
    f_code += n_consonants[0] + n_consonants[2:4]
else:
    f_code += n_consonants + n_vowels[:len(n_consonants) * -1 + 3]

print(f_code)
