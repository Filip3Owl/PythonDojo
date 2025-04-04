import json
from datetime import datetime
from typing import List, Dict, Optional

# 📝 CLASSE TAREFA - Representa cada item da sua lista de afazeres
class Tarefa:
    def __init__(self, titulo: str, descricao: str, data_limite: str, status: str = "pendente"):
        self.titulo = titulo          # ✏️ Título da tarefa
        self.descricao = descricao    # 📄 Descrição detalhada
        self.data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # ⏰ Data/hora atual
        self.data_limite = data_limite # 🗓️ Data limite para conclusão
        self.status = status          # 🏷️ Status inicial (pendente)
    
    # 🔄 Método para atualizar o status da tarefa
    def atualizar_status(self, novo_status: str):
        status_validos = ["pendente", "em_andamento", "concluida"]  # 🚦 Status possíveis
        if novo_status.lower() in status_validos:
            self.status = novo_status.lower()
            return True  # ✅ Atualização bem-sucedida
        return False  # ❌ Status inválido
    
    # 📤 Converte tarefa para dicionário (para salvar em JSON)
    def to_dict(self) -> Dict:
        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "data_criacao": self.data_criacao,
            "data_limite": self.data_limite,
            "status": self.status
        }
    
    # 📥 Cria tarefa a partir de dicionário (para carregar do JSON)
    @classmethod
    def from_dict(cls, data: Dict):
        tarefa = cls(
            titulo=data["titulo"],
            descricao=data["descricao"],
            data_limite=data["data_limite"],
            status=data["status"]
        )
        tarefa.data_criacao = data["data_criacao"]  # ⏳ Mantém a data original de criação
        return tarefa
    
    # 🖨️ Formatação bonita para impressão
    def __str__(self):
        return (f"📌 Tarefa: {self.titulo}\n"
                f"📝 Descrição: {self.descricao}\n"
                f"⏱️ Criada em: {self.data_criacao}\n"
                f"⏳ Data limite: {self.data_limite}\n"
                f"🏷️ Status: {self.status}\n")


# 🗃️ CLASSE GERENCIADOR - Gerencia todas as tarefas
class GerenciadorTarefas:
    def __init__(self, arquivo_tarefas: str = "tarefas.json"):
        self.arquivo_tarefas = arquivo_tarefas  # 💾 Arquivo para salvar os dados
        self.tarefas: List[Tarefa] = []         # 📋 Lista de tarefas
        self.carregar_tarefas()                 # 🔄 Carrega tarefas do arquivo
    
    # ➕ Adiciona nova tarefa
    def adicionar_tarefa(self, titulo: str, descricao: str, data_limite: str) -> bool:
        # 🔍 Verifica se tarefa já existe
        if any(tarefa.titulo.lower() == titulo.lower() for tarefa in self.tarefas):
            return False  # ❌ Tarefa duplicada
        
        nova_tarefa = Tarefa(titulo, descricao, data_limite)
        self.tarefas.append(nova_tarefa)  # 📥 Adiciona à lista
        self.salvar_tarefas()              # 💾 Salva no arquivo
        return True  # ✅ Sucesso
    
    # ➖ Remove tarefa existente
    def remover_tarefa(self, titulo: str) -> bool:
        for i, tarefa in enumerate(self.tarefas):
            if tarefa.titulo.lower() == titulo.lower():
                del self.tarefas[i]        # 🗑️ Remove da lista
                self.salvar_tarefas()      # 💾 Salva alterações
                return True  # ✅ Sucesso
        return False  # ❌ Tarefa não encontrada
    
    # 📜 Lista todas as tarefas (ou filtra por status)
    def listar_tarefas(self, filtro_status: Optional[str] = None) -> List[Tarefa]:
        if filtro_status:
            return [tarefa for tarefa in self.tarefas if tarefa.status == filtro_status]  # 🔍 Filtra
        return self.tarefas  # 📋 Retorna todas
    
    # 🔄 Atualiza status de uma tarefa
    def atualizar_status_tarefa(self, titulo: str, novo_status: str) -> bool:
        for tarefa in self.tarefas:
            if tarefa.titulo.lower() == titulo.lower():
                return tarefa.atualizar_status(novo_status)  # 🏷️ Atualiza status
        return False  # ❌ Tarefa não encontrada
    
    # 💾 Salva tarefas no arquivo JSON
    def salvar_tarefas(self):
        with open(self.arquivo_tarefas, 'w') as f:
            json.dump([tarefa.to_dict() for tarefa in self.tarefas], f, indent=4)  # ✨ Formata bonito
    
    # 🔄 Carrega tarefas do arquivo JSON
    def carregar_tarefas(self):
        try:
            with open(self.arquivo_tarefas, 'r') as f:
                dados = json.load(f)
                self.tarefas = [Tarefa.from_dict(tarefa) for tarefa in dados]  # 📥 Converte de JSON
        except FileNotFoundError:
            self.tarefas = []  # 📁 Arquivo não existe ainda (primeira execução)
    
    # 🔍 Busca uma tarefa específica
    def buscar_tarefa(self, titulo: str) -> Optional[Tarefa]:
        for tarefa in self.tarefas:
            if tarefa.titulo.lower() == titulo.lower():
                return tarefa  # 🎯 Tarefa encontrada
        return None  # ❌ Não encontrada


# 🎮 INTERFACE PRINCIPAL (menu interativo)
if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()  # 🏁 Inicia o gerenciador
    
    while True:
        print("\n--- 🗂️ Gerenciador de Tarefas ---")
        print("1. ➕ Adicionar Tarefa")
        print("2. 📜 Listar Tarefas")
        print("3. 🔄 Atualizar Status")
        print("4. ➖ Remover Tarefa")
        print("5. 🚪 Sair")
        
        opcao = input("🔘 Escolha uma opção: ")
        
        if opcao == "1":  # ➕ Adicionar
            titulo = input("✏️ Título: ")
            descricao = input("📄 Descrição: ")
            data_limite = input("🗓️ Data limite (YYYY-MM-DD): ")
            if gerenciador.adicionar_tarefa(titulo, descricao, data_limite):
                print("✅ Tarefa adicionada com sucesso!")
            else:
                print("❌ Erro: Já existe uma tarefa com esse título.")
        
        elif opcao == "2":  # 📜 Listar
            print("\n--- 📋 Todas as Tarefas ---")
            for tarefa in gerenciador.listar_tarefas():
                print(f"📌 Título: {tarefa.titulo}")
                print(f"🏷️ Status: {tarefa.status}")
                print(f"⏳ Data Limite: {tarefa.data_limite}")
                print("-" * 30)
        
        elif opcao == "3":  # 🔄 Atualizar status
            titulo = input("✏️ Título da tarefa a atualizar: ")
            novo_status = input("🏷️ Novo status (pendente/em_andamento/concluida): ")
            if gerenciador.atualizar_status_tarefa(titulo, novo_status):
                print("✅ Status atualizado com sucesso!")
            else:
                print("❌ Erro: Tarefa não encontrada ou status inválido.")
        
        elif opcao == "4":  # ➖ Remover
            titulo = input("✏️ Título da tarefa a remover: ")
            if gerenciador.remover_tarefa(titulo):
                print("✅ Tarefa removida com sucesso!")
            else:
                print("❌ Erro: Tarefa não encontrada.")
        
        elif opcao == "5":  # 🚪 Sair
            print("👋 Saindo do sistema...")
            break
        
        else:
            print("⚠️ Opção inválida. Tente novamente.")