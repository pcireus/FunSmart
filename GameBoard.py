from tkinter import*
import os
def main(root, frame, results):
    frame.destroy()
    root.title("FunSmart Gameboard Screen")
    frame = Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    print("GameBoard "+ results)