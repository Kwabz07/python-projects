import random

def main():
    winners = get_winners_data()
    
    print("Welcome to the soccer trivia game!")
    print("You have three questions to answer with two clues available for each question.")

    ask_question(winners)
    

def get_winners_data():
    #this function creates and returns a dictionary with the winners ofthe award.
    winners_dict = {"2000": {'name':'Luis Figo', 'team':'Real Madrid', 'position':'Winger'},
    "2001": {'name':'Michael Owen', 'team':'Liverpool', 'position':'Striker'},
    "2002": {'name':'Ronaldo', 'team':'Real Madrid', 'position':'Striker'}, 
    "2003": {'name':'Pavel Nedved', 'team':'Juventus', 'position':'midfielder'},
    "2004": {'name':'Andriy Shevchenko', 'team':'AC Milan', 'position':'striker'},
    "2005": {'name':'Ronaldinho', 'team':'Barcelona', 'position':'attacking midfielder'},
    "2006": {'name':'Fabio Cannavaro', 'team':'Real Madrid', 'position':'Center Back'},
    "2007": {'name':'Kaka', 'team':'AC Milan', 'position':'attacking midfielder'},
    "2008": {'name':'Cristiano Ronaldo', 'team': 'Manchester United', 'position':'winger'},
    "2009": {'name':'Lionel Messi', 'team':'Barcelona', 'position':'forward'},
    "2010": {'name':'Lionel Messi', 'team':'Barcelona', 'position':'forward'},
    "2011": {'name':'Lionel Messi', 'team': 'Barcelona', 'position':'forward'},
    "2012": {'name':'Lionel Messi', 'team':'Barcelona', 'position':'forward'},
    "2013": {'name':'Cristiano Ronaldo', 'team': 'Real Madrid', 'position':'winger'},
    "2014": {'name':'Cristiano Ronaldo', 'team': 'Real Madrid', 'position':'winger'},
    "2015": {'name':'Lionel Messi', 'team': 'Barcelona', 'position':'forward'},
    "2016": {'name':'Cristiano Ronaldo', 'team': 'Real Madrid', 'position':'winger'},
    "2017": {'name':'Cristiano Ronaldo', 'team': 'Real Madrid', 'position':'winger'},
    "2018": {'name':'Luka Modric', 'team': 'Real Madrid', 'position':'midfielder'},
    "2019": {'name':'Lionel Messi', 'team': 'Barcelona', 'position':'forward'},
    "2021": {'name':'Lionel Messi', 'team': 'Barcelona', 'position':'forward'},
    "2022": {'name':'Karim Benzema', 'team': 'Real Madrid', 'position':'striker'},
    "2023": {'name':'Lionel Messi', 'team': 'PSG', 'position':'forward'},
    "2024": {'name':'Rodri', 'team': 'Manchester City', 'position':'defensive midfielder'}}
    return winners_dict


def ask_question(winners):
    #this function does most of the logic of this game. it takes the winners dictionary as a paramter to develop questions and clues
    rounds = 3
    score = 0
    years = list(winners.keys())
    for i in range(rounds):
        
        
        selected_year = random.choice(years)
        winner_info = winners[selected_year]
        winner_name = winner_info["name"] 
        winner_team = winner_info["team"]
        winner_position = winner_info["position"]
        correct_winner =  winner_name
        years.remove(selected_year) #to prevent repetition of the question
        print(f"Who won the Ballon D'or in {selected_year}? ")
        attempts = 3
        clues_used = 0
        while attempts > 0:
            
            clues_left = 2 - clues_used
            print(f"You have {clues_left} clue(s)")
            if clues_used < 2:
                clue_request = input("Would you like a clue? Yes/No ").lower()
                if clue_request == "yes":
                    if clues_used == 0:
                        print(f"Clue: He played for {winner_team}.")
                        
                    elif clues_used == 1:
                        print(f"Clue: He played as a/an {winner_position}")
                    clues_used +=1

                user_answer = input("Your answer: ").strip()
        
            if user_answer.lower() == correct_winner.lower():
                print("That's correct! Way to go!")
                score += 1
                print()
                break
            else:
                print("That's incorrect.")
                print()
                attempts -=1
                score = score
            print()
        if attempts == 0:
            print(f"The correct answer was: {winner_name}\n")

    print(f"You got {score} out of 3 correct. Thanks for playing!")   

if __name__ == "__main__":
    main()