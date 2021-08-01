# 1

# 関数 print_hand を定義してください
def print_hand():
    print('グーを出しました')

# 関数 print_hand を呼び出してください
print_hand()


# 2

# 引数を受け取れるようにしてください
def print_hand(hand):
    # 「 ◯◯を出しました 」と出力されるように書き換えてください
    print(hand + 'を出しました')

# 引数に文字列「 グー 」を入れてください
print_hand('グー')

# 引数を文字列「 パー 」として関数 print_hand を呼び出してください
print_hand('パー')

# 3

# 名前を第2引数で受け取れるようにしてください
def print_hand(hand, name):
    # 「 ◯◯は□□を出しました 」と出力されるように書き換えてください
    print(name+ 'は' + hand + 'を出しました')

# 第2引数に文字列「 にんじゃわんこ 」を入れてください
print_hand('グー', 'にんじゃわんこ')

# 第2引数に文字列「 コンピューター 」を入れてください
print_hand('パー', 'コンピューター')


# 4

# 仮引数 name の初期値を設定してください
def print_hand(hand, name = 'ゲスト'):
    print(name + 'は' + hand + 'を出しました')

# 引数に文字列「 グー 」のみを入れてください
print_hand('グー')

# 5

def print_hand(hand, name='ゲスト'):
    print(name + 'は' + hand + 'を出しました')

print('じゃんけんをはじめます')

# input を用いて入力を受け取り、変数 player_name に代入してください
# 入力を受け取るには次のように書きましょう。
# 変数名 = input('表示したい文章')
player_name = input('名前を入力してください：')

# 変数 player_name の値によって関数 print_hand の呼び出し方を変更してください
if player_name == '':
    print_hand('グー')
else:
    print_hand('グー', player_name)

# 6

