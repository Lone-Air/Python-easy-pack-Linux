# python-easy-pack For Linux/Unix, Changed by laman28

Original version of windows: 
https://github.com/shr-NaHCO3/python-easy-pack

make pack up python files easier.

# 如何使用?
1. Install: Download the .zip archive then decompress or use 'git clone https://github.com/Lone-Air/Python-easy-pack-Linux.git' in your terminal
1. 打开你的terminal
3. 切换到程序所在目录，输入`python index.py`来运行程序。当然，你直接输入运行./index.py也无妨。
4. 按照要求输入。请注意：目前安装第三方库的功能还未完全完善（一点也不银杏），如果需要第三方库，建议手动在`./pyvenv-easypack/bin`目录里使用pip命令安装第三方库。
5. 请认真查看每一条要求输入的信息。这很重要，直接关乎打包的成功与否。
6. 打包完成并显示成功信息后，你可以在`./dist`文件夹里找到你想要的东西。

# New
1. Program won't always create the python virtual environment
2. Program won't always check for pyinstaller
