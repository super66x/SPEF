#this tool was written by super66x
#https://github.com/super66x/SPEF
import py_compile
import marshal
import os
logo =''' 

███████╗██████╗ ███████╗███████╗
██╔════╝██╔══██╗██╔════╝██╔════╝
███████╗██████╔╝█████╗  █████╗  
╚════██║██╔═══╝ ██╔══╝  ██╔══╝  
███████║██║     ███████╗██║     
╚══════╝╚═╝     ╚══════╝╚═╝     
                                 
                         
++++++++++++++++++++++++++++++++++++++++
github: https://github.com/super66x/SPEF
++++++++++++++++++++++++++++++++++++++++
'''
choose =''' ######################################
1_marshal 
2_py_compile
3_exit the tool
######################################'''
print(logo)
print(choose)
def marshal_enc():
    os.system('clear')        
    os.system('cls')
    print(logo)
    file = input("Enter your tool to Encrypt : ")
    new_file =input("output name : ")    
    openfile =open(file,'r').read()
    com =compile(openfile,'','exec')
    encrypt =marshal.dumps(com)
    enc =open(str(new_file),'w')
    enc.write('import marshal \n')
    enc.write('exec(marshal.loads('+repr(encrypt)+'))')
    print(f'the file was encrypted |file saved as {new_file}')

def py_compile_enc():
    os.system('clear')
    os.system('cls')
    tool = input("Enter your tool to Encrypt : ")
    py_compile.compile(tool)

again =0
while True :
    if again >= 1 :
        os.system('clear')        
        os.system('cls')
        print(logo)
        print(choose)
        
    ask =input("Enter :")
    if ask == '1':
        marshal_enc()
        again =again+1
    elif ask == '2':
        py_compile_enc()
        again =again+1
    elif ask == '3':
        break ;
        again =again+1
    else :
        print("the input is invaild")
       
