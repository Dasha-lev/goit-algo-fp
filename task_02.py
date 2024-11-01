import turtle

screen = turtle.Screen()
screen.title("Фрактал 'дерево Піфагора'")
pen = turtle.Turtle()
pen.speed(0)  
pen.left(90)  


def draw_tree(branch_length, level):
    if level == 0: 
        return


    pen.forward(branch_length)
    
    pen.left(45)
    draw_tree(branch_length * 0.7, level - 1)

    pen.right(90)
    draw_tree(branch_length * 0.7, level - 1)

    pen.left(45)
    pen.backward(branch_length)

level = int(input("Введіть рівень рекурсії для дерева (наприклад, 3 або 5): "))
draw_tree(100, level)  

turtle.done()
