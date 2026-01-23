import os

# Estrutura de dados
alunos = []

def limpar_tela():
    """
    Limpa o ecrã do terminal.
    Usa 'cls' para Windows e 'clear' para Linux/macOS.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_aluno():
    """
    Insere um novo aluno. Verifica se o código já existe.
    Solicita nome e três notas (validadas entre 0 e 20).
    """
    codigo = input("Código do aluno: ").strip()
    
    # Verifica se o código já existe
    for aluno in alunos:
        if aluno['codigo'] == codigo:
            print("Código já existe! Escolha outro.")
            input("Enter para continuar...")
            return
    
    nome = input("Nome do aluno: ").strip()
    
    # Lê e valida três notas
    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Notas {i+1} (0-20): "))
                if 0 <= nota <= 20:
                    notas.append(nota)
                    break
                else:
                    print("Nota deve estar entre 0 e 20!")
            except ValueError:
                print("Introduza um número válido!")
    
    aluno = {
        'codigo': codigo,
        'nome': nome,
        'notas': notas
    }
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")
    input("Enter para continuar...")

def listar_alunos():
    """
    Mostra todos os alunos com código, nome, notas e média.
    """
    if not alunos:
        print("Nenhum aluno cadastrado.")
        input("Enter para continuar...")
        return
    
    limpar_tela()
    print("Lista de Alunos:")
    print("-" * 60)
    for aluno in alunos:
        media = sum(aluno['notas']) / 3
        notas_str = ", ".join(f"{n:.1f}" for n in aluno['notas'])
        print(f"{aluno['codigo']} | {aluno['nome']} | Notas: {notas_str} | Média: {media:.1f}")
    print("-" * 60)
    input("Enter para continuar...")

def mostrar_medias():
    """
    Apresenta média individual de cada aluno e média geral da turma.
    """
    if not alunos:
        print("Nenhum aluno cadastrado.")
        input("Enter para continuar...")
        return
    
    limpar_tela()
    print("Médias dos Alunos:")
    print("-" * 50)
    total_medias = 0
    
    for aluno in alunos:
        media = sum(aluno['notas']) / 3
        print(f"{aluno['nome']}: {media:.1f}")
        total_medias += media
    
    media_geral = total_medias / len(alunos)
    print("-" * 50)
    print(f"Média geral da turma: {media_geral:.1f}")
    input("Enter para continuar...")

def eliminar_aluno():
    """
    Remove um aluno através do código.
    """
    if not alunos:
        print("Nenhum aluno cadastrado.")
        input("Enter para continuar...")
        return
    
    codigo = input("Código do aluno para eliminar: ").strip()
    for i, aluno in enumerate(alunos):
        if aluno['codigo'] == codigo:
            removido = alunos.pop(i)
            print(f"Aluno '{removido['nome']}' eliminado.")
            input("Enter para continuar...")
            return
    print("Aluno não encontrado.")
    input("Enter para continuar...")

def menu():
    """
    Mostra o menu principal.
    """
    limpar_tela()
    print("=== Programa de Gestão de Alunos ===")
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Mostrar médias")
    print("4. Eliminar aluno")
    print("0. Sair")

# Programa principal
while True:
    menu()
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == '1':
        cadastrar_aluno()
    elif opcao == '2':
        listar_alunos()
    elif opcao == '3':
        mostrar_medias()
    elif opcao == '4':
        eliminar_aluno()
    elif opcao == '0':
        print("A sair do programa. Obrigado!")
        break
    else:
        print("Opção inválida!")
        input("Enter para continuar...")