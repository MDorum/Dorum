
count = 36
player1 = 0
player2 = 0

def cards():
    global player1
    global player2
    global count
    while count > 0:
        x = int(input("First player, take your card = "))
        if count - x < 0:
            print("You can't take that amount of cards.", count, "left.")
        else:
            if x > 6:
                while x > 6:
                    print("You can take only 6 cards by one.", count, "cards left.")
                    x = int(input("Take your card = "))
                player1 = x + player1
                count = count - x
                print(count, "cards left.")
            else:
                player1 = x + player1
                count = count - x
                print(count, "cards left.")

        y = int(input("Second player, take your card = "))
        if count - y < 0:
            print("You can't take that amount of cards.", count, "left.")
        else:
            if y > 6:
                while y > 6:
                    print("You can take only 6 cards by one.", count, "cards left.")
                    y = int(input("Take your card = "))
                player2 = y + player2
                count = count - y
                print(count, "cards left.")
            else:
                player2 = y + player2
                count = count - y
                print(count, "cards left.")


cards()
print("First player have =", player1, "cards.")
print("Second player have =", player2, "cards.")
