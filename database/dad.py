# def word (name):
#     print(f'helo {name}')



# def letter (name):
#     print(f'how are you {name} ?')


###    OOP  =>> Object Oriented Programming
# why OOP =>> allowed to organaize the code and make it readable and reusable  ,.,, everything in python is object
# python support  OOP  ,, OOP=>> is paradigm or a style to write the coding 
# paradigm  =>> make structure progeam by Methods[function] and Attributes[data]
# Methods[function] use infromation of the object to apply a task in the App
# Atteributes =>> data[information]
# python multiparadigm programming language[procedural,OOP,functional]
# procedural =>> (formula)or recipe or set of structure to make a task
# functional =>> depend on methematical function puruel more than function to do the task
##              IF MAN IS OBJECT  
# methods=>     behavior >> walking ,eating ,singing ,playing =>> action which object do
# Attribute =>  info >>     name ,age ,address ,phone number    =>> info about the object

####   CLASS
# is the tempelate for creating the object [object constructor]as scheme or[blueprint]
# template for creating thousands of cars   ,,, class user can creat many users object 
# class instantiate =>> creat instance of a class ---#instance => object crested from class and have thier methods and attributes
# class define with key word CLASS -- ,, class name witten with Pascalcase or[UpperCamalCase]style
# class may contain methods and attributes or not 
# generally everytime when you make object from the class PYTHON look for =>> built in function (__init__) and call it 
#(__init__)=>  initialize make prepare data to creat the object  
# any method contain with two underscore in  start and end (__method__) =>> called =>>> Dunder or Magic method
# (self)=>> must be first pramater refer to the current instance created from the class ;can named any thing
                                    # syntax 

class Member:                #class => keyword,,,,,,member => class name
    def __init__(self):        #=>>> constructor[instantiation(creat instance from a class)]each instance is seperate objectd =>>> def __int__(self,other_data)
        print('A New Member Has Been Added')                     # Body of function 

# Member()                # =>> object 
# Member()                # =>> object 

V1=Member()               #instance member(argument)
V2=Member()               #instance
print(V1.__class__())     #=>> لو حبيت تعرف البيانات دي تبع الكلاس المعين

print('$'*40)
# instance attribute defind inside the constructor
# class Queen:
#     def __init__(self) :          #  self=>> point to instance creat from class
#         self.people='fady'        # instance attribute defind inside the constructor

# guy_one = Queen()
# guy_two = Queen()
# guy_three = Queen()
# # print(dir(guy_one ))  # will find people in it because people will be its attribute
# print(guy_one.people)      #to access attribute

# class Queen:
#     def __init__(self, any_thing) :          
#         self.people= any_thing          #constructor
# guy_one = Queen('fady')                 #instance
# guy_two = Queen('emad')                 #instance
# guy_three = Queen('hossam')             #instance
# # print(dir(guy_one )) 
# print(guy_one.people)      
# print(guy_two.people)     
# print(guy_three.people)      

# Instance method =>> take self pramater to poit instance ,,may have more than pramater like function 
# can access attribute and methods on the same object ,, can access the class itself


####   there attribute in class but locate outside construct

###  Class method =>> marked with @classmethod to flag it as class methods ,,it take CLS pramater not self to point the class
# it deosn't require to creat class instance to run ,, use when you do soething with the class itself ,,,,related by class attribute

###  static method: =>> it doesn't  take pramater  ,, it bound to the class not instance 
#  use when you do something relate by the class without access to the object or class,,,, NOT related by class attribute

class Queen:

    not_allowed_names=['shit','hell','baloot']              #=>> attribut relate by the class itself
    users_num=0                                             # =>> arrtibute class need instance method or instance attibute and instance

    @classmethod                                             
    def c_meth(cls):
        print( f'we have {cls.users_num} user in our system ')

    @staticmethod
    def say_hello():
        print('hello from static method')

    def __init__(self, any_thing,every_thing,some_thing,gender) :       # >>>>>>>>>>>>>> the bigenning of construct
        self.a_people= any_thing            #  a_people =>>atribut instance name
        self.e_people= every_thing          # attribute instance
        self.s_people= some_thing          #
        self.g_people= gender
        Queen.users_num +=1

