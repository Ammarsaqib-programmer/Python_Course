from tkinter import *
import wikipedia

def on_press():
    query = get_q.get()
    try:
        summary = wikipedia.summary(query)
        text.delete(1.0, END)
        text.insert(END, summary)
    except wikipedia.exceptions.DisambiguationError as e:
        text.delete(1.0, END)
        text.insert(END, f"Disambiguation error: {e.options}")
    except wikipedia.exceptions.PageError:
        text.delete(1.0, END)
        text.insert(END, "Page not found.")

root = Tk()
root.title("Wiki Search App")
root.configure(bg='#ADD8E6')  
frame = Frame(root, padx=10, pady=10, bg='#ADD8E6')  
frame.pack(pady=10)

question = Label(frame, text="Question", bg='#e3cc8d', fg='#00008B', font=('Helvetica', 12, 'bold'))  
question.grid(row=0, column=0, sticky=W, pady=5)

get_q = Entry(frame, width=40, bd=5, bg='#FFFFFF', fg='#00008B', font=('Helvetica', 12))  
get_q.grid(row=0, column=1, pady=5)

submit = Button(frame, text="Search", command=on_press, bg='#86c4c2', fg='#FFFFFF', font=('Helvetica', 12, 'bold'))  
submit.grid(row=0, column=2, padx=10, pady=5)

text = Text(root, wrap=WORD, padx=10, pady=10, width=60, height=20, bg='#FFFFFF', fg='#00008B', font=('Helvetica', 12))  
text.pack(padx=10, pady=10)

root.mainloop()
