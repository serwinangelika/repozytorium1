#czytelny, estetyczny program, cieszę się, ze wykorzystujesz wbudowane zmienne
def setup():
    size(400, 400)
    textSize(128)
    textAlign(CENTER)
    background(0)


def draw():
    text("A", width/2-75, (height/3)*2)
    text("S", width/2+75, (height/3)*2)
    print(mouseX, mouseY)

#brakuje zaznaczenia litery na wybranie jej na klawiaturze

#to miało działać gdy już jest zaznaczony, czyli jako zagnieżdżony warunek w innym warunku
    if keyCode == 37:
        fill(150, 200, 40)
        text("A", width/2-75, (height/3)*2)
        fill(250)
        
    if keyCode == 39:
        fill(150, 200, 40)
        text("S", width/2+75, (height/3)*2)
        fill(250)
     
#sposób z wykorzystaniem collider'ów :)
    if (mouseX >= 80 and mouseX <= 170 and mouseY >= 170 and mouseY <= 270):
        fill(150, 200, 40)
        text("A", width/2-75, (height/3)*2)
        fill(250)

    if (mouseX >= 245 and mouseX <= 305 and mouseY >= 170 and mouseY <= 270):
        fill(150, 200, 40)
        text("S", width/2+75, (height/3)*2)
        fill(250)
    
#brakuje też własnego kształtu, który miałpodkreślać litery
