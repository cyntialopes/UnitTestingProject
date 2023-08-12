from unittest import TestCase
from src.service.service_user import ServiceUser

class TestServiceUser(TestCase):

    def setUp(self):
        self.service = ServiceUser()

    def test_add_user_success(self):
        us1 = self.service.add_user("Grupo5", "Testadores")
        self.assertEqual(us1, "Usuário adicionado")

    def test_add_user_failure(self):
        self.assertRaises(ValueError, self.service.add_user, 10, "Analista")

    def test_add_user_duplicate(self):
        self.service.add_user("Grupo5", "Testadores")
        self.assertRaises(ValueError, self.service.add_user, "Grupo5", "Testadores")

    def test_remove_user_success(self):
        self.service.add_user("Grupo5", "Testadores")
        user_remove = self.service.remove_user("Grupo5")
        self.assertEqual(user_remove, "Usuário Removido")

    def test_remove_user_failure(self):
        self.service.add_user("Grupo5", "Testadores")
        user_remove = self.service.remove_user("Passaro")
        self.assertEqual(user_remove, "Usuário não está na lista")

    def test_get_user_success(self):
        self.service.add_user("Grupo5", "Testadores")
        user_job = self.service.get_user_by_name("Grupo5")
        self.assertEqual(user_job, "Testadores")

    def test_get_user_failure(self):
        self.service.add_user("Grupo5", "Testadores")
        user_job = self.service.get_user_by_name("João")
        self.assertEqual(user_job, "Usuário não encontrado")

    def test_update_user_success(self):
        self.service.add_user("Grupo5", "Testadores")
        user_up = self.service.update_user("Grupo5", "Desenvolvedores")
        self.assertEqual(user_up, "Job atualizado")

    def test_update_user_failure(self):
        self.service.add_user("Grupo5", "Testadores")
        user_up = self.service.update_user("João", "Developer")
        self.assertEqual(user_up, "Usuário não cadastrado")