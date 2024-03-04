import pygame
import time

pygame.init()

background = pygame.image.load("background.jpg")
background = pygame.transform.scale_by(background, 1.5)
click_obj = pygame.image.load("holygrail.png")
click_obj = pygame.transform.scale(click_obj, (click_obj.get_width() // 2, click_obj.get_height() // 2))
shop = pygame.image.load("shop.jpg")
shop = pygame.transform.scale_by(shop, 1.5)
holy_grail_final = pygame.image.load("holygrailfinal.jpg")
holy_grail_final = pygame.transform.scale_by(holy_grail_final, 2)

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("King Arthur Clicker")
font = pygame.font.SysFont("Quicksand", 36)
clock = pygame.time.Clock()
running = True
time_since_last_auto_click = 0
points = 0
total_auto_points_per_click = 0
time_to_end = 360

#points
point_per_click = 10000000000
green_knight_click_points_per_click = 4
gawain_click_points_per_click = 8
bedivere_click_points_per_click = 20
merlin_click_points_per_click = 60
guinevere_click_points_per_click = 160
morgaine_click_points_per_click = 400
lancelot_click_points_per_click = 1000
mordred_click_points_per_click = 2000
arthur_click_points_per_click = 50000

#prices
price_point_per_click = 1
price_green_knight = 120
price_gawain = 240
price_bedivere = 600
price_merlin = 1800
price_guinevere = 4800
price_morgaine = 12000
price_lancelot = 30000
price_mordred = 60000
price_arthur = 120000
price_holy_grail = 1000000

green_knight = False
gawain = False
bedivere = False
merlin = False
guinevere = False
morgaine = False
lancelot = False
mordred = False
arthur = False
holy_grail = False


shop_open = False  # Initialize the shop state

while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not shop_open:  # If the shop is closed
                if click_obj_rect.collidepoint(event.pos):
                    points += point_per_click
                elif shop_enter_rect.collidepoint(event.pos):
                    shop_open = True
            else:  # If the shop is open
                if exit_rect.collidepoint(event.pos):
                    shop_open = False
                elif player_click_upgrade_rect.collidepoint(event.pos) and points >= price_point_per_click:
                    point_per_click += 1
                    points -= price_point_per_click
                    price_point_per_click *= 1.15
                elif green_knight_auto_clicker_rect.collidepoint(event.pos) and points >= price_green_knight:
                    total_auto_points_per_click += green_knight_click_points_per_click
                    points -= price_green_knight
                    green_knight = True
                elif gawain_auto_clicker_rect.collidepoint(event.pos) and points >= price_gawain:
                    total_auto_points_per_click += gawain_click_points_per_click
                    points -= price_gawain
                    gawain = True
                elif bedivere_auto_clicker_rect.collidepoint(event.pos) and points >= price_bedivere:
                    total_auto_points_per_click += bedivere_click_points_per_click
                    points -= price_bedivere
                    bedivere = True
                elif merlin_auto_clicker_rect.collidepoint(event.pos) and points >= price_merlin:
                    total_auto_points_per_click += merlin_click_points_per_click
                    points -= price_merlin
                    merlin = True
                elif guinevere_auto_clicker_rect.collidepoint(event.pos) and points >= price_guinevere:
                    total_auto_points_per_click += guinevere_click_points_per_click
                    points -= price_guinevere
                    guinevere = True
                elif morgaine_auto_clicker_rect.collidepoint(event.pos) and points >= price_morgaine:
                    total_auto_points_per_click += morgaine_click_points_per_click
                    points -= price_morgaine
                    morgaine = True
                elif lancelot_auto_clicker_rect.collidepoint(event.pos) and points >= price_lancelot:
                    total_auto_points_per_click += lancelot_click_points_per_click
                    points -= price_lancelot
                    lancelot = True
                elif mordred_auto_clicker_rect.collidepoint(event.pos) and points >= price_mordred:
                    total_auto_points_per_click += mordred_click_points_per_click
                    points -= price_mordred
                    mordred = True
                elif arthur_auto_clicker_rect.collidepoint(event.pos) and points >= price_arthur:
                    total_auto_points_per_click += arthur_click_points_per_click
                    points -= price_arthur
                    arthur = True
                elif holy_grail_rect.collidepoint(event.pos) and points >= price_holy_grail:
                    points -= price_holy_grail
                    holy_grail = True

                    


    if not shop_open:  # If the shop is closed, draw the holy grail and shop text
        click_obj_rect = click_obj.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(click_obj, click_obj_rect)

        shop_enter_text = font.render("SHOP", True, (255, 160, 70))
        shop_enter_rect = shop_enter_text.get_rect(topleft=(50, 50))
        screen.blit(shop_enter_text, shop_enter_rect)
    else:  # If the shop is open, draw the shop background and exit text
        screen.blit(shop, (0, 0))
        exit_text = font.render("EXIT", True, (255, 0, 0))
        exit_rect = exit_text.get_rect(topleft=(50, 50))
        screen.blit(exit_text, exit_rect)

        # Draw upgrades
        player_click_upgrade = font.render(f"Points per click: {point_per_click} UPGRADE {round(price_point_per_click, 1)}", True, (255,255,255))
        player_click_upgrade_rect = player_click_upgrade.get_rect(center=(WIDTH / 2, 70))
        screen.blit(player_click_upgrade, player_click_upgrade_rect)

        # Green Knight
        green_knight_auto_clicker = font.render(f"Green Knight autoclick points: {green_knight_click_points_per_click} BUY {price_green_knight}", True, (255,255,255))
        green_knight_auto_clicker_rect = green_knight_auto_clicker.get_rect(center=(WIDTH / 2, 150))
        if not green_knight: screen.blit(green_knight_auto_clicker, green_knight_auto_clicker_rect)

        # Gawain
        gawain_auto_clicker = font.render(f"Gawain autoclick points: {gawain_click_points_per_click} BUY {price_gawain}", True, (255,255,255))
        gawain_auto_clicker_rect = gawain_auto_clicker.get_rect(center=(WIDTH / 2, 190))
        if not gawain: screen.blit(gawain_auto_clicker, gawain_auto_clicker_rect)

        # Bedivere
        bedivere_auto_clicker = font.render(f"Bedivere autoclick points: {bedivere_click_points_per_click} BUY {price_bedivere}", True, (255,255,255))
        bedivere_auto_clicker_rect = bedivere_auto_clicker.get_rect(center=(WIDTH / 2, 230))
        if not bedivere: screen.blit(bedivere_auto_clicker, bedivere_auto_clicker_rect)

        # Merlin
        merlin_auto_clicker = font.render(f"Merlin autoclick points: {merlin_click_points_per_click} BUY {price_merlin}", True, (255,255,255))
        merlin_auto_clicker_rect = merlin_auto_clicker.get_rect(center=(WIDTH / 2, 270))
        if not merlin: screen.blit(merlin_auto_clicker, merlin_auto_clicker_rect)

        # Guinevere
        guinevere_auto_clicker = font.render(f"Guinevere autoclick points: {guinevere_click_points_per_click} BUY {price_guinevere}", True, (255,255,255))
        guinevere_auto_clicker_rect = guinevere_auto_clicker.get_rect(center=(WIDTH / 2, 310))
        if not guinevere: screen.blit(guinevere_auto_clicker, guinevere_auto_clicker_rect)

        # Morgaine
        morgaine_auto_clicker = font.render(f"Morgaine autoclick points: {morgaine_click_points_per_click} BUY {price_morgaine}", True, (255,255,255))
        morgaine_auto_clicker_rect = morgaine_auto_clicker.get_rect(center=(WIDTH / 2, 350))
        if not morgaine: screen.blit(morgaine_auto_clicker, morgaine_auto_clicker_rect)

        # Lancelot
        lancelot_auto_clicker = font.render(f"Lancelot autoclick points: {lancelot_click_points_per_click} BUY {price_lancelot}", True, (255,255,255))
        lancelot_auto_clicker_rect = lancelot_auto_clicker.get_rect(center=(WIDTH / 2, 390))
        if not lancelot: screen.blit(lancelot_auto_clicker, lancelot_auto_clicker_rect)

        # Mordred
        mordred_auto_clicker = font.render(f"Mordred autoclick points: {mordred_click_points_per_click} BUY {price_mordred}", True, (255,255,255))
        mordred_auto_clicker_rect = mordred_auto_clicker.get_rect(center=(WIDTH / 2, 440))
        if not mordred: screen.blit(mordred_auto_clicker, mordred_auto_clicker_rect)

        # Arthur
        arthur_auto_clicker = font.render(f"Arthur autoclick points: {arthur_click_points_per_click} BUY {price_arthur}", True, (255,255,255))
        arthur_auto_clicker_rect = arthur_auto_clicker.get_rect(center=(WIDTH / 2, 480))
        if not arthur: screen.blit(arthur_auto_clicker, arthur_auto_clicker_rect)

        # Win condition
        holy_grail_text = pygame.font.SysFont("Quicksand", 72).render("BUY THE HOLY GRAIL!!! 1,000,000", True, (255, 160, 70))
        holy_grail_rect = holy_grail_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        if green_knight and gawain and bedivere and merlin and guinevere and morgaine and lancelot and mordred and arthur:
            screen.blit(holy_grail_text, holy_grail_rect)

        # Holy Grail
        if holy_grail:
            screen.blit(holy_grail_final, (0,0))
            holy_grail_final_text = pygame.font.SysFont("Quicksand", 72).render("YOU WIN!!", True, (255, 160, 70))
            holy_grail_final_rect = holy_grail_final_text.get_rect(center=(WIDTH / 2, 100))
            screen.blit(holy_grail_final_text, holy_grail_final_rect)
            time_to_end -= 1
       




    # Points
    points_text = font.render(f"Chivalry: {round(points, 1)}", True, (255, 160, 70))
    points_rect = points_text.get_rect(center=(WIDTH/2, 550))
    screen.blit(points_text, points_rect)

    if time_since_last_auto_click == 60:
        points += total_auto_points_per_click
        time_since_last_auto_click = 0

    if time_to_end == 0:
        running = False

    time_since_last_auto_click += 1

    pygame.display.flip()

    clock.tick(60)

pygame.quit()


