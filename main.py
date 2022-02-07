#/usr/bin/python3

from task import Task

lista = ['Adicionar tarefa', 'Concluir tarefa', 'Deletar tarefa', 'Mostrar tarefas abertas', 'Mostrar todas as tarefas', 'Sair']
task_list = []
id = 1

def main():
    while(True):
        try:
            choice = menu()        
            if choice == 1:    
                add_task()
            if choice == 2:
                finish_task()
            if choice == 3:
                delete_task()
            if choice == 4:
                show_accomplished_tasks()
            if choice == 5:
                show_tasks()
            if choice == 6:
                break            
        except:
            print("Favor digitar um numero valido da lista")

def menu():
    for i in range(0,len(lista)):
        print( i+1, lista[i] )
    menuChoice = (int(input("Digite sua escolha: ")))
    return menuChoice

def add_task():
    global id
    title = input("Nome da tarefa: ")
    description = input("Descricao da tarefa: ")
    task_list.append(Task(id, title, description))
    id += 1
    return

def finish_task():
    show_tasks()
    task_to_accomplish = (int(input("Escolha qual tarefa deseja finalizar: ")))
    task_list.__getitem__(task_to_accomplish-1).end()
    return

def show_accomplished_tasks():
    for task in task_list:
        if task.status == True:
            print(
            task.id,"\n",
            task.title,"\n",
            task.description,"\n",
            task.status
            )
    return

def show_tasks():
    for task in task_list:
        print(
            task.id,"\n",
            task.title,"\n",
            task.description,"\n",
            task.status
        )
    return

def delete_task():
    show_tasks()
    task_to_delete = (int(input("Escolha qual tarefa deseja deletar: ")))
    task_list.pop(task_to_delete-1)
    return

if __name__ == "__main__":
    main()