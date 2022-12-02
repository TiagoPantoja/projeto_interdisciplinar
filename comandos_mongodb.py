from pymongo import MongoClient

connection_string = "mongodb://localhost:27017"

client = MongoClient(connection_string)

nome_db: str = "projeto_calculo_viga"

db = client[nome_db] # criando banco de dados

# primeira collection - viga
id_viga: int = 1
nome_doc1: str = "viga" 
documento_viga = db[nome_doc1]

def adicionar_viga(carga: float, comprimento: float, base: float, altura: float, resistencia_material: float) -> None:
    global id_viga
    dados: dict[str, float] = {
        "_id": id_viga,
        "carga": carga,
        "comprimento": comprimento,
        "base": base,
        "altura": altura,
        "resistencia_material": resistencia_material
    }
    documento_viga.insert_one(dados)
    id_viga += 1
    
def mostrar_dados_viga(id_viga_requerida: int) -> str:
    viga_query = documento_viga.find_one({"_id": id_viga_requerida})
    texto: str = ""
    if viga_query == None: # se não achar ou não existir
        texto = f"a viga numero {id_viga_requerida} não existe"
    else:
        viga_query = dict(viga_query)
        for field, valor in viga_query.items():
            texto += f"{field}: {valor}\n"
    return texto


def deletar_viga(carga: float, comprimento: float, base: float, altura: float, resistencia_material: float) -> str:
    dados: dict[str, float] = {
        "carga": carga,
        "comprimento": comprimento,
        "base": base,
        "altura": altura,
        "resistencia_material": resistencia_material
    }
    documento_viga.find_one_and_delete(dados)


# Segunda collection - usuario
id_usuario: int = 1
nome_doc2: str = "usuario"
documento_usuario = db[nome_doc2]

def adicionar_usuario(nome: str, email: str, senha: str):
    global id_usuario
    dados: dict[str, str] = {
        "_id": id_usuario,
        "nome": nome,
        "email": email,
        "senha": senha
    }
    documento_usuario.insert_one(dados)
    id_usuario += 1

def mostrar_dados_usuario(id_usuario_requerida: int) -> str:
    usuario_query = documento_usuario.find_one({"_id": id_usuario_requerida})
    texto: str = ""
    if usuario_query == None: # se não achar ou não existir
        texto = f"o usuario numero {id_usuario_requerida} não existe"
    else:
        usuario_query = dict(usuario_query)
        for field, valor in usuario_query.items():
            texto += f"{field}: {valor}\n"
    return texto

def deletar_usuario(nome: str, email: str, senha: str) -> str:
    dados: dict[str, str] = {
        "nome": nome,
        "email": email,
        "senha": senha
    }
    documento_usuario.find_one_and_delete(dados)

# inserts para testar o banco, deram certo
# adicionar_viga(10, 11, 8, 10, 5)
# adicionar_viga(20, 8, 5, 19, 1)
# adicionar_usuario("VictorFS", "victorFrankenstein@gmail.com", "111818")