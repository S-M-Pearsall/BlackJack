#
# File: peasm009.py
# Author: Scott Pearsall
# Email Id: peasm009
# Description: Assignment 2 – A program to simulate blackjack
# This is my own work as defined by the University's
# Academic Misconduct policy.
# 

#imports the playing cards.py file
import playing_cards

#A list of indexes to count the amount of games played, lost, won and drawn
played_index = 0

won_index = 0

lost_index = 0

drawn_index = 0
    

#A user defined function to get the total of a player or dealers hand.
def get_hand_total(hand):

    #Variable for total
    total = 0

    #Scrolls through each value in the specified hand, converts it to an int and adds it to the total
    for value in hand:

        #checks if the first part of an element is a letter. If true, checks what
        #kind of letter and applies the appropriate number in its place to total
        if value.isalpha() == True:

            if value[0] == 'T' or value[0] == 'J' or value[0] == 'Q' or value[0] == 'K':
                
                total = total + 10
                
            elif value[0] == 'A' and total < 11:
                
                total = total + 11
                
            elif value[0] == 'A' and total >= 11:
                
                total = total + 1
                
        #Checks if the first value is a number and does an int conversion if found to be false.
        elif value.isalpha() == False:
            
            refined_value = int(value[0])
            total = total + refined_value

    #returns the total number
    return total

#take element, split in two, read letter, create string with if statements containing the new string and the letter/number
#put in index element new list
def display_hand(hand_text, hand):

    #various variables to contain the items in the loop
    hand_total = get_hand_total(hand)
    
    string_index = 0

    string = ""

    final_holding_string = ""
    
    #Goes through each element of the list, removing it and splitting it in two then checks what suite of cards it belongs
    #to and adjusts the final string based on it.
    for x in hand:
        
        hand_list = hand[string_index]
        string_holding = hand_list[1]
        number_string = hand_list[0]

        #Checks which letter the second element corresponds with
        if string_holding == "H" :
            new_string = " of Hearts | "
            
        elif string_holding == "C" :
            new_string = " of Clubs | "
            
        elif string_holding == "D" :
            new_string = " of Diamonds | "
            
        elif string_holding == "S" :
            new_string = " of Spades | "

        #Concatenates the final product together into a long string
        final_holding_string = final_holding_string + number_string + new_string
        
        string_index = string_index + 1

    #prints out the final product
    print(hand_text, hand_total, ":", final_holding_string)

#A function to play out the player's hand
def play_player_hand(player_hand):

    #The function asks the useer whether they want to hit or stand
    print()
    what_user_chose = get_hit_choice()

    #The loop runs if the player has chosen to hit and adds a card to the player's hand
    while what_user_chose == "h":
        
            card = playing_cards.deal_one_card()
            player_hand.append(card)
            print()
            display_hand("Player's hand is", player_hand)

            #If the player's hand goes above 21, the player busts
            if get_hand_total(player_hand)>21:
                
                what_user_chose = "s"
                print("--> Player busts!")

            #If the player's hand does not, it asks what they want to do again    
            elif get_hand_total(player_hand) <= 21:
                
                print()
                what_user_chose = get_hit_choice()

    #This checks if the player has stood while having a hand of less than 15 and forces them to take a card            
    while what_user_chose == "s" and get_hand_total(player_hand)<15:
        
        print()
        print("Cannot stand on value less than 15!")
        card = playing_cards.deal_one_card()
        player_hand.append(card)
        print()
        display_hand("Player's hand is", player_hand)

        #If the player goes over 21, they bust
        if get_hand_total(player_hand)>21:
            
            what_user_chose = "s"
            print("--> Player busts!")

        #Else they get asked to hit or stand again    
        else:
            print()
            what_user_chose = get_hit_choice()

#A function to play the dealer's hand
def play_dealer_hand(dealer_hand):

    #Display's the dealer's hand and then proceeds to add cards to the dealers hand while it is less than 17
    display_hand("Dealer's hand is", dealer_hand)
    
    while get_hand_total(dealer_hand)<17:
        
        card = playing_cards.deal_one_card()
        dealer_hand.append(card)
        display_hand("Dealer's hand is", dealer_hand)

        #if the dealer's hand goes over 21 they bust
        if get_hand_total(dealer_hand) > 21:
            print("--> Dealer busts!")

#A function that asks the user if they want to hit or stand and validates the choice
def get_hit_choice():
    
    deal_no_deal =   input("Please enter h or s (h - Hit, s = Stand):")
    
    while deal_no_deal != "h" and deal_no_deal != "s":
        
        deal_no_deal = input("Please enter h or s (h - Hit, s = Stand):")
        
    return deal_no_deal

