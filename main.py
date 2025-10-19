
try:
    import os
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from datetime import datetime
    import tkinter as tk
    from tkinter import simpledialog, messagebox
    import json
    import qrcode
    import flask
    from flask import request, jsonify
except Exception as e:
    messagebox.showerror("错误", f"导入模块时发生错误：{e}\n\
                         请下载最新的release版本后重试\n\
                             或者联系开发者并截图本页面\n\
                             你也可以尝试直接编译源文件\n\
                             有可能是pyinstaller特性发力了（bushi）\n\
                             记得在目录下运行pip install -r requirements.txt\n\
                             当前版本：{VERSION}")
    exit(1)
messagebox.showinfo("欢迎使用", "正在初始化，请稍等...")
VERSION = json.load(open("config.json"))["version"]
def init():
    windows = tk.Tk()
    windows.withdraw()
    windows.geometry("800x800")
    # Set codec to utf-8 so that we can use Chinese on Linux or Mac
    windows.encoding = "utf-8"
    windows.title(f"中国铁路电子报销凭证生成器({VERSION})")

    # Create menu
    menu = tk.Menu(windows)
    windows.config(menu=menu)
    
    if json.load(open("config.json"))["uimode"] == "default":
        # Create file menu
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="文件", menu=file_menu)
        file_menu.add_command(label="退出", command=exit(0))
        # Create help menu
        help_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="帮助", menu=help_menu)
        help_menu.add_command(label="关于", command=lambda: messagebox.showinfo("关于", f"中国铁路电子报销凭证生成器({VERSION})\n\
                                 开发者：@CRTianyu 工作室\n\
                                 联系开发者：https://github.com/CRTianyu\n\
                                 项目地址：https://github.com/CRTianyu/tvmcr"))
        file_menu.add_command(label="打开json文件", command=lambda: messagebox.showinfo("打开json文件", "暂未实现"))
        file_menu.add_command(label="保存json文件", command=lambda: messagebox.showinfo("保存json文件", "暂未实现"))
        file_menu.add_command(label="")
    
        # Create settings menu
        settings_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="设置", menu=settings_menu)
        settings_menu.add_command(label="经典UI", command=lambda: json.dump({"uimode": "default"}, open("config.json", "w")))
        settings_menu.add_command(label="国铁TVM UI", command=lambda: messagebox.showinfo("国铁TVM UI", "暂未实现"))
    elif json.load(open("config.json"))["uimode"] == "tvm":
        
        # Use Flask to display the UI
        # Use Flask to display the UI
        app = flask.Flask(__name__)
        @app.route('/')
        def index():
            return open("index.html", "r", encoding="utf-8").read()
        
        # Start the Flask server
        app.run(debug=True, host='0.0.0.0', port=14514)
    else:
        messagebox.showerror("错误", f"配置文件中的uimode参数错误：{json.load(open('config.json'))['uimode']}\n\
                         请将其修改为default或tvm\n\
                             当前版本：{VERSION}")
        exit(1)

init()