

def main():
    import tkinter as tk

    root = tk.Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()

    janela_w = 600
    janela_h = 600
    x = w - janela_w - 10
    y = 30
    

    root.title('Timer')
    root.geometry(f"{janela_w}x{janela_h}+{x}+{y}")
    root.config(background= "#FFFFFF")

    

    root.mainloop()
if __name__ == "__main__":
    main()
    