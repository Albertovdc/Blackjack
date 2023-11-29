# Blackjack game
# Modify a global vairable

````python
# Global scope
number = 1

def add():
    global number
    number += 1
    print(number)
add()
````