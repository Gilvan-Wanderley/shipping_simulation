import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Criar um canvas para conter o conteúdo rolável
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Criar uma barra de rolagem vertical
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configurar a barra de rolagem para funcionar com o canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Criar um frame dentro do canvas para conter o conteúdo
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Adicionar algum conteúdo ao frame (por exemplo, uma caixa de listagem)
listbox = tk.Listbox(frame)
for i in range(100):
    listbox.insert(tk.END, f"Item {i}")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configurar a função de rolagem do canvas
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", on_configure)

root.mainloop()
