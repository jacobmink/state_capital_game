states = [
    {"Alabama":"Montgomery"},
    {"Alaska":"Juneau"},
    {"Arkansas":"Little Rock"},
    {"Arizona":"Phoenix"}
]

def state_game(arr):
    print("Welcome to Capital Punishment")
    answer = input("What is the capital of {}? ".format(arr[random.randint(0,len(arr))]))

state_game(states)
