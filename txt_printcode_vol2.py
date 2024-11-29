import change_to_csv as change
import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil

def txt_print(filename, file_path):
    os.chdir(file_path)
    newfile_path = file_path + "/" + filename.replace(".txt","") + "_work"
    if not os.path.isdir(newfile_path):
        os.makedirs(filename.replace(".txt","") + "_work", exist_ok=True)
    newcsvfile = change.chenge_to_csv(filename, file_path, newfile_path) #txtファイルの":"が","に変わったcsvファイルが生成され、そのファイル名が返ってくる
    os.chdir(newfile_path)
    df = pd.read_csv(newcsvfile) #csvファイルをデータフレームとして読み込む
#print(df)

    with open(newcsvfile) as file: #一行目だけ取り出して項目を確認
        contents = file.readline()
        contents = contents.replace("\n","")
        contents = contents.split(",")
    #print(contents)

    #df.plot(x="time",y="speed",kind="bar")

    contents = contents[1:len(contents)]
    #print(contents)
    #os.chdir(newfile_path)
    os.chdir(__file__.replace("txt_printcode_b.py",""))#このファイルの絶対パスを取得、ファイル名を除外して作業ディレクトリを移動
    if os.path.isdir("preview"):
        shutil.rmtree("preview")
    os.makedirs("preview", exist_ok=True)#previewの中に全てのグラフ画像保存、あとでpreviewフォルダごと消すor次のタイミングで更新。データを残さないように
    os.chdir("preview")

    #print(os.getcwd)
    for content in contents: 
        #df.plot(x="time",y=content,kind="bar") #これ消すとpltのほうもデータがなくなる　データの作成
        df.plot(x="time",y=content,kind="line",title=f"{content}_line",grid=True) #折れ線型 
        #plt.plot() #いらない？
        plt.savefig("time_"+content+"(line)"+".png", dpi = 70, bbox_inches="tight") #データの保存　(名前, 解像度, なんかオプション)
        df.plot(x="time",y=content,kind="bar",title=f"{content}_bar")
        plt.savefig("time_"+content+"(bar)"+".png", dpi = 70, bbox_inches="tight") #データの保存　(名前, 解像度, なんかオプション)

    #plt.savefig("a.png", dpi = 300, bbox_inches="tight") #ここで書くと最後のデータだけ出てくる
    #plt.savefig("b.png", dpi = 300, bbox_inches="tight") #同じのが出てくる
    #plt.show() #plt.show()はデータが蓄積されるっぽい　一回データ表示したら再表示されない気がする
    #plt.show() #2回目は何も表示されない

    return contents

