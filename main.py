import pygame
import random


pygame.init()


screen = pygame.display.set_mode((900, 750))
pygame.display.set_caption("BLACKJACK")

my_font = pygame.font.SysFont('Comic Sans MS', 30)


#Main part
#creating deck 

first_deck = []
#creating an empty list

value = ["Ace","2","3","4","5","6","7","8","9","10","J","Q","K"]
suits = ["Spades","Hearts","Diamonds","Clubs"]

for card in suits:
    for card1 in value:


         first_deck.append(card1 + " of " + card)

hit_button_clicked = False
#Dealers cards 

j = 1
i = 1

flag_p1 = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((107,5,7))



    #Dealer's Cards
    if i == 1:

        dealer = []
        x = random.choice(first_deck)
        first_deck.remove(x)
        dealer.append(x)
        x2 = random.choice(first_deck)
        first_deck.remove(x2)
        dealer.append(x2)
        i = i + 1


    text = my_font.render("Dealer's Cards : ", True, (255, 250, 250))
    screen.blit(text,(50,10))

    image = pygame.image.load(f"{dealer[0]}.png")

    image = pygame.transform.scale(image, (176, 200)) #size of image
    screen.blit(image,(50,70))

    text = my_font.render("X", True, (8, 8, 8))
    screen.blit(text,(400,50))

    #Player's Cards

    if j == 1:
        player = []

        y = random.choice(first_deck)
        first_deck.remove(y)
        player.append(y)
        y2 = random.choice(first_deck)
        first_deck.remove(y2)
        player.append(y2)
        j = j + 1

    #displaying players cards

    text1 = my_font.render("Player's Cards : ", True, (255, 250, 250))
    screen.blit(text1,(50,350))
    image1 = pygame.image.load(f"{player[0]}.png")
    image1 = pygame.transform.scale(image1,(176,200))
    screen.blit(image1,(50,410))
    image2 = pygame.image.load(f"{player[1]}.png")
    image2 = pygame.transform.scale(image2,(176,200))
    screen.blit(image2,(250,410))
    hit_button_clicked = False
    #hitandstandbutton
    hit_text = "HIT"
    
    hit_text_surface = my_font.render(hit_text, True, (8, 8, 8))
    hit_rect = hit_text_surface.get_rect()
    hit_rect.center = (50, 650)

    stand_text = "STAND"
    
    stand_text_surface = my_font.render(stand_text, True, (8, 8, 8))
    stand_rect = stand_text_surface.get_rect()
    stand_rect.center = (400, 650)
    
    mouse_state = pygame.mouse.get_pressed()

    # Check if the left mouse button is pressed
    if mouse_state[0] == 1:
        # Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Check if the HIT button is clicked
        if hit_rect.collidepoint(mouse_pos):
            hit_button_clicked = not hit_button_clicked
            if hit_button_clicked:
                
                flag_p1 = True
    
    if flag_p1:
        when_hit_secondcard = pygame.image.load(f"{player[1]}.png")
        when_hit_secondcard = pygame.transform.scale(when_hit_secondcard,(176,200))
        screen.blit(when_hit_secondcard,(450,410))
        mouse_state[0] == 0
    
                




        """if hit_rect.collidepoint(mouse_pos):
            when_hit_secondcard = pygame.image.load(f"{player[1]}.png")
            when_hit_secondcard = pygame.transform.scale(when_hit_secondcard,(176,200))
            screen.blit(when_hit_secondcard,(750,410))"""


        # Check if the STAND button is clicked
        if stand_rect.collidepoint(mouse_pos):
            print("STAND button clicked!")






    #screen.blit(hit_text,(50,650)) 
    #screen.blit(stand_text,(400,650))
    screen.blit(hit_text_surface, hit_rect)
    screen.blit(stand_text_surface, stand_rect)
