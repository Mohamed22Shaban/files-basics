from argparse import ArgumentParser
from task_controler import TaskControl    #to boun the class here



def main():
    
    # to boun the class make file to stor tasks in it
    controller = TaskControl('task.txt')
    parser = ArgumentParser(description='Simple Task In CIL')
    add_sub = parser.add_subparsers()

    add_task = add_sub.add_parser('add' ,help='add the given task')
    add_task.add_argument('title',help='title of the task',type=str)
    add_task.add_argument('-d','--description',help='short description of the task',type=str ,default=None)
    add_task.add_argument('-s','--start_date',help='date to begin the task',type=str ,default=None)
    add_task.add_argument('-e','--end_date',help='date to end  the task',type=str ,default=None)
    add_task.add_argument('--done',help='check weather the task is done or not',default=False)
    # to boun add_task with add
    add_task.set_defaults(func=controller.add_task)


    list_tasks = add_sub.add_parser('list' ,help='list unfinnshed task')
    list_tasks.add_argument('-a' ,'-all' ,help='list all the tasks' ,action='store_true')

    # to boun add_task with add
    list_tasks.set_defaults(func=controller.display)

    check_task = add_sub.add_parser('check' ,help='check the given task')
    check_task.add_argument('-t' ,'--task' ,help='nomber of the task to be done' ,type=int)
    # to boun add_task with add
    check_task.set_defaults(func=controller.check_task)


    remove = add_sub.add_parser('remove' ,help='remove the task')
    remove.add_argument('-t' ,'--task' ,help='the task to be removed (number)' ,type=int)
    # to boun add_task with add
    remove.set_defaults(func=controller.remove)


    reset = add_sub.add_parser('reset' ,help='remove all tasks')
    # to boun add_task with add
    reset.set_defaults(func=controller.reset)


    args = parser.parse_args()
    args.func(args)







if __name__ == '__main__':
    main()