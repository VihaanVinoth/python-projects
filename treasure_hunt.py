import random 

import math 

status = "" 

wins = 0 

loss = 0 

def multiple_rounds(wins): 

    x2 = random.randint(1, 100) 

    y2 = random.randint(1, 100) 

    while True: 

        guess = input("Enter your guess (x, y): ") 

        if guess[0].isnumeric(): 

            x1 = int(guess[0]) 

        elif guess[0:2].isnumeric(): 

            x1 = int(guess[0:2]) 

        elif guess[0:3].isnumeric(): 

            x1 = int(guess[0:3]) 

        if guess[3].isnumeric(): 

            y1 = int(guess[3]) 

        elif guess[4:6].isnumeric(): 

            y1 = int(guess[4:6]) 

        elif guess[5:8].isnumeric(): 

            y1 = int(guess[4:7]) 

        d =  math.sqrt((x2 - x1)**2+(y2 - y1)**2) 

        if x1 <= 100: 

            if guess[1] == "," or guess[2] == "," or guess[3] == ",": 

                if guess[2].isspace() or guess[3].isspace() or guess[4].isspace(): 

                    if y1 <= 100: 

                        pass 

                    else: 

                        print("Invalid") 

                        pass 

                else: 

                    print("Invalid") 

                    pass 

            else:  

                print("Invalid") 

                pass 

        else: 

            print("Invalid") 

            pass 

        if d <= 2 and d > 0.00: 

            status = "Very Close" 

            print(f"You are {status}! Distance: {d:.2f}") 

        elif d <= 5 and d > 0.00: 

            status = "Close" 

            print(f"You are {status}! Distance: {d:.2f}") 

        elif d > 5: 

            status = "Far Away" 

            print(f"You are {status}! Distance: {d:.2f}") 

        elif d == 0.00: 

            print("Congratulations! You found the treasure!") 

            wins += 1 

            game_reset = input("Would you like to play again? (yes/no): ").lower() 

            if game_reset == "yes": 

                x2 = random.randint(1, 100) 

                y2 = random.randint(1, 100) 

                return "Yes" 

            elif game_reset == "no": 

                print("Thanks for playing!") 

                return "No" 

            if game_reset == "no": 

                break 

def attempt_mode(w, l): 

    attempts = 5 

    for attempt in range(attempts): 

        x2 = random.randint(1, 100) 

        y2 = random.randint(1, 100) 

        print(f"Attempt {attempts}") 

        guess = input("Enter your guess (x, y): ") 

        if guess[0].isnumeric(): 

            x1 = int(guess[0]) 

        elif guess[0:2].isnumeric(): 

            x1 = int(guess[0:2]) 

        elif guess[0:3].isnumeric(): 

            x1 = int(guess[0:3]) 

        if guess[3].isnumeric(): 

            y1 = int(guess[3]) 

        elif guess[4:6].isnumeric(): 

            y1 = int(guess[4:6]) 

        elif guess[5:8].isnumeric(): 

            y1 = int(guess[4:7]) 

        d =  math.sqrt((x2 - x1)**2+(y2 - y1)**2) 

        if x1 <= 100: 

            if guess[1] == "," or guess[2] == "," or guess[3] == ",": 

                if guess[2].isspace() or guess[3].isspace() or guess[4].isspace(): 

                    if y1 <= 100: 

                        pass 

                    else: 

                        print("Invalid") 

                        pass 

                else: 

                    print("Invalid") 

                    pass 

            else:  

                print("Invalid") 

                pass 

        else: 

            print("Invalid") 

            pass 

        if d <= 2 and d > 0.00: 

            status = "Very Close" 

            print(f"You are {status}! Distance: {d:.2f}") 

            attempts -= 1 

        elif d <= 5 and d > 0.00: 

            status = "Close" 

            print(f"You are {status}! Distance: {d:.2f}") 

            attempts -= 1 

        elif d > 5: 

            status = "Far Away" 

            print(f"You are {status}! Distance: {d:.2f}") 

            attempts -= 1 

        elif d == 0.00: 

            print("Congratulations! You found the treasure!") 

            w += 1 

            game_reset = input("Would you like to play again? (yes/no): ").lower() 

            if game_reset == "yes": 

                attempts = 5 

                x2 = random.randint(1, 100) 

                y2 = random.randint(1, 100) 

                return "Yes" 

            elif game_reset == "no": 

                print("Thanks for playing!") 

                return "No" 

        if attempts == 0: 

            print(f"You lost! the treasure coordinates were: {str(x2) + ", " + str(y2)}") 

            l += 1 

            game_reset = input("Would you like to play again? (yes/no): ").lower() 

            attempts -= 1 

            if game_reset == "yes": 

                return "Yes" 

            elif game_reset == "no": 

                print("Thanks for playing!") 

                return "No" 

             

            if game_reset == "no": 

                break 

while True: 

    print(f"You have won {wins} times and lost {loss} times.") 

    game_mode = int(input("Would you like to play multiple rounds or attempts? (1/2): ")) 

    if game_mode == 1: 

        multiple_rounds(wins) 

    elif game_mode == 2: 

        attempt_mode(wins, loss) 

    else: 

        break 

    if multiple_rounds(wins) == "Yes": 

        x2 = random.randint(1, 100) 

        y2 = random.randint(1, 100) 

        multiple_rounds(wins) 

    elif attempt_mode(wins, loss) == "Yes": 

        x2 = random.randint(1, 100) 

        y2 = random.randint(1, 100) 

        attempts = 5 

        attempt_mode(wins, loss) 

    elif multiple_rounds(wins) == "No" or attempt_mode(wins, loss) == "No": 

        break    