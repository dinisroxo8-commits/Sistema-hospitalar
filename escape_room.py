import os
import random

# ============================================================
# MINI-PROJETO: MISSÃO ESCAPE ROOM (COMPLETO)
# ============================================================

# UTILITÁRIOS
def limpar_tela():
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)

def pausar():
    input("\nPressione Enter para continuar...")

def titulo(texto):
    limpar_tela()
    linha = "=" * (len(texto) + 6)
    print(linha)
    print(f"== {texto} ==")
    print(linha)
    print()

# DADOS DO JOGO
loja = {
    "Lanterna": {"preco": 4, "descricao": "Ajuda a ver pistas melhor."},
    "Chave": {"preco": 6, "descricao": "Pode desbloquear uma porta extra."},
    "Mapa": {"preco": 3, "descricao": "Mostra o progresso."},
    "Café": {"preco": 2, "descricao": "Recupera energia (+3)."},
}

missoes = [
    {"id": 1, "nome": "Vencer 2 desafios", "objetivo": 2, "recompensa": 5},
    {"id": 2, "nome": "Comprar 1 item na loja", "objetivo": 1, "recompensa": 3},
    {"id": 3, "nome": "Ganhar 10 moedas no total", "objetivo": 10, "recompensa": 5},
]

perguntas_quiz = [
    {"pergunta": "Qual o tipo de dados usado para True/False?", "resposta": "bool"},
    {"pergunta": "Como se chama uma coleção ordenada e mutável em Python?", "resposta": "lista"},
    {"pergunta": "Que estrutura usa pares chave:valor?", "resposta": "dicionario"},
    {"pergunta": "Qual ciclo repete enquanto a condição for verdadeira?", "resposta": "while"},
    {"pergunta": "Como se chama um bloco reutilizável de código?", "resposta": "funcao"},
]

palavras_secretas = ["python", "lista", "dicionario", "funcao", "while"]

# JOGADOR
def criar_jogador():
    titulo("MISSÃO ESCAPE ROOM – CRIAR JOGADOR")
    nome = input("👤 Nome do jogador: ").strip()
    if nome == "":
        nome = "Jogador(a)"
    jogador = {
        "nome": nome,
        "moedas": 5,
        "energia": 10,
        "inventario": [],
        "historico": [],
        "desafios_vencidos": 0,
        "itens_comprados": 0,
        "moedas_ganhas": 0,
        "missoes_concluidas": [],
    }
    jogador["historico"].append(f"O jogador {nome} começou a missão!")
    return jogador

# MENU / ESTADO
def mostrar_menu():
    print("1 - Jogar desafio")
    print("2 - Loja (comprar itens)")
    print("3 - Ver estado do jogador")
    print("4 - Ver missões")
    print("5 - Relatório final")
    print("6 - Sair\n")

def mostrar_estado(jogador):
    titulo("ESTADO DO JOGADOR")
    print(f"👤 Nome: {jogador['nome']}")
    print(f"🪙 Moedas: {jogador['moedas']}")
    print(f"⚡ Energia: {jogador['energia']}")
    print(f"🏆 Desafios vencidos: {jogador['desafios_vencidos']}")
    print(f"🛒 Itens comprados: {jogador['itens_comprados']}")
    print("\n🎒 Inventário:")
    if jogador["inventario"]:
        for item in jogador["inventario"]:
            print(f" - {item}")
    else:
        print(" (vazio)")
    pausar()

# DESAFIOS
def desafio_matematica():
    titulo("DESAFIO: MATEMÁTICA RÁPIDA")
    a = random.randint(2, 12)
    b = random.randint(2, 12)
    op = random.choice(["+", "-", "*"])
    if op == "+":
        certo = a + b
    elif op == "-":
        certo = a - b
    else:
        certo = a * b
    print(f"Resolve: {a} {op} {b}")
    tentativa = input("Resposta: ").strip()
    if not tentativa.lstrip("-").isdigit():
        print("❌ Isso não é um número.")
        return False
    if int(tentativa) == certo:
        print("✅ Certo!")
        return True
    else:
        print(f"❌ Errado. A resposta era {certo}.")
        return False

def desafio_quiz_python():
    titulo("DESAFIO: QUIZ PYTHON")
    p = random.choice(perguntas_quiz)
    print(p["pergunta"])
    resp = input("Resposta: ").strip().lower()
    if resp == p["resposta"].lower():
        print("✅ Correto!")
        return True
    else:
        print(f"❌ Errado. Era '{p['resposta']}'.")
        return False

def desafio_palavra_secreta():
    titulo("DESAFIO: PALAVRA SECRETA")
    palavra = random.choice(palavras_secretas)
    dica = palavra[0].upper()
    print(f"Dica: começa com {dica} (tenta a palavra toda!)")
    tentativas = 0
    while tentativas < 4:
        chute = input("Palavra: ").strip().lower()
        if chute == palavra:
            print("✅ Acertaste!")
            return True
        print(f"❌ Errado. Tentativa {tentativas+1}/4")
        tentativas += 1
    print(f"💀 Perdeu! Era '{palavra}'.")
    return False

