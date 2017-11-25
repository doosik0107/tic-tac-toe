from tkinter import *
import sys
from tkinter import messagebox


def checked(i):
    # checked함수의 정의, 현재 플레이어가 누군지 확인하여 버튼의 텍스트값과 배경색을 저장한다
    global player

    button = list[i]
    OX_list = ["X", "O"]
    if button["text"] != i:
        return
    button["text"] = player
    win_checked[i] = player
    button["bg"] = "yellow"
    # win_checked의 값이 n이 아니고 같은 값일 경우를 판단하는 if문
    if(win_checked[0] != 'n') and (win_checked[1] != 'n') and (win_checked[2] != 'n'):
        if win_checked.get(0) == win_checked.get(1)== win_checked.get(2):
            info_print(player)
            sys.exit()
    elif(win_checked[0] != 'n') and (win_checked[3] != 'n') and (win_checked[6] != 'n'):
        if win_checked.get(0) == win_checked.get(3) == win_checked.get(6):
            info_print(player)
            sys.exit()
    elif(win_checked[2] != 'n') and (win_checked[5] != 'n') and (win_checked[8] != 'n'):
        if win_checked.get(2) == win_checked.get(5) == win_checked.get(8):
            info_print(player)
            sys.exit()
    elif (win_checked[6] != 'n') and (win_checked[7] != 'n') and (win_checked[8] != 'n'):
        if win_checked.get(6) == win_checked.get(7) == win_checked.get(8):
            info_print(player)
            sys.exit()
    elif(win_checked[0] != 'n') and (win_checked[4] != 'n') and (win_checked[8] != 'n'):
        if win_checked.get(0) == win_checked.get(4) == win_checked.get(8):
            info_print(player)
            sys.exit()
    elif(win_checked[1] != 'n') and (win_checked[4] != 'n') and (win_checked[7] != 'n'):
        if win_checked.get(1) == win_checked.get(4) == win_checked.get(7):
            info_print(player)
            sys.exit()
    elif(win_checked[2] != 'n') and (win_checked[4] != 'n') and (win_checked[6] != 'n'):
        if win_checked.get(2) == win_checked.get(4) == win_checked.get(6):
            info_print(player)
            sys.exit()
    elif(win_checked[3] != 'n') and (win_checked[4] != 'n') and (win_checked[5] != 'n'):
        if win_checked.get(3) == win_checked.get(4) == win_checked.get(5):
            info_print(player)
            sys.exit()
    else:
        print("이긴사람없음")

    if player == "X":
        player = "O"
        button["bg"] = "gray"
    else:
        player = "X"
        button["bg"] = "red"

def info_print(player):
    infor = "player " + player + " win"
    messagebox.showinfo("tic tac toe", infor)

window = Tk()  # 윈도우시작
player = "X"
list = []
win_checked = {0: 'n', 1: 'n', 2: 'n', 3: 'n', 4: 'n', 5: 'n', 6: 'n', 7: 'n', 8: 'n'}
for i in range(9):  # 버튼을 생성하기위한 반복문이며, 체크드함수에 연결하여 이벤트를 처리한다
    b = Button(window, text=i, command=lambda k=i: checked(k))
    b.grid(row=i // 3, column=i % 3)  # 3행 3열의 형태로 배치한다
    list.append(b)

window.mainloop()  # 이벤트를 기다리는 루프
