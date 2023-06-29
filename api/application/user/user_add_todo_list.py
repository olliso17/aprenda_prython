from api.domain.shared.shared_base_usecase import SharedBaseUseCase
from api.infra.repository.task_repository import TaskRepository
from api.infra.repository.todo_list_repository import TodoListRepository


class UserAddTodoListUseCase():
    # repo: TodoListRepository
    # criar 
    def __init__(self, todo_list: TodoListRepository, task:TaskRepository):
        self.todo_list = todo_list
        self.task = task

    # def execute(self, other: BaseModel) -> BaseEntity:
    #     with self.repo as repo:
    #         return repo.add(transform(other))