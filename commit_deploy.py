
import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import shutil

class GitDeployApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Git Commit Deploy Tool")

        self.source_paths = {
            "Gestão": "C:\\wamp64\\www\\alfa",
            "Consulta Servidor": "C:\\wamp64\\www\\alfa-con",
            "Gestão (Agricultura)": "C:\\wamp64\\www\\beta",
            "Consulta Servidor (Agricultura)": "C:\\wamp64\\www\\beta-con",
        }

        self.git_bash_path = "C:\\Program Files\\Git\\bin\\bash.exe"
        self.deploy_base_path = "C:\\wamp64\\www\\deploy"

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Escolha o sistema:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.system_choice = tk.StringVar(self.root)
        self.system_choice.set("Gestão")

        self.system_menu = tk.OptionMenu(self.root, self.system_choice, *self.source_paths.keys())
        self.system_menu.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        tk.Label(self.root, text="Hashes do Commit (separados por espaço):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.commit_hashes_entry = tk.Entry(self.root, width=50)
        self.commit_hashes_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        tk.Label(self.root, text="Nome da pasta de deploy:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.deploy_folder_entry = tk.Entry(self.root, width=50)
        self.deploy_folder_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.deploy_button = tk.Button(self.root, text="Executar Deploy", command=self.execute_deploy)
        self.deploy_button.grid(row=3, column=0, columnspan=2, pady=10)

    def execute_deploy(self):
        system = self.system_choice.get()
        commit_hashes_str = self.commit_hashes_entry.get()
        deploy_folder = self.deploy_folder_entry.get()

        if not commit_hashes_str or not deploy_folder:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        source_path = self.source_paths[system]
        destiny_path = os.path.join(self.deploy_base_path, deploy_folder)

        if os.path.exists(destiny_path):
            response = messagebox.askyesno("Pasta Existente", f"A pasta '{deploy_folder}' já existe. Deseja limpá-la?")
            if response:
                try:
                    shutil.rmtree(destiny_path)
                    os.makedirs(destiny_path)
                    messagebox.showinfo("Sucesso", f"Pasta '{deploy_folder}' limpa com sucesso.")
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao limpar a pasta: {e}")
                    return
            else:
                messagebox.showinfo("Informação", f"Mantendo os arquivos da pasta '{deploy_folder}'.")
        else:
            try:
                os.makedirs(destiny_path)
                messagebox.showinfo("Sucesso", f"Pasta '{deploy_folder}' criada com sucesso.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao criar a pasta: {e}")
                return

        commit_hashes = [h.strip() for h in commit_hashes_str.split(' ') if h.strip()]

        for commit_hash in commit_hashes:
            try:
                command = [
                    self.git_bash_path,
                    "-c",
                    f"cd '{source_path}' && git diff-tree --name-only -r {commit_hash} | xargs -I {{}} cp -r --parents {{}} '{destiny_path}'"
                ]
                result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
                messagebox.showinfo("Sucesso", f"Arquivos do commit {commit_hash} copiados com sucesso.\n{result.stdout}")
            except subprocess.CalledProcessError as e:
                continue
            except FileNotFoundError:
                messagebox.showerror("Erro", f"Git Bash não encontrado em '{self.git_bash_path}'. Verifique o caminho.")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro inesperado ao processar o commit {commit_hash}: {e}")
        
        messagebox.showinfo("Concluído", "Operação de deploy concluída!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GitDeployApp(root)
    root.mainloop()


