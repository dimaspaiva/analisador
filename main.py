from tkinter import *


def main():
    root = Tk()
    root.title('Analisador Léxico - Dimas e Guilherme')

    x = root.winfo_screenwidth()
    y = root.winfo_screenheight()

    main = Frame(root, width=x, height=y, bg='#333333')

    header = Frame(main, width=x, height=y*0.045, bg='#333333')
    codeBlock = Frame(main, width=x, height=y, bg='#515151')
    fileInfos = Frame(main, width=x*0.12, height=y, bg='#999999')
    debug = Frame(main, width=x, height=y*0.21, bg='#a9a9a9')
    footer = Frame(main, width=x, height=y*0.027, bg='#b7b7b7')
    header.pack(side='top')
    footer.pack(side='bottom')
    fileInfos.pack(side='left')
    debug.pack(side='bottom')
    codeBlock.pack(side='left')

    main.pack()
    root.state('zoomed')
    root.mainloop()


main()
