from tkinter import*
import subprocess
from tkinter.filedialog import asksaveasfilename, askopenfilename
compiler=Tk()
compiler.title('My IDE')
file_address=''
def set_file_path(path):
    global file_address
    file_address=path
def run1():
    if(file_address==''):
        save_prompt=Toplevel()
        text=Label(save_prompt,text="Please save your code befor executing")
        text.pack()
        return
    command=f'python {file_address}'
    process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output,errror=process.communicate()
    output11.insert('1.0',output)
    output11.insert('1.0',errror)
def open1():
    address=askopenfilename(filetypes=[('Python Files','*.py')])
    with open(address,'r') as file:
        code=file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        set_file_path(address)

def save_as():
    address=asksaveasfilename(filetypes=[('Python Files','*.py')])
    with open(address,'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        set_file_path(address)
def save():
    if(file_address==''):
    
        address=asksaveasfilename(filetypes=[('Python Files','*.py')])
        with open(address,'w') as file:
          code=editor.get('1.0',END)
          file.write(code)
          set_file_path(address)
    else:
        
        with open(file_address,'w') as file:
         code=editor.get('1.0',END)
         file.write(code)
        
    
menu=Menu(compiler)
file=Menu(menu,tearoff=0)
file.add_command(label='Open',command=open1)
file.add_command(label='Save',command=save)
file.add_command(label='Save As',command=save_as)
file.add_command(label='Exit',command=exit)
menu.add_cascade(label='File',menu=file)
run=Menu(menu,tearoff=0)
run.add_command(label='Run',command=run1)
menu.add_cascade(label='Run',menu=run)

compiler.config(menu=menu)
editor=Text()
output11=Text(height=8)
editor.pack()
output11.pack()

compiler.mainloop()

