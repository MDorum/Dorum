from graph import *

windowSize(500, 500)
penColor("black")
brushColor("yellow")
circle(250, 250, 100)  # face
brushColor("black")
rectangle(200, 295, 300, 275)  # mouse
brushColor("red")
circle(210, 225, 20)  # left eay
brushColor("black")
circle(210, 225, 7.5)  # zra4ok left eay's
brushColor("red")
circle(300, 225, 15)  # right eay
brushColor("black")
circle(300, 225, 7.5)  # zra4ok right eay's

run()  # делает так, чтобы програма сразу не закрывалась.
# То есть, исходный код уходит в бесконечный цикл выполнения пока не будет нажат крестик.
