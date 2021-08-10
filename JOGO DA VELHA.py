import turtle
t1 = turtle.Turtle()
turtle.bgcolor("black")
t1.pencolor('white')
scr = turtle.Screen()
jogada = 0
def newgame(x, y):
    global mapax
    mapax = x
    global mapay
    mapay = y
    global matrix
    matrix = []
    for i in range (3):
        matrix.append([-1, -1, -1])
    t1.clear()
    t1.setheading(0)
    t1.penup()
    t1.goto([x, y])
    t1.pendown()
    t1.forward(300)
    t1.penup()
    t1.left(90)
    t1.forward(100)
    t1.left(90)
    t1.pendown()
    t1.forward(300)
    t1.penup()
    t1.left(90)
    t1.forward(200)
    t1.left(90)
    t1.forward(100)
    t1.left(90)
    t1.pendown()
    t1.forward(300)
    t1.right(90)
    t1.penup()
    t1.forward(100)
    t1.pendown()
    t1.right(90)
    t1.forward(300)
    scr.onclick(checarposicao)
scr.onclick(newgame)
t1.speed(-1)
def checarvitoria():
    for r in range (3):
        soma = 0
        for c in range (3):
            if -1 in matrix[r]:
                soma = -1
                break
            else:
                soma += matrix [r][c]
        if soma == 3:
            print("genial!")
            scr.onclick(newgame)

        elif soma == 0:
            print("ilustre!")
            scr.onclick(newgame)

    #checar colunas
    for c in range (3):
        rick = 0
        for line in range (3):
            if matrix[0][c] == -1 or matrix[1][c] == -1 or matrix[2][c] == -1:
                rick = -1
                break
            else:
                rick += matrix [line][c]
        if rick == 3:
            print("genial!")
            scr.onclick(newgame)

        elif rick == 0:
            print("ilustre!")
            scr.onclick(newgame)

  
    #checar diagonais
    morty = 0
    for i in range (3):
        if matrix[i][i] == -1:
            morty = -1
            break
        else:
            morty += matrix[i][i]
    if morty == 3:
        print("genial!")
        scr.onclick(newgame)
    elif morty == 0:
        print("ilustre!")
        scr.onclick(newgame)

    if matrix[2][0] != -1 and matrix[1][1] != -1 and matrix[0][2] != -1:
        Goldenfold = matrix[2][0] + matrix[1][1] + matrix[0][2]
        if Goldenfold  == 3.0:
            print("genial!")
            scr.onclick(newgame)
        elif Goldenfold == 0.0:
            print("ilustre!")
            scr.onclick(newgame)

        else:
            print("ah não vei")
            scr.onclick(newgame)
def checarposicao(x, y):
    if x <= mapax + 100 and y <= mapay and matrix[2][0] == -1:
        draw(mapax + 50, mapay - 50)
        matrix[2][0] = jogada % 2

    if x <= mapax + 200 and y <= mapay and x >= mapax + 100 and matrix[2][1] == -1:
        draw(mapax + 150, mapay - 50)
        matrix[2][1] = jogada % 2
    if x <= mapax + 300 and y <= mapay and x >= mapax + 200 and matrix[2][2] == -1:
        draw(mapax + 250, mapay - 50)
        matrix[2][2] = jogada % 2
    if x <= mapax + 100 and y <= mapay + 100 and y >= mapay + 50 and matrix[1][0] == -1:
        draw(mapax + 50, mapay + 50)
        matrix[1][0] = jogada % 2
    if x <= mapax + 200 and y >= mapay and x >= mapax + 100 and y <= mapay + 100 and matrix[1][1] == -1:
        draw(mapax + 150, mapay + 50)
        matrix[1][1] = jogada % 2
    if y >= mapay and x >= mapax + 200 and y <= mapay + 100 and matrix[1][2] == -1:
        draw(mapax + 250, mapay + 50)
        matrix[1][2] = jogada % 2
    if x <= mapax + 100 and y >= mapay + 100 and matrix[0][0] == -1:
        draw(mapax + 50, mapay + 150)
        matrix[0][0] = jogada % 2
    if x>= mapax + 100 and y >= mapay + 100 and x <= mapax + 200 and matrix[0][1] == -1:
        draw(mapax + 150, mapay + 150)
        matrix[0][1] = jogada % 2
    if y >= mapay + 100 and x >= mapax + 200 and matrix[0][2] == -1:
        draw(mapax + 250, mapay + 150)
        matrix[0][2] = jogada % 2
    checarvitoria()
def draw(x, y):
    global jogada
    jogada += 1
    if jogada % 2 == 0:
        t1.penup()
        t1.goto(x, y)
        t1.pendown()
        t1.circle(15) 
    else:
        t1.penup()
        t1.goto(x + 45, y + 45)
        t1.setheading(220)
        t1.pendown()
        t1.forward(135)
        t1.penup()
        t1.goto(x + 45, y - 45)
        t1.setheading(135)
        t1.pendown()
        t1.forward(135)



input()