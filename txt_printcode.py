import change_to_csv as change
import pandas as pd
import matplotlib.pyplot as plt
import os

def txt_print(filename, file_path):
    os.chdir(file_path)
    os.makedirs(filename.replace(".txt","") + "_work", exist_ok=True)
    newfile_path = file_path + "/" + filename.replace(".txt","") + "_work"
    newcsvfile = change.chenge_to_csv(filename, file_path, newfile_path) #txtファイルの":"が","に変わったcsvファイルが生成され、そのファイル名が返ってくる
    df = pd.read_csv(newcsvfile)
#print(df)

    with open(newcsvfile) as file:
        contents = file.readline()
        contents = contents.replace("\n","")
        contents = contents.split(",")
    #print(contents)

    #df.plot(x="time",y="speed",kind="bar")

    contents = contents[1:len(contents)]
    #print(contents)
    os.chdir(newfile_path)
    for content in contents: 
        #df.plot(x="time",y=content,kind="bar") #これ消すとpltのほうもデータがなくなる　データの作成
        df.plot(x="time",y=content) #折れ線型 
        #plt.plot() #いらない？
        plt.savefig("time_"+content+".png", dpi = 300, bbox_inches="tight") #データの保存　(名前, 解像度, なんかオプション)
        #plt.show() #保存とは別でその場で示したいとき　ここだと一個ずつ書き出すごとに表示されるから賢明じゃないかも
        #plt.figure() #一回づつこれでデータ消したほうがいいって書いてあったけど白いデータが追加されるだけだった

    #plt.savefig("a.png", dpi = 300, bbox_inches="tight") #ここで書くと最後のデータだけ出てくる
    #plt.savefig("b.png", dpi = 300, bbox_inches="tight") #同じのが出てくる
    plt.show() #plt.show()はデータが蓄積されるっぽい　一回データ表示したら再表示されない気がする
    #plt.show() #2回目は何も表示されない

