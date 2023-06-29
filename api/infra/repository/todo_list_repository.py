from api.domain.list.todo_list import TodoList
from api.domain.shared.shared_repository_interface import SharedRepositoryInterface
from api.infra.db.postgres import Database


class TodoListRepository(SharedRepositoryInterface):
    def __init__(self):
        self.db = Database()
    def add(self, input:TodoList):
        query = "INSERT INTO lists (id, name, user_id, type_task, created_at, updated_at, deleted_at, is_active) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)"
        values = (input,)
        self.db.execute_query(query, values)