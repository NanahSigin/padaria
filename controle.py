import tkinter as tk
from tkinter import messagebox
from con import conectar

def atualizar_lista_produtos():
    """Atualiza a lista de produtos com suas quantidades de estoque"""
    produtos_listbox.delete(0, tk.END)
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""SELECT p.id, p.nome, IFNULL(e.quantidade, 0) 
                          FROM produtos p LEFT JOIN estoque e ON p.id = e.produto_id""")
        for produto in cursor.fetchall():
            produtos_listbox.insert(tk.END, f"{produto[0]} | {produto[1]} | Estoque: {produto[2]}")
        conn.close()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao listar produtos no estoque: {e}")

def atualizar_estoque():
    """Atualiza a quantidade de estoque de um produto"""
    item = produtos_listbox.get(tk.ACTIVE)
    if item:
        produto_id = item.split(" | ")[0]
        nova_qtd = entry_qtd.get()

        if not nova_qtd.isdigit():
            messagebox.showwarning("Erro", "Digite um valor numérico para a quantidade.")
            return

        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estoque WHERE produto_id = %s", (produto_id,))
            if cursor.fetchone():
                cursor.execute("UPDATE estoque SET quantidade = %s WHERE produto_id = %s", (nova_qtd, produto_id))
            else:
                cursor.execute("INSERT INTO estoque (produto_id, quantidade) VALUES (%s, %s)", (produto_id, nova_qtd))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Estoque atualizado com sucesso!")
            atualizar_lista_produtos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar o estoque: {e}")

# Interface de Controle de Estoque
janela = tk.Tk()
janela.title("Controle de Estoque")

# Elementos de interface
tk.Label(janela, text="Nova quantidade").pack()
entry_qtd = tk.Entry(janela)
entry_qtd.pack()

tk.Button(janela, text="Atualizar Estoque", command=atualizar_estoque).pack(pady=5)

# Lista de produtos com estoque
produtos_listbox = tk.Listbox(janela, width=50)
produtos_listbox.pack(pady=10)

# Carrega a lista de produtos ao iniciar
atualizar_lista_produtos()

# Executa a interface
janela.mainloop()
