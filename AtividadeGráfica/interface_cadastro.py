import tkinter as tk
from tkinter import messagebox, ttk

class SistemaCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        
        self.cadastros = []
        
        titulo = tk.Label(root, text="Cadastro de Pessoas", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)
        
        frame = tk.Frame(root)
        frame.pack(pady=10, padx=20)
        
        tk.Label(frame, text="Nome:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.nome_entry = tk.Entry(frame, width=30, font=("Arial", 10))
        self.nome_entry.grid(row=0, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Sobrenome:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.sobrenome_entry = tk.Entry(frame, width=30, font=("Arial", 10))
        self.sobrenome_entry.grid(row=1, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Idade:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.idade_entry = tk.Entry(frame, width=30, font=("Arial", 10))
        self.idade_entry.grid(row=2, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Sexo:", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
        self.sexo_var = tk.StringVar()
        sexo_frame = tk.Frame(frame)
        sexo_frame.grid(row=3, column=1, sticky="w", pady=5, padx=5)
        tk.Radiobutton(sexo_frame, text="Masculino", variable=self.sexo_var, value="M").pack(side="left", padx=5)
        tk.Radiobutton(sexo_frame, text="Feminino", variable=self.sexo_var, value="F").pack(side="left", padx=5)
        
        botoes_frame = tk.Frame(root)
        botoes_frame.pack(pady=10)
        
        tk.Button(botoes_frame, text="Cadastrar", command=self.cadastrar, 
                 bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), 
                 width=12, cursor="hand2").pack(side="left", padx=5)
        
        tk.Button(botoes_frame, text="Listar", command=self.listar, 
                 bg="#2196F3", fg="white", font=("Arial", 10, "bold"), 
                 width=12, cursor="hand2").pack(side="left", padx=5)
        
        tk.Button(botoes_frame, text="Limpar", command=self.limpar, 
                 bg="#FF9800", fg="white", font=("Arial", 10, "bold"), 
                 width=12, cursor="hand2").pack(side="left", padx=5)
        
        self.status_label = tk.Label(root, text="", font=("Arial", 9), fg="green")
        self.status_label.pack(pady=5)
    
    def validar_campos(self):
        nome = self.nome_entry.get().strip()
        sobrenome = self.sobrenome_entry.get().strip()
        idade = self.idade_entry.get().strip()
        sexo = self.sexo_var.get()
        
        if not nome:
            messagebox.showwarning("Aviso", "Por favor, preencha o campo Nome!")
            return False
        
        if not sobrenome:
            messagebox.showwarning("Aviso", "Por favor, preencha o campo Sobrenome!")
            return False
        
        if not idade:
            messagebox.showwarning("Aviso", "Por favor, preencha o campo Idade!")
            return False
        
        try:
            idade_int = int(idade)
            if idade_int < 0 or idade_int > 150:
                messagebox.showwarning("Aviso", "Por favor, insira uma idade válida (0-150)!")
                return False
        except ValueError:
            messagebox.showwarning("Aviso", "A idade deve ser um número!")
            return False
        
        if not sexo:
            messagebox.showwarning("Aviso", "Por favor, selecione o Sexo!")
            return False
        
        return True
    
    def cadastrar(self):
        if self.validar_campos():
            cadastro = {
                'nome': self.nome_entry.get().strip(),
                'sobrenome': self.sobrenome_entry.get().strip(),
                'idade': int(self.idade_entry.get().strip()),
                'sexo': 'Masculino' if self.sexo_var.get() == 'M' else 'Feminino'
            }
            
            self.cadastros.append(cadastro)
            self.status_label.config(text=f"✓ Cadastro realizado com sucesso! Total: {len(self.cadastros)}", fg="green")
            messagebox.showinfo("Sucesso", 
                              f"Cadastro realizado com sucesso!\n\n"
                              f"Nome: {cadastro['nome']} {cadastro['sobrenome']}\n"
                              f"Idade: {cadastro['idade']} anos\n"
                              f"Sexo: {cadastro['sexo']}")
            self.limpar()
    
    def listar(self):
        if not self.cadastros:
            messagebox.showinfo("Listagem", "Nenhum cadastro realizado ainda!")
            return
        
        janela_lista = tk.Toplevel(self.root)
        janela_lista.title("Lista de Cadastros")
        janela_lista.geometry("500x400")
        
        tk.Label(janela_lista, text="Cadastros Realizados", 
                font=("Arial", 14, "bold")).pack(pady=10)
        
        frame_lista = tk.Frame(janela_lista)
        frame_lista.pack(fill="both", expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side="right", fill="y")
        
        text_widget = tk.Text(frame_lista, yscrollcommand=scrollbar.set, 
                             font=("Courier", 10), wrap="word")
        text_widget.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text_widget.yview)
        
        for i, cadastro in enumerate(self.cadastros, 1):
            text_widget.insert("end", f"{'='*50}\n")
            text_widget.insert("end", f"Cadastro #{i}\n")
            text_widget.insert("end", f"{'='*50}\n")
            text_widget.insert("end", f"Nome Completo: {cadastro['nome']} {cadastro['sobrenome']}\n")
            text_widget.insert("end", f"Idade: {cadastro['idade']} anos\n")
            text_widget.insert("end", f"Sexo: {cadastro['sexo']}\n\n")
        
        text_widget.config(state="disabled")
        
        tk.Button(janela_lista, text="Fechar", command=janela_lista.destroy,
                 bg="#f44336", fg="white", font=("Arial", 10, "bold"),
                 width=15).pack(pady=10)
    
    def limpar(self):
        self.nome_entry.delete(0, tk.END)
        self.sobrenome_entry.delete(0, tk.END)
        self.idade_entry.delete(0, tk.END)
        self.sexo_var.set("")
        self.nome_entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaCadastro(root)
    root.mainloop()
