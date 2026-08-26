# bot_initializer.py
# Script de inicialização do robô RPA

# --- Declaração e inicialização das variáveis de configuração ---

BOT_NAME: str = "RPA_FINANCEIRO_01"   # Nome do robô
MAX_RETRIES: int = 3                   # Número máximo de tentativas em caso de falha
EXECUTION_TIMEOUT: float = 30.5        # Tempo limite por tarefa em segundos
IS_PRODUCTION: bool = True             # Flag de ambiente de produção

# --- Mensagem de inicialização formatada ---

print("=" * 50)
print("       INICIALIZAÇÃO DO ROBÔ RPA")
print("=" * 50)
print(f"  BOT_NAME          : {BOT_NAME}")
print(f"  Tipo              : {type(BOT_NAME)}")
print("-" * 50)
print(f"  MAX_RETRIES       : {MAX_RETRIES}")
print(f"  Tipo              : {type(MAX_RETRIES)}")
print("-" * 50)
print(f"  EXECUTION_TIMEOUT : {EXECUTION_TIMEOUT}s")
print(f"  Tipo              : {type(EXECUTION_TIMEOUT)}")
print("-" * 50)
print(f"  IS_PRODUCTION     : {IS_PRODUCTION}")
print(f"  Tipo              : {type(IS_PRODUCTION)}")
print("=" * 50)
print("  Robô inicializado com sucesso!")
print("=" * 50)
