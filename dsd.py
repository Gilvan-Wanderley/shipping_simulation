import tkinter as tk

def on_scale_change(value):
    label.config(text=f"Velocidade: {value}")

# Cria uma janela Tkinter
root = tk.Tk()
root.title("Barra de Velocidade")

# Cria uma label para o texto
text_label = tk.Label(root, text="Selecione a velocidade:")
text_label.pack()

# Cria um controle deslizante (Scale) sem mostrar o valor atual
scale = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200, showvalue=False, command=on_scale_change)
scale.pack(pady=10)

# Cria uma label para mostrar o valor da velocidade selecionada
label = tk.Label(root, text="Velocidade: 0")
label.pack()

# Inicia o loop de eventos do Tkinter
root.mainloop()
