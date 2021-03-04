i = 0
def get_int():
    global i
    while i < 1 or i > 8:
        try:
            i = int(input("Height:"))
        except ValueError:
            print("This is not a valid number")

get_int()
blocks = '#'
spaces= i
for x in range(i):
    print(spaces*' ', blocks, ' ', blocks)
    blocks = blocks + '#'
    spaces = spaces-1
