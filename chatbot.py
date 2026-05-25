from tkinter import *
def send():
    user =entry.get().lower()
    chat.insert(END, "You: " + user + "\n")
    if user=="hi"or user=="hello":
        bot="Hello! How can I help you?"
    elif user=="how are you?":
        bot="I'm good, thank you! How about you?"
    elif user=="what is your name?":
        bot="I am a simple chatbot created in python"
    elif user=="How was your day?":
        bot="It was great! I got to chat with you."
    elif user=="bye" or user=="goodbye":
        bot="Goodbye! Have a nice day!"
    elif user=="what can you do?":
        bot="I can chat with you and answer simple questions."
    elif user=="what is the weather like?":
        bot="I'm sorry, I don't have access to real-time weather information."
    elif user=="okay" or user=="ok":
        bot="Great! Let me know if you have any other questions."
    elif user=="thank you" or user=="thanks":
        bot="You're welcome! I'm here to help."
    else:
        bot="Sorry, I don't understand that."
    chat.insert(END, "Bot: " + bot + "\n")
    entry.delete(0, END)
root=Tk()
root.title("chatbot")
root.geometry("500x500")

chat=Text(root)
chat.pack()

entry=Entry(root, width=50)
entry.pack()

button=Button(root, text="Send", command=send)
button.pack()

root.mainloop()
