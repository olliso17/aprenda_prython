from api.domain.task.task_entity import Task
import uuid
from datetime import date

data = date.today()
task = Task("teste","testando a entidade", True, uuid.uuid4(), data)

print(task.createdAt)