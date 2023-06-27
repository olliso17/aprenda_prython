from api.domain.task.task_entity import Task


class ListEntity():
    def __init__(self, name: str, typeTask: str, userId: str, tasks: list):
        self.__name = name
        self.__typeTask = typeTask
        self.__userId = userId
        self.__tasks = tasks

    @property
    def name(self):

        return self.__name.title()

    @property
    def typeTask(self):

        return self.__typeTask

    @property
    def userId(self):

        return self.__userId

    @property
    def tasks(self, task: Task):

        tasksAppend = self.__tasks.append(task)
        return tasksAppend
