

class Task():

    def __init__(self, title, description, status, listId, timeSelect):
        self.__title = title
        self.__description = description
        self.__status = status
        self.__listId = listId
        self.__timeSelect = timeSelect

    @property
    def title(self):

        return self.__title

    @property
    def description(self):

        return self.__description

    @property
    def status(self):
        return self.__status

    @property
    def listId(self):
        return self.__listId

    @property
    def timeSelect(self):
        return self.__timeSelect
