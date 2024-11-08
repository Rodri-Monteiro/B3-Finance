def main():
    import tkinter as tk
    import stocks

    root = tk.Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()

    janela_w = 600
    janela_h = 600
    x = w - janela_w - 10
    y = 30
    

    root.title('N.Y.I')
    root.geometry(f"{janela_w}x{janela_h}+{x}+{y}")
    root.config(background= "#4C00B9")


    root.mainloop()

    teste = stocks.stock(2020,2021, 'HAPV3')

    teste.add(2018,2018)
    print(teste.working_capital_(2019,2020))
    
    


if __name__ == "__main__":
    main()
    