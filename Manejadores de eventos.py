import tkinter as tk
from tkinter import messagebox

# Funciones de la aplicación
def add_task(event=None):
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, ingrese una tarea.")

def mark_completed(event=None):
    try:
        index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(index)
        if not task.startswith("[Completado] "):
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, "[Completado] " + task)
        else:
            messagebox.showinfo("Tarea ya completada", "Esta tarea ya está marcada como completada.")
    except IndexError:
        messagebox.showwarning("Selección inválida", "Por favor, seleccione una tarea.")

def delete_task(event=None):
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Selección inválida", "Por favor, seleccione una tarea.")

def close_app(event=None):
    root.quit()

# Configuración de la interfaz
root = tk.Tk()
root.title("Gestor de Tareas Pendientes")

# Entrada para agregar nuevas tareas
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)

# Lista de tareas
listbox_tasks = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE)
listbox_tasks.pack(pady=10)

# Botones
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_add_task = tk.Button(frame_buttons, text="Añadir Tarea", width=15, command=add_task)
btn_add_task.grid(row=0, column=0, padx=5)

btn_mark_completed = tk.Button(frame_buttons, text="Marcar Completada", width=15, command=mark_completed)
btn_mark_completed.grid(row=0, column=1, padx=5)

btn_delete_task = tk.Button(frame_buttons, text="Eliminar Tarea", width=15, command=delete_task)
btn_delete_task.grid(row=0, column=2, padx=5)

# Atajos de teclado
root.bind("<Return>", add_task)           # Tecla Enter para añadir tarea
root.bind("<c>", mark_completed)          # Tecla C para marcar como completada
root.bind("<d>", delete_task)             # Tecla D para eliminar tarea
root.bind("<Delete>", delete_task)        # Tecla Delete para eliminar tarea
root.bind("<Escape>", close_app)          # Tecla Escape para cerrar la aplicación

# Iniciar la aplicación
root.mainloop()
