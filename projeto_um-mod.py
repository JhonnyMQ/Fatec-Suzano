import os
import tkinter as tk
from tkinter import messagebox

# --- CONFIGURAÇÃO INICIAL DO ARQUIVO ---
ARQUIVO = "ListaNomes.txt"

if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, "w", encoding='utf-8') as f:
        pass

# Carrega a lista inicial (garantindo tamanho 10 para posições fixas)
with open(ARQUIVO, "r", encoding='utf-8') as f:
    lista_Nomes = f.read().splitlines()

# Garante que a lista comece com 10 posições preenchidas (vazias ou com nomes)
while len(lista_Nomes) < 10:
    lista_Nomes.append("")


# --- FUNÇÕES DE PERSISTÊNCIA ---
def salvar_no_arquivo():
    """Grava o estado atual da lista_Nomes no arquivo txt."""
    with open(ARQUIVO, "w", encoding='utf-8') as f:
        for nome in lista_Nomes:
            f.write(f"{nome}\n")


# --- FUNÇÕES DO CRUD ---
def obter_posicao():
    """Valida e retorna a posição digitada pelo usuário (0 a 9 no código)."""
    try:
        pos = int(entry_posicao.get()) - 1
        if 0 <= pos < 10:
            return pos
        else:
            messagebox.showwarning("Aviso", "Por favor, escolha uma posição entre 1 e 10.")
            return None
    except ValueError:
        messagebox.showerror("Erro", "A posição deve ser um número inteiro de 1 a 10.")
        return None


def inserir():
    pos = obter_posicao()
    if pos is None: return
    
    nome = entry_nome.get().strip()
    if not nome:
        messagebox.showwarning("Aviso", "Digite um nome válido.")
        return

    if lista_Nomes[pos] == "":
        lista_Nomes[pos] = nome
        salvar_no_arquivo()
        messagebox.showinfo("Sucesso", f"Nome '{nome}' inserido na posição {pos+1}.")
        listar()
    else:
        messagebox.showwarning("Aviso", "Espaço já ocupado, tente outra posição ou altere.")


def consultar():
    pos = obter_posicao()
    if pos is None: return
    
    nome = entry_nome.get().strip()
    if lista_Nomes[pos] == nome and nome != "":
        messagebox.showinfo("Resultado", f"Nome '{nome}' encontrado na posição {pos+1}!")
    else:
        messagebox.showinfo("Resultado", "Nome não encontrado nesta posição.")


def alterar():
    pos = obter_posicao()
    if pos is None: return
    
    nome_antigo = entry_nome.get().strip()
    
    if lista_Nomes[pos] == nome_antigo and nome_antigo != "":
        # Nova janela simples para pedir o novo nome
        def confirmar_alteracao():
            novo_nome = entry_novo_nome.get().strip()
            if novo_nome:
                lista_Nomes[pos] = novo_nome
                salvar_no_arquivo()
                messagebox.showinfo("Sucesso", "Nome substituído com sucesso!")
                listar()
                janela_alt.destroy()
            else:
                messagebox.showwarning("Aviso", "Digite um nome válido.")

        janela_alt = tk.Toplevel(janela)
        janela_alt.title("Novo Nome")
        tk.Label(janela_alt, text="Digite o novo nome:").pack(padx=10, pady=5)
        entry_novo_nome = tk.Entry(janela_alt)
        entry_novo_nome.pack(padx=10, pady=5)
        tk.Button(janela_alt, text="Confirmar", command=confirmar_alteracao).pack(pady=5)
    else:
        messagebox.showerror("Erro", "O nome digitado não corresponde ao que está nessa posição.")


def deletar():
    pos = obter_posicao()
    if pos is None: return
    
    nome = entry_nome.get().strip()
    if lista_Nomes[pos] == nome and nome != "":
        lista_Nomes[pos] = ""
        salvar_no_arquivo()
        messagebox.showinfo("Sucesso", f"Nome deletado com sucesso na posição {pos+1}.")
        listar()
    else:
        messagebox.showerror("Erro", "O nome digitado não corresponde ao que está nessa posição.")


def listar():
    # Limpa a listbox antes de atualizar
    listbox_nomes.delete(0, tk.END)
    for i, nome in enumerate(lista_Nomes):
        exibicao = nome if nome != "" else "[Vazio]"
        listbox_nomes.insert(tk.END, f"{i+1} - {exibicao}")


# --- INTERFACE GRÁFICA (TKINTER) ---
janela = tk.Tk()
janela.title("Gerenciador de Lista de Nomes")
janela.geometry("450x450")

# Widgets de Entrada de Dados
frame_inputs = tk.Frame(janela)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Posição (1-10):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_posicao = tk.Entry(frame_inputs, width=10)
entry_posicao.grid(row=0, column=1, padx=5, pady=5, sticky="w")

tk.Label(frame_inputs, text="Nome:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_nome = tk.Entry(frame_inputs, width=30)
entry_nome.grid(row=1, column=1, padx=5, pady=5)

# Widgets de Botões (Ações)
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Inserir", width=10, command=inserir).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_botoes, text="Consultar", width=10, command=consultar).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_botoes, text="Alterar", width=10, command=alterar).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_botoes, text="Deletar", width=10, command=deletar).grid(row=1, column=1, padx=5, pady=5)

# Área de exibição da lista (Listbox)
tk.Label(janela, text="Lista Atual (Máx 10 nomes):", font=("Arial", 10, "bold")).pack(pady=5)
listbox_nomes = tk.Listbox(janela, width=40, height=11)
listbox_nomes.pack(pady=5)

# Inicializa preenchendo a listbox logo na abertura do app
listar()

# Roda o aplicativo
janela.mainloop()