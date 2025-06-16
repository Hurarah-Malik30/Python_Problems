

def getNoOfNotes(amount):
    notes_500 = amount // 500
    amount = amount % 500

    notes_100 = amount // 100
    amount = amount % 100

    notes_50 = amount // 50
    amount = amount % 50

    notes_10 = amount // 10
    amount = amount % 10

    coins = amount

    print("No of 500 notes:", notes_500)
    print("No of 100 notes:", notes_100)
    print("No of 50 notes:", notes_50)
    print("No of 10 notes:", notes_10)
    print("No of coins:", coins)


getNoOfNotes(1550)
