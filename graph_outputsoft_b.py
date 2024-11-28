import txt_printcode_b as printcode
from tkinter import*
import pandas as pd
import matplotlib.pyplot as plt
import os
import PySimpleGUI as sg

sg.theme('LightBlue3')

fileinput = sg.InputText(key='filepath', default_text="ファイルパス", enable_events=True, font=("",15), size=(50, 50))
fileselect = sg.FileBrowse('ファイルを選択', key='filebtn', target="filepath",enable_events=True)
do_btn = sg.Button("実行", key="do_btn", enable_events=True)

radiobuttons = sg.Text("")
contents = {}
frame_contents =[
    sg.Image('default_picture.png', key='-Canvas-1'),
    sg.Image('default_picture.png', key='-Canvas-2'),
    radiobuttons,
    sg.Button("選択", key="radio_btn_indicate", enable_events=True)]

selector = [
    sg.Checkbox("line",key="checkbox_line",pad=(130,0),enable_events=True),
    sg.Checkbox("bar",key="checkbox_bar",pad=(170,0),enable_events=True)
]

output = [
    sg.Button("出力", key = "output_btn",pad=(500,0),enable_events=True)
    ]

layout = [[fileinput,fileselect,do_btn],
          [sg.Column([frame_contents])],
          [selector,output]]

window = sg.Window('txtデータグラフ化ソフト', layout, resizable=True)


filepath_and_filename = None
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        print("exit")
        break

    if event =="do_btn":
        print(values["filepath"])
        if filepath_and_filename != values["filepath"]:
            #データ用意
            filepath_and_filename = values["filepath"]
            filepath_splited = filepath_and_filename.split("/")
            filename = filepath_splited.pop()
            filepath = ""
            for i in filepath_splited:
                filepath += i + "/"
            contents_orig = printcode.txt_print(filename,filepath) #実行フォルダの位置に画像生成、項目のリストを返す

            memory = {}
            for x in contents_orig:
                memory[x] = [0,0]
            print(memory)

            #gui
            
            for i in range(len(contents_orig)):
                contents[i] = contents_orig[i]

            newradiobuttons = []
            for item in contents.items():
                newradiobuttons.append([sg.Radio(item[1], key=item[0], group_id='0')])
            
            window.extend_layout(radiobuttons,newradiobuttons)

            pass
        else:
            pass

    if event == "radio_btn_indicate":
        for x in range(len(contents_orig)):
            if values[x]:
                i = contents[x]
        window["-Canvas-1"].update(source=f"time_{i}(line).png")
        window["-Canvas-2"].update(source=f"time_{i}(bar).png")
        if (memory[i])[0] == 1:
            window["checkbox_line"].update(True)
        else:
            window["checkbox_line"].update(False)
        if (memory[i])[1] == 1:
            window["checkbox_bar"].update(True)
        else:
            window["checkbox_bar"].update(False)

    if event == "checkbox_line":
        if values["checkbox_line"]:
            for x in range(len(contents_orig)):
                if values[x]:
                    i = contents[x]
            memory[i][0] = 1
        else:
            memory[i][0] = 0
    if event == "checkbox_bar":
        if values["checkbox_bar"]:
            for x in range(len(contents_orig)):
                if values[x]:
                    i = contents[x]
            memory[i][1] = 1
        else:
            memory[i][1] = 0

    if event == "output_btn":
        os.chdir(filepath+f"/{filename.replace('.txt','')}_work")
        df = pd.read_csv(filename.replace("txt","csv"))
        for item in memory.items():
            if item[1][0] == 1:
                df.plot(x="time",y=item[0],kind="line",title=f"{item[0]}_line",grid=True) #折れ線型
                plt.savefig("time_"+item[0]+"(line)"+".png", dpi = 300, bbox_inches="tight") #データの保存　(名前, 解像度, なんかオプション)
            if item[1][1] == 1:
                 df.plot(x="time",y=item[0],kind="bar",title=f"{item[0]}_bar")#棒グラフ
                 plt.savefig("time_"+item[0]+"(bar)"+".png", dpi = 300, bbox_inches="tight") #データの保存　(名前, 解像度, なんかオプション)
        os.chdir(__file__.replace("graph_outputsoft_b.py",""))#このファイルの絶対パスを取得、ファイル名を除外して作業ディレクトリを移動
        os.chdir("preview")


window.close()

"""
timeが横軸のデータを一括出力モード
指定した縦軸、横軸、グラフ形式を出力モード
指定したデータを一つの画像データ(サブプロット)にして出力モード

範囲指定
"""
