import tkinter as tk
import secrets
class HelloWorld:
    # Constructing the window
    def __init__(self):
        self.text = "Hello world!"
        self.window = tk.Tk(screenName="Hello world")
        self.window.config(bg='Black')
        self.window.attributes('-topmost',True)
        self.width = 500
        self.height = 150
        self.screenw = self.window.winfo_screenwidth()
        self.screenh = self.window.winfo_screenheight()
        self.x = int((self.screenw/2)-(self.width/2))
        self.y = int((self.screenh/2)-(self.height/2))
        self.window.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
        self.display_text = tk.Label(self.window,font=('Helvetica',40),fg='White',bg='Black')
        self.display_text.pack(expand=True)
    #The windows mainloop and functions that write the text and change it's colors randomly
    def run(self):
        self.write_text()
        self.change_colors()
        self.window.mainloop()
    #Randomizes the colors
    def colors(self):
        return f'#{secrets.randbelow(256):02x}{secrets.randbelow(256):02x}{secrets.randbelow(256):02x}'
    #Writes the 'Hello world' text letter by letter (cool animation in my opinion)
    def write_text(self,index=0):
        if index < len(self.text):
            self.display_text.config(text=self.display_text.cget('text')+self.text[index])
            self.display_text.after(100,self.write_text,index+1)
    #Repeatedly changes the color of the text to a random rgb value
    def change_colors(self):
        self.display_text.config(fg=self.colors())
        self.display_text.after(100,self.change_colors)
helloworld = HelloWorld()
#The run function is called here
helloworld.run()