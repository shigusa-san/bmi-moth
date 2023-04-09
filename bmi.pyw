import PySimpleGUI as sg

layout = [[sg.T("身長と体重を記入")],
          [sg.T("身長"),sg.I(k="hei")],
          [sg.T("体重"),sg.I(k="fat")],
          [sg.B("実行", k="btn")],
          [sg.T("実行結果",k="bmi")]]

Win = sg.Window("BMIデスクトップアプリ", layout)

def moth():
    hei = float(v["hei"]) / 100.0
    fat = float(v["fat"])
    bmi = fat / (hei * hei)
    Win["bmi"].update(bmi)

while True:
    e, v = Win.read()
    if e == "btn":
        moth()
    if e == None:
        break

win.close()    
    
