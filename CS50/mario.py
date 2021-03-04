
def get_int():
    i = 0
    while True:
        try:
            i = int(input("Height:"))
            if i < 1 or i > 8:
                continue
            return i
        except ValueError:
            print("This is not a valid number")

i = get_int ()
blocks = '#'
spaces = i
for x in range(i):
    print(spaces*' ', blocks, ' ', blocks)
    blocks = blocks + '#'
    spaces = spaces-1
