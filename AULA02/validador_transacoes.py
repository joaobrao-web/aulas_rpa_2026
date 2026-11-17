"""
Lab 02 - Motor de decisao e resiliencia de repeticao.

O bot percorre a fila de transacoes pendentes do banco:
- valor acima de R$ 10.000,00: manda para auditoria humana e segue a fila;
- valor menor ou igual a zero: e invalido, para tudo para manutencao;
- qualquer outro valor: processa normalmente.
"""

LIMITE_AUDITORIA = 10000.00

transacoes = [150.0, 3200.5, 12500.0, 450.0, -50.0, 800.0, 0]

for valor in transacoes:
    if valor > LIMITE_AUDITORIA:
        print(f"[ALERTA] Transação suspeita de R$ {valor:.2f}: Encaminhada para auditoria.")
        continue
    elif valor <= 0:
        print(f"[ERRO CRÍTICO] Transação inválida encontrada (R$ {valor:.2f}). Interrompendo bot...")
        break
    else:
        print(f"[SUCESSO] Transação de R$ {valor:.2f} processada.")
