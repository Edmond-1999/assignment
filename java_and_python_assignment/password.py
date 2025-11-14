# PSEUDOCODE
# 1. Input password
# 2. count = length of password
# 3. If count < 1  (invalid)
#    If < 6  (weak)
#    If between 6 and 10  (medium)
#    If > 10  (strong)
# 4. Print strength




password = input("Enter password: ")
length = len(password)

if length < 1:
    print("Invalid")
elif length < 6:
    print("Weak")
elif length <= 10:
    print("Medium")
else:
    print("Strong")
