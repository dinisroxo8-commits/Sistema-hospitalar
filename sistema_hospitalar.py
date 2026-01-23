import os
import datetime

pacientes = []
consultas = []

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("\n" + "="*25)
    print("    SISTEMA HOSPITALAR V2.0")
    print("="*25)
    print("1. Cadastrar paciente")
    print("2. Listar pacientes")
    print("3. Marcar consulta")
    print("4. Listar consultas")
    print("5. Ver consultas de um paciente")
    print("6. Ver próxima consulta de um paciente")
    print("7. Alterar estado da consulta")
    print("8. Eliminar paciente")
    print("9. Sair")

def obter_proximo_id_paciente():
    if not pacientes:
        return 1
    ids_existentes = [p['id'] for p in pacientes]
    for i in range(1, max(ids_existentes) + 2):
        if i not in ids_existentes:
            return i

def reorganizar_ids_pacientes():
    for i, p in enumerate(pacientes):
        id_antigo = p['id']
        id_novo = i + 1
        p['id'] = id_novo
        for c in consultas:
            if c['id'] == id_antigo:
                c['id'] = id_novo
            if c['id_paciente'] == id_antigo:
                c['id_paciente'] = id_novo

def cadastrar_paciente():
    limpar()
    print("=== NOVO CADASTRO ===")
    nome = input("Nome completo (ou 0 para voltar): ")
    if nome == "0":
        return
    idade = input("Idade: ")
    contacto = input("Contacto telefónico: ")
    novo_id = obter_proximo_id_paciente()
    paciente = {
        'id': novo_id,
        'nome': nome.strip(),
        'idade': idade,
        'contacto': contacto
    }
    pacientes.append(paciente)
    print(f"\n✅ Paciente {nome} cadastrado com ID {novo_id}")
    input("\nPressione ENTER para voltar ao menu...")

def listar_pacientes():
    limpar()
    if not pacientes:
        print("❌ Nenhum paciente cadastrado.")
    else:
        print(f"\n📋 {len(pacientes)} paciente(s) registado(s):")
        for p in pacientes:
            print(f"ID: {p['id']:2d} | {p['nome']:<20} | {p['idade']:>3} anos | {p['contacto']}")
    input("\nPressione ENTER para voltar ao menu...")

def buscar_paciente(id_paciente):
    for p in pacientes:
        if p['id'] == id_paciente:
            return p
    return None