## methods access attributes
    def full_name(self):                 # >>>> fullame =>>> method instance
        if self.a_people in Queen.not_allowed_names:
            raise ValueError('this name is forbeden')
        else:
            return f'{self.a_people} {self.e_people} {self.s_people}'        #  =>> instance ,, a_people=>>attribute name

    def hello(self):
        if self.g_people == 'male':
            return f'hello mr {self.a_people}'
        elif self.g_people == 'famle':
            return f'hiya ms {self.a_people}'
        else:
            print('gdgfggfgfg')

## methods access methods
    def acces_methd(self):
        return f'{self.hello()} ,and your full name is {self.full_name()}'
    def delete_user(self):
        Queen.users_num -=1
        return f'user {self.a_people} deleted'


print(Queen.users_num)      #class attribute
guy_one = Queen('fady','muhammed','ahmed','male')                 #instance =>>  guy_one =>> instance name
guy_two = Queen('emad','suliman','saeed','male')                 #instance
guy_three = Queen('mona','sayed','omer','famle')             #instance
guy_four = Queen('shit','hell','zewo','neow')             #instance
print(Queen.users_num)         #class attribute
# print(dir(guy_one )) 

# print(guy_one.a_people,guy_one.e_people,guy_one.s_people)       =>>print attributes instance
# print(guy_two.s_people)     
# print(guy_three.e_people)   
     
# print(guy_three.full_name())     #=> print method(instance.method name)
print(guy_three.hello())
print(guy_three.acces_methd())     # take place behind the seine =>> print(Queen.acces_methot(guy_three))
print(guy_three.delete_user())
print(Queen.users_num)                                  # print class attribute
# print(dir(Queen))
Queen.c_meth()                                          # print class methods
Queen.say_hello()



###--------------------- MAGIC METHODS -------------------

# my_string='muhammed'
# print(type(my_string))    #=>> will return class str so (str,int,float,list,dict---)is class and have methods
# so my_string is (constractor) from (str)    =>> print(str.title(my_string))
# print(my_string.__class__)
# print(dir(str()))    # to know the method in the class (str) =>> print(dir(type)) ,, print(dir(int))
# print(dir(skill))
# print(str.title(my_string))    # this what happen in the background
# --------------------------------------------------------
# __init__  called automatically when instantiating class or when constructe a new object 
# self.__class__  belong to the instnce
# __str__ =>> give you humanreadable output of the object
# __len__ =>> return length of the container called when use built in len() function on the object
# class skill:
#     def __init__(self):
#         self.skills =['Html','Css','Js']

#     def __str__(self):                      #  without do print will give human readable output
#         return f'this is my skills {self.skills}'

#     def __len__(self):                       #return length of the container in the output         
#         return len(self.skills)


# profile=skill()                    #  >>>>>instance
# print(profile)
# print(len(profile))
# profile.skills.append('Java')
# print(len(profile))
# print(profile.__class__)            #>>>>>>>>> to know which class this instance belong

###-----------------Inheritance------------------------####---------------------------------
# can inherit everything from the Headquerter class to Derived class by put name of the class notice below
#=>> class branches (headquerter),,,,,,supper().__init__(the name of headquerter pramater ,or more)
# branch class make override in the headquerter one  ,,, if have method to make override => make copy it in the branch one
# if you have trait or method exceed in the branch class =>> make normal attribute without inheritance
class food :                            # Headquerter class
    def __init__(self,name,price):
        self.name=name
        self.price=price
        print(f'food is created from the base class {self.name}')

    def eat(self):
        print('eat method from main class')



class Apple (food):                            # Derived class
    def __init__(self,name,price, color):           # add pramater that you import from the headquerter
        # food.__init__(self, name)    # =>> inherit  like =>> self.name=name
        super().__init__(name,price)              # =>> inherit for basic one
        self.color=color
        print(f'\"{self.name}\" apple is created from the derived class \"{self.price}\" and its color is \"{self.color}\"')

    # def eat(self):            # to inherit the method and override the main one
        # print('eat method to overrid the first one')


# food_one=food('pizza')                   # instance the headquerter
food_two=Apple('burger' ,250 ,'black')
# food_two.eat()     # to access method in class one => the same instance ane the name of the method

print('*'*50)

class base_one :
    def __init__(self):
        print('base one')

    def func_one(self):
        print('one')
class base_two :
    def __init__(self):
        print('base one')
    def func_two(self):
        print('two')

class derived (base_one,base_two):
    pass

