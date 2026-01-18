def mostrar_menu():
    print('\n--- Gerenciador de Tarefas ---')
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefas')
    print('3 - Concluir tarefa')
    print('4 - Remover tarefa')
    print('5 - Sair')

tarefas = []

while True:
    mostrar_menu()
    escolha_do_usuario = int(input('Escolha uma opção: '))
    
    if escolha_do_usuario == 1:
        descricao = input('\nQual tarefa quer adicionar? ')
        tarefa = {'descricao': descricao,
                  'concluida': False}
        tarefas.append(tarefa)
           
           
    elif escolha_do_usuario == 2:
        print('\n')
        if not tarefas:
            print('Nenhuma tarefa cadastrada.')
            continue
        print('---Lista de Tarefas Atual---')
        # O i representa o índice, a tarefa é a frase.
        # Enumerate permite receber esses 2 valores.
        # Start 1 faz com que o print não começa do índice 0. ex: 0.andar, 1.jogar..
        for i, tarefa in enumerate(tarefas, start=1): 
            print(f"{i}. {tarefa['descricao']} - {'Concluída' if tarefa['concluida'] else 'Pendente'}")
    
    
    elif escolha_do_usuario == 3:
        if not tarefas:
            print('Nenhuma tarefa para concluir.')
            continue
        mudar_tarefa = int(input('Qual tarefa está concluída? '))
        # Se 1 for menor/igual que mudar_tarefa, e mudar_tarefa for menor/igual ao comprimento da lista.
        if 1 <= mudar_tarefa <= len(tarefas):
            tarefas[mudar_tarefa - 1]['concluida'] = True
        else:
            print('Número inválido.')
    
    elif escolha_do_usuario == 4:
        if not tarefas:
            print('Nenhuma tarefa para remover.')
            continue
        remover_tarefa = int(input('Qual tarefa quer remover? '))
        
        if 1 <= remover_tarefa <= len(tarefas):
            tarefas.pop(remover_tarefa - 1)
        else:
            print('Numero inválido.')
        
    elif escolha_do_usuario == 5:
        break
        
        
    else:
        print('Opção inválida!')