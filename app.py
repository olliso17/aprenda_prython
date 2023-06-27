from api.domain.list.list_entity import ListEntity
from api.domain.task.task_entity import Task
import uuid
from datetime import date

data = date.today()

task = Task("teste","testando a entidade", True, uuid.uuid4().hex, data)
task1 = []

listEntity1 = ListEntity("lista de compras","checkbox",uuid.uuid4().hex, [])
listEntity = ListEntity("lista de compras","checkbox",uuid.uuid4().hex, [])
listEntity.addTasks(task)
listEntity1.addTasks(task1)
print(listEntity1.tasks)


for lisTask in listEntity.tasks:
    print(lisTask.title)
    