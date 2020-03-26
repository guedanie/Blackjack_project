# Black Jack Basic Strategy Program
    # Follows basic strategy for "Dealer Stands on Soft 17"
    # Based on chards in: https://wizardofodds.com/games/blackjack/strategy/4-decks/

def input_cards():
    print("What are the two cards you have?")
    card_1 = int(input("Card one is: "))
    card_2 = int(input("Card two is: "))

    print("What card does the dealer have?")
    dealer = int(input("Dealer card is: "))

    return ([card_1, card_2], dealer)

def black_jack_suggestion(hand, dealer_card):
    hard_count=sum(hand)
    cards=len(hand)
    aces_count= 1*(1 in hand)
    soft_count=hard_count
    
    if cards < 2:
        return 'Not enough cards'
    
    if hard_count <= 11:
        soft_count= hard_count + 10 * aces_count
        
    if cards == 2 and soft_count== 21:
        return 'Blackjack'
    
    
    if soft_count >= 19:
        return 'Stay'
    
    if hand == [9,9] and dealer_card not in [1,7,10]:
        return 'Split'
    
    if hard_count >= 17 :
        return 'Stay'

    
    if cards>2:
        if hard_count==soft_count:
            if hard_count<=11:
                return 'Hit'

            if hard_count==12 and dealer_card <=3:
                return 'Hit'

            if dealer_card in [1,7,8,9,10]:
                return 'Hit'

            return 'Stay'
        
        
        if soft_count<=17:
            return 'Hit'
        
        if soft_count==18 and dealer_card in [1,9,10]:
            return 'Hit'
        
        
        
        return 'Stay'
    
            
        
    
    if cards==2:
        
        if hand[0]==hand[1]:
            card= hand[0]
            
            if card==1 or card==11:
                return 'Split'
            
            if card==8 and dealer_card!=1:
                return 'Split'
            
            if card in [2,3,7] and dealer_card not in [1,8,9,10]:
                return 'Split'
            
            if card==6 and dealer_card not in [1,7,8,9,10]:
                return 'Split'
            
            if card==4 and dealer_card in [5,6]:
                return 'Split'

            
        if hard_count==soft_count:
            
            if hard_count==11 and dealer_card!=1:
                return 'Double'
            
            if hard_count==10 and dealer_card not in [1,10]:
                return 'Double'
            
            if hard_count==9 and dealer_card not in [1, 2,7,8,9,10]:
                return 'Double'
            
            if hard_count<=11:
                return 'Hit'

            if hard_count==12 and dealer_card <=3:
                return 'Hit'

            if dealer_card in [1,7,8,9,10]:
                return 'Hit'

            return 'Stay'
            
        
        if hard_count!=soft_count:
            

                
            if soft_count==18:
                
                if dealer_card not in [1,2,7,8,9,10]:
                    return 'Double'
                
                if dealer_card in [2,7,8]:
                    return 'Stay'
                
            if soft_count==17 and dealer_card in [3,4,5,6]:
                return 'Double'
            
            if soft_count in [15,16] and dealer_card in [4,5,6]:
                return 'Double'
            
            if soft_count in [13,14] and dealer_card in [5,6]:
                return 'Double'
            
            return 'Hit'
        

player_cards, dealer_card = input_cards()
suggestion = black_jack_suggestion(player_cards, dealer_card)
print(f"You should: {suggestion}")