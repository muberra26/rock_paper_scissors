# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:17:09 2024

@author: muber
"""
import random

def rock_paper_scissors_Muberra_Ozdemir():
    greeting()
    
    choices = ["Rock", "Paper", "Scissors"]
    will_continue = ["Yes", "No"]
    
    outer_break = False
    while not outer_break:
        player_want = input("Do you want to play the game? Please enter Yes or No: \n")
        
        game_number = 1
        game_round_number = 1
        computer_score = 0
        player_score = 0
        exit_flag = False
        
        if player_want.strip().lower().capitalize() not in will_continue:
            print("Invalid input! Please enter 'Yes' or 'No': ")
            continue
        
        if player_want.strip().lower().capitalize() == "No":
            if game_number == 1:
                print("Why are you going to exit the game? If that is what you want, bye...")
                break
            else:
                print("Thank you for visiting! See you soon!")
                break
                
        
        while (computer_score < 2 and player_score < 2): 
            
            print()
            print("***** GAME", game_number, "- ROUND", game_round_number, "*****")
            player_choice = input("Please enter Rock, Paper, Scissors or Exit: ").strip().lower().capitalize()
            if (player_choice not in choices) and (player_choice != "Exit"):
                print("Invalid choice!")
                continue
            
            if player_choice == "Exit":
                if(game_number + game_round_number == 2):
                    print("Why are you going to exit the game? If that is what you want, bye...")
                else:
                    print("Thank you for playing! See you next time!")
                exit_flag = True
                break
            
                
            computer_choice = random.choice(choices)
            print()
            print("Computer chose", computer_choice, ", You chose", player_choice)
        
    
            if player_choice == computer_choice:
                print("It's a tie!")
                
            elif (player_choice == "Rock" and computer_choice == "Scissors") or \
                (player_choice == "Paper" and computer_choice == "Rock") or \
                (player_choice == "Scissors" and computer_choice == "Paper"):
                print("You get 1 point!")
                player_score += 1
                
            else:
                print("Computer gets 1 point!")
                computer_score += 1
            
            print()
            print("-Score-\nYou:", player_score, ",Computer:", computer_score)
            
            if player_score == 2:
                print("\n\n***** CONGRATULATIONS! YOU ARE THE WINNER! *****")
            
            elif computer_score ==2:
                print("\n\nThe computer won the game. Better luck next time :(")
                print()
             
            game_round_number += 1
        
        if exit_flag:
            outer_break = True
        else:     
            computer_want = random.choice(will_continue)
            print("Computer wants to play a game again:", computer_want) 
            if computer_want == "No":
                print("Computer doesn't want to play again. The game is over. Goodbye!")
                break

def greeting():
    print("Welcome to the Rock, Paper, Scissors game, Dear Player!")
    print("At the beginning of each game, you will be asked if you want to play. Please enter your answer as 'Yes' or 'No'.")
    print("A game consists of  multiple rounds, and the winner will be first to score 2 points.")
    print("The game is beginning!")
    print()

rock_paper_scissors_Muberra_Ozdemir()

