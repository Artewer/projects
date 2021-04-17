Matrix = [[0 for x in range(2)] for y in range(2)]
Matrix[0][0] = float(input("Give number for 0.1: "))
Matrix[0][1] = float(input("Give number for 0.1: "))
Matrix[1][0] = float(input("Give number for 1.0: "))
Matrix[1][1] = float(input("Give number for 1.1: "))
def potenz_berechen(i):
    global Matrix
    for x in range(i-1):
        Matrix_new = [[0 for x in range(2)] for y in range(2)]
        Matrix_new[0][0] = Matrix[0][0] * Matrix[0][0] + Matrix[0][1]* Matrix[1][0]
        Matrix_new[0][1] = Matrix[0][0] * Matrix[0][1] + Matrix[0][1]* Matrix[1][1]
        Matrix_new[1][0] = Matrix[1][0] * Matrix[0][0] + Matrix[1][1] * Matrix[1][0]
        Matrix_new[1][1] = Matrix[1][0] * Matrix[0][1] + Matrix[1][1] * Matrix[1][1]
        Matrix = Matrix_new
    return Matrix

print(potenz_berechen(int(input("To which power?"))))