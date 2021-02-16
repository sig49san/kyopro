'''
問題文AtCoder 社は、オフィスの入り口に 3 桁の暗証番号を設定することにしました。
AtCoder 社には N 桁のラッキーナンバー S があります。
社長の高橋君は、S から N−3 桁を消して残りの 3 桁を左から読んだものを暗証番号として設定することにしました。
このとき、設定されうる暗証番号は何種類あるでしょうか？
ただし、ラッキーナンバーや暗証番号はいずれも 0 から始まっても良いものとします。

制約4≤N≤30000
S は半角数字からなる長さ N の文字列
'''

N = input().split()
S = list(input())
 
Slist = list(S)
 
#print(Slist)
 
ans = 0
for i in range(0, 1000):
  a = i // 100
  b = (i % 100) // 10
  c = i % 10
  
  if(str(a) in Slist):
    nextList = Slist[Slist.index(str(a))+1:]
    if(str(b) in nextList):
      finalList = nextList[nextList.index(str(b))+1:]
#      print(finalList)
      if(str(c) in finalList):
        ans += 1
 
print(ans)