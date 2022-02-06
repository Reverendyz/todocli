#/usr/bin/python3

from task import Task

lista = ['Adicionar tarefa', 'Concluir tarefa', 'Deletar tarefa', 'Mostrar Tarefas', 'Sair']
lista_tarefas = []
id = 1

def menu():
    for i in range(0,len(lista)):
        print( i+1, lista[i] )
    menuChoice = (int(input("Digite sua escolha: ")))
    return menuChoice

def add_task():
    global id
    title = input("Nome da tarefa: ")
    description = input("Descricao da tarefa: ")
    lista_tarefas.append({
        id,
        title,
        description
    })
    id += 1

def finish_task():
    print("finalizado")

def show_tasks():
    print(lista_tarefas)

def delete_task():
    show_tasks()
    task_to_delete = (int(input("Escolha qual tarefa deseja deletar: ")))
    lista_tarefas.pop(task_to_delete-1)
    show_tasks()

while(True):
    choice = menu()        
    if choice == 1:    
        add_task()
    if choice == 2:
        finish_task()
    if choice == 3:
        delete_task()
    if choice == 4:
        show_tasks()
    if choice == 5:
        break
