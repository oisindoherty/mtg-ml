#import tensorflow as tf
import random

def play_game(deck):
    opponent_life = 20
    turn = 0

    #bolt, guide, mountain
    hand = [0,0,0]

    field_lands = 0
    field_amana = 0
    field_guide = 0

    draw_pointer = 0

    for i in range(7):
        hand[deck[draw_pointer]] += 1
        draw_pointer += 1

    while opponent_life > 0 and draw_pointer != len(deck):
        turn += 1
        
        hand[deck[draw_pointer]] += 1
        draw_pointer += 1

        if hand[2] > 0:
            hand[2] -= 1
            field_lands += 1

        amana = field_lands

        if min(hand[0], amana) * 3 > opponent_life:
            while hand[0] > 0 and amana > 0:
                hand[0] -= 1
                amana -= 1
                opponent_life -= 3

        while hand[1] > 0 and amana > 0:
            hand[1] -= 1
            amana -= 1
            field_guide += 1

        while hand[0] > 0 and amana > 0:
            hand[0] -= 1
            amana -= 1
            opponent_life -= 3

        opponent_life -= field_guide * 2

    return turn

#bolt, guide, land
print("Lands\tBolts\tGuides\tAverage")
for lands in range(61):
    for bolts in range(61-lands):
        deck = []
        for land in range(lands):
            deck.append(2)
        for bolt in range(bolts):
            deck.append(0)
        for guide in range(60-lands-bolts):
            deck.append(1)

        average = 0
        
        for trial in range(1000):
            random.shuffle(deck)
            average += play_game(deck)

        average /= 1000

        print(str(lands) + "\t" + str(bolts) + "\t" +str(60-lands-bolts) + "\t" + str(average))
