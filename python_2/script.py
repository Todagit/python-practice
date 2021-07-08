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


# 5

fruits = {'apple': 100, 'banana': 200, 'orange': 400}

# キー「 banana 」の値を数値 300 に更新してください
fruits['banana'] = 300

# キーが「 grape 」、値が数値の 500 の要素を辞書 fruits に追加してください
fruits['grape'] = 500

# fruits の値を出力してください
print(fruits)


# 6

fruits = {'apple': 'りんご', 'banana': 'バナナ', 'grape': 'ぶどう'}

# for 文を用いて、辞書のキーを1つずつ取り出し、繰り返しの中で「 ◯◯は△△という意味です 」と出力させてください
for fruit_key in fruits:
    print( fruit_key + 'は' + fruits[fruit_key]+ 'という意味です')
