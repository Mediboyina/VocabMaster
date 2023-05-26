from tkinter import Tk ,messagebox
from tkinter import simpledialog
from typing import Dict
import random
def read_from_file():
    try:
        with open('vocab_data.txt') as file:
            for line in file:
                line=line.rstrip('\n')
                word,meaning = line.split(':')
                dictionary[word.lower()] = meaning
    except FileNotFoundError:
        messagebox.showerror('Error,File not Found')
    except Exception as e:
        messagebox.showerror('Error' ,str(e))
def write_to_file(word,meaning):
    with open('vocab_data.txt', 'a') as file:
        file.write('\n' + word.lower() +':' + meaning)
def conduct_quiz(num=None):
    quiz_que = list(dictionary.keys())
    if not quiz_que:
        messagebox.showinfo('Quiz','No word found')
        return
    if num is not None:
        quiz_que = quiz_que[:num]
    random.shuffle(quiz_que)
    messagebox.showinfo('Quiz','Let\'s start the quiz')
    correct=0
    for que in quiz_que:
        answer=simpledialog.askstring('Quiz',f"what does '{que}' mean? ")
        if answer and answer.lower() == dictionary[que].lower():
            correct+=1
    total_que=len(quiz_que)
    score_percent=(correct/total_que)*100
    messagebox.showinfo('Quiz',f'Quiz completed!\n\nTotal questions: {total_que}\nCorrect answers: {correct}\nScore:{score_percent:.2f}%')
print('Ask the Expert -word meaning')
root=Tk()
root.withdraw()
dictionary: Dict[str,str] = {}
read_from_file()
query_=""
while True:
    query_ = simpledialog.askstring('word' , 'Type the word:')
    query_ = query_ .lower()
    if not query_:
        break
    if query_ in dictionary:
        result= dictionary[query_]
        messagebox.showinfo('Answer', 'This word '  + query_.capitalize() + ' means ' +result.capitalize()+ '!')
    else:
        new_word = simpledialog.askstring('Teach me', 'I dont\'t know ! what does this mean ? ')
        dictionary[query_]=new_word
        write_to_file(query_,new_word)
    choice=messagebox.askyesno('Quiz choice','Do you want to take the quiz?')
    if choice:
        num=simpledialog.askinteger('Quiz choice', 'How many questions do you want to answer ?')
        conduct_quiz(num)
root.mainloop()