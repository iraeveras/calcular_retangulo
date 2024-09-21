tarefas = []

tarefa = {
    "nome": "",
    "descricao": "",
    "prioridade": "",
    "categoria": "",
    "status": False,
}

def inserir_tarefa(nome, descricao, prioridade, categoria, status):
    if nome != "" and descricao != "" and prioridade != "" and categoria != "" and status != "":
        tarefa = {
            "nome": nome,
            "descricao": descricao,
            "prioridade": prioridade,
            "categoria": categoria,
            "status": status,
        }
        tarefas.append(tarefa)

def listar_tarfeas():
    for i,item in tarefas:
        print(i, item)

def excluir_tarefa():
    for i in range(len(tarefas)):
        valor = tarefas[i]
        print(i, valor["nome"])

excluir_tarefa()

while True:
    print("1 - Inserir tarefa")
    print("2 - Listar tarefa")
    print("3 - Editar tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")
    opcao = input("Digite uma opção: ")
    if opcao == "5":
        break
    elif opcao == "1":
        nome = input("Digite o nome da tarefa: ")
        descricao = input("Digite o descrição da tarefa: ")
        prioridade = input("Digite o prioridade da tarefa: ")
        categoria = input("Digite o categoria da tarefa: ")
        status = int(input("Digite o status da tarefa: "))

        inserir_tarefa(nome, descricao, prioridade, categoria, status)
        opcao = input("Deseja inserir mais tarefa? 1 - sim 2 - não: ")
        if opcao == "1":
            continue
        else:
            listar_tarfeas()
            break
    elif opcao == "2":
        print("função listar")
        listar_tarfeas()
        break
    elif opcao == "3":
        print("funçao editar tarefa")
        break
    elif opcao == "4":
        print("funçao excluir tarefa")
        excluir_tarefa()
        break

