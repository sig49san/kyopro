"""
ABC122 B問
https://atcoder.jp/contests/abc122/tasks/abc122_b

問題文
英大文字からなる文字列Sが与えられます。
Sの部分文字列 (注記を参照) であるような最も長い ACGT 文字列 の長さを求めてください。

ここで、ACGT 文字列とは A, C, G, T 以外の文字を含まない文字列です。

注記
文字列 Tの部分文字列とは、Tの先頭と末尾から0文字以上を取り去って得られる文字列です。
例えば、ATCODER の部分文字列には TCO, AT, CODER, ATCODER,  (空文字列) が含まれ、AC は含まれません。

制約Sは長さ1以上10以下の文字列である。Sの各文字は英大文字である。
"""

import re

#S = input()
S = 'HATAGAYA'

S = re.sub('[ACGT]', '1', S)
S = re.sub('[A-Z]', '0', S)

S = S.split('0')

print(len(max(S, key = len)))