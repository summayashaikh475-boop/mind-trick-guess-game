import random

def play_game():
    score = 0

    print("\n-----👋 Welcome to Mind Trick Guess Game!-----")
 
    while True:
        while True:
            print("\nChoose Level:")
            print("1. Easy (1-20)")
            print("2. Moderate (1-50)")
            print("3. Hard (1-100)")

            level =input("Enter level (1/2/3): ")

            if level in ["1", "2", "3"]:
                level = int(level)
                break
            else:
                print("⚠️ Invalid input! Please choose 1, 2 or 3.")

        if level == 1:
            base = 10
            computer = random.randint(1, 20)
            attempts = 5
        elif level == 2:
            base = 20
            computer = random.randint(1, 50)
            attempts = 4
        else:
            base = 30
            computer = random.randint(1,100)
            attempts = 3
                            
        print("\n🔀 I have picked a number ....")
        print(f"You have {attempts} 👈 attempts")    

        while attempts > 0:
            guess = int(input("\nEnter your guess: "))

            if guess == computer:
                print("🎊 Correct! You cracked my mind!🤯 ")
                score += base * 10
                break

            if computer % 2 == 0:
                print("🧠 HINT: My number is even")
            else:
                print("🧠 HINT: My number is odd") 

            if abs(computer - guess) <=5:
                print("🔥 You are very close!")

            if guess > computer:
                print("📈 Too high!")  
            else:
                print("📉 Too low!")      


            attempts -= 1
            print(f"🧮Attempts left: {attempts}")    

        if attempts == 0:
            print(f"\n💀 You lost! Number was {computer} ")   

        print(f"🥳 Your Score: {score}")  

        choice = input("\n🔄 Wanna play again? (y/n): ")
        if choice.lower() != "y":
            print("👋 Thanks for playing dude! ")
            break
    print("\n🏆 FINAL SCORE:", score)
    print("🎮 Game session completed successfully! ")        

play_game()   


