# auth.py

from werkzeug.security import generate_password_hash, check_password_hash

# Criando hash de senha
hashed_pw = generate_password_hash("minhasenha123")

# Verificando senha
check_password_hash(hashed_pw, "minhasenha123")  # True