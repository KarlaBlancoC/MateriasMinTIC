from repository.estudiante_repository import RepositorioEstudiante
from repository.materia_repository import RepositorioMateria
from model.materia import Materia

repo = RepositorioEstudiante()
repo_materia = RepositorioMateria()

mat1 = Materia({
    "_id": "63644f7fb2fbaf26d5bd4dae",
    "nombre": "Quimica Organica",
    "creditos": 6
})

# res = repo_materia.save(mat1)
# print(res)

res = repo_materia.find_all()
print(res)
