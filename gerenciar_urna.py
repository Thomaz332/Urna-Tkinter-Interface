import tkinter as tk
from tkinter import messagebox, simpledialog
from common import *
from eleicao import Urna

urna = None

def iniciar_urna(eleitores, candidatos):
    def save_urna():
        global urna  
        try:
            secao = int(secao_entry.get())
            zona = int(zona_entry.get())

            nome_mes = nome_mes_entry.get()
            rg_mes = rg_mes_entry.get()
            cpf_mes = cpf_mes_entry.get()

            mesario = Pessoa(nome_mes, rg_mes, cpf_mes)

            urna = Urna(mesario, secao, zona, candidatos, eleitores)
            messagebox.showinfo("Sucesso", "Urna Iniciada com sucesso!")
            iniciar_window.quit()

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    iniciar_window = tk.Tk()
    iniciar_window.title("Iniciar Urna")

    tk.Label(iniciar_window, text="Número da Seção:").pack()
    secao_entry = tk.Entry(iniciar_window)
    secao_entry.pack()

    tk.Label(iniciar_window, text="Número da Zona:").pack()
    zona_entry = tk.Entry(iniciar_window)
    zona_entry.pack()

    tk.Label(iniciar_window, text="Nome do Mesário:").pack()
    nome_mes_entry = tk.Entry(iniciar_window)
    nome_mes_entry.pack()

    tk.Label(iniciar_window, text="RG do Mesário:").pack()
    rg_mes_entry = tk.Entry(iniciar_window)
    rg_mes_entry.pack()

    tk.Label(iniciar_window, text="CPF do Mesário:").pack()
    cpf_mes_entry = tk.Entry(iniciar_window)
    cpf_mes_entry.pack()

    tk.Button(iniciar_window, text="Iniciar Urna", command=save_urna).pack(pady=5)

    iniciar_window.mainloop()


def votar(event = None):
    if urna is None:
        messagebox.showerror("Erro", "A urna não foi iniciada!")
        return

    def registrar_voto():
        try:
            titulo_eleitor = int(titulo_entry.get())
            eleitor = urna.get_eleitor(titulo_eleitor)

            if not eleitor:
                messagebox.showerror("Erro", "Eleitor não é desta Urna")
            else:
                voto = int(voto_entry.get())
                urna.registrar_voto(eleitor, voto)
                messagebox.showinfo("Sucesso", f"Voto de {eleitor} registrado com sucesso!")
                votar_window.quit()

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    votar_window = tk.Tk()
    votar_window.title("Votação")

    tk.Label(votar_window, text="Digite seu Título de Eleitor:").pack()
    titulo_entry = tk.Entry(votar_window)
    titulo_entry.pack()

    tk.Label(votar_window, text="Digite seu Voto (Número do Candidato):").pack()
    voto_entry = tk.Entry(votar_window)
    voto_entry.pack()

    tk.Button(votar_window, text="Registrar Voto", command=registrar_voto).pack(pady=5)

    votar_window.mainloop()