def jogar_desafio(jogador):
    titulo("SALA DE DESAFIOS")
    if jogador["energia"] <= 0:
        print("😴 Sem energia! Vai à loja comprar Café.")
        pausar()
        return
    print("1. Matemática | 2. Quiz Python | 3. Palavra Secreta")
    escolha = input("Escolha: ").strip()
    vitoria = False
    if escolha == "1":
        vitoria = desafio_matematica()
    elif escolha == "2":
        vitoria = desafio_quiz_python()
    elif escolha == "3":
        vitoria = desafio_palavra_secreta()
    else:
        print("❌ Inválido.")
        pausar()
        return
    jogador["energia"] -= 1
    if vitoria:
        ganho = random.randint(2, 5)
        jogador["moedas"] += ganho
        jogador["moedas_ganhas"] += ganho
        jogador["desafios_vencidos"] += 1
        jogador["historico"].append(f"Venceu desafio! +{ganho} moedas.")
    else:
        jogador["historico"].append("Perdeu desafio.")
    verificar_missoes(jogador)
    pausar()

# LOJA
def mostrar_loja():
    titulo("LOJA DO ESCAPE ROOM")
    print("Itens disponíveis:")
    for nome_item, info in loja.items():
        print(f"- {nome_item} | {info['preco']} moedas | {info['descricao']}")
    print()

def comprar_item(jogador):
    mostrar_loja()
    print(f"🪙 Tens {jogador['moedas']} moedas.")
    item = input("Item a comprar (ou 'sair'): ").strip().title()
    if item == "Sair":
        return
    if item not in loja:
        print("❌ Item não existe.")
        pausar()
        return
    info = loja[item]
    if jogador["moedas"] < info["preco"]:
        print("❌ Moedas insuficientes.")
        pausar()
        return
    jogador["moedas"] -= info["preco"]
    jogador["inventario"].append(item)
    jogador["itens_comprados"] += 1
    jogador["historico"].append(f"Comprou {item}.")
    if item == "Café":
        jogador["energia"] = min(10, jogador["energia"] + 3)
        print("☕ +3 energia!")
    verificar_missoes(jogador)
    pausar()

# MISSÕES
def mostrar_missoes(jogador):
    titulo("MISSÕES")
    for m in missoes:
        status = "✅" if m["id"] in jogador["missoes_concluidas"] else "⬜"
        prog = "Concluída" if m["id"] in jogador["missoes_concluidas"] else "Pendente"
        print(f"{status} {m['nome']} - {prog}")
    pausar()

def verificar_missoes(jogador):
    for m in missoes:
        if m["id"] in jogador["missoes_concluidas"]:
            continue
        concluida = False
        if m["id"] == 1 and jogador["desafios_vencidos"] >= m["objetivo"]:
            concluida = True
        elif m["id"] == 2 and jogador["itens_comprados"] >= m["objetivo"]:
            concluida = True
        elif m["id"] == 3 and jogador["moedas_ganhas"] >= m["objetivo"]:
            concluida = True
        if concluida:
            jogador["missoes_concluidas"].append(m["id"])
            jogador["moedas"] += m["recompensa"]
            jogador["historico"].append(f"Missão {m['id']} concluída! +{m['recompensa']} moedas.")

# RELATÓRIO FINAL
def relatorio_final(jogador):
    titulo("RELATÓRIO FINAL")
    print(f"🏆 {jogador['nome']}: {jogador['desafios_vencidos']} desafios, {jogador['itens_comprados']} itens.")
    print(f"🪙 Moedas finais: {jogador['moedas']} | Energia: {jogador['energia']}")
    print(f"✅ Missões: {len(jogador['missoes_concluidas'])}/{len(missoes)}")
    print("\n🎒 Inventário:", ", ".join(jogador["inventario"]) or "vazio")
    print("\n📜 Histórico:")
    for evento in jogador["historico"]:
        print(f" - {evento}")
    pausar()

# PROGRAMA PRINCIPAL
def main():
    jogador = criar_jogador()
    while True:
        limpar_tela()
        print("🎮 MISSÃO ESCAPE ROOM – MENU PRINCIPAL\n")
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            jogar_desafio(jogador)
        elif opcao == "2":
            comprar_item(jogador)
        elif opcao == "3":
            mostrar_estado(jogador)
        elif opcao == "4":
            mostrar_missoes(jogador)
        elif opcao == "5":
            relatorio_final(jogador)
        elif opcao == "6":
            limpar_tela()
            print("A sair do jogo... 👋")
            break
        else:
            print("❌ Opção inválida!")
            pausar()

if __name__ == "__main__":
    main()
