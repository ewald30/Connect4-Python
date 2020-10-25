from UI import*

window = Tk()
window.title('Connect4')
window.geometry('300x300')
btn = Button(window, text="Click Me")
btn.grid(column=1, row=0)
window.mainloop()

def startup():
    b = Board()
    c = colors
    s = symbols(c)
    p = PrettyPrintedBoard(b, s)
    ai = AI(b)
    name1 = input('                          Enter player 1 name: ')
    name1 = c.blue+name1+c.white
    name2 = input('                          Enter player 2 name: ')
    if name2 == "AI":
        ai.Activate()
    name2 = c.green+name2+c.white
    ui = UI(b,p,name1,name2,c,ai)
    ui.run()

startup()