my_var=derived()                    # =>> instance
my_var.func_one()    # =>> to access method in heritance =>>the same instance and the name of the method
my_var.func_two()       # =>> to access method in heritance

# print(my_var.func_one)    # to which class bound (func_one)
# print(derived.mro()) # => mro =>> method resolution order  => to know the order of methods


class base:
    pass

class derived_two(base):
    pass

class derived_three(derived_two):   # will inheritance "base","derived_two"
    pass

###------------- Polymorphism(miniforms)-----------------###-----------------------------------
# method do task in place and the same method do another task in another place
print(len([1,2,3,4,5]))  # => len()
print(len('muahmmed'))   #=> len()
print(2+8+10)                    # => +
print('Gmal'+' '+'Hossam')       # => +

class A:
    def do_something(self):
        print('From class A') # => to do Implement at any class  =>> raise error
        raise NotImplementedError('dervied class must inplement this method')

class B(A):
    pass

class C(A):                      #to inherit the method and the new one override the main one
    def do_something(self):
        print('Now there are not raise error')  #Therefore do_something is >> Polymotphism << do differrnt action in different place
my_instance = C()
my_instance.do_something()


#------------------------Encapsulation-------------------------------
# restrict access to the data stored in method and attributes
#-----PUBLIC----every attributes and method we used in class so far  ,can modified ,and run from anywhere inside or outside the class
#----PROTECTED--attributes and method prefixed with one underscore(_) can be access withen CLASS or SUB CLASS
#----PRIVATE---- attributes and methods prefixed with two underscore(__) access withen the CLASS and OBJECT  can not be modified
# Attributes == Variables == Properties
# class Member:
#     def __init__(self,name):
#         self.name=name   #public

# my_instance=Member('memdouh')
# print(my_instance.name)
# my_instance.name='glal'     # can be modified
# print(my_instance.name)
#---------------------------------------------------------------------------------------------------
# class Member:
#     def __init__(self,name):
#         self._name=name   #proticted

# my_instance=Member('memdouh')
# print(my_instance._name)
# my_instance._name='glal'     # can be modified
# print(my_instance._name)
#--------------------------------------------------------------------------------------------------
class Member:
    def __init__(self,name):
        self.__name=name   #Private
    def say_hello(self):
        return f'Hello {self.__name}'

my_instance=Member('memdouh')
# print(my_instance.__name)     # Error =>>> cannot  access outside the class
print(my_instance.say_hello())   # access withen the class
print(my_instance._Member__name) # will print private(__)as public from outside the class ==>> wron way
my_instance._Member__name='sayed'# =>> will modified on private but wrong way =>>> will make it no private

# the write way by use=>>>>------ GETTER----------------- SETTER
class country:
    def __init__(self,city):
        self.__village=city

    def get_village(self):       # =>> method getter
        return self.__village

    def set_village(self,new_city):  # =>> set (modified)
        self.__village=new_city


one=country('Cairo')
print(one.get_village())   #=>>>>> get method out the class by right way 
one.set_village('Alex')    # to make set or (modified)
print(one.get_village())   # get after set 


#----------------------------------------@ Property decerator----------------------------------------------------
# if a method in the class just contain (self) can call as @properaty"attribute"
class member:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hello(self):
        return f'hello {self.name}'
    @property
    def age_days(self):
        return self.age*365

d=member('muhammed',30)
print(d.age)
print(d.say_hello())
# print(d.age_days())   # =>> normal callable for method   
print(d.age_days)     # =>> @ a property decerator callable as a normal attribute 

#------كلاص مجرد---- ABC=>>>>> Abstract base class---------------=> as a pattern class or method to trace it 
# class called abstract class if it has one or more abstract methods  => to make the inheatinc class follow it
# 'abc' [module] in python provide infrastructureto define custom abstract base classes
# by adding @abstractmethod decorator on the method ,,, 'ABCMeta' class is used to define abstract base class
from abc import ABCMeta ,abstractmethod
class programming(metaclass=ABCMeta):   # add this to the basic class to make it as a pattern
    @abstractmethod
    def has_oop(self):
        pass                # =>> desont do any thing just as a pattern so write "pass" as abstract function

    @abstractmethod
    def n_ame(self):
        pass

class python(programming):
     def has_oop(self):
        return 'Yes'

    #  def n_ame(self):         #=>>> follow abstractmethod (n_ame)
        #  return 'ddddddddddddddd'

