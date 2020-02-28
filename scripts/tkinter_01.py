
import tkinter

def main ():
    root = tkinter.Tk()
    root.title = ("Silly Program")
  
   
    def about():
        print ("About was selected")
        
    bar = tkinter.Menu (root)
    fileMenu = tkinter.Menu (bar, tearoff = 0)
    fileMenu.add_command (label = "About", command = about)
    bar.add_cascade (label = "Help", menu = fileMenu)
    root.config(menu=bar)

   
   

    
if __name__ == "__main__":
    main()
    tkinter.mainloop()