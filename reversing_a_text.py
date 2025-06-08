import tkinter as tk
# THERE IS NO BUTTON BECAUSE I MADE IT SO THAT YOU PRESS ENTER/RETURN TO RUN THE FUNCTION
class TextReversingApp:
    # Constructing the window and it's components
    def __init__(self):
        self.window = tk.Tk(screenName='Reverse Text')
        self.window.config(bg='Black')
        self.window.attributes('-topmost',True)
        self.window.title('Reverse Text')
        self.Title = tk.Label(self.window,font=('Helvetica',30),fg='White',bg='Black',text='\nReverse Text\n')
        self.Title.pack()
        self.var = tk.StringVar()
        self.Original_text = tk.Entry(self.window,font=('Helvetica',30),justify='center',textvariable=self.var)
        self.Original_text.pack()
        self.Original_text.focus()
        self.reversed_text = tk.Label(self.window,font=('Helvetica',30),fg='White',bg='Black')
        self.reversed_text.pack()
        self.width = 500
        self.height = 300
        self.screenw = self.window.winfo_screenwidth()
        self.screenh = self.window.winfo_screenheight()
        self.x = int((self.screenw/2)-(self.width/2))
        self.y = int((self.screenh/2)-(self.height/2))
        self.window.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
    # Running the mainloop
    def run(self):
        self.window.bind('<Return>',self.runEvent)
        self.window.mainloop()
    # This will run the function that displays the reversed text on the window and clear the text before displaying a second text
    def runEvent(self,event):
        self.reversed_text.config(text="")
        self.display_text()
    # This function will display the text to the window
    def display_text(self,index=0):
        self.txt = str(self.var.get())[::-1]
        if index < len(self.txt):
            self.reversed_text.config(text=self.reversed_text.cget('text')+self.txt[index])
            self.window.after(100,self.display_text,index+1)
app = TextReversingApp()
app.run()