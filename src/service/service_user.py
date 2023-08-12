from src.models.store import Store
from src.models.user import User

class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if not isinstance(name, str) or not isinstance(job, str):
            raise ValueError("Entradas devem ser strings")

        if any(u.name == name for u in self.store.bd):
            raise ValueError("Usuário duplicado")

        user = User(name, job)
        self.store.bd.append(user)
        return "Usuário adicionado"

    def remove_user(self, name):
        if not isinstance(name, str):
            raise ValueError("Entrada deve ser uma string")

        user_to_remove = next((u for u in self.store.bd if u.name == name), None)
        if user_to_remove:
            self.store.bd.remove(user_to_remove)
            return "Usuário Removido"
        else:
            return "Usuário não está na lista"

    def get_user_by_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Entrada deve ser uma string")

        user = next((u for u in self.store.bd if u.name == name), None)
        if user:
            return user.job
        else:
            return "Usuário não encontrado"

    def update_user(self, name, newjob):
        if not isinstance(name, str) or not isinstance(newjob, str):
            raise ValueError("Entradas devem ser strings")

        user = next((u for u in self.store.bd if u.name == name), None)
        if user:
            user.job = newjob
            return "Job atualizado"
        else:
            return "Usuário não cadastrado"