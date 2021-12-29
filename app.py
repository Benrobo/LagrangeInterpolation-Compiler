import os
import subprocess
import pyfiglet
from util.index import *

fig = pyfiglet 

# print compiler title
print(fig.figlet_format("LangComp", font='big'))

# show compiler options

options = """
    Welcome To Langrange Compiler
    
    -r --run : run and compile java codes

    -l --langrange : compile the LagrangeInterpolation
    
    -c-f --create-file: create a file 

    -cc-f --compile-file : compile the codes written in that file.

    -h --help : get some useful informations about this compile
"""

print(options)

print("")
print("Enter some options from the info above")

dirname = os.getcwd()
child_dir = os.path.join(dirname)
parent_dir = os.path.normpath(child_dir)


# get java compilers

def getJavaCompiler():
    data = os.listdir(parent_dir + "/executable")
    return {"java": data[0], "javac": data[1]}

def createJavaFile(filename, code="", extension="java"):
    # check if temp folder is available
    # cause that were all java files would be created

    newDir = f"{parent_dir}/temp"
    

    if os.path.isdir(parent_dir + "/temp") == False:
        # create new directory
        os.mkdir(newDir)
        print("directory created")

    # after making a new directory
    # create a file
    fileName = f"{filename}.{extension}"
    fileDir = os.path.join(newDir, fileName)
    
    # write data to that file
    
    f = open(fileDir, "w")
    f.write(code)
    f.close()
    
    print("")
    
    return { "fileDir": fileDir, "filename": fileName }


def compileJavaCode(filename, code = "", ext="java", cb=None):
    
    compilers = getJavaCompiler()
    filedata = createJavaFile(filename, code, ext)
        
    java = compilers["java"]
    javac = compilers["javac"]
    fileDir = filedata["fileDir"]
    fileName = filedata["filename"]
    
    command = f"cd {parent_dir}/temp && {java} {fileName}"
    
    output = {}
    
    compilerResult = subprocess.run(command, shell=True)
    
    output["output"] = compilerResult
    
    return output

def createFile():
    # ask the user the file to create
    filename = input(f"Enter just the name of the java file you would like create, for eg Kola, Main, Test.:- ")

    if filename == "" or filename == None:
        print("Cant create empty file.")
        return

    defaultCode = """
    // write your java codes here..
    """
    createJavaFile(filename, defaultCode, "java")
    
    print("")
    print(f"The given filename {filename} was created succesfully, you can now write your java codes in the file")
    print("")
    return

# compile the code within a given file

def compileCodeWrittenInAFile():

    compilers = getJavaCompiler()
    fileDir = f"{parent_dir}/temp"
    fileInput = input("Enter the name of the file you wanna compile:- ")

    if fileInput == "" or fileInput == None:
        print("Input given is empty, please enter a valid input.")

    # check if file exist
    chk = os.path.isfile(f"{fileDir}/{fileInput}")

    if chk == False:
        return print(f"""
            File given doesnt exist at: {fileDir}/{fileInput}
            please enter a valid file name.
        """)
    
    print("Compiling......")
    
    # compile java code from the file name provided
    java = compilers["java"]
    command = f"cd {parent_dir}/temp && {java} {fileInput}"
    compilerResult = subprocess.run(command, shell=True)


    return compilerResult

def compileLagrangeInterpolation():
    # get the java compiler exe file 
    compilers = getJavaCompiler()    
    
    java = compilers["java"]
 
    command = f"cd {parent_dir}/temp && {java} LagrangeInterpolation.java"
    
    compilerResult = subprocess.run(command, shell=True)
    
    return compilerResult


 
def runCompile():
    # get the filename user wanna create
    print("")
    print("Provide the name of the file you wanna create without having extensions")
    filename = input()
    # get muli-line input from users
    userInputs = Input("Write some java codes here..")
    output = compileJavaCode(filename, userInputs, "java")
    print("")
    print(output["output"])
    print("")
    print("Continue or pres ctrl+c to quit")

def init():
    userOpt = input()

    if userOpt == "-h" or userOpt == "--heplp":
        return print(options)
        
    elif userOpt == "-r" or userOpt == "--run":
        return runCompile()
    elif userOpt == "-l" or userOpt == "--langrange":
        return compileLagrangeInterpolation()
    elif userOpt == "-cc-f" or userOpt == "--compile-file":
        return compileCodeWrittenInAFile()
    elif userOpt == "-c-f" or userOpt == "--create-file":
        return createFile()
    else:
        return print("Sorry, command enter isnt valid, try again.")
    
while True:
    init()
    
    