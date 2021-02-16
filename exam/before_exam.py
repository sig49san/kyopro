import os, sys, pathlib, shutil
from sys import path

print("コンテスト名入力")
contest = input().upper()
if(contest == ""):
    print("コンテスト名が入力されていません")
    sys.exit()

if(os.path.exists(contest)):
    print("すでに作成されています")
    sys.exit()

os.mkdir(contest)

abc_exam = "abcdef"

for word in abc_exam:
    shutil.copyfile("./tmp.py", "./" + contest + "/" + word + ".py")

p_new = pathlib.Path(contest + "/test.txt")
with p_new.open(mode= "w") as f:
    f.write("")

