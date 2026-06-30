import bcrypt


def gerar_hash(senha):
    senha_bytes = senha.encode("utf-8")
    return bcrypt.hashpw(senha_bytes, bcrypt.gensalt()).decode("utf-8")


def verificar_senha(senha, hash_senha):
    senha_bytes = senha.encode("utf-8")
    hash_bytes = hash_senha.encode("utf-8")
    return bcrypt.checkpw(senha_bytes, hash_bytes)
