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

def print_hand(hand, name='ゲスト'):
    # 変数 hands に、複数の文字列を要素に持つリストを代入してください
    hands = ['グー', 'チョキ', 'パー']
    
    # リスト hands を用いて、選択した手が出力されるように書き換えましょう
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
# 「 何を出しますか？（0: グー, 1: チョキ, 2: パー） 」と出力してください
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')

# input を用いて入力を受け取り、数値に型変換してから変数 player_hand に代入してください
player_hand = int(input('数字で入力してください：'))

if player_name == '':
    # 第1引数を変数 player_hand に書き換えてください
    print_hand(player_hand)
else:
    # 第1引数を変数 player_hand に書き換えてください
    print_hand(player_hand, player_name)

# 7

# 関数 validate を定義してください
def validate(hand):
    # hand の値によって条件分岐してください
    if hand < 0 or hand > 2:
        return False
    else:
        return True

def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

# 関数 validate の戻り値が True の場合、以下の if~else 文が実行されるようにしてください
if validate(player_hand):
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
# 関数 validate の戻り値が False の場合「 正しい数値を入力してください 」と出力してください
else:
    print('正しい数値を入力してください')



# 8

def validate(hand):
    if hand < 0 or hand > 2:
        return False
    # else を消してインデントを直してください
    return True

def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if validate(player_hand):
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
else:
    print('正しい数値を入力してください')
