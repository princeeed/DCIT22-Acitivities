# py -3.12 F:\pygame\pygame_GUI\startingUI.py
import pygame
import sys

pygame.init()

screen_width = 750
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe Starting")

clock = pygame.time.Clock()

background_image = pygame.image.load('./Images/Background_main.jpg')
# logo = pygame.image.load('./Images/TicTacToe-removebg-preview.png')

#COLORS AREA
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200) 
LIGHT_GRAY = (220, 220, 220)
DARK_GRAY = (100, 100, 100)
BLUE = (70, 130, 200)
LIGHT_BLUE = (100, 160, 230)
GREEN = (76, 175, 80)
LIGHT_GREEN = (106, 205, 110)

START_BUTTON_COLOR = (65, 186, 182) 
START_BUTTON_HOVER_COLOR = (121, 217, 214)
EXIT_BUTTON_COLOR = (163, 0, 76)
EXIT_BUTTON_HOVER_COLOR = (204, 2, 96)
SIMPLE_MODE_BUTTON_COLOR = (250, 168, 5)
SIMPLE_MODE_BUTTON_HOVER_COLOR = (242, 178, 51)  
MODIFIED_MODE_BUTTON_COLOR = (65, 186, 182)
MODIFIED_MODE_BUTTON_HOVER_COLOR = (121, 217, 214)

class Button():
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        
    def drawButtonSets(self, surface):
        #BUTTON SHADOW
        shadow_rect = self.rect.copy()
        shadow_rect.y += 5
        pygame.draw.rect(screen, DARK_GRAY, shadow_rect, border_radius=20)
        
        #BUTTON AND BORDER
        pygame.draw.rect(surface, self.current_color, self.rect,  border_radius=20) #BUTTON
        pygame.draw.rect(surface, WHITE, self.rect, 1, border_radius=20) #BORDER
        
        #TEXT
        text_surface = buttons_font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def updatesB(self, mouse_posi):
        if self.rect.collidepoint(mouse_posi):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color
        
    def is_clickedB(self, mouse_posi):
        return self.rect.collidepoint(mouse_posi)

#FONTS CUSTOMIZED
Header_title = pygame.font.Font('./Font/kids_magazine/Kids Magazine.ttf', 40)
buttons_font = pygame.font.Font('./Font/grobold/GROBOLD.ttf', 27)
# buttons_font = pygame.font.Font('./Font/compro_oro/Compro Oro.ttf', 27)

#BUTTON SETUP
start_button = Button(230, 250, 300, 80, "START", START_BUTTON_COLOR, START_BUTTON_HOVER_COLOR)
exit_button = Button(230, 340, 300, 80, "EXIT", EXIT_BUTTON_COLOR, EXIT_BUTTON_HOVER_COLOR)
simpleMode_button = Button(200, 250, 360, 80, "SIMPLE MODE", SIMPLE_MODE_BUTTON_COLOR, SIMPLE_MODE_BUTTON_HOVER_COLOR)
modifieMode_button = Button(200, 340, 360, 80, "ULTIMATE TIC TAC TOE", MODIFIED_MODE_BUTTON_COLOR, MODIFIED_MODE_BUTTON_HOVER_COLOR)

state_m = "start"

is_running = True
while is_running:
    mouse_posi = pygame.mouse.get_pos()
    
    screen.blit(background_image, (-130, -220))
    # screen.blit(logo, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if state_m == "start":
                if start_button.is_clickedB(mouse_posi):
                    state_m = "mode_selection"
                elif exit_button.is_clickedB(mouse_posi):
                    is_running = False
                    
            elif state_m == "mode_selection":
                if simpleMode_button.is_clickedB(mouse_posi):
                    print("Simple Mode Selected")
                    #PAKI LAGAY DITO YUNG SET NG SIMPLE MODE
                elif modifieMode_button.is_clickedB(mouse_posi):
                    print("Ultimate Tic tac toe Mode Selected")
                    #PAKI LAGAY DITO YUNG SET NG ULTIMATE MODE
                
        #
    if state_m == "start":
        start_button.updatesB(mouse_posi)
        exit_button.updatesB(mouse_posi)
        
    elif state_m == "mode_selection":
        simpleMode_button.updatesB(mouse_posi)
        modifieMode_button.updatesB(mouse_posi)
    
    # screen.fill(DARK_NAVY)
    
        #START BUTTON
    if state_m == "start":
        header_title = Header_title.render("TIC TAC TOE", True, WHITE)
        x_HeaderPosition = 180
        y_HeaderPosition = 100
        screen.blit(header_title, (x_HeaderPosition, y_HeaderPosition))
        start_button.drawButtonSets(screen)
        exit_button.drawButtonSets(screen)

        #MODE SELECTION 
    elif state_m == "mode_selection":
        header_title = Header_title.render("SELECT MODE", True, WHITE)
        x_HeaderPosition = 180
        y_HeaderPosition = 100
        screen.blit(header_title, (x_HeaderPosition, y_HeaderPosition))
        simpleMode_button.drawButtonSets(screen)
        modifieMode_button.drawButtonSets(screen)

    
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
sys.exit()