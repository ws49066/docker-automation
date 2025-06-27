from werkzeug.security import generate_password_hash, check_password_hash
from config.database import get_db

# Obtém a referênia da coleção de usuários
db = get_db()
user_collection = db["users"]

" Realiza o cadastro de um usuário no banco de dados"

def create_user(email, password, role):
    # Verifica se o usuário já existe
    if user_collection.find_one({"email": email}):
        return {"error": "User already exists"}, 400
    
    " Cria o usuário com a senha criptografada"
    hashed_password = generate_password_hash(password)
    user = {
        "email": email,
        "password": hashed_password,
        "role": role
    }

    # Insere o usuário no banco de dados
    user_collection.insert_one(user)
    return {"message": "Usuário criado com sucesso"}, 201

# Realiza o login do usuário verificando as credenciais
def login_user(email, password):
    user = user_collection.find_one({"email": email})
    if not user or not check_password_hash(user["password"], password):
        return {"error": "Invalid credentials"}, 401
    return user