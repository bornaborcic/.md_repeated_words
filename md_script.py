from tkinter import *
import f_md_repeats

list = ['']

def get_loco():
    """"""
    t = Text(root)
    for x in f_md_repeats.md_repeats(entry.get()):
        t.insert(END, x + '\n')
    t.pack()
    

root = Tk()
root.geometry("480x480")
root.title("Checking for repeated words in an .md file.")


button = Button(
    text='Click here to check the document for repeated words.',
    width='480',
    height=5,
    bg='#C0C0C0',
    fg='#800080',
    command = get_loco,
)

label = Label(
    text="""Input the absolute path of an .md file on your computer into the purple text box. 
    Example: C:/Users/Keith/Desktop/Vault/file.md. Using forward slashes is perfectly fine.
    Your .md file must contain a single generic # Heading with the text body following.""",
    foreground="#FFFFFF",
    background="black",
    width='480',
    height=4,
)

entry = Entry(fg='#FFFFFF', bg='#800080', width='480')

label.pack()
entry.pack()
button.pack()


root.mainloop()