#A function that prompts the user if they want to play/play again and validates the choice
def get_play_choice(prompt_text):
    
    to_play_game = input(prompt_text)
    
    while to_play_game != "y" and to_play_game != "n":
        
        to_play_game = input(prompt_text)
        
    print()
    print()
    
    return to_play_game

#A function that displays the details required for the assessment
def display_details():
    
    print("File    : peasm009.py")
    print("Author  : Scott Pearsall")
    print("Stud ID : 110313662")
    print("Email Id: peasm009")
    print("This is my own work as defined by the University's Academic Misconduct policy.")
    print()
    print()

#Displays the details
display_details()
        
play_again = get_play_choice("Would you like to play BlackJack [y|n]?")


#While the play again variable is set to positive, the game of blackjack runs.
while play_again == "y":

    print("---------------------- START GAME ----------------------")

    #lists to hold player and dealers hands
    player_hand = []


    dealer_hand = []
    
    #Deals a card and then adds them to the specified hand
    card = playing_cards.deal_one_card()
    player_hand.append(card)

    card = playing_cards.deal_one_card()
    player_hand.append(card)

    card = playing_cards.deal_one_card()
    dealer_hand.append(card)

    card = playing_cards.deal_one_card()
    dealer_hand.append(card)

    #Calls display hand functions to show both hands
    display_hand("Dealer's hand is", dealer_hand[0:1])

    display_hand("Player's hand is", player_hand)

    #Several if and statements to check for blackjack on either hand or push if both blackjack
    #with a final one to continue the game if no blackjack
    if get_hand_total(player_hand) == 21 and get_hand_total(dealer_hand) != 21:
        
        print()
        print("*** Blackjack! Player Wins! ***")
        
        won_index = won_index + 1
        played_index = played_index + 1
    
    elif get_hand_total(player_hand) == 21 and get_hand_total(dealer_hand) == 21:
        
        print()
        print("*** Blackjack --")
        
        display_hand("Dealer's hand is", dealer_hand)
        display_hand("Player's hand is", player_hand)
        
        print()
        print("***Blackjack! Push - no winners! ***")
        
        drawn_index = drawn_index + 1
        played_index = played_index + 1
    
    elif get_hand_total(dealer_hand) == 21 and get_hand_total(player_hand) != 21:
        
        print()
        display_hand("Dealer's hand is", dealer_hand)
        print()
        print("***Blackjack! Dealer Wins! ***")
        
        lost_index = lost_index + 1
        played_index = played_index + 1

    #If neither blackjack, play both hands
    elif get_hand_total(dealer_hand) != 21 and get_hand_total(player_hand) != 21:
        
        play_player_hand(player_hand)
        print()
        
        play_dealer_hand(dealer_hand)
        print()

        #If both get the same result, it's a draw
        if get_hand_total(player_hand) == get_hand_total(dealer_hand):
            
            print("--- Dealer:", get_hand_total(dealer_hand), "Player:", get_hand_total(player_hand), "-> Push - no winners! ---")

            won_index = won_index + 1
            played_index = played_index + 1

        #If dealer gets closer to blackjack without going over, dealer wins    
        elif get_hand_total(player_hand) < get_hand_total(dealer_hand) and get_hand_total(dealer_hand) <= 21 or get_hand_total(player_hand) > 21 and get_hand_total(dealer_hand) <= 21 :

            print("--- Dealer:", get_hand_total(dealer_hand), "Player:", get_hand_total(player_hand), "-> Dealer Wins! ---")

            lost_index = lost_index + 1
            played_index = played_index + 1

        #if player gets closer to blackjack without going over, player wins    
        elif get_hand_total(player_hand) > get_hand_total(dealer_hand) and get_hand_total(player_hand) <= 21 or get_hand_total(dealer_hand) > 21 and get_hand_total(player_hand) <= 21 :

            print("--- Dealer:", get_hand_total(dealer_hand), "Player:", get_hand_total(player_hand), "-> Player Wins! ---")

            won_index = won_index + 1
            played_index = played_index + 1
            
    print("----------------------- END GAME -----------------------")
    print()
    print("That was fun!")
    print()

    #Asks if the player wants to play again
    play_again = get_play_choice("Play again [y|n]?")

#If player chooses not to play again, stops the game and displays the statistics
if play_again == "n":
    
    print("You played", played_index, "games!")
    print(" -> Won:", won_index )
    print(" -> Lost:", lost_index )
    print(" -> Drawn:", drawn_index )
    print()
    print("Thanks for playing! :)")

            
