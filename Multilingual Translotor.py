from tkinter import *
import pyttsx3
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from tkinter import ttk

root = Tk()
root.title('MULTI LANGUAGE CONVERTER')
root.geometry("650x410")

def text():
    def tex():
        text_speech = pyttsx3.init()
        answer = text_box1.get()
        text_speech.say(answer)
        text_speech.runAndWait()
    r1 = Tk()
    r1.title('SECOND ACTIVITY')
    r1.geometry("600x340")

    label3 = Label(r1, text='Enter  the  text :       ', fg='blue', font=('Arial', 18, 'bold'))
    label3.grid(row=0, column=0)

    s1 = StringVar()

    text_box1 = Entry(r1, textvariable=s1, fg='black', font=('Arial',12), width=35)
    text_box1.grid(row=0, column=1)

    label4_button = Button(r1, command=tex, text='Convert into Speech', padx=50, pady=10, bg='light green')
    label4_button.grid(row=1, column=1)

    r1.mainloop()

def speak():
    r2 = Tk()
    r2.title('THIRD ACTIVITY')
    r2.geometry("600x340")

    def sp():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                print("Recognizing...")
                te = r.recognize_google(audio, language='en-in')

                print(format(te))

            except:
                print("Say that again please...")

    label5 = Label(r2, text='SPEECH  TO  TEXT :       ', fg='blue', font=('Arial', 18, 'bold'))
    label5.grid(row=0, column=0)
    sp_var = StringVar()

    label4_button = Button(r2, command=sp, text='Convert Text', padx=50, pady=10, bg='light green')
    label4_button.grid(row=1, column=1)

    root.mainloop()

def lng():
    root = Tk()
    root.geometry('1080x400')
    listener = sr.Recognizer()  # This statement is used for recognize your voice
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  # This statement is used to get a voice of alexa
    engine.setProperty('voice', voices[1].id)

    def talk(text):  # This function is used to repeat your text
        engine.say(text)
        engine.runAndWait()

    talk('Hello....')
    root.resizable(0, 0)
    root.config(bg='ghost white')
    root.title("Language Translator")

    def sp():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            talk('What do you want to say...')
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            tet = r.recognize_google(audio, language='en-in')
            print(tet)

            Input_text.insert(INSERT, tet)
        except:
            print("Say that again please...")

    Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='white smoke').pack()

    Label(root, text="S&G team Project", font='arial 15 bold', bg='white smoke', width='20').pack(side='bottom')
    Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=200, y=60)

    Input_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60, )
    Input_text.place(x=30, y=100)

    Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=60)

    Output_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
    Output_text.place(x=600, y=100)
    language = list(LANGUAGES.values())

    src_lang = ttk.Combobox(root, values=language, width=22)
    src_lang.place(x=20, y=60)
    src_lang.set('choose input language')

    sp_button = Button(root, text='Speak', command=sp, font='arial 12 bold', pady=5, bg='royal blue1',
                       activebackground='sky blue')
    sp_button.place(x=505, y=230)

    dest_lang = ttk.Combobox(root, values=language, width=22)
    dest_lang.place(x=890, y=60)
    dest_lang.set('choose output language')

    def Translate():
        translator = Translator()
        translated = translator.translate(text=Input_text.get(1.0, END), src=src_lang.get(), dest=dest_lang.get())

        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)
        talk()

    trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='royal blue1',
                       activebackground='sky blue')

    trans_btn.place(x=490, y=180)
    talk('this is s and g and his team project')

    root.mainloop()



label1 = Label(root, text='TEXT     TO    SPEECH', fg='blue', font=('Arial', 24, 'bold'))
label1.pack()

label1_button = Button(root, command=text,  text='Click', padx=50, pady=10, bg='light green')
label1_button.pack()

label2 = Label(root, text='SPEECH    TO    TEXT', fg='blue', font=('Arial', 24, 'bold'))
label2.pack()

label2_button = Button(root, command=speak, text='Click', padx=50, pady=10, bg='light green')
label2_button.pack()

label3 = Label(root, text='LANGUAGE   TRANSLATOR', fg='blue', font=('Arial', 24, 'bold'))
label3.pack()

label3_button = Button(root,command=lng, text='Click', padx=50, pady=10, bg='light green')
label3_button.pack()
root.mainloop()
