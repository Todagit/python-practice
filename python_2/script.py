# 1

# 変数 fruits に、複数の文字列を要素に持つリストを代入してください
fruits = ['apple', 'banana', 'orange'] 

# インデックス番号が 0 の要素を出力してください
print(fruits[0])

# インデックス番号が 2 の要素を文字列と連結して出力してください
print('好きな果物は' + fruits[2] + 'です')


# 2

fruits = ['apple', 'banana', 'orange']

# リストの末尾に文字列「 grape 」を追加してください
fruits.append('grape')

# 変数 fruits に代入したリストを出力してください
print(fruits)

# インデックス番号が 0 の要素を文字列「 cherry 」に更新してください
fruits[0] = 'cherry'

# インデックス番号が 0 の要素を出力してください
print(fruits[0])


# 3

fruits = ['apple', 'banana', 'orange']

# for 文を用いてリストの要素を1つずつ取り出し、「 好きな果物は◯◯です 」と出力してください
for fruit in fruits:
    print('好きな果物は' + fruit + 'です')


# 4

# 変数 fruits に辞書を代入してください
fruits = { 'apple' : 'りんご', 'banana' : 'バナナ'}

# 辞書 fruits のキー「 banana 」に対応する値を出力してください
print(fruits['banana'])

# 辞書 fruits を用いて、「 appleは◯◯という意味です 」となるように出力してください
print('appleは' + fruits['apple'] + 'という意味です')
