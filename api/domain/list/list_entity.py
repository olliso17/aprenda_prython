from typing import List
from api.domain.base.base import Base
from api.domain.task.task_entity import Task


class ListEntity(Base):
    def __init__(self, name: str, typeTask: str, userId: str, tasks: List[Task]):
        super().__init__()
        self.__name = name
        self.__typeTask = typeTask
        self.__userId = userId
        self.__tasks = tasks

    @property
    def name(self):

        return self.get_String(self.__name, "Name")

    @property
    def typeTask(self):

        return self.get_String(self.__typeTask, "Type of Task")

    @property
    def userId(self):

        return self.get_String(self.__userId, "User id")

    @property
    def tasks(self):
        return self.__tasks
           
    def addTasks(self, task:Task):
        
        listTask = set(self.__tasks)
        
        if task in listTask:
            raise ValueError('Task already exists')
       
        self.__tasks.append(task)

    def removeTasks(self, task:Task):
                
        listTask = set(self.__tasks)
            
        if len(self.__tasks) == 0:
            raise ValueError('Tasks not found')
    
        if task not in listTask:
            raise ValueError('Task not found')        
        self.__tasks.remove(task)      