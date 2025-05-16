import tkinter as tk
from tkinter import messagebox
from con import conectar

def cadastrar_cliente():
    """Cadastra um novo cliente no banco de dados"""
    nome = entry_nome.get().strip()
    telefone = entry_telefone.get().strip()

    if not nome:
        messagebox.showwarning("Atenção", "O campo nome é obrigatório.")
        return

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, telefone) VALUES (%s, %s)", (nome, telefone))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        listar_clientes()  # Atualiza a lista de clientes
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar cliente: {e}")

def listar_clientes():
    """Lista todos os clientes cadastrados"""
    lista.delete(0, tk.END)
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        for cliente in cursor.fetchall():
            lista.insert(tk.END, f"{cliente[0]} | {cliente[1]} | Tel: {cliente[2]}")
        conn.close()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao listar clientes: {e}")

# Interface de Cadastro de Clientes
janela = tk.Tk()
janela.title("Cadastro de Clientes")

# Elementos de interface
tk.Label(janela, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="Telefone").grid(row=1, column=0)
entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=1, column=1)

tk.Button(janela, text="Cadastrar Cliente", command=cadastrar_cliente).grid(row=2, column=0, columnspan=2)

# Lista de clientes
lista = tk.Listbox(janela, width=50)
lista.grid(row=3, column=0, columnspan=2)

# Carrega a lista de clientes ao iniciar
listar_clientes()

# Executa a interface
janela.mainloop()
