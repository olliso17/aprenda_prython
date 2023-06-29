from abc import ABC, abstractmethod

from api.domain.list.dto.add_todo_list_dto import AddTodoListDto


class SharedRepositoryInterface(ABC):
    @abstractmethod
    def add(self, input):
        pass
    def find(self):
        pass
    def findAll(self):
        pass
    def update(self):
        pass
    def activate(self):
        pass