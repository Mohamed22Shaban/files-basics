from task import Task
from datetime import date
import tabulate
from argparse import Namespace

class TaskControl:
    def __init__(self,file_name):
        self.file_name = file_name


    def add_task(self ,args):
        # start date
        if not args.start_date:
            now =date.today().isoformat()
            args.start_date = now

        # task
        task = Task(args.title, args.description, args.start_date , args.end_date , args.done )

        #3 open file and save info
        with open(self.file_name,'a') as x:
            x.write(str(task) + '\n')


        # must convert str to the contrast value in python => 'None' =>> None
    def list_tasks(self):
        unfinnish_task = []
        with open(self.file_name,'r') as x:
            for line in x:
                title ,description ,start_date ,end_date ,done = line.split(',')
                end_date = None if end_date == 'None' else end_date
                done = False if done.strip('\n') == 'False' else True
                # to avoid the finnished task
                if done :
                    continue
                 # not finnish will add to list
                unfinnish_task.append({'title':title, 'description':description  ,'start_date':start_date  ,'end_date':end_date  })
        return unfinnish_task



# will show all tasks
    def list_all_tasks(self):
        tasks = []
        with open(self.file_name,'r') as x:
            for line in x:
                title ,description ,start_date ,end_date ,done = line.split( ',')
                end_date = None if end_date == 'None' else end_date
                done = False if done.strip('\n') == 'False' else True

                 # not finnish will add to list
                tasks.append({'title':title, 'description':description  ,'start_date':start_date  ,'end_date':end_date ,'done':done})
        return tasks

    
    #print  priod to finnish task
    def due_date(self , start , end):
        start_date =date.fromisoformat(start)
        end_date =date.fromisoformat(end)
        delta_date = start_date - end_date
        return f'{delta_date.days} days left'
    # this will print tasks as table

    def print_table(self,tasks):
        formatted_task =[]
        for number ,task in enumerate(tasks ,1):
            if task['start_date'] or task['end_date']:
                due_date = self.due_date(task['start_date'], task['end_date'])
            
            else:
                due_date = 'open'
             # فك تحزيم القاموس  **
            formatted_task.append({'no.':number,**task ,'due_date':due_date})
            print(tabulate(formatted_task, headers ='keys'))


    # this will control in print process
    def display(self,args):
        all_tasks = self.list_all_tasks()
        unchecked_task = self.list_tasks()

        if not all_tasks:
            print('ther are no task , to add a task use add "task"')
            return

        if args.all:
            self.print_table(all_tasks)
        else:
            if unchecked_task:
                self.print_table(unchecked_task)

            else:
                print('all tasks are checked')



    def check_task(self ,args):
        index = args.task()
        tasks = self.list_all_tasks()
        if index <= 0 or index > len(tasks):
            print(f'task number {index} does not excist')
            return

        tasks[index -1]['done'] =True
        #import namespase
        with open(self.file_name,'w') as x:
            for task in tasks:
                self.add_task(Namespace(**task))


    def remove(self ,args):
        tasks =self.list_all_tasks()  #list of task
        if args.task:  #verify weather the user not delet or none
            index =args.task

        else:
            index = len(tasks) -1     #if not will delet the last one

        #verify number that user have been entring
        if index <= 0 or index > len(tasks):
            print(f'task number {index} does not excist')
            return

        # to delet task from the list of the dict
        tasks.pop(index - 1)  #=> the dict we need to delet

        # write the new dict in the list
        with open(self.file_name,'w') as x:
            for task in tasks:
                self.add_task(Namespace(**task))


    # identify reset which clear all the content
    def reset(self ,*args):                              #=>*args  => will pass Namespace an emty object to this method
        with open(self.file_name,'w') as x:
            x.write('')    #=>write nothing to clear everything
            print('you have delet all tasks')




