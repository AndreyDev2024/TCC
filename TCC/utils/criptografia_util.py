from passlib.context import CryptContext

bcrypt_context = CryptContext(
    schemes = ['bcrypt'],
    deprecated = 'auto'
)

def gerar_hash(senha):
    return bcrypt_context.hash(senha)
def verificar_senha(senha, hash_senha):
    return bcrypt_context.verify(
        senha,
        hash_senha
    )
