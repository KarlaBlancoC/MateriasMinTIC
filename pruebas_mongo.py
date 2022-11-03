import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://karlablanco:1143Krbc$@cluster0.mxetqiw.mongodb.net/bd-registro-academico?retryWrites=true&w=majority",tlsCAFile=ca)

ra_db = client["bd-registro-academico"]
coll_estudiantes = ra_db["estudiantes"]
estudiante = {
    "nombre" : "Pepito",
    "apellido": "Perez",
    "edad": 30,
    "telefonos": ["12345678","789456123","457114"],
    "materias": [
        {
            "nombre": "Fisica",
            "creditos": 5},
        {
            "nombre": "Calculo",
            "creditos": 3
        }
    ]
}
coll_estudiantes.insert_one(estudiante)
print(ra_db.list_collection_names())