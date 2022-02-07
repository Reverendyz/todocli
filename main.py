#/usr/bin/python3

from task import Task

lista = ['Adicionar tarefa', 'Concluir tarefa', 'Deletar tarefa', 'Mostrar Tarefas', 'Sair']
task_list = []
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
    obj = {id, "[  ]", title, description}
    task_list.append(obj)
    id += 1

def finish_task():
    show_tasks()
    task_to_accomplish = (int(input("Escolha qual tarefa deseja finalizar: ")))

def show_tasks():
    for task in task_list:
        print(task)

def delete_task():
    show_tasks()
    task_to_delete = (int(input("Escolha qual tarefa deseja deletar: ")))
    task_list.pop(task_to_delete-1)
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
