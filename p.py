# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Yash Tariyal Welcome')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import turtle

col=('red','yellow','green','cyan','pink','white')

t=turtle.Turtle()

screen=turtle.Screen()

screen.bgcolor('black')

t.speed(30)

for i in range (200):
    t.color(col[i%6])
    t.forward(i*1.5)
    t.left(59)
    t.width(3)
