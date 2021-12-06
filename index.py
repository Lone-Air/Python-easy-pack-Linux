#!/usr/local/bin/python3
# Auther: 碳酸氢钠
# Changed by: laman28(LMFS)
# For linux
import os
import time
import sys

def pack(clearVenv=False):
    if clearVenv:
        os.system("rm -rf pyvenv-easypack")
        os.system("rm -rf build")
        os.system("rm *.spec")

    if(not os.path.isdir("./pyvenv-easypack")):
        start_time = time.time()
        print('正在创建python venv虚拟环境……(大约需要15s)')
        if os.system('python -m venv ./pyvenv-easypack'):
            raise Exception("创建虚拟环境时出现错误。")
        print(f'创建完成。用时：{time.time()-start_time}s')
    else:
        print("[\033[92;1mINFO\033[0m] Python virtual environment was already in the directory")

    if(os.path.exists("./.PYI.insd")):
        if(os.path.isfile("./.PYI.insd")):
            f=open("./.PYI.insd")
            has_pyi=f.read()
            if(has_pyi=="1"): has_pyi=True
            else:             has_pyi=False
        else:
            os.system("rm -rf ./.PYI.insd")
            f=open("./.PYI.insd","w")
            has_pyi=False
    else:
        f=open("./.PYI.insd","w")
        has_pyi=False
    if(not has_pyi):
        start_time = time.time()
        print('安装pyinstaller到虚拟环境……')
        if os.system('pyvenv-easypack/bin/pip install pyinstaller'):
            raise Exception("安装出现错误。")
        print(f'安装完成。用时：{time.time()-start_time}s')
        f.write("1")
        f.close()
        has_pyi=True
    else:
        print("[\033[92;1mINFO\033[0m] Pyinstaller was already in pyvenv_easypack/lib")

    

    start_time = time.time()
    print("安装其他第三方库……")
    for i in modules:
        print("安装第三方库："+i)
        if os.system('pyvenv-easypack/bin/pip install '+i):
            raise Exception("安装出现错误。")

    
    start_time = time.time()
    print('打包'+pyFileName+"……")
    pack_command = 'pyvenv-easypack/bin/pyinstaller -F '
    if needConsole!="1":pack_command += '-w '
    if iconURL!='':pack_command += '-i '+iconURL+' '
    if os.system(pack_command+pyFileName):
        raise Exception("打包时出现错误。请重试。")



clearVenv = False
if input("是否希望重置虚拟环境？如果是请输入1，不是请直接回车。") == "1":clearVenv = True
pyFileName = input("请输入要打包的.py文件名或路径。请添加.py后缀。\n- ")
iconURL = input("是否需要程序图标？如果是，请输入图标路径；不是，请直接回车。")
needConsole = input("是否需要控制台？如果是，请输入1；不是，请直接回车。(注:如果你的程序不需要控制台的输入输出，那么强烈建议开启此选项以优化体验。)")
haveModules = input("源代码是否包含有第三方库？如果有，请输入1；如果没有，请直接回车。")


modules = []
if(haveModules=="1"):
    way_to_pack_modules = input("你想要如何安装第三方库？手动输入，请输入1；自动检索，请直接回车。")
    if(way_to_pack_modules == "1"):
        i=-1
        while True:
            modules.append(input("键入第三方库名称。结束请键入“[end]”(不带双引号)。"))
            i+=1
            if modules[i] == '[end]':
                break
        modules.pop()
    else:
        print('功能正在开发中，暂时无法使用。')

start_time = time.time()
pack(clearVenv)
print(f"打包成功！\n\
    共用时：{time.time()-start_time}s\n\
    文件在/dist文件夹下。")