class pascal(programming):      #=>>> follow abstractmethod (has_oop)
    def has_oop(self):
        return 'No'
    def n_ame(self):
        pass
# o=programming()      =>>> will give ERROR because call abstract class or method
# print(o.has_oop())   =>>> will give ERROR because call abstract class or method

one=pascal()           # when call class must be have all method as abstract class
print(one.has_oop())  
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
### ------------------Databases------------####---------------------
# database is a place where we can store data ,, then organized data into =>tables   every table has=> columns ,, every culmns has=> rows
# there many types of databases =>> (MongoDB, MySQL, SQLite)
# SQL stand for =>>>>> structured Query Language
# SQLite =#>>>>> can run in memory or in a single file
# data inside database has types(integer,text,date)

# ----------------Creat & Conect--------------------------
# import sqlite3
# db = sqlite3.connect('app.db') #=>>>>>>>>>>db extention for database =>> will creat app in workplace   =>> emerge place
#------------------creat the tables and culmns-------------
# db.execute('Create Table if not exists skills(name text ,progress integer,user_id integer)')
#  # => to define the sort of data add extention like name=>text---
# # =>>>> "creat table"=>> QUERY in SQL ,, "skills" =>>variable
# # if not exists  =>>>>>must writ this message before Data to prevent ERROR
# # app.db=>>>place contain data,,,,,,,Create Table if not exists =>>> query,,,,skills=>>>>table,,,,name text ,progress integer,=>>>culmns

# #------------------------Cursor-------------------------------insert data into database
# #  =>>> all operation in SQL done by cursor not connection .,,by cursor can do more than task in the sametime
# #-----------------------------Commit---------------------save all changes
# cr = db.cursor() # => creat varaible control cursor method now you can use this variable to excute commands
# cr.execute('Create Table if not exists skills(name text ,progress integer,user_id integer)')
# cr.execute('create table if not exists users (users_id integer , name text)')
# #--------------------inserting data----------------------insert inside the culmns
# # cr.execute('Insert Into users(users_id ,name) values(3,"ahmed")')  #=>> (3,"ahmed")=>> ROWS
""" can i remove the first palences and start from valeus"""
# # cr.execute('Insert Into users(users_id ,name) values(6,"shaban")') # notice the change of doublequets inside singlequets
# cr.execute('Insert Into skills(name  ,progress ,user_id ) values(9,"telb","yussf")')

# my_list=['muhammed','shaban','telb','hilal','gmaal','bassam','mansour']
# for key,user in enumerate(my_list):
#     cr.execute(f'Insert Into users(users_id ,name) values({key+1} ,"{user}")') #=>this string has query but treat all as string
""" can  i offset formating by replace key , user with (?,?)',(key,user)"""
# db.commit()     #=>> must save changes after inserting

# # --------------------------close---------------
# # db.close() # =>>>> must close connection database after finnish

# # #---------------------------------------------------------------------------------
# # # --------------------------------------Retrieve or fetchجلب او استرجاع data from database------------------
# # cr.execute('select name from users') 
# # fetchone=>>>> returns asingle row or none if no more rows are available
# # fetchall=>>>> returns all rows as a list evry row is tuples  or an empty list if no more rows are available
# #fetchmany(size)

#---------------------update----------------delete---------------------------
# cr.execute('Create Table if not exists skills(name text ,progress integer,user_id integer)')
# cr.execute('create table if not exists users (users_id integer , name text)')

# cr.execute('Insert Into users(users_id ,name) values(3,"ahmed")') # => notice everytime you run during the unserting will repeate the run again
# cr.execute('Insert Into users(users_id ,name) values(6,"shaban")') # notice the change of doublequets inside singlequets
# cr.execute('Insert Into users(users_id,name ) values(9,"telb")')
#------------------------------update happen in row--------------
# cr.execute('update users set name = "job" where users_id=3') #=>>will change name to job

# can i add data during the DB browser by inser bottom then apply then write changes
#------------------------------delete also happen in row not colmns-----------
# cr.execute('delete from users where users_id=6 ') 
# cr.execute('select name from users')    #=> select culmn from table
""" can identify where in select according => where user_id IN (tuble),=> or where user_id not in (1,2).
,,or select from user order by user_id, user_id desc , user_id asc ,name limit4 , name limit 4 offset 2=> , user_id > 1, or > 1 and < 4"""
# # print(cr.fetchone())
# # print(cr.fetchone())
# # print(cr.fetchone())
# # print(cr.fetchone())          #=>>> return none because there are no more 

