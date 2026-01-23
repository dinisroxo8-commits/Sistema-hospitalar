import os

# Lista de restaurantes
restaurantes = []

def limpar_ecra():
    """
    Limpa o ecrã do terminal.
    Usa 'cls' para Windows e 'clear' para Linux/Mac.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_restaurante():
    """
    Pede ao utilizador o nome e a categoria do restaurante.
    O restaurante é guardado como um dicionário com nome, categoria e estado ativo (False por defeito).
    """
    nome = input("Nome do restaurante: ").strip()
    categoria = input("Categoria do restaurante: ").strip()
    restaurante = {
        'nome': nome,
        'categoria': categoria,
        'ativo': False
    }
    restaurantes.append(restaurante)
    print(f"Restaurante '{nome}' criado com sucesso!")

def listar_restaurantes():
    """
    Mostra todos os restaurantes cadastrados.
    Cada restaurante é apresentado com número, nome, categoria e estado (Ativo ou Desativado).
    """
    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
        return
    
    limpar_ecra()
    print("Lista de Restaurantes:")
    print("-" * 50)
    for i, rest in enumerate(restaurantes, 1):
        estado = "Ativo" if rest['ativo'] else "Desativado"
        print(f"{i}. {rest['nome']} | {rest['categoria']} | {estado}")
    print("-" * 50)

def alterar_estado_restaurante():
    """
    Permite ativar ou desativar um restaurante.
    O utilizador digita o nome do restaurante e o estado é alternado automaticamente.
    """
    nome = input("Nome do restaurante para alterar estado: ").strip().lower()
    for rest in restaurantes:
        if rest['nome'].lower() == nome:
            rest['ativo'] = not rest['ativo']
            novo_estado = "Ativo" if rest['ativo'] else "Desativado"
            print(f"Estado de '{rest['nome']}' alterado para {novo_estado}.")
            return
    print("Restaurante não encontrado.")

def remover_restaurante():
    """
    Remove um restaurante da lista com base no nome introduzido pelo utilizador.
    """
    nome = input("Nome do restaurante para remover: ").strip().lower()
    for i, rest in enumerate(restaurantes):
        if rest['nome'].lower() == nome:
            removido = restaurantes.pop(i)
            print(f"Restaurante '{removido['nome']}' removido com sucesso.")
            return
    print("Restaurante não encontrado.")

def menu():
    """
    Mostra o menu principal e controla toda a navegação do programa.
    O programa fica em execução até o utilizador escolher a opção 0 (Sair).
    """
    while True:
        limpar_ecra()
        print("=== Programa de Gestão de Restaurantes ===")
        print("1. Criar restaurante")
        print("2. Listar restaurantes")
        print("3. Alterar estado do restaurante")
        print("4. Remover restaurante")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            criar_restaurante()
            input("\nEnter para continuar...")
        elif opcao == '2':
            listar_restaurantes()
            input("\nEnter para continuar...")
        elif opcao == '3':
            alterar_estado_restaurante()
            input("\nEnter para continuar...")
        elif opcao == '4':
            remover_restaurante()
            input("\nEnter para continuar...")
        elif opcao == '0':
            print("A sair do programa. Obrigado!")
            break
        else:
            print("Opção inválida!")
            input("\nEnter para continuar...")

# Execução do programa
if __name__ == "__main__":
    menu()