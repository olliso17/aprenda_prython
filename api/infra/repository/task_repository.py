from api.domain.shared.shared_repository_interface import SharedRepositoryInterface
from api.domain.task.task_entity import Task
from api.infra.db.postgres import Database


class TaskRepository(SharedRepositoryInterface):
    def __init__(self):
        self.db = Database()
    def add(self, input:Task):
        query = "INSERT INTO tasks (id, title, description, status, list_id, created_at, updated_at, deleted_at, is_active, time_select) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)"
        values = (input,)
        self.db.execute_query(query, values)