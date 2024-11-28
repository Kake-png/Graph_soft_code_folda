from tkinter import filedialog
from tkinter import messagebox as mbox
from pathlib import Path
import tkinter
import txt_printcode


class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=500, height=250, borderwidth=1, relief="groove")
        self.root=root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '閉じる'
        quit_btn["command"] = self.root.destroy
        quit_btn.pack(side = "bottom")

        submit_btn = tkinter.Button(self)
        submit_btn["text"] = "ファイル選択"
        submit_btn["command"] = self.save_data
        submit_btn.pack()

        self.message = tkinter.Message(self)
        self.message.pack()

    def save_data(self):
        #text = self.text_box.get()
        file_path = \
        filedialog.askopenfilename(initialdir=Path.cwd())
        filepathedited = file_path.split('/')
        #print(filepathedited)
        self.message["aspect"] = 1000
        filename = filepathedited.pop()
        filenameedited = filename.split(".")
        if filenameedited[-1] == "txt":
            self.message["text"] = filename
            file_path = ""
            for i in filepathedited:
                file_path = file_path +"/" + i
            txt_printcode.txt_print(filename, file_path)
        else:
            self.message["text"] = "指定したファイルは.txtではありません"

root = tkinter.Tk()
root.title("HoPE電装テキストファイル描画ソフト")
root.geometry("500x250")
app = Application(root = root)
app.mainloop()