def marcar_consulta():
    limpar()
    if not pacientes:
        print("❌ Nenhum paciente cadastrado.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    print("\n📋 Pacientes disponíveis:")
    for p in pacientes:
        print(f"ID: {p['id']:2d} | {p['nome']:<20} | {p['idade']} anos")
    id_input = input("\nID do paciente (ou 0 para voltar): ")
    if id_input == "0":
        return
    try:
        id_paciente = int(id_input)
    except:
        print("❌ ID inválido.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    if not buscar_paciente(id_paciente):
        print("❌ Paciente não encontrado.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    data = input("Data (dd/mm/aaaa): ")
    hora = input("Hora (hh:mm): ")
    tipo = input("Tipo de consulta: ")
    
    print("\n📅 Estado inicial da consulta:")
    print("1. Agendada")
    print("2. Realizada") 
    print("3. Cancelada")
    opcao_estado = input("Escolha (1/2/3): ")
    
    if opcao_estado == "1":
        estado = "agendada"
    elif opcao_estado == "2":
        estado = "realizada"
    elif opcao_estado == "3":
        estado = "cancelada"
    else:
        print("⚠️ Opção inválida. Estado definido como 'agendada'.")
        estado = "agendada"
    
    consulta = {
        'id': obter_proximo_id_paciente(),  # ID único para consulta
        'id_paciente': id_paciente,
        'data': data,
        'hora': hora,
        'tipo': tipo,
        'estado': estado,
        'data_criacao': datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    consultas.append(consulta)
    print(f"\n✅ Consulta marcada! ID: {consulta['id']} - Estado: {estado}")
    input("\nPressione ENTER para voltar ao menu...")

def listar_consultas():
    limpar()
    if not consultas:
        print("❌ Nenhuma consulta registada.")
    else:
        print(f"\n📅 {len(consultas)} consulta(s) registada(s):")
        for c in consultas:
            paciente = buscar_paciente(c['id_paciente'])
            nome = paciente['nome'] if paciente else "DESCONHECIDO"
            print(f"ID:{c['id']:3d} | {nome:<15} | {c['data']} {c['hora']:<6} | {c['tipo']:<12} | {c['estado'].upper()}")
    input("\nPressione ENTER para voltar ao menu...")

def consultas_de_paciente():
    limpar()
    if not consultas:
        print("❌ Nenhuma consulta registada.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    ids_com_consulta = list(set([c['id_paciente'] for c in consultas]))
    pacientes_com_consulta = [p for p in pacientes if p['id'] in ids_com_consulta]
    if not pacientes_com_consulta:
        print("❌ Nenhum paciente com consultas.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    print("\n👥 Pacientes com consultas:")
    for p in pacientes_com_consulta:
        print(f"ID: {p['id']:2d} | {p['nome']:<20}")
    id_input = input("\nID do paciente (ou 0 para voltar): ")
    if id_input == "0":
        return
    try:
        id_paciente = int(id_input)
    except:
        print("❌ ID inválido.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    if not buscar_paciente(id_paciente):
        print("❌ Paciente não encontrado.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    cons = [c for c in consultas if c['id_paciente'] == id_paciente]
    if not cons:
        print("❌ Nenhuma consulta para este paciente.")
    else:
        print(f"\n📋 Consultas do paciente ID {id_paciente}:")
        for c in cons:
            print(f"  ID:{c['id']:3d} | {c['data']} {c['hora']:<6} | {c['tipo']:<12} | {c['estado'].upper()}")
    input("\nPressione ENTER para voltar ao menu...")

def proxima_consulta():
    limpar()
    if not pacientes:
        print("❌ Nenhum paciente cadastrado.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    print("\n👥 Pacientes:")
    for p in pacientes:
        print(f"ID: {p['id']:2d} | {p['nome']:<20}")
    id_input = input("\nID do paciente (ou 0 para voltar): ")
    if id_input == "0":
        return
    try:
        id_paciente = int(id_input)
    except:
        print("❌ ID inválido.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    if not buscar_paciente(id_paciente):
        print("❌ Paciente não encontrado.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    cons = [c for c in consultas if c['id_paciente'] == id_paciente and c['estado'] == 'agendada']
    if not cons:
        print("❌ Nenhuma consulta agendada.")
    else:
        proxima = min(cons, key=lambda x: x['data'] + ' ' + x['hora'])  # Pega a mais próxima
        print(f"\n⏰ PRÓXIMA CONSULTA:")
        print(f"ID: {proxima['id']} | Data: {proxima['data']} | Hora: {proxima['hora']} | {proxima['tipo']}")
    input("\nPressione ENTER para voltar ao menu...")

def alterar_estado():
    limpar()
    if not consultas:
        print("❌ Nenhuma consulta registada.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    print("\n📋 Consultas disponíveis:")
    for c in consultas:
        paciente = buscar_paciente(c['id_paciente'])
        nome = paciente['nome'] if paciente else "DESCONHECIDO"
        print(f"ID:{c['id']:3d} | {nome:<15} | {c['data']} {c['hora']:<6} | {c['tipo']:<12} | {c['estado'].upper()}")
    id_input = input("\nID da consulta (ou 0 para voltar): ")
    if id_input == "0":
        return
    try:
        id_consulta = int(id_input)
    except:
        print("❌ ID inválido.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    cons_id = [c for c in consultas if c['id'] == id_consulta]
    if not cons_id:
        print("❌ Consulta não encontrada.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    
    print("\n🔄 Novo estado:")
    print("1. Agendada")
    print("2. Realizada")
    print("3. Cancelada")
    opcao_estado = input("Escolha (1/2/3): ")
    
    if opcao_estado == "1":
        novo_estado = "agendada"
    elif opcao_estado == "2":
        novo_estado = "realizada"
    elif opcao_estado == "3":
        novo_estado = "cancelada"
    else:
        print("❌ Opção inválida.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    
    if len(cons_id) == 1:
        cons_id[0]['estado'] = novo_estado
        print(f"\n✅ Estado alterado para: {novo_estado.upper()}")
    else:
        print(f"\n📋 Consultas com ID {id_consulta}:")
        for c in cons_id:
            print(f"  Data: {c['data']} | Hora: {c['hora']} | Tipo: {c['tipo']}")
        data_input = input("\nData da consulta a alterar (dd/mm/aaaa): ")
        for c in cons_id:
            if c['data'] == data_input:
                c['estado'] = novo_estado
                print(f"\n✅ Estado alterado para: {novo_estado.upper()}")
                input("\nPressione ENTER para voltar ao menu...")
                return
        print("❌ Data não encontrada.")
    input("\nPressione ENTER para voltar ao menu...")

def eliminar_paciente():
    limpar()
    if not pacientes:
        print("❌ Nenhum paciente cadastrado.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    print("\n🗑️ Pacientes para eliminar:")
    for p in pacientes:
        print(f"ID: {p['id']:2d} | {p['nome']:<20} | {p['idade']} anos")
    id_input = input("\nID do paciente a eliminar (ou 0 para voltar): ")
    if id_input == "0":
        return
    try:
        id_paciente = int(id_input)
    except:
        print("❌ ID inválido.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    paciente = buscar_paciente(id_paciente)
    if not paciente:
        print("❌ Paciente não encontrado.")
        input("\nPressione ENTER para voltar ao menu...")
        return
    
    cons_marcadas = [c for c in consultas if c['id_paciente'] == id_paciente and c['estado'] == 'agendada']
    
    if cons_marcadas:
        print("\n" + "="*60)
        print("🚫 ERRO: IMPOSSÍVEL ELIMINAR PACIENTE!")
        print("="*60)
        print(f"❌ O paciente tem {len(cons_marcadas)} consulta(s) AGENDADA(S).")
        print("\nConsultas pendentes:")
        for c in cons_marcadas:
            print(f"   • {c['data']} {c['hora']} - {c['tipo']}")
        print("\n💡 Altere primeiro o estado das consultas agendadas!")
        print("="*60)
        input("\nPressione ENTER para voltar ao menu...")
        return
    
    pacientes.remove(paciente)
    consultas_para_remover = [c for c in consultas if c['id_paciente'] == id_paciente]
    for c in consultas_para_remover:
        consultas.remove(c)
    reorganizar_ids_pacientes()
    print("\n✅ Paciente eliminado com sucesso!")
    input("\nPressione ENTER para voltar ao menu...")

# LOOP PRINCIPAL
while True:
    limpar()
    mostrar_menu()
    opcao = input("\n▶️ Escolha uma opção: ")
    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        listar_pacientes()
    elif opcao == "3":
        marcar_consulta()
    elif opcao == "4":
        listar_consultas()
    elif opcao == "5":
        consultas_de_paciente()
    elif opcao == "6":
        proxima_consulta()
    elif opcao == "7":
        alterar_estado()
    elif opcao == "8":
        eliminar_paciente()
    elif opcao == "9":
        limpar()
        print("👋 Até breve! Sistema encerrado.")
        break
    else:
        print("❌ Opção inválida! Tente novamente.")
        input("\nPressione ENTER para voltar ao menu...")

        