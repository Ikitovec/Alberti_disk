from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter import messagebox


def clicked():
    txt_original = txt.get("1.0", 'end-1c').lower()
    key1=txt2.get("1.0", 'end-1c').lower()
    key2=txt3.get("1.0", 'end-1c').lower()
    txt4.delete(1.0, END)

    eng_low_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rus_low_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet=''
    temp_flag=0
    for i in txt_original:
        if eng_low_alphabet.find(i,0)!=-1:
            alphabet=eng_low_alphabet
            break
        elif rus_low_alphabet.find(i,0)!=-1:
            alphabet=rus_low_alphabet
            break
    if alphabet=='':
        temp_flag=1
        messagebox.showinfo('Ошибка!', f'Не удалось определить алфавит!')

    for i in key1:
        if alphabet.find(i,0)==-1:
            temp_flag=1
            messagebox.showinfo('Ошибка!', f'Не совпадают алфавиты у шифруемого сообщения и ключа 1!')
            break

    for i in key2:
        if alphabet.find(i,0)==-1:
            messagebox.showinfo('Ошибка!', f'Не совпадают алфавиты у шифруемого сообщения и ключа 2!')
            temp_flag=1
            break

    if temp_flag==0:
        new=''
        for i in range(len(key1)):
            if new.find(key1[i],0)==-1:
                new=new+key1[i]


        for i in range(len(alphabet)):
            if new.find(alphabet[i],0)==-1:
                new=new+alphabet[i]

        temp=0
        print(new)
        if ((combo2.get() == 'Зашифровать') | (combo2.get() == 'Расшифровать')):
            for i in txt_original:
                if alphabet.find(i,0)!=-1:


                    if combo2.get() == "Зашифровать":
                        index = alphabet.find(f'{i}', 0)
                        step = alphabet.find(f'{key2[temp % len(key2)]}', 0)
                        txt4.insert(INSERT,new[(index-step) % len(new)])

                    elif combo2.get() == "Расшифровать":
                        index = new.find(f'{i}', 0)
                        step = alphabet.find(f'{key2[temp % len(key2)]}', 0)
                        txt4.insert(INSERT, alphabet[(index + step) % len(new)])

                    temp += 1
                else:
                    txt4.insert(INSERT, i)
        else:
            messagebox.showinfo('Ошибка!', f'Вы неверно ввели действие! (Зашифровать или Расшифровать)')

def swap():
    temporary=txt4.get("1.0", 'end-1c')
    txt.delete(1.0, END)
    txt.insert(INSERT, temporary)
    txt4.delete(1.0, END)


window = Tk()
window.title("Диск Альберти")
window.geometry('500x600')

lbl = Label(window, text="Ваше сообщение:")
lbl.grid(column=0, row=0)


lbl = Label(window, text="Действие:")
lbl.grid(column=0, row=5)


combo2 = Combobox(window)
combo2['values'] = ("Зашифровать", "Расшифровать")
combo2.current(0)
combo2.grid(column=2, row=5)



btn = Button(window, text="Получить ответ", command=clicked)
btn.grid(column=0, row=16)
lbl = Label(window)

btn = Button(window, text="Перенести результат в исходное сообщение", command=swap)
btn.grid(column=2, row=16)
lbl = Label(window)




txt = scrolledtext.ScrolledText(window, width=40, height=1)
txt.grid(column=2, row=0)

lbl = Label(window, text="Первый ключ:")
lbl.grid(column=0, row=9)
txt2 = scrolledtext.ScrolledText(window, width=40, height=1)
txt2.grid(column=2, row=9)

lbl = Label(window, text="Второй ключ:")
lbl.grid(column=0, row=10)
txt3 = scrolledtext.ScrolledText(window, width=40, height=1)
txt3.grid(column=2, row=10)


lbl = Label(window, text="Результат:")
lbl.grid(column=0, row=13)
txt4 = scrolledtext.ScrolledText(window, width=40, height=1)
txt4.grid(column=2, row=13)


window.mainloop()

