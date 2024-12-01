import pickle
import tkinter as tk
from tkinter import messagebox
import gerenciar_urna
from common import *

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'

urna = None

def menu():
    menu_window = tk.Tk()
    menu_window.title("Sistema Eleitoral")
    
    def close():
        menu_window.quit()
    
    def option1():
        inserir_eleitor(eleitores)
    
    def option2():
        atualizar_eleitor(eleitores)
    
    def option3():
        inserir_candidato(candidatos)
    
    def option4():
        listar_candidatos(candidatos)
    
    def option5():
        global urna
        urna = gerenciar_urna.iniciar_urna(eleitores.values(), candidatos.values())
    
    def option6():
        gerenciar_urna.votar(urna)

    tk.Button(menu_window, text="Novo Eleitor", command=option1, width=30, height=2).pack(pady=10)
    tk.Button(menu_window, text="Atualizar Eleitor", command=option2, width=30, height=2).pack(pady=10)
    tk.Button(menu_window, text="Inserir Candidato", command=option3, width=30, height=2).pack(pady=10)
    tk.Button(menu_window, text="Listar Candidatos", command=option4, width=30, height=2).pack(pady=10)
    tk.Button(menu_window, text="Iniciar Urna", command=option5, width=30, height=2).pack(pady=10)
    tk.Button(menu_window, text="Testar Urna", command=option6, width=30, height=2).pack(pady=10)
    
    menu_window.mainloop()

def inserir_eleitor(eleitores):
    def save_eleitor():
        try:
            titulo = int(titulo_entry.get())
            if titulo in eleitores:
                raise Exception("Título já existente!")
            
            nome = nome_entry.get()
            RG = RG_entry.get()
            CPF = CPF_entry.get()
            secao = int(secao_entry.get())
            zona = int(zona_entry.get())

            eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona)
            eleitores[eleitor.get_titulo()] = eleitor

            with open(FILE_ELEITORES, 'wb') as arquivo:
                pickle.dump(eleitores, arquivo)

            messagebox.showinfo("Sucesso", "Eleitor gravado com sucesso!")
            inserir_window.quit()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    inserir_window = tk.Tk()
    inserir_window.title("Novo Eleitor")

    tk.Label(inserir_window, text="Digite o Título:").pack()
    titulo_entry = tk.Entry(inserir_window)
    titulo_entry.pack()

    tk.Label(inserir_window, text="Digite o Nome:").pack()
    nome_entry = tk.Entry(inserir_window)
    nome_entry.pack()

    tk.Label(inserir_window, text="Digite o RG:").pack()
    RG_entry = tk.Entry(inserir_window)
    RG_entry.pack()

    tk.Label(inserir_window, text="Digite o CPF:").pack()
    CPF_entry = tk.Entry(inserir_window)
    CPF_entry.pack()

    tk.Label(inserir_window, text="Digite a Seção:").pack()
    secao_entry = tk.Entry(inserir_window)
    secao_entry.pack()

    tk.Label(inserir_window, text="Digite a Zona:").pack()
    zona_entry = tk.Entry(inserir_window)
    zona_entry.pack()

    tk.Button(inserir_window, text="Salvar", command=save_eleitor).pack(pady=5)
    inserir_window.mainloop()

def atualizar_eleitor(eleitores):
    def save_atualizar():
        try:
            titulo = int(titulo_entry.get())
            if titulo in eleitores:
                eleitor = eleitores[titulo]
                secao = int(secao_entry.get())
                zona = int(zona_entry.get())
                eleitor.secao = secao
                eleitor.zona = zona

                with open(FILE_ELEITORES, 'wb') as arquivo:
                    pickle.dump(eleitores, arquivo)

                messagebox.showinfo("Sucesso", "Dados do eleitor atualizados!")
                atualizar_window.quit()
            else:
                raise Exception("Título inexistente!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    atualizar_window = tk.Tk()
    atualizar_window.title("Atualizar Eleitor")

    tk.Label(atualizar_window, text="Digite o Título do Eleitor:").pack()
    titulo_entry = tk.Entry(atualizar_window)
    titulo_entry.pack()

    tk.Label(atualizar_window, text="Digite a nova Seção:").pack()
    secao_entry = tk.Entry(atualizar_window)
    secao_entry.pack()

    tk.Label(atualizar_window, text="Digite a nova Zona:").pack()
    zona_entry = tk.Entry(atualizar_window)
    zona_entry.pack()

    tk.Button(atualizar_window, text="Atualizar", command=save_atualizar).pack(pady=5)
    atualizar_window.mainloop()

def inserir_candidato(candidatos):
    def save_candidato():
        try:
            numero = int(numero_entry.get())
            if numero in candidatos:
                raise Exception("Candidato já existente!")
            
            nome = nome_entry.get()
            RG = RG_entry.get()
            CPF = CPF_entry.get()

            candidato = Candidato(nome, RG, CPF, numero)
            candidatos[candidato.get_numero()] = candidato

            with open(FILE_CANDIDATOS, 'wb') as arquivo:
                pickle.dump(candidatos, arquivo)

            messagebox.showinfo("Sucesso", "Candidato gravado com sucesso!")
            inserir_window.quit()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    inserir_window = tk.Tk()
    inserir_window.title("Novo Candidato")

    tk.Label(inserir_window, text="Digite o Número do Candidato:").pack()
    numero_entry = tk.Entry(inserir_window)
    numero_entry.pack()

    tk.Label(inserir_window, text="Digite o Nome:").pack()
    nome_entry = tk.Entry(inserir_window)
    nome_entry.pack()

    tk.Label(inserir_window, text="Digite o RG:").pack()
    RG_entry = tk.Entry(inserir_window)
    RG_entry.pack()

    tk.Label(inserir_window, text="Digite o CPF:").pack()
    CPF_entry = tk.Entry(inserir_window)
    CPF_entry.pack()

    tk.Button(inserir_window, text="Salvar", command=save_candidato).pack(pady=5)
    inserir_window.mainloop()

def listar_candidatos(candidatos):
    lista_window = tk.Tk()
    lista_window.title("Candidatos")

    for candidato in candidatos.values():
        tk.Label(lista_window, text=str(candidato)).pack()

    tk.Button(lista_window, text="Fechar", command=lista_window.quit).pack(pady=5)
    lista_window.mainloop()

if __name__ == "__main__":
    eleitores = {}
    try:
        print("Carregando arquivo de eleitores ...")
        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum eleitor carregado!")

    candidatos = {}
    try:
        print("Carregando arquivo de candidatos ...")
        with open(FILE_CANDIDATOS, 'rb') as arquivo:
            candidatos = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum candidato carregado!")

    menu()