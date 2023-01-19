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

for dls in suits:
    for card1 in value:


         first_deck.append(card1 + " of " + dls)

hit_button_clicked = False
checkdeal = 1
#Dealers cards 
hit1 = False
hit2 = False
hit3 = False
h_count = 0
u = 1
j = 1
i = 1
h = 1
hit_button_clicked = False
sumdealer = 0

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
    print("DEALERS CARDS :",dealer)


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
    keys = pygame.key.get_pressed()



    if keys[pygame.K_h]:
        hit1 = True
    if hit1:
        if h == 1:


            y3 = random.choice(first_deck)
            first_deck.remove(y3)
            player.append(y3)
            image3 = pygame.image.load(f"{player[2]}.png")
            image3 = pygame.transform.scale(image3,(176,200))
            h = h + 1
            h_count = 1
            

        
        

        screen.blit(image3,(450,410))

    if keys[pygame.K_SPACE]:
        hit2 = True
    elif hit2:
        if u == 1 and h > 1:
            



            y4 = random.choice(first_deck)
            first_deck.remove(y4)
            player.append(y4)
            image4 = pygame.image.load(f"{player[3]}.png")
            image4 = pygame.transform.scale(image4,(176,200))
            u = u + 1
        screen.blit(image4,(650,410))



    
    
        

    
    
                


    #screen.blit(hit_text,(50,650)) 
    #screen.blit(stand_text,(400,650))
    screen.blit(hit_text_surface, hit_rect)
    screen.blit(stand_text_surface, stand_rect)


    """if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if hit_rect.collidepoint(mouse_pos):
                print("HIT button clicked!")
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if stand_rect.collidepoint(mouse_pos):
                print("STAND button clicked!")"""











    """hit = my_font.render("HIT",True,(8,8,8))
    stand = my_font.render("STAND",True,(8,8,8))
    screen.blit(hit,(50,650)) 
    screen.blit(stand,(400,650))
    textrect1 = hit.get_rect()
    textrect2 = stand.get_rect()
    textrect1.center = (50,650)
    textrect2.center = (400,650)
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    if textrect1.collidepoint(mouse_pos):
        text = my_font.render("HIT", True, (38, 255, 0))"""

    #score calculation
    count = 2
    tot = 0
    for dls in player:
        if dls[0] in ["J","K","Q"]:
            tot = tot + 10
        elif dls[0] in ["2","3","4","5","6","7","8","9"]:
            tot = tot + int(dls[0])
        elif dls[0] == "1":
            if dls[1] == "0":
                tot = tot + 10
            else:
                tot = tot + 1       
        else:
            tot = tot + 11
    print(tot)
    if count == 2:
        if tot == 21:
            wintxt = my_font.render("YOU WIN!!! ", True, (255, 250, 250))
            screen.blit(wintxt,(400,350))
    if tot > 21:
        screen.fill((0,0,255))
        losstxt = my_font.render("YOU HAVE EXCEEDED THE VALUE OF 21 AND GONE BUST",True,(255,250,250))
        screen.blit(losstxt,(50,350))
    if keys[pygame.K_s]:
        hit3 = True
    elif hit3:
        for dls in dealer:
            if checkdeal <= 2:
                print(dls[0])
                if dls[0] in ["J","K","Q"]:
                    sumdealer = sumdealer + 10
                elif dls[0] in ["2","3","4","5","6","7","8","9"]:
                    sumdealer = sumdealer + int(dls[0])
                elif dls[0] == "1":
                    if dls[1] == "0":
                        sumdealer = sumdealer + 10
                    else:
                        sumdealer = sumdealer + 1       
                else:
                    sumdealer = sumdealer + 11
            checkdeal = checkdeal + 1
        

            if sumdealer > tot:
                screen.fill((0,0,255))
                wintxt1 = my_font.render("YOU LOSE",True,(255,250,250))
            elif sumdealer > 21:
                screen.fill((0,153,25))
                wintxt2 = my_font.render("YOU WIN",True,(255,250,250))
            elif tot > sumdealer:
                wintxt3 = my_font.render("YOU WIN",True,(255,250,250))
                screen.fill((0,153,25))
                
            else:
                screen.fill((153,187,255))
                wintxt4 = my_font.render("YOU WIN",True,(255,250,250))

    print("SUMDEALER MONI : ",sumdealer)
            
            




    #screen.blit(image,(50,50))
    
    #text = my_font.render("Dealer's Cards : ", True, (8, 8, 8))
    #screen.blit(text,(50,10))

    pygame.display.update()

