# print(cr.fetchall())  #==== cr.execute('select name from users')can write users_id, name or write * instead
# db.commit()

# def database_exame():
#     try:
#         db=sqlite3.connect('app.db')
#         print('connected to database seccessfuly')
#         cr=db.cursor()
#         cr.execute('select * from users')
#         # assign data to variable
#         my_result=cr.fetchall()   #=>> print (my_reslut[0])
        
#         # print number of rows 
#         print(f'Database has {len(my_result)} row')
#         print('showing data')

#         # loop on results
#         for me ,you in enumerate(my_result):
#             print(f'{me+1} - user id =>> {you[0]} ,,', end= ' ')
#             print(f'and the name =>>> {you[1]}')

#     except sqlite3.Error as er:
#         print(f'there ERROR {er}')

#     finally:
#         if (db):
#             db.close()
#             print('connection to database is closed')

# database_exame()

# #------------------------------------ prectical test-----------
# input_message='''what do you want ? 
# "s" => show skills
# "a" => add skill
# "d" => delete skill
# "u" => update skill
# "q" => quit the app
# Choose option :  
# '''
# import sqlite3
# db = sqlite3.connect('app.db')
# cr=db.cursor()
# # commit and closd method =>>>>>put commit and closed in one method to control whenever i want
# def commit_and_closed():
#     db.commit()
#     db.close()
#     print('connection to database closed')
# #my user ID
# usr=1

# user_input=input(input_message).strip().lower()
# #commands list
# commands_list=['s','a','d','u','q']
# #define the methods
# def show_skill():
#     # cr.execute(f'select * from skills where user_id = {usr} ')
#     # cr.execute(f'select * from skills where user_id > {usr} ')# => wherever user_id you want
#     cr.execute(f'select * from skills order by user_id = {usr} asc ') #=>> order as you like 
#     you = cr.fetchall()
#     print(f'you have {len(you)} skills')
#     if len(you)>=1:
#         print('showing skill')
#     for h, my in enumerate(you):
#         print(f' {h+1} = my skill =>> {my[0]}')
#         print(f'and my progress =>> {my[1]}')
#         print(f'and my user_id =>> {my[2]}')
#     commit_and_closed()
    
# def add_skill():
#     nam=input('write skill name: ').strip().capitalize()
#     cr.execute('select name from skills where name = (?) and user_id = (?)',(nam,usr))
#     result=cr.fetchone()
#     if result == None: #=> there is no skill you can add it
#         print('the skill is not exist you can add it')
#         prog=input('write skill progress: ').strip()
#         cr.execute(f'insert into skills values("{nam}",{prog},{usr})') # skip => (name,progress,user_id)
#         commit_and_closed()
#     else:
#         option = input('sorry the skill is already exist ,, \n Do you want to update or delete : ')
#         if  option == 'update':
#             update_skill()
#         elif option == 'delete':
#             delete_skill()
#         else:
#             raise ValueError('wrong input')
#     '''notice below make query as string formmating => this is not fortified way in database'''
    

# def delete_skill():
#     nam=input('write skill name: ').strip().capitalize()
#     # cr.execute(f'delete from skills where name = "{nam}" and user_id={usr}') #=>>must defined user_id 
#     cr.execute('delete from skills where name = (?) and user_id= (?)',(nam,usr)) #=>>must defined user_id ,,(?) => to offset the injection query
#     commit_and_closed()    

# def update_skill():
#     # prog=input('write the new skill progress: ').strip()
#     nam=input('write skill name: ').strip().capitalize()
#     cr.execute(f'update skills set progress =  "{prog}" where name="{nam}" and user_id={usr}') #=>>must defined user_id 
#     # cr.execute(f'update skills set name =  "{nam}"  where user_id={usr}') #=>>must defined user_id    =>> 
#     commit_and_closed()    


# def quit_skill():
#    exit()

# if user_input in commands_list:
    
#     if user_input == "s":
#         show_skill()
#     elif user_input == "a":
#         add_skill()
#     elif user_input == "d":
#         delete_skill()
#     elif user_input == "u":
#         update_skill()
#     else:
#         print()

# else:
#     print(f'sorry command \"{user_input}\" is not found')


#