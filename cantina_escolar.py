import os
from datetime import datetime

# Estruturas de dados
alunos = []
pratos = [
    {"nome": "Arroz de pato", "preco": 3.50},
    {"nome": "Bacalhau à Brás", "preco": 4.00},
    {"nome": "Frango assado", "preco": 3.00},
    {"nome": "Lasanha", "preco": 3.20},
    {"nome": "Pizza vegetariana", "preco": 3.80}
]
bebidas = [
    {"nome": "Água", "preco": 0.50},
    {"nome": "Sumo laranja", "preco": 1.00},
    {"nome": "Coca-Cola", "preco": 1.20},
    {"nome": "Leite chocolate", "preco": 0.80}
]
reservas = []  # [{"codigo_aluno": str, "data": str (YYYY-MM), "prato": dict, "bebida": dict}]

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("\n=== SISTEMA REFEITÓRIO ESCOLAR ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Mostrar ementa")
    print("4 - Fazer reserva de almoço")
    print("5 - Listar reservas de um aluno")
    print("6 - Mostrar fatura mensal de um aluno")
    print("7 - Cancelar reserva")
    print("8 - Sair")

def aluno_existe(codigo):
    for a in alunos:
        if a['codigo'] == codigo:
            return True
    return False

def cadastrar_aluno():
    limpar()
    print("=== CADASTRO DE ALUNO ===")
    codigo = input("Código do aluno: ").strip()
    if aluno_existe(codigo):
        print("Código já existe!")
        input("\nEnter para continuar...")
        return
    nome = input("Nome do aluno: ").strip()
    alunos.append({"codigo": codigo, "nome": nome})
    print("Aluno cadastrado com sucesso!")
    input("\nEnter para continuar...")

def listar_alunos():
    limpar()
    print("=== LISTA DE ALUNOS ===")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for a in alunos:
            print(f"Código: {a['codigo']} - {a['nome']}")
    input("\nEnter para continuar...")

def mostrar_ementa():
    limpar()
    print("=== EMENTA - PRATOS ===")
    for i, p in enumerate(pratos, 1):
        print(f"{i}. {p['nome']} - €{p['preco']:.2f}")
    print("\n=== BEBIDAS ===")
    for i, b in enumerate(bebidas, 1):
        print(f"{i}. {b['nome']} - €{b['preco']:.2f}")
    input("\nEnter para continuar...")

def fazer_reserva():
    limpar()
    print("=== RESERVA DE ALMOÇO ===")
    codigo = input("Código do aluno: ").strip()
    if not aluno_existe(codigo):
        print("Aluno não encontrado!")
        input("\nEnter para continuar...")
        return
    
    data_str = input("Data (YYYY-MM, ex: 2026-01): ").strip()
    try:
        datetime.strptime(data_str, '%Y-%m')
    except:
        print("Data inválida!")
        input("\nEnter para continuar...")
        return
    
    print("Escolha o prato:")
    for i, p in enumerate(pratos, 1):
        print(f"{i}. {p['nome']} - €{p['preco']:.2f}")
    p_idx = int(input("Número do prato: ")) - 1
    if 0 <= p_idx < len(pratos):
        prato = pratos[p_idx]
    else:
        print("Prato inválido!")
        return
    
    print("Escolha a bebida:")
    for i, b in enumerate(bebidas, 1):
        print(f"{i}. {b['nome']} - €{b['preco']:.2f}")
    b_idx = int(input("Número da bebida: ")) - 1
    if 0 <= b_idx < len(bebidas):
        bebida = bebidas[b_idx]
    else:
        print("Bebida inválida!")
        return
    
    total = prato['preco'] + bebida['preco']
    reservas.append({
        "codigo_aluno": codigo,
        "data": data_str,
        "prato": prato,
        "bebida": bebida,
        "total": total
    })
    print(f"Reserva feita! Total: €{total:.2f}")
    input("\nEnter para continuar...")

def listar_reservas_aluno():
    limpar()
    print("=== RESERVAS DE UM ALUNO ===")
    codigo = input("Código do aluno: ").strip()
    res_aluno = [r for r in reservas if r['codigo_aluno'] == codigo]
    if not res_aluno:
        print("Nenhuma reserva encontrada.")
    else:
        for r in res_aluno:
            print(f"Data: {r['data']} | Prato: {r['prato']['nome']} | Bebida: {r['bebida']['nome']} | €{r['total']:.2f}")
    input("\nEnter para continuar...")

def fatura_mensal():
    limpar()
    print("=== FATURA MENSAL ===")
    codigo = input("Código do aluno: ").strip()
    mes_ano = input("Mês/Ano (YYYY-MM): ").strip()
    res_mes = [r for r in reservas if r['codigo_aluno'] == codigo and r['data'] == mes_ano]
    if not res_mes:
        print("Nenhuma reserva no período.")
    else:
        total = sum(r['total'] for r in res_mes)
        print(f"Total a pagar: €{total:.2f}")
        print("Detalhes:")
        for r in res_mes:
            print(f"  - {r['data']}: {r['prato']['nome']} + {r['bebida']['nome']} = €{r['total']:.2f}")
    input("\nEnter para continuar...")

def cancelar_reserva():
    limpar()
    print("=== CANCELAR RESERVA ===")
    codigo = input("Código do aluno: ").strip()
    data_str = input("Data (YYYY-MM): ").strip()
    res_cancel = [r for r in reservas if r['codigo_aluno'] == codigo and r['data'] == data_str]
    if not res_cancel:
        print("Reserva não encontrada.")
    else:
        print("Reservas encontradas:")
        for i, r in enumerate(res_cancel):
            print(f"{i+1}. {r['prato']['nome']} + {r['bebida']['nome']}")
        idx = int(input("Número a cancelar (0 para none): ")) - 1
        if 0 <= idx < len(res_cancel):
            del reservas[reservas.index(res_cancel[idx])]
            print("Reserva cancelada!")
        else:
            print("Cancelamento ignorado.")
    input("\nEnter para continuar...")

# Programa principal
while True:
    limpar()
    mostrar_menu()
    opcao = input("\nEscolha uma opção: ").strip()
    
    if opcao == '1':
        cadastrar_aluno()
    elif opcao == '2':
        listar_alunos()
    elif opcao == '3':
        mostrar_ementa()
    elif opcao == '4':
        fazer_reserva()
    elif opcao == '5':
        listar_reservas_aluno()
    elif opcao == '6':
        fatura_mensal()
    elif opcao == '7':
        cancelar_reserva()
    elif opcao == '8':
        print("Obrigado por usar o sistema!")
        break
    else:
        print("Opção inválida!")
        input("Enter para continuar...")
