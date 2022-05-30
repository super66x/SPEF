#version 1.1.2
#this tool was written by super66x
#https://github.com/super66x/SPEF
#libaraies
import py_compile
import marshal
import os
import time
import sys 
#colours
gery = '\033[1:30m'
red = '\033[1;31m'
green = '\033[1:32m'
yellow = '\033[1:33m'
blue = '\033[1;34m'
purple = '\033[1;35m'
cyan = '\033[1;36m'
white = '\033[1;37m'
#write function
def type(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0005)
#logo
logo =f''' 
{green}
███████╗██████╗ ███████╗███████╗
██╔════╝██╔══██╗██╔════╝██╔════╝
███████╗██████╔╝█████╗  █████╗  
╚════██║██╔═══╝ ██╔══╝  ██╔══╝  
███████║██║     ███████╗██║     
╚══════╝╚═╝     ╚══════╝╚═╝     
                                 
{purple}                           V1.1.0                         
{red}++++++++++++++++++++++++++++++++++++++++
{yellow}github{red}:{cyan} https://github.com/super66x/SPEF
{red}++++++++++++++++++++++++++++++++++++++++
'''
#choose
choose =f'''{green}######################################
{yellow}1_marshal 
2_py_compile
3_exit the tool
{green}######################################'''
os.system('clear'or 'cls')
type(logo)
type(choose)

def marshal_enc():
    os.system('clear'or 'cls')
    type(logo)
    file = input(f"{yellow}Enter your tool to Encrypt :{cyan} ")
    new_file =input(f"{yellow}output name :{cyan} ")    
    os.chdir('output')
    openfile =open(file,'r').read()
    com =compile(openfile,'','exec')
    encrypt =marshal.dumps(com)
    enc =open(str(new_file),'w')
    enc.write('import marshal \n')
    enc.write('exec(marshal.loads('+repr(encrypt)+'))')
    print(f'{yellow}the file was encrypted |file saved as {red}{new_file}')

def py_compile_enc():
    os.system('clear' or 'cls')
    type(logo)
    tool = input(f"{yellow}Enter your tool to Encrypt :{cyan} ")
    os.chdir('output')
    py_compile.compile(tool)

again =0
while True :
    if again >= 1 :
        os.system('clear'or'cls')
        type(logo)
        print(choose)
        
    ask =input(f"{yellow}Enter : {cyan}")
    if ask == '1':
        marshal_enc()
        again =again+1
    elif ask == '2':
        py_compile_enc()
        again =again+1
    elif ask == '3':
        os.system('clear'or'cls')
        break ;
        again =again+1
    else :
        print(f"{red}the input is invaild")
       
