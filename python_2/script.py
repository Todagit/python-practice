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


# 7

x = 10

# while 文を用いて、「変数 x が 0 より大きい」間、繰り返される繰り返し処理を作ってください
while x > 0:
    # 変数 x を出力してください
    print(x)
    # 変数 x から 1 引いてください
    x -= 1


# 8

numbers = [765, 921, 777, 256]
for number in numbers:
    print(number)
    # 変数 number が 777 のとき「 777が見つかったので処理を終了します 」と出力した後、処理を終了させてください
    if number == 777:
        print('777が見つかったので処理を終了します')
        break


# 9

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    # 変数 number の値が 3 の倍数のとき、繰り返し処理をスキップしてください
    if number % 3 == 0:
        continue
    print(number)



# 10

# 文字列のキーと数値の値を持つ辞書を作って、変数 items に代入してください
items = {'apple': 100, 'banana': 200, 'orange': 400}

# for 文を用いて、辞書 items のキーを1つずつ取り出していく繰り返し処理を作成してください
for item_name in items:
    # 「 --------------------------------------------- 」を出力してください
    print('---------------------------------------------')
    # 「 ◯◯は1個△△円です 」となるように出力してください
    print(item_name + 'は1個' + str(items[item_name]) + '円です')

# 11

items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')
    
    # input を用いて入力を受け取り、変数 input_count に代入してください
    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    # キーと変数 input_count を用いて「 購入する◯◯の個数は△△個です 」となるように出力してください
    print('購入する' +  item_name + 'の個数は' + input_count + '個です')
    
    # input_count を数値として変数 count に代入してください
    count = int(input_count)
    # 変数 total_price に果物1個の値段と変数 count を掛けた値を代入してください
    total_price = items[item_name] * count
    # 変数 total_price と型変換を用いて、「 支払い金額は◯◯円です 」となるように出力してください
    print('支払い金額は' + str(total_price) + '円です')


# 12

# 変数 money に数値 1000 を代入してください
money = 1000

items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    # 変数 money を用いて「 財布には◯◯円入っています 」のように出力してください
    print('財布には' + str(money) + '円入っています')
    
    print(item_name + 'は1個' + str(items[item_name]) + '円です')
    
    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    print('購入する' + item_name + 'の個数は' + input_count + '個です')
    
    count = int(input_count)
    total_price = items[item_name] * count
    print('支払い金額は' + str(total_price) + '円です')
    
    # money と total_price の比較結果によって条件を分岐してください
    if money >=  total_price:
        print(item_name + 'を' + input_count + '個買いました')
        money = money - total_price
    else:
        print('お金が足りません')
        print(item_name + 'を買えませんでした')

