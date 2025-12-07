lista_de_tarefas = [
    {"titulo":"Responder e-mails",
     "prioridade": 2,
     "completa": False},

    {"titulo":"Atender chamados",
    "prioridade": 1,
    "completa": False},

    {"titulo":"Organizar planilhas",
    "prioridade": 3,
    "completa": True}
]

for tarefa in lista_de_tarefas:
    titulo = tarefa["titulo"]
    prioridade = tarefa["prioridade"]
    print(f'Título: {titulo} | Prioridade: {prioridade}')