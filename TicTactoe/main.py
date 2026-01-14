# py -3.12 main.py
# py -3.12 F:\DCIT22-Acitivities-main\TicTactoe\main.py
import pygame
import sys
from tic_tac_toe import Game
from colors import *
from button import Button

pygame.init()

screen_width = 750
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")

clock = pygame.time.Clock()

background_image = pygame.image.load('./Images/Background_main.jpg').convert_alpha()
# logo = pygame.image.load('./Images/TicTacToe-remove
# bg-preview.png')

draw_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
draw_surface.fill((0,0,0,0))

#FONTS CUSTOMIZED
Header_title = pygame.font.Font('./Font/kids_magazine/Kids Magazine.ttf', 40)
BUTTON_FONT = pygame.font.Font('./Font/grobold/GROBOLD.ttf', 27)
# BUTTON_FONT = pygame.font.Font('./Font/compro_oro/Compro Oro.ttf', 27)

#BUTTON SETUP
start_button = Button(230, 250, 300, 80, "START", START_BUTTON_COLOR, START_BUTTON_HOVER_COLOR, BUTTON_FONT)
exit_button = Button(230, 340, 300, 80, "EXIT", EXIT_BUTTON_COLOR, EXIT_BUTTON_HOVER_COLOR, BUTTON_FONT)
simple_mode_button = Button(200, 250, 360, 80, "SIMPLE MODE", SIMPLE_MODE_BUTTON_COLOR, SIMPLE_MODE_BUTTON_HOVER_COLOR, BUTTON_FONT)
ultimate_mode_button = Button(200, 340, 360, 80, "ULTIMATE TIC TAC TOE", MODIFIED_MODE_BUTTON_COLOR, MODIFIED_MODE_BUTTON_HOVER_COLOR, BUTTON_FONT)
player_mode_button = Button(200, 250, 340, 80, "PLAYER VS PLAYER", PLAYER_MODE_BUTTON_COLOR, PLAYER_MODE_BUTTON_HOVER_COLOR, BUTTON_FONT)
computer_mode_button = Button(200, 340, 340, 80, "COMPUTER VS PLAYER", COMPUTER_MODE_BUTTON_COLOR, COMPUTER_MODE_BUTTON_HOVER_COLOR, BUTTON_FONT)

state_m = "start"
game = Game(draw_surface)

is_running = True
while is_running:
    mouse_position = pygame.mouse.get_pos()

    screen.blit(background_image, (-130, -220))
    # screen.blit(logo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if state_m == "start":
                if start_button.is_clicked(mouse_position):
                    state_m = "mode_selection"
                elif exit_button.is_clicked(mouse_position):
                    is_running = False
                    
            elif state_m == "mode_selection":
                if simple_mode_button.is_clicked(mouse_position):
                    state_m = "game_simple_mode"
                elif ultimate_mode_button.is_clicked(mouse_position):
                    state_m = "game_ultimate_mode"
                    
            elif state_m == "game_simple_mode":
                if player_mode_button.is_clicked(mouse_position):
                    print("PLAYER MODE")
                elif computer_mode_button.is_clicked(mouse_position):
                    print("COMPUTER MODE")
                    
            elif state_m == "game_ultimate_mode":
                if player_mode_button.is_clicked(mouse_position):
                    print("PLAYER MODE") 
                elif computer_mode_button.is_clicked(mouse_position):
                    print("COMPUTER MODE")

                    
                            
    if state_m == "start":
        start_button.button_update(mouse_position)
        exit_button.button_update(mouse_position)

    elif state_m == "mode_selection":
        simple_mode_button.button_update(mouse_position)
        ultimate_mode_button.button_update(mouse_position)
        
    elif state_m == "game_simple_mode":
        player_mode_button.button_update(mouse_position)
        computer_mode_button.button_update(mouse_position)
        
    elif state_m == "game_ultimate_mode":
        player_mode_button.button_update(mouse_position)
        computer_mode_button.button_update(mouse_position)

    # screen.fill(DARK_NAVY)

        #START BUTTON
    if state_m == "start":
        header = Header_title.render("TIC TAC TOE", True, WHITE)

        x_header_position = 180
        y_header_position = 100
        screen.blit(header, (x_header_position, y_header_position))
        start_button.draw_button_sets(screen)
        exit_button.draw_button_sets(screen)

        #MODE SELECTION
    elif state_m == "mode_selection":
        header = Header_title.render("SELECT MODE", True, WHITE)

        x_header_position = 180
        y_header_position = 100
        screen.blit(header, (x_header_position, y_header_position))
        simple_mode_button.draw_button_sets(screen)
        ultimate_mode_button.draw_button_sets(screen)
        
        #SIMPLE MODE
    elif state_m == "game_simple_mode":
        header = Header_title.render("SIMPLE MODE", True, WHITE)

        x_header_position = 180
        y_header_position = 100
        screen.blit(header, (x_header_position, y_header_position))
        player_mode_button.draw_button_sets(screen)
        computer_mode_button.draw_button_sets(screen)
        
        #ULTIMATE MODE
    elif state_m == "game_ultimate_mode":
        header = Header_title.render("ULTIMATE MODE", True, WHITE)

        x_header_position = 140
        y_header_position = 100
        screen.blit(header, (x_header_position, y_header_position))
        player_mode_button.draw_button_sets(screen)
        computer_mode_button.draw_button_sets(screen)

        #GAME
    # elif state_m == "game":
    #     game.update()
    #     screen.blit(draw_surface, (0,0))

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
sys.exit()