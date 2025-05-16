import tkinter as tk
import subprocess
import os 

# Caminho absoluto onde os scripts estão localizados
diretorio = "/home/aluno/Downloads/padaria/"

# Função para abrir os scripts corretamente
def abrir_produtos():
    try:
        subprocess.Popen(["python3", os.path.join(diretorio, "padaria.py")])  # Usando o caminho absoluto
    except Exception as e:
        print(f"Erro ao abrir o script padaria.py: {e}")

def abrir_estoque():
    try:
        subprocess.Popen(["python3", os.path.join(diretorio, "controle.py")])  # Usando o caminho absoluto
    except Exception as e:
        print(f"Erro ao abrir o script controle.py: {e}")

def abrir_clientes():
    try:
        subprocess.Popen(["python3", os.path.join(diretorio, "cadastro.py")])  # Usando o caminho absoluto
    except Exception as e:
        print(f"Erro ao abrir o script cadastro.py: {e}")

# Interface do Menu Principal
janela = tk.Tk()
janela.title("Sistema de Padaria - Menu Principal")

tk.Label(janela, text="Bem-vindo ao Sistema de Padaria", font=("Arial", 14)).pack(pady=10)

tk.Button(janela, text="Gerenciar Produtos", width=30, command=abrir_produtos).pack(pady=5)
tk.Button(janela, text="Controle de Estoque", width=30, command=abrir_estoque).pack(pady=5)
tk.Button(janela, text="Cadastro de Clientes", width=30, command=abrir_clientes).pack(pady=5)

# Executa a interface
janela.mainloop()
