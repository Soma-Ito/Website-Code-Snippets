
x = 10

# Stringと変数を分ける方法
print("x is", x)  # stringとxを並べて表示
print("x is " + str(x)) # stringとxを足し合わせて表示

# Formatを用いた方法
print("x is {x_value}".format(x_value=x)) # {}の中にx_valueという一時的な変数を設定し、その後xを割り当て

# F-Stringを用いた方法
print(f"x is {x}") # F-Stringでは" "の前にfを記述
