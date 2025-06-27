from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from services.auth_service import create_user, login_user
from models.user_model import user_serializer

# Define o blueprint para o auth
auth_bp = Blueprint('auth', __name__)

# Rota para exinibir o formulário de Login
@auth_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

# Processa o formulário de Login@auth_bp.route('/login', methods=['POST'])
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.form
    result = login_user(data['email'], data['password'])
    
    # Se login_user retornar uma tupla, indica erro
    if isinstance(result, tuple):
        flash(result[0]['error'], 'error')  # Mostra mensagem de erro
        return redirect(url_for('auth.login_page'))
    
    # Caso contrário, é usuário válido
    user = result
    
    # Armazena o usuário na sessão
    session['user'] = user_serializer(user)
    return redirect(url_for('auth.dashboard'))

# Rota para exibir o formulário de cadastro
@auth_bp.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')

# Processa o formulário de cadastro
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.form
    result, status = create_user(data['email'], data['password'], data.get('role', 'cliente'))

    if status != 201:
        flash(result['error'])
        return redirect(url_for('auth.register_page'))
                        
    flash('Usuário criado com sucesso', 'success')
    return redirect(url_for('auth.login_page'))

# Rota para exibir o dashboard
@auth_bp.route('/dashboard', methods=['GET'])
def dashboard():
    user = session.get('user')
    if not user:
        return redirect(url_for('auth.login_page'))
    return f"<h1>Bem vindo, {user['email']}</h1><p>Função:  {user['role']}</h1></p>"