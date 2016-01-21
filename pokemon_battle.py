#Pokemon Battle 
#By Banji Afolabi

'''
Copyright (C) 2016  Banji Afolabi

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Move image boxes from Pokémon Online.

Pokémon © 2002-2016 Pokémon. © 1995-2016 Nintendo/Creatures Inc./GAME FREAK inc. TM, ® and Pokémon character names are trademarks of Nintendo.
'''

import pygame, sys, random, time
from pygame.locals import *

#IMAGES
battleFieldImg = ((pygame.image.load('images/battlefield0.png'), pygame.image.load('images/battlefield0bg.png')),
                  (pygame.image.load('images/battlefield1.png'), pygame.image.load('images/battlefield1bg.png')),
                  (pygame.image.load('images/battlefield2.png'), pygame.image.load('images/battlefield2bg.png')))
pageOneBack = pygame.image.load('images/page1bg.png')
startButton = pygame.image.load('images/pokEball.png')


#PIXEL CONSTANTS
BFWIDTH = 432
BFHEIGHT = 265
HUDHEIGHT = 88
HUDGAP = 10
WINDOWWIDTH = 692
WINDOWHEIGHT = 618
L_MOVE_W = 130
R_MOVE_W = 346
T_MOVE_H = 378
B_MOVE_H = 444
MOVES_HEIGHT = 147
HELPBOXHEIGHT = HUDHEIGHT + HUDGAP + BFHEIGHT + MOVES_HEIGHT #510
HELPSTACKTOP = (WINDOWHEIGHT - HELPBOXHEIGHT,) #DO NOT CHANGE THIS VALUE ANYWHERE IN THIS CODE, EVER!
blazikenCoords = (170, 218)

#COLORS      R    G    B
WHITE    = (255, 255, 255)
GREY     = (128, 128, 128)
BLACK    = (  0,   0,   0)

#MOVEDEX
class Move():
    def __init__(self, name, img, typ, category, basepower, accuracy):
        self.name = name 
        self.image = img
        self.type = typ
        self.category = category
        self.basepower = basepower
        self.accuracy = accuracy
        
SWORDSDANCE = Move('Swords Dance', pygame.image.load('images/swordsdance.png'), 'Normal', 'Other', None, None)
NASTYPLOT = Move('Nasty Plot', pygame.image.load('images/nastyplot.png'), 'Dark', 'Other', None, None) 
COSMICPOWER = Move('Cosmic Power', pygame.image.load('images/cosmicpower.png'), 'Psychic', 'Other', None, None) 
HPUP = Move('HP Up', pygame.image.load('images/hpup.png'), 'Psychic', 'Other', None, None)
        
FLAREBLITZ = Move('Flare Blitz', pygame.image.load('images/flareblitz.png'), 'Fire', 'Physical', 120, 100) 
HJK = Move('High Jump Kick', pygame.image.load('images/hjk.png'), 'Fighting', 'Physical', 130, 90) 
STONEEDGE = Move('Stone Edge', pygame.image.load('images/stoneedge.png'), 'Rock', 'Physical', 100, 80) 
THUNDERPUNCH = Move('Thunder Punch', pygame.image.load('images/thunderpunch.png'), 'Electric', 'Physical', 75, 100) 

VACUUMWAVE = Move('Vacuum Wave', pygame.image.load('images/vacuumwave.png'), 'Fighting', 'Special', 40, 100) 
FLAMETHROWER = Move('Flamethrower', pygame.image.load('images/flamethrower.png'), 'Fire', 'Special', 95, 100)
OVERHEAT = Move('Overheat', pygame.image.load('images/overheat.png'), 'Fire', 'Special', 140, 90)
SOLARBEAM = Move('Solar Beam', pygame.image.load('images/solarbeam.png'), 'Grass', 'Special', 120, 100)

blazikenMove = ((SWORDSDANCE, NASTYPLOT, COSMICPOWER, HPUP), (HJK, FLAREBLITZ, STONEEDGE, THUNDERPUNCH), (VACUUMWAVE, FLAMETHROWER, OVERHEAT, SOLARBEAM))

PSYSTRIKE = Move('Psystrike', None, 'Psychic', 'Physical', 100, 100) 
CALMMIND = Move('Calm Mind', None, 'Psychic', 'Other', None, None)
FOCUSBLAST = Move('Focus Blast', None, 'Fighting', 'Special', 120, 70)
SHADOWBALL = Move('Shadow Ball', None, 'Ghost', 'Special', 80, 100)
mewtwoMove = (PSYSTRIKE, CALMMIND, FOCUSBLAST, SHADOWBALL)

DRAGONCLAW = Move('Dragon Claw', None, 'Dragon', 'Physical', 80, 100) 
FIREPUNCH = Move('Fire Punch', None, 'Fire', 'Physical', 75, 100)
EARTHQUAKE = Move('Earthquake', None, 'Ground', 'Physical', 100, 100)
DRAGONDANCE = Move('Dragon Dance', None, 'Dragon', 'Other', None, None)
dragoniteMove = (DRAGONCLAW, FIREPUNCH, EARTHQUAKE, DRAGONDANCE)

SYNTHESIS = Move('Synthesis', None, 'Grass', 'Other', None, None) 
GIGADRAIN = Move('Giga Drain', None, 'Grass', 'Special', 75, 100)
SLUDGEBOMB = Move('Sludge Bomb', None, 'Poison', 'Special', 90, 100)
mvenusaurMove = (SYNTHESIS, GIGADRAIN, EARTHQUAKE, SLUDGEBOMB)

SACREDFIRE = Move('Sacred Fire', None, 'Fire', 'Physical', 100, 90)
BRAVEBIRD = Move('Brave Bird', None, 'Flying', 'Physical', 120, 100)
ROOST = Move('Roost', None, 'Flying', 'Other', None, None)
hoohMove = (SACREDFIRE, BRAVEBIRD, ROOST, EARTHQUAKE)

PSYCHIC = Move('Psychic', None, 'Psychic', 'Special', 90, 100)
AEROBLAST = Move('Aeroblast', None, 'Flying', 'Special', 100, 95)
lugiaMove = (PSYCHIC, AEROBLAST, ROOST, CALMMIND)

CURSE = Move('Curse', None, 'Ghost', 'Other', None, None)
CRUNCH = Move('Crunch', None, 'Dark', 'Physical', 80, 100)
mtyranitarMove = (CURSE, CRUNCH, STONEEDGE, EARTHQUAKE)

groudonMove = (EARTHQUAKE, STONEEDGE, FIREPUNCH, DRAGONCLAW)

HYDROPUMP = Move('Hydro Pump', None, 'Water', 'Special', 120, 80) 
SURF = Move('Surf', None, 'Water', 'Special', 95, 100)
ICEBEAM = Move('Ice Beam', None, 'Ice', 'Special', 95, 100)
THUNDERBOLT = Move('Thunderbolt', None, 'Electric', 'Special', 95, 100)
kyogreMove = (HYDROPUMP, SURF, ICEBEAM, THUNDERBOLT)

BRICKBREAK = Move('Brick Break', None, 'Fighting', 'Physical', 75, 100)
rayquazaMove = (DRAGONDANCE, DRAGONCLAW, EARTHQUAKE, BRICKBREAK)


#PokeDex 
class Pokemon():
    def __init__(self, name, img, type1, type2, hp, atk, df, satk, sdf, spe, hudtext, hudtype, moves):
        self.name = name
        self.image = img
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.attack = atk
        self.defense = df
        self.sattack = satk
        self.sdefense = sdf
        self.speed = spe
        self.hudtext = hudtext
        self.hudtype = hudtype
        self.moves = moves
        self.chp = hp
    
    accuracymod = 1 
    evasionmod = 1
    attackmod = 1
    defensemod = 1
    sattackmod = 1
    sdefensemod = 1
    speedmod = 1
    
blaziken =  Pokemon('Blaziken', pygame.image.load('images/blazikenback.png'), 'Fire', 'Fighting', 364 * 1.75, 372, 284, 350, 284, 284 * 1.5, pygame.image.load('images/blazikenhud.png'),
                    pygame.image.load('images/blaztype.png'), None)

mewtwo =  Pokemon('Mewtwo', pygame.image.load('images/mewtwo.png'), 'Psychic', None, 354, 447, 216, 447, 216, 359, pygame.image.load('images/mew2hud.png'),
                    pygame.image.load('images/mew2type.png'), mewtwoMove)

dragonite =  Pokemon('Dragonite', pygame.image.load('images/dragonite.png'), 'Dragon', 'Flying', 324, 403, 226, 212, 236, 259, pygame.image.load('images/nitehud.png'),
                    pygame.image.load('images/nitetype.png'), dragoniteMove)

mvenusaur =  Pokemon('Venusaur', pygame.image.load('images/megavenusaur.png'), 'Grass', 'Poison', 364, 236, 310, 343, 276, 177, pygame.image.load('images/mvenhud.png'),
                    pygame.image.load('images/mventype.png'), mvenusaurMove)

hooh =  Pokemon('Ho-Oh', pygame.image.load('images/hooh.png'), 'Fire', 'Flying', 353 * 1.5, 394, 216 * 1.5, 230, 345, 279, pygame.image.load('images/hoohhud.png'),
                    pygame.image.load('images/hoohtype.png'), hoohMove)

lugia =  Pokemon('Lugia', pygame.image.load('images/lugia.png'), 'Psychic', 'Flying', 416, 194, 296, 306, 344, 257, pygame.image.load('images/lugiahud.png'),
                    pygame.image.load('images/lugiatype.png'), lugiaMove)

mtyranitar =  Pokemon('Tyranitar', pygame.image.load('images/mtyranitar.png'), 'Rock', 'Dark', 404, 469, 336, 226, 248, 178, pygame.image.load('images/mttarhud.png'),
                    pygame.image.load('images/mttartype.png'), mtyranitarMove)

groudon =  Pokemon('Groudon', pygame.image.load('images/groudon.png'), 'Ground', None, 404, 337, 379, 212, 237, 216, pygame.image.load('images/groudonhud.png'),
                    pygame.image.load('images/groudontype.png'), groudonMove)

kyogre =  Pokemon('Kyogre', pygame.image.load('images/kyogre.png'), 'Water', None, 404, 212, 217, 369, 216, 279, pygame.image.load('images/kyogrehud.png'),
                    pygame.image.load('images/kyogretype.png'), kyogreMove)

rayquaza =  Pokemon('Rayquaza', pygame.image.load('images/rayquaza.png'), 'Dragon', 'Flying', 351, 438, 216, 302, 216, 289, pygame.image.load('images/rayquazahud.png'),
                    pygame.image.load('images/raytype.png'), rayquazaMove)

eps1 = [mewtwo, dragonite, mvenusaur] #Stage 1 enemy pokemon
eps2 = [hooh, lugia, mtyranitar] #Stage 2 enemy pokemon
eps3 = [groudon, kyogre, rayquaza] #Stage 3 enemy pokemon

statboost = [1, 1.5, 2, 2.5, 3, 3.5, 4]
statdrop = [1, 0.66, 0.5, 0.4, 0.33, 0.29, 0.25]

def main():
    global DISPLAYSURF, log_text_top, font, log_text, e_set, eventfont, blaziken 
    pygame.init()
    
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH , WINDOWHEIGHT)) #find out how to set icons
    pygame.display.set_caption('Pokemon Battle')
    
    #Reset paradigms and all variables that need resetting
    WINDOWPAGE = 1 #Should start at 1
    STAGE = 1 #should start at 1
    
    stage1anim = 1
    stage2anim = 1
    stage3anim = 1
    
    #PARADIGM SYSTEM VARIABLES
    SYNERGIST = 0
    COMMANDO = 1
    RAVAGER = 2
   
    paradigm = COMMANDO #DEFAULT PARADIGM

    leftParadigmShiftButton = pygame.Rect(0, HUDHEIGHT+HUDGAP+BFHEIGHT+15, L_MOVE_W/2, 132)
    rightParadigmShiftButton = pygame.Rect(BFWIDTH + L_MOVE_W + L_MOVE_W/2, HUDHEIGHT+HUDGAP+BFHEIGHT+15, L_MOVE_W/2, 132)
    
    font = pygame.font.Font(None, 28) 
    eventfont = pygame.font.Font(None, 100)
    
    log_text = [None, None, None, None, None, None, None, None]
    log_text_top = 0 #max is 7
    
    while True: #The Main Game Loop
        
        if WINDOWPAGE == 1:
            
            DISPLAYSURF.blit(pageOneBack, (0, 0))
            DISPLAYSURF.blit(startButton, (310, 500))
            startButtonCoords = pygame.Rect(310, 500, 64, 64)
            
            
            for event in pygame.event.get(): #Page 1 Event Handler

                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:

                   mouse_pos = pygame.mouse.get_pos()
                   if (startButtonCoords.collidepoint(mouse_pos)): #Start Button
                       WINDOWPAGE = 2

        if WINDOWPAGE == 2:

            DISPLAYSURF.blit(pygame.image.load('images/megaken.png'), (0, 0))
            releaseBlaziken = pygame.Rect(534, 307, 64, 74)
            
            for event in pygame.event.get(): #Page 2 Event Handler

                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:
                    
                   mouse_pos = pygame.mouse.get_pos()
                   if (releaseBlaziken.collidepoint(mouse_pos)):
                       WINDOWPAGE = 3
         

        if WINDOWPAGE == 3:
            
           if STAGE == 1:
            DISPLAYSURF.blit(battleFieldImg[0][1], (0, 0)) #fill with background image

            #Stage 1 Animation
            if stage1anim == 1:
                DISPLAYSURF.blit(pygame.image.load('images/stage1.png'), (L_MOVE_W, HUDHEIGHT+10))
                pygame.display.update()
                time.sleep(3)
                stage1anim = 0

            #Battle Field Window    
            DISPLAYSURF.blit(battleFieldImg[0][0], (L_MOVE_W, HUDHEIGHT+10)) #battle field image (same as bg)
            pygame.draw.rect(DISPLAYSURF, BLACK, (L_MOVE_W, HUDHEIGHT+10, BFWIDTH, BFHEIGHT), 3) #battle field rect/container

            #HUD
            DISPLAYSURF.blit(pygame.image.load('images/hud.png'), (0, 0)) #hud

            #Blaziken & Blaziken's Stats
            DISPLAYSURF.blit(blaziken.hudtext, (0, 0)) #load blaziken's name on the hud
            DISPLAYSURF.blit(blaziken.hudtype, (-5, 22)) #blaziken's type
            DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (0, 26)) #hp container of blaziken image
            DISPLAYSURF.blit(blaziken.image, blazikenCoords)
            health_string = str(int((blaziken.chp / blaziken.hp) * 100))
            if health_string == '0' and blaziken.chp != 0:
                health_string = str((blaziken.chp / blaziken.hp) * 100)
                textSurf = font.render(health_string[0:4] + "%" , True, BLACK)
            else:    
                textSurf = font.render(health_string + "%" , True, BLACK)
            textSurfRect = textSurf.get_rect() 
            textSurfRect.topleft = (35, 42)
            DISPLAYSURF.blit(textSurf, textSurfRect)
            
            if stage1anim == 0: #just uses the stage 1 animation flag as there's no risk, these are just to make sure this only happens the first time
                DISPLAYSURF.blit(pygame.image.load('images/3reserve.png'), (347, 26))
                pygame.display.update()
                time.sleep(2)
                cs1p = 0 #current stage 1 pokemon is the first one
                stage1anim = 2

            #Current Enemy   
            DISPLAYSURF.blit(eps1[cs1p].hudtext, (345, 0)) #load hud of enemy
            DISPLAYSURF.blit(eps1[cs1p].hudtype, (340, 25)) #enemy's typing
            DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (347, 26)) #hp container image of enemy            
            if eps1[cs1p] == lugia:
                DISPLAYSURF.blit(eps1[cs1p].image, (218 + 130 +20, HUDHEIGHT + 10))
            elif eps1[cs1p] == groudon: 
                DISPLAYSURF.blit(eps1[cs1p].image, (218+130+30, 140))
            elif eps1[cs1p] == kyogre:
                DISPLAYSURF.blit(eps1[cs1p].image, (218+130+30, 160))
            elif eps1[cs1p] == mvenusaur or eps1[cs1p] == mtyranitar:
                DISPLAYSURF.blit(eps1[cs1p].image, (218+130+35, 140))
            elif eps1[cs1p] == dragonite: 
                DISPLAYSURF.blit(eps1[cs1p].image, (218+130+30, 140))
            elif eps1[cs1p] == hooh: 
                DISPLAYSURF.blit(eps1[cs1p].image, (218+130+25, 100))
            elif eps1[cs1p] == rayquaza: 
                DISPLAYSURF.blit(eps1[cs1p].image, (218+130+45, 100))
            elif eps1[cs1p] == mewtwo:
                DISPLAYSURF.blit(eps1[cs1p].image, (218+130+25, 145))
                
            health_string2 = str(int((eps1[cs1p].chp / eps1[cs1p].hp) * 100))
            if health_string2 == '0' and eps1[cs1p].chp != 0:
                health_string2 = str((eps1[cs1p].chp / eps1[cs1p].hp) * 100)
                textSurf2 = font.render(health_string2[0:4] + "%" , True, BLACK)
            else:    
                textSurf2 = font.render(health_string2 + "%" , True, BLACK)
            
            textSurfRect2 = textSurf2.get_rect() 
            textSurfRect2.topleft = (382, 42)
            DISPLAYSURF.blit(textSurf2, textSurfRect2)
            
            if cs1p == 0: #if current pokemon is the first, there are 2 left
                DISPLAYSURF.blit(pygame.image.load('images/2reserve.png'), (347, 26))
            elif cs1p == 1: #if current pokemon is the second, there is 1 left
                DISPLAYSURF.blit(pygame.image.load('images/1reserve.png'), (347, 26))
            #if the current pokemon is the last(3), no image gets shown
            
            #help box
            pygame.draw.rect(DISPLAYSURF, GREY, (0, HELPBOXHEIGHT, WINDOWWIDTH, WINDOWHEIGHT - (HELPBOXHEIGHT)), 0)
            pygame.draw.rect(DISPLAYSURF, BLACK, (0, HELPBOXHEIGHT, WINDOWWIDTH, WINDOWHEIGHT - (HELPBOXHEIGHT)), 6)
            
            for event in pygame.event.get(): #Page 3 Event Handler

                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:

                   mouse_pos = pygame.mouse.get_pos()
                   
                   #PARADIGM SHIFT CHECK
                   if (leftParadigmShiftButton.collidepoint(mouse_pos)):
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       if paradigm == COMMANDO:
                           
                           paradigm = SYNERGIST
                           
                           log_text[log_text_top] = pygame.image.load('images/synshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps1[cs1p])

                           if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2
                                                
                           
                       elif paradigm == RAVAGER:
                           
                           paradigm = COMMANDO

                           log_text[log_text_top] = pygame.image.load('images/comshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps1[cs1p])

                           if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2
                           
                       elif paradigm == SYNERGIST:
                           
                           paradigm = RAVAGER
                           
                           log_text[log_text_top] = pygame.image.load('images/ravshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps1[cs1p])

                           if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2
                           
                   elif (rightParadigmShiftButton.collidepoint(mouse_pos)):
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       if paradigm == COMMANDO:
                           
                           paradigm = RAVAGER
                           
                           log_text[log_text_top] = pygame.image.load('images/ravshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps1[cs1p])

                           if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2
                           
                       elif paradigm == RAVAGER:
                           
                           paradigm = SYNERGIST
                           
                           log_text[log_text_top] = pygame.image.load('images/synshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps1[cs1p])

                           if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2
                           
                       elif paradigm == SYNERGIST:
                       
                           paradigm = COMMANDO

                           log_text[log_text_top] = pygame.image.load('images/comshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps1[cs1p])

                           if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2

                   #MOVE BUTTON CHECK
                   elif pygame.Rect(L_MOVE_W, T_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 1
                       
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       
                       if paradigm == COMMANDO:
                           
                             if blaziken.speed > (eps1[cs1p].speed * eps1[cs1p].speedmod):
                            
                                    blazikensMove(HJK, eps1[cs1p])
                        
                                    if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2
                                    else:
                                             opponentsMove(eps1[cs1p])

                                             if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  

                             else:
                                   opponentsMove(eps1[cs1p])
                                    
                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2
                                                        
                                   blazikensMove(HJK, eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                  
                       elif paradigm == RAVAGER:

                                    blazikensMove(VACUUMWAVE, eps1[cs1p])
                        
                                    if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2
                                    else:
                                             opponentsMove(eps1[cs1p])

                                             if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                       if paradigm == SYNERGIST:

                             if blaziken.speed > (eps1[cs1p].speed * eps1[cs1p].speedmod):
                            
                                    blazikensMove(SWORDSDANCE, eps1[cs1p])
                        
                                    if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2
                                    else:
                                             opponentsMove(eps1[cs1p])
                                             
                                             if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                             else:
                                   opponentsMove(eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2   
                                   
                                   blazikensMove(SWORDSDANCE, eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2
                           
                   elif pygame.Rect(R_MOVE_W, T_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 2

                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       
                       if paradigm == COMMANDO:

                             if blaziken.speed > (eps1[cs1p].speed * eps1[cs1p].speedmod):
                            
                                    blazikensMove(FLAREBLITZ, eps1[cs1p])
                        
                                    if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                    else:
                                             opponentsMove(eps1[cs1p])
                                             
                                             if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                             else:
                                   opponentsMove(eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2     
                                   
                                   blazikensMove(FLAREBLITZ, eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                           
                       elif paradigm == RAVAGER:
                           
                             if blaziken.speed > (eps1[cs1p].speed * eps1[cs1p].speedmod):
                            
                                    blazikensMove(FLAMETHROWER, eps1[cs1p])
                        
                                    if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                    else:
                                             opponentsMove(eps1[cs1p])
                                             
                                             if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                             else:
                                   opponentsMove(eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2     
                                   
                                   blazikensMove(FLAMETHROWER, eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                                        
                       if paradigm == SYNERGIST:

                             if blaziken.speed > (eps1[cs1p].speed * eps1[cs1p].speedmod):
                            
                                    blazikensMove(NASTYPLOT, eps1[cs1p])
                        
                                    if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                    else:
                                             opponentsMove(eps1[cs1p])
                                             
                                             if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                             else:
                                   opponentsMove(eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2     
                                   
                                   blazikensMove(NASTYPLOT, eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                           
                   elif pygame.Rect(L_MOVE_W, B_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 3
                       
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       
                       if paradigm == COMMANDO:

                             if blaziken.speed > (eps1[cs1p].speed * eps1[cs1p].speedmod):
                            
                                    blazikensMove(STONEEDGE, eps1[cs1p])
                        
                                    if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                    else:
                                             opponentsMove(eps1[cs1p])
                                             
                                             if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                             else:
                                   opponentsMove(eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2    
                                   
                                   blazikensMove(STONEEDGE, eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2                                   
                           
                       elif paradigm == RAVAGER:
                             if blaziken.speed > (eps1[cs1p].speed * eps1[cs1p].speedmod):
                            
                                    blazikensMove(OVERHEAT, eps1[cs1p])
                        
                                    if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                    else:
                                             opponentsMove(eps1[cs1p])
                                             
                                             if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                             else:
                                   opponentsMove(eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2     
                                   
                                   blazikensMove(OVERHEAT, eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2                                           
                           
                       if paradigm == SYNERGIST:

                             if blaziken.speed > (eps1[cs1p].speed * eps1[cs1p].speedmod):
                            
                                    blazikensMove(COSMICPOWER, eps1[cs1p])
                        
                                    if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                    else:
                                             opponentsMove(eps1[cs1p])
                                             
                                             if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2    
                             else:
                                   opponentsMove(eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2     
                                   
                                   blazikensMove(COSMICPOWER, eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                           
                   elif pygame.Rect(R_MOVE_W, B_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 4
                       
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       
                       if paradigm == COMMANDO:
                             if blaziken.speed > (eps1[cs1p].speed * eps1[cs1p].speedmod):
                            
                                    blazikensMove(THUNDERPUNCH, eps1[cs1p])
                        
                                    if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                    else:
                                             opponentsMove(eps1[cs1p])
                                             
                                             if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2    
                             else:
                                   opponentsMove(eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2    
                                   
                                   blazikensMove(THUNDERPUNCH, eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2                                  

                                
                       elif paradigm == RAVAGER:

                             if blaziken.speed > (eps1[cs1p].speed * eps1[cs1p].speedmod):
                                  log_text[log_text_top] = pygame.image.load('images/sbtext.png')
                                  log_text_top+=1

                                  if eps1[cs1p] == groudon:
                                       blazikensMove(SOLARBEAM, eps1[cs1p])
                                  else:
                                   opponentsMove(eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                   #END OF TURN
                                   loadHelp('turnlog') 
                                   calcHealth(blaziken)
                                   calcHealth(eps1[cs1p])

                                   time.sleep(5)
                                   
                                   #After Charge, NEW TURN
                                   log_text = [None, None, None, None, None, None, None, None]
                                   log_text_top = 0
                                   
                                   blazikensMove(SOLARBEAM, eps1[cs1p])
                                    
                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                   else:
                                             opponentsMove(eps1[cs1p])
                                             
                                             if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                             else:
                                  opponentsMove(eps1[cs1p])

                                  if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2    

                                  log_text[log_text_top] = pygame.image.load('images/sbtext.png')
                                  log_text_top+=1

                                  if eps1[cs1p] == groudon:
                                       blazikensMove(SOLARBEAM, eps1[cs1p])
                                  else:
                                   opponentsMove(eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                   #END OF TURN
                                   loadHelp('turnlog') 
                                   calcHealth(blaziken)
                                   calcHealth(eps1[cs1p])

                                   time.sleep(5)         

                                   #NEW TURN
                                   log_text = [None, None, None, None, None, None, None, None]
                                   log_text_top = 0
                                   
                                   blazikensMove(SOLARBEAM, eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                                        
                       if paradigm == SYNERGIST:
                           
                             if blaziken.speed > (eps1[cs1p].speed * eps1[cs1p].speedmod):
                            
                                    blazikensMove(HPUP, eps1[cs1p])
                        
                                    if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2  
                                    else:
                                             opponentsMove(eps1[cs1p])
                                             
                                             if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2    
                             else:
                                   opponentsMove(eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2   
                                   
                                   blazikensMove(HPUP, eps1[cs1p])

                                   if eps1[cs1p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs1p < 3: 
                                                        cs1p+=1
                                                        if cs1p == 3:
                                                            victory(eps1[cs1p - 1] )
                                                            STAGE = 2
                           
            #LOAD MOVE BUTTONS
            DISPLAYSURF.blit(blazikenMove[paradigm][0].image, (L_MOVE_W, T_MOVE_H))
            DISPLAYSURF.blit(blazikenMove[paradigm][1].image, (R_MOVE_W, T_MOVE_H))
            DISPLAYSURF.blit(blazikenMove[paradigm][2].image, (L_MOVE_W, B_MOVE_H))
            DISPLAYSURF.blit(blazikenMove[paradigm][3].image, (R_MOVE_W, B_MOVE_H))
            
            #LOAD PARADIMGM SHIFT BUTTONS
            if paradigm == COMMANDO:
                DISPLAYSURF.blit(pygame.image.load('images/SYN-L.png'), (0, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
                DISPLAYSURF.blit(pygame.image.load('images/RAV-R.png'), (BFWIDTH + L_MOVE_W + L_MOVE_W/2, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
            elif paradigm == RAVAGER:
                DISPLAYSURF.blit(pygame.image.load('images/COM-L.png'), (0, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
                DISPLAYSURF.blit(pygame.image.load('images/SYN-R.png'), (BFWIDTH + L_MOVE_W + L_MOVE_W/2, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
            elif paradigm == SYNERGIST:
                DISPLAYSURF.blit(pygame.image.load('images/RAV-L.png'), (0, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
                DISPLAYSURF.blit(pygame.image.load('images/COM-R.png'), (BFWIDTH + L_MOVE_W + L_MOVE_W/2, HUDHEIGHT+HUDGAP+BFHEIGHT+15))

            #LOAD HELP TEXT
            mouse_pos = pygame.mouse.get_pos()
            #PARADIGM HELP CHECK
            if (leftParadigmShiftButton.collidepoint(mouse_pos)):
                       if paradigm == COMMANDO:
                           loadHelp('synhelp')
                       elif paradigm == RAVAGER:
                           loadHelp('comhelp')
                       elif paradigm == SYNERGIST:
                           loadHelp('ravhelp')
            elif (rightParadigmShiftButton.collidepoint(mouse_pos)):
                       if paradigm == COMMANDO:
                           loadHelp('ravhelp')
                       elif paradigm == RAVAGER:
                           loadHelp('synhelp')
                       elif paradigm == SYNERGIST:
                           loadHelp('comhelp')

            #MOVE HELP CHECK
            elif pygame.Rect(L_MOVE_W, T_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 1
                       if paradigm == COMMANDO:
                           loadHelp('hjkhelp')
                       elif paradigm == RAVAGER:
                           loadHelp('vwhelp')
                       if paradigm == SYNERGIST:
                           loadHelp('sdhelp')
            elif pygame.Rect(R_MOVE_W, T_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 2
                       if paradigm == COMMANDO:
                           loadHelp('fbhelp')
                       elif paradigm == RAVAGER:
                           loadHelp('fthelp')
                       if paradigm == SYNERGIST:
                           loadHelp('nphelp')
            elif pygame.Rect(L_MOVE_W, B_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 3
                       if paradigm == COMMANDO:
                           loadHelp('sehelp')
                       elif paradigm == RAVAGER:
                           loadHelp('ohhelp')
                       if paradigm == SYNERGIST:
                           loadHelp('cphelp')
            elif pygame.Rect(R_MOVE_W, B_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 4
                       if paradigm == COMMANDO:
                           loadHelp('tphelp')
                       elif paradigm == RAVAGER:
                           loadHelp('sbhelp')
                       if paradigm == SYNERGIST:
                           loadHelp('huhelp')
            else:
                       loadHelp('turnlog')            
           
                       
           elif STAGE == 2:
    
                        
            DISPLAYSURF.blit(battleFieldImg[1][1], (0, 0)) #fill with background image

            #Stage 2 Animation
            if stage2anim == 1:
                blaziken =  Pokemon('Blaziken', pygame.image.load('images/blazikenback.png'), 'Fire', 'Fighting', 364 * 1.75, 372, 284, 350, 284, 284 * 1.5, pygame.image.load('images/blazikenhud.png'),
                    pygame.image.load('images/blaztype.png'), None)
                paradigm = COMMANDO
                log_text = [None, None, None, None, None, None, None, None]
                log_text_top = 0
                DISPLAYSURF.blit(pygame.image.load('images/stage2.png'), (L_MOVE_W, HUDHEIGHT+10))
                pygame.display.update()
                time.sleep(3)
                stage2anim = 0

            #Battle Field Window    
            DISPLAYSURF.blit(battleFieldImg[1][0], (L_MOVE_W, HUDHEIGHT+10)) #battle field image (same as bg)
            pygame.draw.rect(DISPLAYSURF, BLACK, (L_MOVE_W, HUDHEIGHT+10, BFWIDTH, BFHEIGHT), 3) #battle field rect/container

            #HUD
            DISPLAYSURF.blit(pygame.image.load('images/hud.png'), (0, 0)) #hud

            #Blaziken & Blaziken's Stats
            DISPLAYSURF.blit(blaziken.hudtext, (0, 0)) #load blaziken's name on the hud
            DISPLAYSURF.blit(blaziken.hudtype, (-5, 22)) #blaziken's type
            DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (0, 26)) #hp container of blaziken image
            DISPLAYSURF.blit(blaziken.image, blazikenCoords)
            health_string = str(int((blaziken.chp / blaziken.hp) * 100))
            if health_string == '0' and blaziken.chp != 0:
                health_string = str((blaziken.chp / blaziken.hp) * 100)
                textSurf = font.render(health_string[0:4] + "%" , True, BLACK)
            else:    
                textSurf = font.render(health_string + "%" , True, BLACK)
            textSurfRect = textSurf.get_rect() 
            textSurfRect.topleft = (35, 42)
            DISPLAYSURF.blit(textSurf, textSurfRect)
            
            if stage2anim == 0: #just uses the stage 2 animation flag as there's no risk, these are just to make sure this only happens the first time
                DISPLAYSURF.blit(pygame.image.load('images/3reserve.png'), (347, 26))
                pygame.display.update()
                time.sleep(2)
                cs2p = 0 #current stage 2 pokemon is the first one
                stage2anim = 2

            #Current Enemy   
            DISPLAYSURF.blit(eps2[cs2p].hudtext, (345, 0)) #load hud of enemy
            DISPLAYSURF.blit(eps2[cs2p].hudtype, (340, 25)) #enemy's typing
            DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (347, 26)) #hp container image of enemy            
            if eps2[cs2p] == lugia:
                DISPLAYSURF.blit(eps2[cs2p].image, (218 + 130 +20, HUDHEIGHT + 10))
            elif eps2[cs2p] == groudon: 
                DISPLAYSURF.blit(eps2[cs2p].image, (218+130+30, 140))
            elif eps2[cs2p] == kyogre:
                DISPLAYSURF.blit(eps2[cs2p].image, (218+130+30, 160))
            elif eps2[cs2p] == mvenusaur or eps2[cs2p] == mtyranitar:
                DISPLAYSURF.blit(eps2[cs2p].image, (218+130+35, 140))
            elif eps2[cs2p] == dragonite: 
                DISPLAYSURF.blit(eps2[cs2p].image, (218+130+30, 140))
            elif eps2[cs2p] == hooh: 
                DISPLAYSURF.blit(eps2[cs2p].image, (218+130+25, 100))
            elif eps2[cs2p] == rayquaza: 
                DISPLAYSURF.blit(eps2[cs2p].image, (218+130+45, 100))
            elif eps2[cs2p] == mewtwo:
                DISPLAYSURF.blit(eps2[cs2p].image, (218+130+25, 145))
                
            health_string2 = str(int((eps2[cs2p].chp / eps2[cs2p].hp) * 100))
            if health_string2 == '0' and eps2[cs2p].chp != 0:
                health_string2 = str((eps2[cs2p].chp / eps2[cs2p].hp) * 100)
                textSurf2 = font.render(health_string2[0:4] + "%" , True, BLACK)
            else:    
                textSurf2 = font.render(health_string2 + "%" , True, BLACK)
            
            textSurfRect2 = textSurf2.get_rect() 
            textSurfRect2.topleft = (382, 42)
            DISPLAYSURF.blit(textSurf2, textSurfRect2)
            
            if cs2p == 0: #if current pokemon is the first, there are 2 left
                DISPLAYSURF.blit(pygame.image.load('images/2reserve.png'), (347, 26))
            elif cs2p == 1: #if current pokemon is the second, there is 1 left
                DISPLAYSURF.blit(pygame.image.load('images/1reserve.png'), (347, 26))
            #if the current pokemon is the last(3), no image gets shown
            
            #help box
            pygame.draw.rect(DISPLAYSURF, GREY, (0, HELPBOXHEIGHT, WINDOWWIDTH, WINDOWHEIGHT - (HELPBOXHEIGHT)), 0)
            pygame.draw.rect(DISPLAYSURF, BLACK, (0, HELPBOXHEIGHT, WINDOWWIDTH, WINDOWHEIGHT - (HELPBOXHEIGHT)), 6)
            
            for event in pygame.event.get(): #Page 3 Event Handler

                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:

                   mouse_pos = pygame.mouse.get_pos()
                   
                   #PARADIGM SHIFT CHECK
                   if (leftParadigmShiftButton.collidepoint(mouse_pos)):
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       if paradigm == COMMANDO:
                           
                           paradigm = SYNERGIST
                           
                           log_text[log_text_top] = pygame.image.load('images/synshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps2[cs2p])

                           if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3
                                                
                           
                       elif paradigm == RAVAGER:
                           
                           paradigm = COMMANDO

                           log_text[log_text_top] = pygame.image.load('images/comshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps2[cs2p])

                           if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3
                           
                       elif paradigm == SYNERGIST:
                           
                           paradigm = RAVAGER
                           
                           log_text[log_text_top] = pygame.image.load('images/ravshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps2[cs2p])

                           if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3
                           
                   elif (rightParadigmShiftButton.collidepoint(mouse_pos)):
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       if paradigm == COMMANDO:
                           
                           paradigm = RAVAGER
                           
                           log_text[log_text_top] = pygame.image.load('images/ravshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps2[cs2p])

                           if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3
                           
                       elif paradigm == RAVAGER:
                           
                           paradigm = SYNERGIST
                           
                           log_text[log_text_top] = pygame.image.load('images/synshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps2[cs2p])

                           if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3
                           
                       elif paradigm == SYNERGIST:
                       
                           paradigm = COMMANDO

                           log_text[log_text_top] = pygame.image.load('images/comshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps2[cs2p])

                           if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3

                   #MOVE BUTTON CHECK
                   elif pygame.Rect(L_MOVE_W, T_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 1
                       
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       
                       if paradigm == COMMANDO:
                           
                             if blaziken.speed > (eps2[cs2p].speed * eps2[cs2p].speedmod):
                            
                                    blazikensMove(HJK, eps2[cs2p])
                        
                                    if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3
                                    else:
                                             opponentsMove(eps2[cs2p])

                                             if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  

                             else:
                                   opponentsMove(eps2[cs2p])
                                    
                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3
                                                        
                                   blazikensMove(HJK, eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                  
                       elif paradigm == RAVAGER:

                                    blazikensMove(VACUUMWAVE, eps2[cs2p])
                        
                                    if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3
                                    else:
                                             opponentsMove(eps2[cs2p])

                                             if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                       if paradigm == SYNERGIST:

                             if blaziken.speed > (eps2[cs2p].speed * eps2[cs2p].speedmod):
                            
                                    blazikensMove(SWORDSDANCE, eps2[cs2p])
                        
                                    if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3
                                    else:
                                             opponentsMove(eps2[cs2p])
                                             
                                             if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                             else:
                                   opponentsMove(eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3   
                                   
                                   blazikensMove(SWORDSDANCE, eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3
                           
                   elif pygame.Rect(R_MOVE_W, T_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 2

                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       
                       if paradigm == COMMANDO:

                             if blaziken.speed > (eps2[cs2p].speed * eps2[cs2p].speedmod):
                            
                                    blazikensMove(FLAREBLITZ, eps2[cs2p])
                        
                                    if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                    else:
                                             opponentsMove(eps2[cs2p])
                                             
                                             if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                             else:
                                   opponentsMove(eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3     
                                   
                                   blazikensMove(FLAREBLITZ, eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                           
                       elif paradigm == RAVAGER:
                           
                             if blaziken.speed > (eps2[cs2p].speed * eps2[cs2p].speedmod):
                            
                                    blazikensMove(FLAMETHROWER, eps2[cs2p])
                        
                                    if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                    else:
                                             opponentsMove(eps2[cs2p])
                                             
                                             if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                             else:
                                   opponentsMove(eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3     
                                   
                                   blazikensMove(FLAMETHROWER, eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                                        
                       if paradigm == SYNERGIST:

                             if blaziken.speed > (eps2[cs2p].speed * eps2[cs2p].speedmod):
                            
                                    blazikensMove(NASTYPLOT, eps2[cs2p])
                        
                                    if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                    else:
                                             opponentsMove(eps2[cs2p])
                                             
                                             if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                             else:
                                   opponentsMove(eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3     
                                   
                                   blazikensMove(NASTYPLOT, eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                           
                   elif pygame.Rect(L_MOVE_W, B_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 3
                       
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       
                       if paradigm == COMMANDO:
                           
                             if blaziken.speed > (eps2[cs2p].speed * eps2[cs2p].speedmod):
                            
                                    blazikensMove(STONEEDGE, eps2[cs2p])
                        
                                    if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                    else:
                                             opponentsMove(eps2[cs2p])
                                             
                                             if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                             else:
                                   opponentsMove(eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3    
                                   
                                   blazikensMove(STONEEDGE, eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3                                   
                           
                       elif paradigm == RAVAGER:
                             if blaziken.speed > (eps2[cs2p].speed * eps2[cs2p].speedmod):
                            
                                    blazikensMove(OVERHEAT, eps2[cs2p])
                        
                                    if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                    else:
                                             opponentsMove(eps2[cs2p])
                                             
                                             if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                             else:
                                   opponentsMove(eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3     
                                   
                                   blazikensMove(OVERHEAT, eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3                                           
                           
                       if paradigm == SYNERGIST:

                             if blaziken.speed > (eps2[cs2p].speed * eps2[cs2p].speedmod):
                            
                                    blazikensMove(COSMICPOWER, eps2[cs2p])
                        
                                    if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                    else:
                                             opponentsMove(eps2[cs2p])
                                             
                                             if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3    
                             else:
                                   opponentsMove(eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3     
                                   
                                   blazikensMove(COSMICPOWER, eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                           
                   elif pygame.Rect(R_MOVE_W, B_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 4
                       
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       
                       if paradigm == COMMANDO:
                             if blaziken.speed > (eps2[cs2p].speed * eps2[cs2p].speedmod):
                            
                                    blazikensMove(THUNDERPUNCH, eps2[cs2p])
                        
                                    if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                    else:
                                             opponentsMove(eps2[cs2p])
                                             
                                             if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3    
                             else:
                                   opponentsMove(eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3    
                                   
                                   blazikensMove(THUNDERPUNCH, eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3                                  

                                
                       elif paradigm == RAVAGER:

                             if blaziken.speed > (eps2[cs2p].speed * eps2[cs2p].speedmod):
                                  log_text[log_text_top] = pygame.image.load('images/sbtext.png')
                                  log_text_top+=1

                                  if eps2[cs2p] == groudon:
                                       blazikensMove(SOLARBEAM, eps2[cs2p])
                                  else:
                                   opponentsMove(eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                   #END OF TURN
                                   loadHelp('turnlog') 
                                   calcHealth(blaziken)
                                   calcHealth(eps2[cs2p])

                                   time.sleep(5)
                                   
                                   #After Charge, NEW TURN
                                   log_text = [None, None, None, None, None, None, None, None]
                                   log_text_top = 0
                                   
                                   blazikensMove(SOLARBEAM, eps2[cs2p])
                                    
                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                   else:
                                             opponentsMove(eps2[cs2p])
                                             
                                             if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                             else:
                                  opponentsMove(eps2[cs2p])

                                  if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3    

                                  log_text[log_text_top] = pygame.image.load('images/sbtext.png')
                                  log_text_top+=1

                                  if eps2[cs2p] == groudon:
                                       blazikensMove(SOLARBEAM, eps2[cs2p])
                                  else:
                                   opponentsMove(eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                   #END OF TURN
                                   loadHelp('turnlog') 
                                   calcHealth(blaziken)
                                   calcHealth(eps2[cs2p])

                                   time.sleep(5)         

                                   #NEW TURN
                                   log_text = [None, None, None, None, None, None, None, None]
                                   log_text_top = 0
                                   
                                   blazikensMove(SOLARBEAM, eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                                        
                       if paradigm == SYNERGIST:
                           
                             if blaziken.speed > (eps2[cs2p].speed * eps2[cs2p].speedmod):
                            
                                    blazikensMove(HPUP, eps2[cs2p])
                        
                                    if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3  
                                    else:
                                             opponentsMove(eps2[cs2p])
                                             
                                             if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3    
                             else:
                                   opponentsMove(eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3   
                                   
                                   blazikensMove(HPUP, eps2[cs2p])

                                   if eps2[cs2p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs2p < 3: 
                                                        cs2p+=1
                                                        if cs2p == 3:
                                                            victory(eps2[cs2p - 1] )
                                                            STAGE = 3
                           
            #LOAD MOVE BUTTONS
            DISPLAYSURF.blit(blazikenMove[paradigm][0].image, (L_MOVE_W, T_MOVE_H))
            DISPLAYSURF.blit(blazikenMove[paradigm][1].image, (R_MOVE_W, T_MOVE_H))
            DISPLAYSURF.blit(blazikenMove[paradigm][2].image, (L_MOVE_W, B_MOVE_H))
            DISPLAYSURF.blit(blazikenMove[paradigm][3].image, (R_MOVE_W, B_MOVE_H))
            
            #LOAD PARADIMGM SHIFT BUTTONS
            if paradigm == COMMANDO:
                DISPLAYSURF.blit(pygame.image.load('images/SYN-L.png'), (0, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
                DISPLAYSURF.blit(pygame.image.load('images/RAV-R.png'), (BFWIDTH + L_MOVE_W + L_MOVE_W/2, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
            elif paradigm == RAVAGER:
                DISPLAYSURF.blit(pygame.image.load('images/COM-L.png'), (0, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
                DISPLAYSURF.blit(pygame.image.load('images/SYN-R.png'), (BFWIDTH + L_MOVE_W + L_MOVE_W/2, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
            elif paradigm == SYNERGIST:
                DISPLAYSURF.blit(pygame.image.load('images/RAV-L.png'), (0, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
                DISPLAYSURF.blit(pygame.image.load('images/COM-R.png'), (BFWIDTH + L_MOVE_W + L_MOVE_W/2, HUDHEIGHT+HUDGAP+BFHEIGHT+15))

            #LOAD HELP TEXT
            mouse_pos = pygame.mouse.get_pos()
            #PARADIGM HELP CHECK
            if (leftParadigmShiftButton.collidepoint(mouse_pos)):
                       if paradigm == COMMANDO:
                           loadHelp('synhelp')
                       elif paradigm == RAVAGER:
                           loadHelp('comhelp')
                       elif paradigm == SYNERGIST:
                           loadHelp('ravhelp')
            elif (rightParadigmShiftButton.collidepoint(mouse_pos)):
                       if paradigm == COMMANDO:
                           loadHelp('ravhelp')
                       elif paradigm == RAVAGER:
                           loadHelp('synhelp')
                       elif paradigm == SYNERGIST:
                           loadHelp('comhelp')

            #MOVE HELP CHECK
            elif pygame.Rect(L_MOVE_W, T_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 1
                       if paradigm == COMMANDO:
                           loadHelp('hjkhelp')
                       elif paradigm == RAVAGER:
                           loadHelp('vwhelp')
                       if paradigm == SYNERGIST:
                           loadHelp('sdhelp')
            elif pygame.Rect(R_MOVE_W, T_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 2
                       if paradigm == COMMANDO:
                           loadHelp('fbhelp')
                       elif paradigm == RAVAGER:
                           loadHelp('fthelp')
                       if paradigm == SYNERGIST:
                           loadHelp('nphelp')
            elif pygame.Rect(L_MOVE_W, B_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 3
                       if paradigm == COMMANDO:
                           loadHelp('sehelp')
                       elif paradigm == RAVAGER:
                           loadHelp('ohhelp')
                       if paradigm == SYNERGIST:
                           loadHelp('cphelp')
            elif pygame.Rect(R_MOVE_W, B_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 4
                       if paradigm == COMMANDO:
                           loadHelp('tphelp')
                       elif paradigm == RAVAGER:
                           loadHelp('sbhelp')
                       if paradigm == SYNERGIST:
                           loadHelp('huhelp')
            else:
                       loadHelp('turnlog') 
            
           elif STAGE == 3:
    
                        
            DISPLAYSURF.blit(battleFieldImg[2][1], (0, 0)) #fill with background image

            #Stage 3 Animation
            if stage3anim == 1:
                blaziken =  Pokemon('Blaziken', pygame.image.load('images/blazikenback.png'), 'Fire', 'Fighting', 364 * 1.75, 372, 284, 350, 284, 284 * 1.5, pygame.image.load('images/blazikenhud.png'),
                    pygame.image.load('images/blaztype.png'), None)
                paradigm = COMMANDO
                log_text = [None, None, None, None, None, None, None, None]
                log_text_top = 0
                DISPLAYSURF.blit(pygame.image.load('images/stage3.png'), (L_MOVE_W, HUDHEIGHT+10))
                pygame.display.update()
                time.sleep(3)
                stage3anim = 0

            #Battle Field Window    
            DISPLAYSURF.blit(battleFieldImg[2][0], (L_MOVE_W, HUDHEIGHT+10)) #battle field image (same as bg)
            pygame.draw.rect(DISPLAYSURF, BLACK, (L_MOVE_W, HUDHEIGHT+10, BFWIDTH, BFHEIGHT), 3) #battle field rect/container

            #HUD
            DISPLAYSURF.blit(pygame.image.load('images/hud.png'), (0, 0)) #hud

            #Blaziken & Blaziken's Stats
            DISPLAYSURF.blit(blaziken.hudtext, (0, 0)) #load blaziken's name on the hud
            DISPLAYSURF.blit(blaziken.hudtype, (-5, 22)) #blaziken's type
            DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (0, 26)) #hp container of blaziken image
            DISPLAYSURF.blit(blaziken.image, blazikenCoords)
            health_string = str(int((blaziken.chp / blaziken.hp) * 100))
            if health_string == '0' and blaziken.chp != 0:
                health_string = str((blaziken.chp / blaziken.hp) * 100)
                textSurf = font.render(health_string[0:4] + "%" , True, BLACK)
            else:    
                textSurf = font.render(health_string + "%" , True, BLACK)
            textSurfRect = textSurf.get_rect() 
            textSurfRect.topleft = (35, 42)
            DISPLAYSURF.blit(textSurf, textSurfRect)
            
            if stage3anim == 0: #just uses the stage 3 animation flag as there's no risk, these are just to make sure this only happens the first time
                DISPLAYSURF.blit(pygame.image.load('images/3reserve.png'), (347, 26))
                pygame.display.update()
                time.sleep(2)
                cs3p = 0 #current stage 3 pokemon is the first one
                stage3anim = 2

            #Current Enemy   
            DISPLAYSURF.blit(eps3[cs3p].hudtext, (345, 0)) #load hud of enemy
            DISPLAYSURF.blit(eps3[cs3p].hudtype, (340, 25)) #enemy's typing
            DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (347, 26)) #hp container image of enemy            
            if eps3[cs3p] == lugia:
                DISPLAYSURF.blit(eps3[cs3p].image, (218 + 130 +20, HUDHEIGHT + 10))
            elif eps3[cs3p] == groudon: 
                DISPLAYSURF.blit(eps3[cs3p].image, (218+130+30, 140))
            elif eps3[cs3p] == kyogre:
                DISPLAYSURF.blit(eps3[cs3p].image, (218+130+30, 160))
            elif eps3[cs3p] == mvenusaur or eps3[cs3p] == mtyranitar:
                DISPLAYSURF.blit(eps3[cs3p].image, (218+130+35, 140))
            elif eps3[cs3p] == dragonite: 
                DISPLAYSURF.blit(eps3[cs3p].image, (218+130+30, 140))
            elif eps3[cs3p] == hooh: 
                DISPLAYSURF.blit(eps3[cs3p].image, (218+130+25, 100))
            elif eps3[cs3p] == rayquaza: 
                DISPLAYSURF.blit(eps3[cs3p].image, (218+130+45, 100))
            elif eps3[cs3p] == mewtwo:
                DISPLAYSURF.blit(eps3[cs3p].image, (218+130+25, 145))
                
            health_string2 = str(int((eps3[cs3p].chp / eps3[cs3p].hp) * 100))
            if health_string2 == '0' and eps3[cs3p].chp != 0:
                health_string2 = str((eps3[cs3p].chp / eps3[cs3p].hp) * 100)
                textSurf2 = font.render(health_string2[0:4] + "%" , True, BLACK)
            else:    
                textSurf2 = font.render(health_string2 + "%" , True, BLACK)
            
            textSurfRect2 = textSurf2.get_rect() 
            textSurfRect2.topleft = (382, 42)
            DISPLAYSURF.blit(textSurf2, textSurfRect2)
            
            if cs3p == 0: #if current pokemon is the first, there are 2 left
                DISPLAYSURF.blit(pygame.image.load('images/2reserve.png'), (347, 26))
            elif cs3p == 1: #if current pokemon is the second, there is 1 left
                DISPLAYSURF.blit(pygame.image.load('images/1reserve.png'), (347, 26))
            #if the current pokemon is the last(3), no image gets shown
            
            #help box
            pygame.draw.rect(DISPLAYSURF, GREY, (0, HELPBOXHEIGHT, WINDOWWIDTH, WINDOWHEIGHT - (HELPBOXHEIGHT)), 0)
            pygame.draw.rect(DISPLAYSURF, BLACK, (0, HELPBOXHEIGHT, WINDOWWIDTH, WINDOWHEIGHT - (HELPBOXHEIGHT)), 6)
            
            for event in pygame.event.get(): #Page 3 Event Handler

                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:

                   mouse_pos = pygame.mouse.get_pos()
                   
                   #PARADIGM SHIFT CHECK
                   if (leftParadigmShiftButton.collidepoint(mouse_pos)):
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       if paradigm == COMMANDO:
                           
                           paradigm = SYNERGIST
                           
                           log_text[log_text_top] = pygame.image.load('images/synshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps3[cs3p])

                           if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                             
                                                
                           
                       elif paradigm == RAVAGER:
                           
                           paradigm = COMMANDO

                           log_text[log_text_top] = pygame.image.load('images/comshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps3[cs3p])

                           if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                             
                           
                       elif paradigm == SYNERGIST:
                           
                           paradigm = RAVAGER
                           
                           log_text[log_text_top] = pygame.image.load('images/ravshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps3[cs3p])

                           if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                             
                           
                   elif (rightParadigmShiftButton.collidepoint(mouse_pos)):
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       if paradigm == COMMANDO:
                           
                           paradigm = RAVAGER
                           
                           log_text[log_text_top] = pygame.image.load('images/ravshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps3[cs3p])

                           if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                             
                           
                       elif paradigm == RAVAGER:
                           
                           paradigm = SYNERGIST
                           
                           log_text[log_text_top] = pygame.image.load('images/synshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps3[cs3p])

                           if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                             
                           
                       elif paradigm == SYNERGIST:
                       
                           paradigm = COMMANDO

                           log_text[log_text_top] = pygame.image.load('images/comshift.png')
                           log_text_top+=1
                           
                           opponentsMove(eps3[cs3p])

                           if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                             

                   #MOVE BUTTON CHECK
                   elif pygame.Rect(L_MOVE_W, T_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 1
                       
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       
                       if paradigm == COMMANDO:
                           
                             if blaziken.speed > (eps3[cs3p].speed * eps3[cs3p].speedmod):
                            
                                    blazikensMove(HJK, eps3[cs3p])
                        
                                    if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                             
                                    else:
                                             opponentsMove(eps3[cs3p])

                                             if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               

                             else:
                                   opponentsMove(eps3[cs3p])
                                    
                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                             
                                                        
                                   blazikensMove(HJK, eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                  
                       elif paradigm == RAVAGER:

                                    blazikensMove(VACUUMWAVE, eps3[cs3p])
                        
                                    if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                             
                                    else:
                                             opponentsMove(eps3[cs3p])

                                             if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                       if paradigm == SYNERGIST:

                             if blaziken.speed > (eps3[cs3p].speed * eps3[cs3p].speedmod):
                            
                                    blazikensMove(SWORDSDANCE, eps3[cs3p])
                        
                                    if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                             
                                    else:
                                             opponentsMove(eps3[cs3p])
                                             
                                             if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                             else:
                                   opponentsMove(eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                
                                   
                                   blazikensMove(SWORDSDANCE, eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                             
                           
                   elif pygame.Rect(R_MOVE_W, T_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 2

                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       
                       if paradigm == COMMANDO:

                             if blaziken.speed > (eps3[cs3p].speed * eps3[cs3p].speedmod):
                            
                                    blazikensMove(FLAREBLITZ, eps3[cs3p])
                        
                                    if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                    else:
                                             opponentsMove(eps3[cs3p])
                                             
                                             if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                             else:
                                   opponentsMove(eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                  
                                   
                                   blazikensMove(FLAREBLITZ, eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                           
                       elif paradigm == RAVAGER:
                           
                             if blaziken.speed > (eps3[cs3p].speed * eps3[cs3p].speedmod):
                            
                                    blazikensMove(FLAMETHROWER, eps3[cs3p])
                        
                                    if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                    else:
                                             opponentsMove(eps3[cs3p])
                                             
                                             if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                             else:
                                   opponentsMove(eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                  
                                   
                                   blazikensMove(FLAMETHROWER, eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                                        
                       if paradigm == SYNERGIST:

                             if blaziken.speed > (eps3[cs3p].speed * eps3[cs3p].speedmod):
                            
                                    blazikensMove(NASTYPLOT, eps3[cs3p])
                        
                                    if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                    else:
                                             opponentsMove(eps3[cs3p])
                                             
                                             if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                             else:
                                   opponentsMove(eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                  
                                   
                                   blazikensMove(NASTYPLOT, eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                           
                   elif pygame.Rect(L_MOVE_W, B_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 3
                       
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       
                       if paradigm == COMMANDO:

                             if blaziken.speed > (eps3[cs3p].speed * eps3[cs3p].speedmod):
                            
                                    blazikensMove(STONEEDGE, eps3[cs3p])
                        
                                    if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                    else:
                                             opponentsMove(eps3[cs3p])
                                             
                                             if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                             else:
                                   opponentsMove(eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                 
                                   
                                   blazikensMove(STONEEDGE, eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                                                
                           
                       elif paradigm == RAVAGER:
                             if blaziken.speed > (eps3[cs3p].speed * eps3[cs3p].speedmod):
                            
                                    blazikensMove(OVERHEAT, eps3[cs3p])
                        
                                    if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                    else:
                                             opponentsMove(eps3[cs3p])
                                             
                                             if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                             else:
                                   opponentsMove(eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                  
                                   
                                   blazikensMove(OVERHEAT, eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                                                        
                           
                       if paradigm == SYNERGIST:

                             if blaziken.speed > (eps3[cs3p].speed * eps3[cs3p].speedmod):
                            
                                    blazikensMove(COSMICPOWER, eps3[cs3p])
                        
                                    if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                    else:
                                             opponentsMove(eps3[cs3p])
                                             
                                             if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                 
                             else:
                                   opponentsMove(eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                  
                                   
                                   blazikensMove(COSMICPOWER, eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                           
                   elif pygame.Rect(R_MOVE_W, B_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 4
                       
                       log_text = [None, None, None, None, None, None, None, None]
                       log_text_top = 0
                       
                       if paradigm == COMMANDO:
                             if blaziken.speed > (eps3[cs3p].speed * eps3[cs3p].speedmod):
                            
                                    blazikensMove(THUNDERPUNCH, eps3[cs3p])
                        
                                    if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                    else:
                                             opponentsMove(eps3[cs3p])
                                             
                                             if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                 
                             else:
                                   opponentsMove(eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                 
                                   
                                   blazikensMove(THUNDERPUNCH, eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                                               

                                
                       elif paradigm == RAVAGER:

                             if blaziken.speed > (eps3[cs3p].speed * eps3[cs3p].speedmod):
                                  log_text[log_text_top] = pygame.image.load('images/sbtext.png')
                                  log_text_top+=1

                                  if eps3[cs3p] == groudon:
                                      
                                       blazikensMove(SOLARBEAM, eps3[cs3p])
                                       if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                       else:
                                           opponentsMove(eps3[cs3p])         
                                                            
                                  else:
                                   opponentsMove(eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                   #END OF TURN
                                   loadHelp('turnlog') 
                                   calcHealth(blaziken)
                                   calcHealth(eps3[cs3p])

                                   time.sleep(5)
                                   
                                   #After Charge, NEW TURN
                                   log_text = [None, None, None, None, None, None, None, None]
                                   log_text_top = 0
                                   
                                   blazikensMove(SOLARBEAM, eps3[cs3p])
                                    
                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                   else:
                                             opponentsMove(eps3[cs3p])
                                             
                                             if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                             else:
                                  opponentsMove(eps3[cs3p])

                                  if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                 

                                  log_text[log_text_top] = pygame.image.load('images/sbtext.png')
                                  log_text_top+=1

                                  if eps3[cs3p] == groudon:
                                       blazikensMove(SOLARBEAM, eps3[cs3p])
                                       if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                              
                                  else:
                                   opponentsMove(eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                   #END OF TURN
                                   loadHelp('turnlog') 
                                   calcHealth(blaziken)
                                   calcHealth(eps3[cs3p])

                                   time.sleep(5)         

                                   #NEW TURN
                                   log_text = [None, None, None, None, None, None, None, None]
                                   log_text_top = 0
                                   
                                   blazikensMove(SOLARBEAM, eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                                        
                       if paradigm == SYNERGIST:
                           
                             if blaziken.speed > (eps3[cs3p].speed * eps3[cs3p].speedmod):
                            
                                    blazikensMove(HPUP, eps3[cs3p])
                        
                                    if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                               
                                    else:
                                             opponentsMove(eps3[cs3p])
                                             
                                             if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                 
                             else:
                                   opponentsMove(eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                                
                                   
                                   blazikensMove(HPUP, eps3[cs3p])

                                   if eps3[cs3p].chp == 0:
                                                 
                                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                                log_text_top+=1
                                                
                                                if cs3p < 3: 
                                                        cs3p+=1
                                                        if cs3p == 3:
                                                            youWin(eps3[cs3p - 1] )
                                                             
                           
            #LOAD MOVE BUTTONS
            DISPLAYSURF.blit(blazikenMove[paradigm][0].image, (L_MOVE_W, T_MOVE_H))
            DISPLAYSURF.blit(blazikenMove[paradigm][1].image, (R_MOVE_W, T_MOVE_H))
            DISPLAYSURF.blit(blazikenMove[paradigm][2].image, (L_MOVE_W, B_MOVE_H))
            DISPLAYSURF.blit(blazikenMove[paradigm][3].image, (R_MOVE_W, B_MOVE_H))
            
            #LOAD PARADIMGM SHIFT BUTTONS
            if paradigm == COMMANDO:
                DISPLAYSURF.blit(pygame.image.load('images/SYN-L.png'), (0, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
                DISPLAYSURF.blit(pygame.image.load('images/RAV-R.png'), (BFWIDTH + L_MOVE_W + L_MOVE_W/2, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
            elif paradigm == RAVAGER:
                DISPLAYSURF.blit(pygame.image.load('images/COM-L.png'), (0, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
                DISPLAYSURF.blit(pygame.image.load('images/SYN-R.png'), (BFWIDTH + L_MOVE_W + L_MOVE_W/2, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
            elif paradigm == SYNERGIST:
                DISPLAYSURF.blit(pygame.image.load('images/RAV-L.png'), (0, HUDHEIGHT+HUDGAP+BFHEIGHT+15))
                DISPLAYSURF.blit(pygame.image.load('images/COM-R.png'), (BFWIDTH + L_MOVE_W + L_MOVE_W/2, HUDHEIGHT+HUDGAP+BFHEIGHT+15))

            #LOAD HELP TEXT
            mouse_pos = pygame.mouse.get_pos()
            #PARADIGM HELP CHECK
            if (leftParadigmShiftButton.collidepoint(mouse_pos)):
                       if paradigm == COMMANDO:
                           loadHelp('synhelp')
                       elif paradigm == RAVAGER:
                           loadHelp('comhelp')
                       elif paradigm == SYNERGIST:
                           loadHelp('ravhelp')
            elif (rightParadigmShiftButton.collidepoint(mouse_pos)):
                       if paradigm == COMMANDO:
                           loadHelp('ravhelp')
                       elif paradigm == RAVAGER:
                           loadHelp('synhelp')
                       elif paradigm == SYNERGIST:
                           loadHelp('comhelp')

            #MOVE HELP CHECK
            elif pygame.Rect(L_MOVE_W, T_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 1
                       if paradigm == COMMANDO:
                           loadHelp('hjkhelp')
                       elif paradigm == RAVAGER:
                           loadHelp('vwhelp')
                       if paradigm == SYNERGIST:
                           loadHelp('sdhelp')
            elif pygame.Rect(R_MOVE_W, T_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 2
                       if paradigm == COMMANDO:
                           loadHelp('fbhelp')
                       elif paradigm == RAVAGER:
                           loadHelp('fthelp')
                       if paradigm == SYNERGIST:
                           loadHelp('nphelp')
            elif pygame.Rect(L_MOVE_W, B_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 3
                       if paradigm == COMMANDO:
                           loadHelp('sehelp')
                       elif paradigm == RAVAGER:
                           loadHelp('ohhelp')
                       if paradigm == SYNERGIST:
                           loadHelp('cphelp')
            elif pygame.Rect(R_MOVE_W, B_MOVE_H, 216, 66).collidepoint(mouse_pos): #SLOT 4
                       if paradigm == COMMANDO:
                           loadHelp('tphelp')
                       elif paradigm == RAVAGER:
                           loadHelp('sbhelp')
                       if paradigm == SYNERGIST:
                           loadHelp('huhelp')
            else:
                       loadHelp('turnlog')             
            
        pygame.display.update()
        


def loadHelp(help_to_show): 
    #PARADIGM HELP
    if help_to_show == 'synhelp':
        DISPLAYSURF.blit(pygame.image.load('images/synhelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))
    elif help_to_show == 'comhelp':
        DISPLAYSURF.blit(pygame.image.load('images/comhelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))
    elif help_to_show == 'ravhelp':
        DISPLAYSURF.blit(pygame.image.load('images/ravhelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))
        
    #MOVE HELP
    elif help_to_show == 'sdhelp':
        DISPLAYSURF.blit(pygame.image.load('images/sdhelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))
    elif help_to_show == 'nphelp':
        DISPLAYSURF.blit(pygame.image.load('images/nphelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))
    elif help_to_show == 'cphelp':
        DISPLAYSURF.blit(pygame.image.load('images/cphelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))
    elif help_to_show == 'huhelp':
        DISPLAYSURF.blit(pygame.image.load('images/huhelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))

    elif help_to_show == 'hjkhelp':
        DISPLAYSURF.blit(pygame.image.load('images/hjkhelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))
    elif help_to_show == 'fbhelp':
        DISPLAYSURF.blit(pygame.image.load('images/fbhelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))
    elif help_to_show == 'sehelp':
        DISPLAYSURF.blit(pygame.image.load('images/sehelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))
    elif help_to_show == 'tphelp':
        DISPLAYSURF.blit(pygame.image.load('images/tphelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))

    elif help_to_show == 'vwhelp':
        DISPLAYSURF.blit(pygame.image.load('images/vwhelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))
    elif help_to_show == 'fthelp':
        DISPLAYSURF.blit(pygame.image.load('images/fthelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))
    elif help_to_show == 'ohhelp':
        DISPLAYSURF.blit(pygame.image.load('images/ohhelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))
    elif help_to_show == 'sbhelp':
        DISPLAYSURF.blit(pygame.image.load('images/sbhelp.png'), (0, WINDOWHEIGHT - HELPSTACKTOP[0] + 48))

    #PREVIOUS TURN LOG
    elif help_to_show == 'turnlog':
        pygame.draw.rect(DISPLAYSURF, GREY, (0, HELPBOXHEIGHT, WINDOWWIDTH, WINDOWHEIGHT - (HELPBOXHEIGHT)), 0)
        pygame.draw.rect(DISPLAYSURF, BLACK, (0, HELPBOXHEIGHT, WINDOWWIDTH, WINDOWHEIGHT - (HELPBOXHEIGHT)), 6)
        
        j = 0 
        for i in range(12,85,12): 
             if log_text[j] != None:
                   DISPLAYSURF.blit(log_text[j],(0, WINDOWHEIGHT - HELPSTACKTOP[0] + i)) 
                   j+=1
   
    
    

    
def damageCalc(atkr, dfndr, move):
    global log_text_top
    
    miss = False
    dmg = None
    
    if move.category != 'Other':
        if move.accuracy<100:
            if random.randrange(1,101) > move.accuracy:
                miss = True
                if move == HJK:
                    log_text[log_text_top] = pygame.image.load('images/miss.png')
                    log_text_top+=1
                    log_text[log_text_top] = pygame.image.load('images/crash.png')
                    log_text_top+=1
                else:
                    log_text[log_text_top] = pygame.image.load('images/miss.png')
                    log_text_top+=1
    if move.category == 'Physical' and miss != True:
        m = modifier(atkr, dfndr, move)
        if m[0] == 1: #if no critical
            dmg = ((0.84 * ((atkr.attack * atkr.attackmod)/(dfndr.defense * dfndr.defensemod)) * move.basepower) + 2) * m[1]
        else: #critical hits ignore defensive mods, this discourages constant boosting (chickening out)
            dmg = ((0.84 * ((atkr.attack * atkr.attackmod)/(dfndr.defense)) * move.basepower) + 2) * m[1]
            
    elif move.category == 'Special' and miss != True:
        m = modifier(atkr, dfndr, move)
        if m[0] == 1: #if no critical
            dmg = ((0.84 * ((atkr.sattack * atkr.sattackmod)/(dfndr.sdefense * dfndr.sdefensemod)) * move.basepower) + 2) * m[1]
        else: #critical hits ignore defensive mods, this discourages constant boosting (chickening out)
            dmg = ((0.84 * ((atkr.sattack * atkr.sattackmod)/(dfndr.sdefense)) * move.basepower) + 2) * m[1]

        if move == GIGADRAIN:
            
            atkr.chp+= (dmg/2)
            
            if atkr.chp > atkr.hp:
                atkr.chp = atkr.hp
                    
            log_text[log_text_top] = pygame.image.load('images/gdtext2.png')
            log_text_top+=1
            
    elif move.category == 'Other':
        if atkr == mewtwo:
            for i in range(0,6):
                done = False
                if atkr.attackmod == statboost[i] and atkr.sattackmod == statboost[i] and atkr.sdefensemod == statboost[i]:
                    atkr.attackmod = statboost[i+1]
                    atkr.sattackmod = statboost[i+1]
                    atkr.sdefensemod = statboost[i+1]
                    done = True 
                    break
    
            if done == True:
                log_text[log_text_top] = pygame.image.load('images/mcmtext2.png')
                log_text_top+=1
            elif done == False:
                log_text[log_text_top] = pygame.image.load('images/nh.png')
                log_text_top+=1

        elif atkr == dragonite:
            for i in range(0,6):
                done = False
                if atkr.attackmod == statboost[i] and atkr.speedmod == statboost[i]:
                    atkr.attackmod = statboost[i+1]
                    atkr.speedmod = statboost[i+1]
                    done = True 
                    break
            
            if done == True:
                log_text[log_text_top] = pygame.image.load('images/dddtext2.png')
                log_text_top+=1
            elif done == False:
                log_text[log_text_top] = pygame.image.load('images/nh.png')
                log_text_top+=1

        elif atkr == mvenusaur:
            if atkr.chp != atkr.hp:
                atkr.chp+=int(atkr.hp/2)
                if atkr.chp > atkr.hp:
                    atkr.chp = atkr.hp
                log_text[log_text_top] = pygame.image.load('images/sttext2.png')
                log_text_top+=1

            else:
                log_text[log_text_top] = pygame.image.load('images/nh.png')
                log_text_top+=1

        elif atkr == hooh:
            if atkr.chp != atkr.hp:
                atkr.chp+=int(atkr.hp/2)
                if atkr.chp > atkr.hp:
                    atkr.chp = atkr.hp
                log_text[log_text_top] = pygame.image.load('images/hrttext2.png')
                log_text_top+=1

            else:
                log_text[log_text_top] = pygame.image.load('images/nh.png')
                log_text_top+=1

        elif atkr == lugia:
           if move == ROOST: 

            if atkr.chp != atkr.hp:
                atkr.chp+=int(atkr.hp/2)
                if atkr.chp > atkr.hp:
                    atkr.chp = atkr.hp
                log_text[log_text_top] = pygame.image.load('images/lrttext2.png')
                log_text_top+=1

            else:
                log_text[log_text_top] = pygame.image.load('images/nh.png')
                log_text_top+=1
            
           else:
               for i in range(0,6):
                done = False
                if atkr.sattackmod == statboost[i] and atkr.sdefensemod == statboost[i]:
                    atkr.sattackmod = statboost[i+1]
                    atkr.sdefensemod = statboost[i+1]
                    done = True 
                    break
    
               if done == True:
                    log_text[log_text_top] = pygame.image.load('images/lcmtext2.png')
                    log_text_top+=1
               elif done == False:
                    log_text[log_text_top] = pygame.image.load('images/nh.png')
                    log_text_top+=1

        elif atkr == mtyranitar:
            for i in range(0,6):
                done = False
                if atkr.attackmod == statboost[i] and atkr.defensemod == statboost[i] and atkr.speedmod == statdrop[i]:
                    atkr.attackmod = statboost[i+1]
                    atkr.defensemod = statboost[i+1]
                    atkr.speedmod = statdrop[i+1]
                    done = True 
                    break
            
            if done == True:
                log_text[log_text_top] = pygame.image.load('images/cutext2.png')
                log_text_top+=1
            elif done == False:
                log_text[log_text_top] = pygame.image.load('images/nh.png')
                log_text_top+=1

        elif atkr == rayquaza:
            for i in range(0,6):
                done = False
                if atkr.attackmod == statboost[i] and atkr.speedmod == statboost[i]:
                    atkr.attackmod = statboost[i+1]
                    atkr.speedmod = statboost[i+1]
                    done = True 
                    break
            
            if done == True:
                log_text[log_text_top] = pygame.image.load('images/rddtext2.png')
                log_text_top+=1
            elif done == False:
                log_text[log_text_top] = pygame.image.load('images/nh.png')
                log_text_top+=1
                
            

    if miss == False and dmg != None:
        return int(dmg)
    else:
        return 0

    
def modifier(atkr, dfndr, move):
    global log_text_top
    stab = 1
    typeadv = 1
    critical = 1
    
    c = random.randrange(1,101)
    if move == STONEEDGE or move == AEROBLAST:
        if c == 100 or c == 12 or c == 30 or c == 44 or c == 5 or c == 65 or c == 10 or c == 2 or c == 3 or c == 4 or c == 50 or c == 6 or c == 13:
            critical = 2
            log_text[log_text_top] = pygame.image.load('images/crit.png')
            log_text_top+=1            
    elif c == 100 or c == 12 or c == 30 or c == 44 or c == 5 or c == 65: #any six numbers can rep 6%
        critical = 2
        log_text[log_text_top] = pygame.image.load('images/crit.png')
        log_text_top+=1
    
    

    if atkr.type1 == move.type or atkr.type2 == move.type:
        stab = 1.5

    #TYPECHART

    #ROCK
    if move.type == 'Rock' and (dfndr.type1 == 'Fire' or dfndr.type1 == 'Flying' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Ice'):
        typeadv =2
        if dfndr.type2 == 'Fire' or dfndr.type2 == 'Flying' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Ice':
            typeadv = 4
        elif dfndr.type2 == 'Ground' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Fighting':
            typeadv = 1
            
    elif move.type == 'Rock' and (dfndr.type1 == 'Ground' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Fighting'):
        typeadv = 0.5
        if dfndr.type2 == 'Ground' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Fighting':
            typeadv = 0.25
        elif dfndr.type2 == 'Fire' or dfndr.type2 == 'Flying' or dfndr.type2 == 'Bug'  or dfndr.type2 == 'Ice':
            typeadv = 1

    if move.type == 'Rock' and (dfndr.type2 == 'Fire' or dfndr.type2 == 'Flying' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Ice'):
        typeadv =2
        if dfndr.type1 == 'Fire' or dfndr.type1 == 'Flying' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Ice':
            typeadv = 4
        elif dfndr.type1 == 'Ground' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Fighting':
            typeadv = 1
            
    elif move.type == 'Rock' and (dfndr.type2 == 'Ground' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Fighting'):
        typeadv = 0.5
        if dfndr.type1 == 'Ground' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Fighting':
            typeadv = 0.25
        elif dfndr.type1 == 'Fire' or dfndr.type1 == 'Flying' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Ice':
            typeadv = 1
    #WATER
    if move.type == 'Water' and (dfndr.type1 == 'Ground' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Fire'):
        typeadv = 2
        if dfndr.type2 == 'Ground' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Fire':
            typeadv = 4
        elif dfndr.type2 == 'Dragon' or dfndr.type2 == 'Water' or dfndr.type2 == 'Grass':
            typeadv = 1

    elif move.type == 'Water' and (dfndr.type1 == 'Dragon' or dfndr.type1 == 'Water' or dfndr.type1 == 'Grass'):
        typeadv = 0.5
        if dfndr.type2 == 'Dragon' or dfndr.type2 == 'Water' or dfndr.type2 == 'Grass':
            typeadv = 0.25
        elif dfndr.type2 == 'Ground' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Fire':
            typeadv = 1

    if move.type == 'Water' and (dfndr.type2 == 'Ground' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Fire'):
        typeadv = 2
        if dfndr.type1 == 'Ground' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Fire':
            typeadv = 4
        elif dfndr.type1 == 'Dragon' or dfndr.type1 == 'Water' or dfndr.type1 == 'Grass':
            typeadv = 1

    elif move.type == 'Water' and (dfndr.type2 == 'Dragon' or dfndr.type2 == 'Water' or dfndr.type2 == 'Grass'):
        typeadv = 0.5
        if dfndr.type1 == 'Dragon' or dfndr.type1 == 'Water' or dfndr.type1 == 'Grass':
            typeadv = 0.25
        elif dfndr.type1 == 'Ground' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Fire':
            typeadv = 1
            
    #ELECTRIC
    if move.type == 'Electric' and (dfndr.type1 == 'Water' or dfndr.type1 == 'Flying'): 
        typeadv = 2
        if dfndr.type2 == 'Water' or dfndr.type2 == 'Flying':
            typeadv = 4
        elif dfndr.type2 == 'Grass' or dfndr.type2 == 'Electric' or dfndr.type2 == 'Dragon':
            typeadv = 1
            
    elif move.type == 'Electric' and (dfndr.type1 == 'Grass' or dfndr.type1 == 'Electric' or dfndr.type1 == 'Dragon'):
        typeadv = 0.5
        if dfndr.type2 == 'Grass' or dfndr.type2 == 'Electric' or dfndr.type2 == 'Dragon':
            typeadv = 0.25
        elif dfndr.type2 == 'Water' or dfndr.type2 == 'Flying':
            typeadv = 1

    if move.type == 'Electric' and (dfndr.type2 == 'Water' or dfndr.type2 == 'Flying'): 
        typeadv = 2
        if dfndr.type1 == 'Water' or dfndr.type1 == 'Flying':
            typeadv = 4
        elif dfndr.type1 == 'Grass' or dfndr.type1 == 'Electric' or dfndr.type1 == 'Dragon':
            typeadv = 1
            
    elif move.type == 'Electric' and (dfndr.type2 == 'Grass' or dfndr.type2 == 'Electric' or dfndr.type2 == 'Dragon'):
        typeadv = 0.5
        if dfndr.type1 == 'Grass' or dfndr.type1 == 'Electric' or dfndr.type1 == 'Dragon':
            typeadv = 0.25
        elif dfndr.type1 == 'Water' or dfndr.type1 == 'Flying':
            typeadv = 1

    if move.type == 'Electric' and (dfndr.type1 == 'Ground' or dfndr.type2 == 'Ground'):
        typeadv = 0
            
    #GRASS
    if move.type == 'Grass' and (dfndr.type1 == 'Water' or dfndr.type1 == 'Ground' or dfndr.type1 == 'Rock'):
        typeadv = 2
        if dfndr.type2 == 'Water' or dfndr.type2 == 'Ground' or dfndr.type2 == 'Rock':
            typeadv = 4
        elif dfndr.type2 == 'Grass' or dfndr.type2 == 'Fire' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Dragon' or dfndr.type2 == 'Flying':
            typeadv = 1
            
    elif move.type == 'Grass' and (dfndr.type1 == 'Grass' or dfndr.type1 == 'Fire' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Dragon' or dfndr.type1 == 'Flying'):
        typeadv = 0.5
        if dfndr.type2 == 'Grass' or dfndr.type2 == 'Fire' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Dragon' or dfndr.type2 == 'Flying':
            typeadv = 0.25
        elif dfndr.type2 == 'Water' or dfndr.type2 == 'Ground' or dfndr.type2 == 'Rock':
            typeadv = 1

    if move.type == 'Grass' and (dfndr.type2 == 'Water' or dfndr.type2 == 'Ground' or dfndr.type2 == 'Rock'):
        typeadv = 2
        if dfndr.type1 == 'Water' or dfndr.type1 == 'Ground' or dfndr.type1 == 'Rock':
            typeadv = 4
        elif dfndr.type1 == 'Grass' or dfndr.type1 == 'Fire' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Dragon' or dfndr.type1 == 'Flying':
            typeadv = 1
            
    elif move.type == 'Grass' and (dfndr.type2 == 'Grass' or dfndr.type2 == 'Fire' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Dragon' or dfndr.type2 == 'Flying'):
        typeadv = 0.5
        if dfndr.type1 == 'Grass' or dfndr.type1 == 'Fire' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Dragon' or dfndr.type1 == 'Flying':
            typeadv = 0.25
        elif dfndr.type1 == 'Water' or dfndr.type1 == 'Ground' or dfndr.type1 == 'Rock':
            typeadv = 1
            
    #PSYCHIC
    if move.type == 'Psychic' and (dfndr.type1 == 'Fighting' or dfndr.type1 == 'Poison'): 
        typeadv = 2
        if dfndr.type2 == 'Fighting' or dfndr.type2 == 'Poison':
            typeadv = 4
        elif dfndr.type2 == 'Steel' or dfndr.type2 == 'Psychic':
            typeadv = 1
            
    elif move.type == 'Psychic' and (dfndr.type1 == 'Steel' or dfndr.type1 == 'Psychic'):
        typeadv = 0.5
        if dfndr.type2 == 'Steel' or dfndr.type2 == 'Psychic':
            typeadv = 0.25
        elif dfndr.type2 == 'Fighting' or dfndr.type2 == 'Poison':
            typeadv = 1
                                   
    if move.type == 'Psychic' and (dfndr.type2 == 'Fighting' or dfndr.type2 == 'Poison'): 
        typeadv = 2
        if dfndr.type1 == 'Fighting' or dfndr.type1 == 'Poison':
            typeadv = 4
        elif dfndr.type1 == 'Steel' or dfndr.type1 == 'Psychic':
            typeadv = 1
            
    elif move.type == 'Psychic' and (dfndr.type2 == 'Steel' or dfndr.type2 == 'Psychic'):
        typeadv = 0.5
        if dfndr.type1 == 'Steel' or dfndr.type1 == 'Psychic':
            typeadv = 0.25
        elif dfndr.type1 == 'Fighting' or dfndr.type1 == 'Poison':
            typeadv = 1
    
    if move.type == 'Psychic' and (dfndr.type1 == 'Dark' or dfndr.type2 == 'Dark'):
        typeadv = 0
        
    #POISON
    if move.type == 'Poison' and dfndr.type1 == 'Grass': 
        typeadv = 2
        if dfndr.type2 == 'Grass':
            typeadv = 4
        elif dfndr.type2 == 'Ground' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Ghost':
            typeadv = 1
            
    elif move.type == 'Poison' and (dfndr.type1 == 'Ground' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Ghost'):
        typeadv = 0.5
        if dfndr.type2 == 'Ground' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Ghost':
            typeadv = 0.25
        elif dfndr.type2 == 'Grass':
            typeadv = 1

    if move.type == 'Poison' and dfndr.type2 == 'Grass': 
        typeadv = 2
        if dfndr.type1 == 'Grass':
            typeadv = 4
        elif dfndr.type1 == 'Ground' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Ghost':
            typeadv = 1
            
    elif move.type == 'Poison' and (dfndr.type2 == 'Ground' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Ghost'):
        typeadv = 0.5
        if dfndr.type1 == 'Ground' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Ghost':
            typeadv = 0.25
        elif dfndr.type1 == 'Grass':
            typeadv = 1
            
    if move.type == 'Poison' and (dfndr.type1 == 'Steel' or dfndr.type2 == 'Steel'):
        typeadv = 0
        
    #FIRE
    if move.type == 'Fire' and (dfndr.type1 == 'Grass' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Ice'):
        typeadv = 2
        if dfndr.type2 == 'Grass' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Ice':
            typeadv = 4
        elif dfndr.type2 == 'Rock' or dfndr.type2 == 'Dragon' or dfndr.type2 == 'Water' or dfndr.type2 == 'Fire':
            typeadv = 1
            
    elif move.type == 'Fire' and (dfndr.type1 == 'Rock' or dfndr.type1 == 'Dragon' or dfndr.type1 == 'Water' or dfndr.type1 == 'Fire'):
        typeadv = 0.5
        if dfndr.type2 == 'Rock' or dfndr.type2 == 'Dragon' or dfndr.type2 == 'Water' or dfndr.type2 == 'Fire':
            typeadv = 0.25
        elif dfndr.type2 == 'Grass' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Ice':
            typeadv = 1

    if move.type == 'Fire' and (dfndr.type2 == 'Grass' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Ice'):
        typeadv = 2
        if dfndr.type1 == 'Grass' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Ice':
            typeadv = 4
        elif dfndr.type1 == 'Rock' or dfndr.type1 == 'Dragon' or dfndr.type1 == 'Water' or dfndr.type1 == 'Fire':
            typeadv = 1
            
    elif move.type == 'Fire' and (dfndr.type2 == 'Rock' or dfndr.type2 == 'Dragon' or dfndr.type2 == 'Water' or dfndr.type2 == 'Fire'):
        typeadv = 0.5
        if dfndr.type1 == 'Rock' or dfndr.type1 == 'Dragon' or dfndr.type1 == 'Water' or dfndr.type1 == 'Fire':
            typeadv = 0.25
        elif dfndr.type1 == 'Grass' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Ice':
            typeadv = 1

    #GROUND
    if move.type == 'Ground' and (dfndr.type1 == 'Fire' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Electric'): 
        typeadv = 2
        if dfndr.type2 == 'Fire' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Electric':
            typeadv = 4
        elif dfndr.type2 == 'Grass' or dfndr.type2 == 'Bug':
            typeadv = 1
            
    elif move.type == 'Ground' and (dfndr.type1 == 'Grass' or dfndr.type1 == 'Bug'):
        typeadv = 0.5
        if dfndr.type2 == 'Grass' or dfndr.type2 == 'Bug':
            typeadv = 0.25
        elif dfndr.type2 == 'Fire' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Electric':
            typeadv = 1

    if move.type == 'Ground' and (dfndr.type2 == 'Fire' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Electric'): 
        typeadv = 2
        if dfndr.type1 == 'Fire' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Electric':
            typeadv = 4
        elif dfndr.type1 == 'Grass' or dfndr.type1 == 'Bug':
            typeadv = 1
            
    elif move.type == 'Ground' and (dfndr.type2 == 'Grass' or dfndr.type2 == 'Bug'):
        typeadv = 0.5
        if dfndr.type1 == 'Grass' or dfndr.type1 == 'Bug':
            typeadv = 0.25
        elif dfndr.type1 == 'Fire' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Electric':
            typeadv = 1
    

    if move.type == 'Ground' and (dfndr.type1 == 'Flying' or dfndr.type2 == 'Flying'):
        typeadv = 0

    #FLYING
    if move.type == 'Flying' and (dfndr.type1 == 'Grass' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Fighting'):
        typeadv = 2
        if dfndr.type2 == 'Grass' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Fighting':
            typeadv = 4
        elif dfndr.type2 == 'Rock' or dfndr.type2 == 'Electric' or dfndr.type2 == 'Steel':
            typeadv = 1
            
    elif move.type == 'Flying' and (dfndr.type1 == 'Rock' or dfndr.type1 == 'Electric' or dfndr.type1 == 'Steel'):
        typeadv = 0.5
        if dfndr.type2 == 'Rock' or dfndr.type2 == 'Electric' or dfndr.type2 == 'Steel':
            typeadv = 0.25
        elif dfndr.type2 == 'Grass' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Fighting':
            typeadv = 1

    if move.type == 'Flying' and (dfndr.type2 == 'Grass' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Fighting'):
        typeadv = 2
        if dfndr.type1 == 'Grass' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Fighting':
            typeadv = 4
        elif dfndr.type1 == 'Rock' or dfndr.type1 == 'Electric' or dfndr.type1 == 'Steel':
            typeadv = 1
            
    elif move.type == 'Flying' and (dfndr.type2 == 'Rock' or dfndr.type2 == 'Electric' or dfndr.type2 == 'Steel'):
        typeadv = 0.5
        if dfndr.type1 == 'Rock' or dfndr.type1 == 'Electric' or dfndr.type1 == 'Steel':
            typeadv = 0.25
        elif dfndr.type1 == 'Grass' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Fighting':
            typeadv = 1
            
    #BUG
    if move.type == 'Bug' and (dfndr.type1 == 'Psychic' or dfndr.type1 == 'Dark' or dfndr.type1 == 'Grass'):
        typeadv = 2
        if dfndr.type2 == 'Psychic' or dfndr.type2 == 'Dark' or dfndr.type2 == 'Grass':
            typeadv = 4
        elif dfndr.type2 == 'Fire' or dfndr.type2 == 'Fighting' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Flying' or dfndr.type2 == 'Ghost':
            typeadv = 1
            
    elif move.type == 'Bug' and (dfndr.type1 == 'Fire' or dfndr.type1 == 'Fighting' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Flying' or dfndr.type1 == 'Ghost'):
        typeadv = 0.5
        if dfndr.type2 == 'Fire' or dfndr.type2 == 'Fighting' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Flying' or dfndr.type2 == 'Ghost':
            typeadv = 0.25
        elif dfndr.type2 == 'Psychic' or dfndr.type2 == 'Dark' or dfndr.type2 == 'Grass':
            typeadv = 1
            
    if move.type == 'Bug' and (dfndr.type2 == 'Psychic' or dfndr.type2 == 'Dark' or dfndr.type2 == 'Grass'):
        typeadv = 2
        if dfndr.type1 == 'Psychic' or dfndr.type1 == 'Dark' or dfndr.type1 == 'Grass':
            typeadv = 4
        elif dfndr.type1 == 'Fire' or dfndr.type1 == 'Fighting' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Flying' or dfndr.type1 == 'Ghost':
            typeadv = 1
            
    elif move.type == 'Bug' and (dfndr.type2 == 'Fire' or dfndr.type2 == 'Fighting' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Flying' or dfndr.type2 == 'Ghost'):
        typeadv = 0.5
        if dfndr.type1 == 'Fire' or dfndr.type1 == 'Fighting' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Flying' or dfndr.type1 == 'Ghost':
            typeadv = 0.25
        elif dfndr.type1 == 'Psychic' or dfndr.type1 == 'Dark' or dfndr.type1 == 'Grass':
            typeadv = 1
            
    #NORMAL
    if move.type == 'Normal' and (dfndr.type1 == 'Rock' or dfndr.type1 == 'Steel'):
        typeadv = 0.5
        if dfndr.type2 == 'Rock' or dfndr.type2 == 'Steel':
            typeadv = 0.25

    if move.type == 'Normal' and (dfndr.type2 == 'Rock' or dfndr.type2 == 'Steel'):
        typeadv = 0.5
        if dfndr.type1 == 'Rock' or dfndr.type1 == 'Steel':
            typeadv = 0.25

    if move.type == 'Normal' and (dfndr.type1 == 'Ghost' or dfndr.type2 == 'Ghost'):
        typeadv = 0

    #GHOST
    if move.type == 'Ghost' and (dfndr.type1 == 'Ghost' or dfndr.type1 == 'Psychic'): 
        typeadv = 2
        if dfndr.type2 == 'Ghost' or dfndr.type2 == 'Psychic':
            typeadv = 4
        elif dfndr.type2 == 'Dark' or dfndr.type2 == 'Steel':
            typeadv = 1
            
    elif move.type == 'Ghost' and (dfndr.type1 == 'Dark' or dfndr.type1 == 'Steel'):
        typeadv = 0.5
        if dfndr.type2 == 'Dark' or dfndr.type2 == 'Steel':
            typeadv = 0.25
        elif dfndr.type2 == 'Ghost' or dfndr.type2 == 'Psychic':
            typeadv = 1

    if move.type == 'Ghost' and (dfndr.type2 == 'Ghost' or dfndr.type2 == 'Psychic'): 
        typeadv = 2
        if dfndr.type1 == 'Ghost' or dfndr.type1 == 'Psychic':
            typeadv = 4
        elif dfndr.type1 == 'Dark' or dfndr.type1 == 'Steel':
            typeadv = 1
            
    elif move.type == 'Ghost' and (dfndr.type2 == 'Dark' or dfndr.type2 == 'Steel'):
        typeadv = 0.5
        if dfndr.type1 == 'Dark' or dfndr.type1 == 'Steel':
            typeadv = 0.25
        elif dfndr.type1 == 'Ghost' or dfndr.type1 == 'Psychic':
            typeadv = 1    
    
    if move.type == 'Ghost' and (dfndr.type1 == 'Normal' or dfndr.type2 == 'Normal'):
        typeadv = 0

    #STEEL
    if move.type == 'Steel' and (dfndr.type1 == 'Rock' or dfndr.type1 == 'Ice'): 
        typeadv = 2
        if dfndr.type2 == 'Rock' or dfndr.type2 == 'Ice':
            typeadv = 4
        elif dfndr.type2 == 'Fire' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Electric' or dfndr.type2 == 'Water':
            typeadv = 1
            
    elif move.type == 'Steel' and (dfndr.type1 == 'Fire' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Electric' or dfndr.type1 == 'Water'):
        typeadv = 0.5
        if dfndr.type2 == 'Fire' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Electric' or dfndr.type2 == 'Water':
            typeadv = 0.25
        elif dfndr.type2 == 'Rock' or dfndr.type2 == 'Ice':
            typeadv = 1

    if move.type == 'Steel' and (dfndr.type2 == 'Rock' or dfndr.type2 == 'Ice'): 
        typeadv = 2
        if dfndr.type1 == 'Rock' or dfndr.type1 == 'Ice':
            typeadv = 4
        elif dfndr.type1 == 'Fire' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Electric' or dfndr.type1 == 'Water':
            typeadv = 1
            
    elif move.type == 'Steel' and (dfndr.type2 == 'Fire' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Electric' or dfndr.type2 == 'Water'):
        typeadv = 0.5
        if dfndr.type1 == 'Fire' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Electric' or dfndr.type1 == 'Water':
            typeadv = 0.25
        elif dfndr.type1 == 'Rock' or dfndr.type1 == 'Ice':
            typeadv = 1

           
    #FIGHTING
    if move.type == 'Fighting' and (dfndr.type1 == 'Normal' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Dark' or dfndr.type1 == 'Ice'): 
        typeadv = 2
        if dfndr.type2 == 'Normal' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Dark' or dfndr.type2 == 'Ice':
            typeadv = 4
        elif dfndr.type2 == 'Flying' or dfndr.type2 == 'Psychic' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Fairy':
            typeadv = 1
        elif dfndr.type2 == 'Ghost':
            typeadv = 0
            
    elif move.type == 'Fighting' and (dfndr.type1 == 'Flying' or dfndr.type1 == 'Psychic' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Fairy' or dfndr.type1 == 'Ghost'):
        if dfndr.type1 == 'Ghost':
            typeadv = 0
        else:
            typeadv = 0.5
        if (dfndr.type2 == 'Flying' or dfndr.type2 == 'Psychic' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Fairy') and dfndr.type1 != 'Ghost':
                typeadv = 0.25
        elif (dfndr.type2 == 'Normal' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Dark' or dfndr.type2 == 'Ice') and dfndr.type1 != 'Ghost':
            typeadv = 1
            
    if move.type == 'Fighting' and (dfndr.type2 == 'Normal' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Dark' or dfndr.type2 == 'Ice'): 
        typeadv = 2
        if dfndr.type1 == 'Normal' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Dark' or dfndr.type1 == 'Ice':
            typeadv = 4
        elif dfndr.type1 == 'Flying' or dfndr.type1 == 'Psychic' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Fairy':
            typeadv = 1
        elif dfndr.type1 == 'Ghost':
            typeadv = 0
            
    elif move.type == 'Fighting' and (dfndr.type2 == 'Flying' or dfndr.type2 == 'Psychic' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Fairy' or dfndr.type2 == 'Ghost'):
        if dfndr.type2 == 'Ghost':
            typeadv = 0
        else:
            typeadv = 0.5
        if (dfndr.type1 == 'Flying' or dfndr.type1 == 'Psychic' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Fairy') and dfndr.type2 != 'Ghost':
                typeadv = 0.25
        elif (dfndr.type1 == 'Normal' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Dark' or dfndr.type1 == 'Ice') and dfndr.type2 != 'Ghost':
            typeadv = 1

    #ICE
    if move.type == 'Ice' and (dfndr.type1 == 'Flying' or dfndr.type1 == 'Ground' or dfndr.type1 == 'Grass' or dfndr.type1 == 'Dragon'): 
        typeadv = 2
        if dfndr.type2 == 'Flying' or dfndr.type2 == 'Ground' or dfndr.type2 == 'Grass' or dfndr.type2 == 'Dragon':
            typeadv = 4
        elif dfndr.type2 == 'Fire' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Ice' or dfndr.type2 == 'Water':
            typeadv = 1
            
    elif move.type == 'Ice' and (dfndr.type1 == 'Fire' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Ice' or dfndr.type1 == 'Water'):
        typeadv = 0.5
        if dfndr.type2 == 'Fire' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Ice' or dfndr.type2 == 'Water':
            typeadv = 0.25
        elif dfndr.type2 == 'Flying' or dfndr.type2 == 'Ground' or dfndr.type2 == 'Grass' or dfndr.type2 == 'Dragon':
            typeadv = 1

    if move.type == 'Ice' and (dfndr.type2 == 'Flying' or dfndr.type2 == 'Ground' or dfndr.type2 == 'Grass' or dfndr.type2 == 'Dragon'): 
        typeadv = 2
        if dfndr.type1 == 'Flying' or dfndr.type1 == 'Ground' or dfndr.type1 == 'Grass' or dfndr.type1 == 'Dragon':
            typeadv = 4
        elif dfndr.type1 == 'Fire' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Ice' or dfndr.type1 == 'Water':
            typeadv = 1
            
    elif move.type == 'Ice' and (dfndr.type2 == 'Fire' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Ice' or dfndr.type2 == 'Water'):
        typeadv = 0.5
        if dfndr.type1 == 'Fire' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Ice' or dfndr.type1 == 'Water':
            typeadv = 0.25
        elif dfndr.type1 == 'Flying' or dfndr.type1 == 'Ground' or dfndr.type1 == 'Grass' or dfndr.type1 == 'Dragon':
            typeadv = 1

    #DRAGON
    if move.type == 'Dragon' and dfndr.type1 == 'Dragon': 
        typeadv = 2
        if dfndr.type2 == 'Dragon':
            typeadv = 4
        elif dfndr.type2 == 'Steel':
            typeadv = 1
            
    elif move.type == 'Dragon' and dfndr.type1 == 'Steel':
        typeadv = 0.5
        if dfndr.type2 == 'Steel':
            typeadv = 0.25
        elif dfndr.type2 == 'Dragon':
            typeadv = 1

    if move.type == 'Dragon' and dfndr.type2 == 'Dragon': 
        typeadv = 2
        if dfndr.type1 == 'Dragon':
            typeadv = 4
        elif dfndr.type1 == 'Steel':
            typeadv = 1
            
    elif move.type == 'Dragon' and dfndr.type2 == 'Steel':
        typeadv = 0.5
        if dfndr.type1 == 'Steel':
            typeadv = 0.25
        elif dfndr.type1 == 'Dragon':
            typeadv = 1

    #DARK
    if move.type == 'Dark' and (dfndr.type1 == 'Ghost' or dfndr.type1 == 'Psychic'): 
        typeadv = 2
        if dfndr.type2 == 'Ghost' or dfndr.type2 == 'Psychic':
            typeadv = 4
        elif dfndr.type2 == 'Dark' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Fighting':
            typeadv = 1
            
    elif move.type == 'Dark' and (dfndr.type1 == 'Dark' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Fighting'):
        typeadv = 0.5
        if dfndr.type2 == 'Dark' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Fighting':
            typeadv = 0.25
        elif dfndr.type2 == 'Ghost' or dfndr.type2 == 'Psychic':
            typeadv = 1

    if move.type == 'Dark' and (dfndr.type2 == 'Ghost' or dfndr.type2 == 'Psychic'): 
        typeadv = 2
        if dfndr.type1 == 'Ghost' or dfndr.type1 == 'Psychic':
            typeadv = 4
        elif dfndr.type1 == 'Dark' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Fighting':
            typeadv = 1
            
    elif move.type == 'Dark' and (dfndr.type2 == 'Dark' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Fighting'):
        typeadv = 0.5
        if dfndr.type1 == 'Dark' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Fighting':
            typeadv = 0.25
        elif dfndr.type1 == 'Ghost' or dfndr.type1 == 'Psychic':
            typeadv = 1


    #Effective Text
    if typeadv > 1:
        log_text[log_text_top] = pygame.image.load('images/se.png')
        log_text_top+=1
    elif typeadv < 1 and typeadv != 0:
        log_text[log_text_top] = pygame.image.load('images/nve.png')
        log_text_top+=1
    elif typeadv == 0:
        log_text[log_text_top] = pygame.image.load('images/immune.png')
        log_text_top+=1
    elif typeadv == 1:
        log_text[log_text_top] = pygame.image.load('images/nd.png')
        log_text_top+=1
        
    return (critical, stab * typeadv * critical * (random.randrange(85,101)/100)) 

def crashModifier(dfndr, move):
    if move.type == 'Fighting' and (dfndr.type1 == 'Normal' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Dark'): 
        typeadv = 2
        if dfndr.type2 == 'Normal' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Dark':
            typeadv = 4
        elif dfndr.type2 == 'Flying' or dfndr.type2 == 'Psychic' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Fairy' or dfndr.type2 == 'Ghost':
            typeadv = 1

    elif move.type == 'Fighting' and (dfndr.type1 == 'Flying' or dfndr.type1 == 'Psychic' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Fairy' or dfndr.type1 == 'Ghost'):
        typeadv = 0.5
        if (dfndr.type2 == 'Normal' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Dark'):
            typeadv = 1
        elif dfndr.type2 == 'Flying' or dfndr.type2 == 'Psychic' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Fairy' or dfndr.type2 == 'Ghost':
            typeadv = 0.25
            
    if move.type == 'Fighting' and (dfndr.type2 == 'Normal' or dfndr.type2 == 'Rock' or dfndr.type2 == 'Steel' or dfndr.type2 == 'Dark'): 
        typeadv = 2
        if dfndr.type1 == 'Normal' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Dark':
            typeadv = 4
        elif dfndr.type1 == 'Flying' or dfndr.type1 == 'Psychic' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Fairy' or dfndr.type1 == 'Ghost':
            typeadv = 1
        
    elif move.type == 'Fighting' and (dfndr.type2 == 'Flying' or dfndr.type2 == 'Psychic' or dfndr.type2 == 'Poison' or dfndr.type2 == 'Bug' or dfndr.type2 == 'Fairy' or dfndr.type2 == 'Ghost'):
        typeadv = 0.5
        if (dfndr.type1 == 'Flying' or dfndr.type1 == 'Psychic' or dfndr.type1 == 'Poison' or dfndr.type1 == 'Bug' or dfndr.type1 == 'Fairy' or dfndr.type1 == 'Ghost'):
                typeadv = 0.25
        elif (dfndr.type1 == 'Normal' or dfndr.type1 == 'Rock' or dfndr.type1 == 'Steel' or dfndr.type1 == 'Dark'):
            typeadv = 1

    return 1.5 * typeadv * (random.randrange(85,101)/100)

def tie(current_enemy):
   
   #To Prevent Monitor Destruction
   #1. Show Blaziken HP

   DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (0, 26)) 
   health_string = str(int((blaziken.chp / blaziken.hp) * 100))
   if health_string == '0' and blaziken.chp != 0:
        health_string = str((blaziken.chp / blaziken.hp) * 100)
        textSurf = font.render(health_string[0:4] + "%" , True, BLACK)
   else:    
        textSurf = font.render(health_string + "%" , True, BLACK)
        
   textSurfRect = textSurf.get_rect() 
   textSurfRect.topleft = (35, 42)
   DISPLAYSURF.blit(textSurf, textSurfRect) 
   
   pygame.display.update() 
   #2. Show Enemy HP
   DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (347, 26))
   
   health_string2 = str(int((current_enemy.chp / current_enemy.hp) * 100))
   if health_string2 == '0' and current_enemy.chp != 0:
        health_string2 = str((current_enemy.chp / current_enemy.hp) * 100)
        textSurf2 = font.render(health_string2[0:4] + "%" , True, BLACK)
   else:    
        textSurf2 = font.render(health_string2 + "%" , True, BLACK)
            
   textSurfRect2 = textSurf2.get_rect() 
   textSurfRect2.topleft = (382, 42)
   DISPLAYSURF.blit(textSurf2, textSurfRect2)
                
   loadHelp('turnlog')
    
   #END GAME     
   textSurf = eventfont.render("IT'S A TIE!", True, BLACK)
   textSurfRect = textSurf.get_rect()
   textSurfRect.topleft = (WINDOWWIDTH, WINDOWHEIGHT/2)
   textSurfRect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/3) 
   DISPLAYSURF.blit(textSurf, textSurfRect)

   pygame.display.update()
   while True:
       for event in pygame.event.get(): #When you want to quit

                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

def gameOver(current_enemy):
   
   #To Prevent Monitor Destruction
   #1. Show Blaziken HP

   DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (0, 26)) 
   health_string = str(int((blaziken.chp / blaziken.hp) * 100))
   if health_string == '0' and blaziken.chp != 0:
        health_string = str((blaziken.chp / blaziken.hp) * 100)
        textSurf = font.render(health_string[0:4] + "%" , True, BLACK)
   else:    
        textSurf = font.render(health_string + "%" , True, BLACK)
        
   textSurfRect = textSurf.get_rect() 
   textSurfRect.topleft = (35, 42)
   DISPLAYSURF.blit(textSurf, textSurfRect) 
   
   pygame.display.update() 
   #2. Show Enemy HP
   DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (347, 26))
   
   health_string2 = str(int((current_enemy.chp / current_enemy.hp) * 100))
   if health_string2 == '0' and current_enemy.chp != 0:
        health_string2 = str((current_enemy.chp / current_enemy.hp) * 100)
        textSurf2 = font.render(health_string2[0:4] + "%" , True, BLACK)
   else:    
        textSurf2 = font.render(health_string2 + "%" , True, BLACK)
            
   textSurfRect2 = textSurf2.get_rect() 
   textSurfRect2.topleft = (382, 42)
   DISPLAYSURF.blit(textSurf2, textSurfRect2)

   loadHelp('turnlog')             
    
   #END GAME     
   textSurf = eventfont.render("GAME OVER!", True, BLACK)
   textSurfRect = textSurf.get_rect()
   textSurfRect.topleft = (WINDOWWIDTH, WINDOWHEIGHT/2)
   textSurfRect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/3) 
   DISPLAYSURF.blit(textSurf, textSurfRect)

   pygame.display.update()
   while True:
       for event in pygame.event.get(): #When you want to quit

                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

def youWin(current_enemy):
   
   #To Prevent Monitor Destruction
   #1. Show Blaziken HP

   DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (0, 26)) 
   health_string = str(int((blaziken.chp / blaziken.hp) * 100))
   if health_string == '0' and blaziken.chp != 0:
        health_string = str((blaziken.chp / blaziken.hp) * 100)
        textSurf = font.render(health_string[0:4] + "%" , True, BLACK)
   else:    
        textSurf = font.render(health_string + "%" , True, BLACK)
        
   textSurfRect = textSurf.get_rect() 
   textSurfRect.topleft = (35, 42)
   DISPLAYSURF.blit(textSurf, textSurfRect) 
   
   pygame.display.update() 
   #2. Show Enemy HP
   DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (347, 26))
   
   health_string2 = str(int((current_enemy.chp / current_enemy.hp) * 100))
   if health_string2 == '0' and current_enemy.chp != 0:
        health_string2 = str((current_enemy.chp / current_enemy.hp) * 100)
        textSurf2 = font.render(health_string2[0:4] + "%" , True, BLACK)
   else:    
        textSurf2 = font.render(health_string2 + "%" , True, BLACK)
            
   textSurfRect2 = textSurf2.get_rect() 
   textSurfRect2.topleft = (382, 42)
   DISPLAYSURF.blit(textSurf2, textSurfRect2)
                
   loadHelp('turnlog') 
    
   #END GAME     
   textSurf = eventfont.render("YOU WIN", True, BLACK)
   textSurfRect = textSurf.get_rect()
   textSurfRect.topleft = (WINDOWWIDTH, WINDOWHEIGHT/2)
   textSurfRect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/3) 
   DISPLAYSURF.blit(textSurf, textSurfRect)

   pygame.display.update()
   while True:
       for event in pygame.event.get(): #When you want to quit

                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                    
def victory(current_enemy):
   
   #1. Show Blaziken HP

   DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (0, 26)) 
   health_string = str(int((blaziken.chp / blaziken.hp) * 100))
   if health_string == '0' and blaziken.chp != 0:
        health_string = str((blaziken.chp / blaziken.hp) * 100)
        textSurf = font.render(health_string[0:4] + "%" , True, BLACK)
   else:    
        textSurf = font.render(health_string + "%" , True, BLACK)
        
   textSurfRect = textSurf.get_rect() 
   textSurfRect.topleft = (35, 42)
   DISPLAYSURF.blit(textSurf, textSurfRect) 
   
   pygame.display.update() 
   #2. Show Enemy HP
   DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (347, 26))
   
   health_string2 = str(int((current_enemy.chp / current_enemy.hp) * 100))
   if health_string2 == '0' and current_enemy.chp != 0:
        health_string2 = str((current_enemy.chp / current_enemy.hp) * 100)
        textSurf2 = font.render(health_string2[0:4] + "%" , True, BLACK)
   else:    
        textSurf2 = font.render(health_string2 + "%" , True, BLACK)
            
   textSurfRect2 = textSurf2.get_rect() 
   textSurfRect2.topleft = (382, 42)
   DISPLAYSURF.blit(textSurf2, textSurfRect2)
                
   loadHelp('turnlog')
            
   #END GAME     
   textSurf = eventfont.render("VICTORY", True, BLACK)
   textSurfRect = textSurf.get_rect()
   textSurfRect.topleft = (WINDOWWIDTH, WINDOWHEIGHT/2)
   textSurfRect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/3) 
   DISPLAYSURF.blit(textSurf, textSurfRect)

   pygame.display.update()
   time.sleep(2)


def opponentsMove(opponent):

                           global log_text_top 
                           move_number = random.randrange(0,4) 

                           #MOVE USE TEXT    
                           if opponent == mewtwo: 
                               if move_number == 0:
                                log_text[log_text_top] = pygame.image.load('images/pstext.png')
                                log_text_top+=1 
                               if move_number == 1:
                                log_text[log_text_top] = pygame.image.load('images/mcmtext.png')
                                log_text_top+=1
                               if move_number == 2:
                                log_text[log_text_top] = pygame.image.load('images/fobtext.png')
                                log_text_top+=1 
                               if move_number == 3:
                                log_text[log_text_top] = pygame.image.load('images/shbtext.png')
                                log_text_top+=1
                                
                           elif opponent == dragonite: 
                               if move_number == 0:
                                log_text[log_text_top] = pygame.image.load('images/ddctext.png')
                                log_text_top+=1 
                               if move_number == 1:
                                log_text[log_text_top] = pygame.image.load('images/dfptext.png')
                                log_text_top+=1
                               if move_number == 2:
                                log_text[log_text_top] = pygame.image.load('images/deqtext.png')
                                log_text_top+=1 
                               if move_number == 3:
                                log_text[log_text_top] = pygame.image.load('images/dddtext.png')
                                log_text_top+=1
                                
                           elif opponent == mvenusaur: 
                               if move_number == 0:
                                log_text[log_text_top] = pygame.image.load('images/sttext.png')
                                log_text_top+=1 
                               if move_number == 1:
                                log_text[log_text_top] = pygame.image.load('images/gdtext.png')
                                log_text_top+=1
                               if move_number == 2:
                                log_text[log_text_top] = pygame.image.load('images/veqtext.png')
                                log_text_top+=1 
                               if move_number == 3:
                                log_text[log_text_top] = pygame.image.load('images/slbtext.png')
                                log_text_top+=1

                           elif opponent == hooh: 
                               if move_number == 0:
                                log_text[log_text_top] = pygame.image.load('images/sftext.png')
                                log_text_top+=1 
                               if move_number == 1:
                                log_text[log_text_top] = pygame.image.load('images/brbtext.png')
                                log_text_top+=1
                               if move_number == 2:
                                log_text[log_text_top] = pygame.image.load('images/hrttext.png')
                                log_text_top+=1 
                               if move_number == 3:
                                log_text[log_text_top] = pygame.image.load('images/heqtext.png')
                                log_text_top+=1

                           elif opponent == lugia: 
                               if move_number == 0:
                                log_text[log_text_top] = pygame.image.load('images/sytext.png')
                                log_text_top+=1 
                               if move_number == 1:
                                log_text[log_text_top] = pygame.image.load('images/abtext.png')
                                log_text_top+=1
                               if move_number == 2:
                                log_text[log_text_top] = pygame.image.load('images/lrttext.png')
                                log_text_top+=1 
                               if move_number == 3:
                                log_text[log_text_top] = pygame.image.load('images/lcmtext.png')
                                log_text_top+=1

                           elif opponent == mtyranitar: 
                               if move_number == 0:
                                log_text[log_text_top] = pygame.image.load('images/cutext.png')
                                log_text_top+=1 
                               if move_number == 1:
                                log_text[log_text_top] = pygame.image.load('images/crtext.png')
                                log_text_top+=1
                               if move_number == 2:
                                log_text[log_text_top] = pygame.image.load('images/tsetext.png')
                                log_text_top+=1 
                               if move_number == 3:
                                log_text[log_text_top] = pygame.image.load('images/teqtext.png')
                                log_text_top+=1

                           elif opponent == groudon: 
                               if move_number == 0:
                                log_text[log_text_top] = pygame.image.load('images/geqtext.png')
                                log_text_top+=1 
                               if move_number == 1:
                                log_text[log_text_top] = pygame.image.load('images/gsetext.png')
                                log_text_top+=1
                               if move_number == 2:
                                log_text[log_text_top] = pygame.image.load('images/gfptext.png')
                                log_text_top+=1 
                               if move_number == 3:
                                log_text[log_text_top] = pygame.image.load('images/gdctext.png')
                                log_text_top+=1

                           elif opponent == kyogre: 
                               if move_number == 0:
                                log_text[log_text_top] = pygame.image.load('images/hptext.png')
                                log_text_top+=1 
                               if move_number == 1:
                                log_text[log_text_top] = pygame.image.load('images/sutext.png')
                                log_text_top+=1
                               if move_number == 2:
                                log_text[log_text_top] = pygame.image.load('images/ibtext.png')
                                log_text_top+=1 
                               if move_number == 3:
                                log_text[log_text_top] = pygame.image.load('images/tbtext.png')
                                log_text_top+=1

                           elif opponent == rayquaza: 
                               if move_number == 0:
                                log_text[log_text_top] = pygame.image.load('images/rddtext.png')
                                log_text_top+=1 
                               if move_number == 1:
                                log_text[log_text_top] = pygame.image.load('images/rdctext.png')
                                log_text_top+=1
                               if move_number == 2:
                                log_text[log_text_top] = pygame.image.load('images/reqtext.png')
                                log_text_top+=1 
                               if move_number == 3:
                                log_text[log_text_top] = pygame.image.load('images/bbtext.png')
                                log_text_top+=1

                           dc = damageCalc(opponent, blaziken, opponent.moves[move_number])     
                           blaziken.chp-=dc

                           if opponent.moves[move_number] == BRAVEBIRD:
                               hooh.chp-=(dc/3)
                               log_text[log_text_top] = pygame.image.load('images/brbtext2.png')
                               log_text_top+=1

                           #After Move Check Up
                           if blaziken.chp < 0:
                                blaziken.chp = 0
                           if opponent.chp < 0:
                                opponent.chp = 0
                               
                           if blaziken.chp == 0 and opponent.chp == 0: #tie, you still lose though :p
                                log_text[log_text_top] = pygame.image.load('images/death.png')
                                log_text_top+=1
                                log_text[log_text_top] = pygame.image.load('images/faint.png')
                                log_text_top+=1
                                loadHelp('turnlog')
                                tie(opponent) 

                           if blaziken.chp == 0: #G-O
                                log_text[log_text_top] = pygame.image.load('images/death.png')
                                log_text_top+=1
                                loadHelp('turnlog')
                                gameOver(opponent)

def blazikensMove(move, enemy): 
                           global log_text_top

                           if move == SWORDSDANCE:
                               log_text[log_text_top] = pygame.image.load('images/sdtext.png')
                               log_text_top+=1
                                        
                               for i in range(0,3):
                                    done = False
                                    if blaziken.attackmod == statboost[i]:
                                        blaziken.attackmod = statboost[i+1]
                                        done = True 
                                        break
    
                               if done == True:
                                        log_text[log_text_top] = pygame.image.load('images/sdtext2.png')
                                        log_text_top+=1
                               elif done == False:
                                        log_text[log_text_top] = pygame.image.load('images/nh.png')
                                        log_text_top+=1

                           elif move == NASTYPLOT:
                               log_text[log_text_top] = pygame.image.load('images/nptext.png')
                               log_text_top+=1
                                        
                               for i in range(0,3):
                                    done = False
                                    if blaziken.sattackmod == statboost[i]:
                                        blaziken.sattackmod = statboost[i+1]
                                        done = True 
                                        break
                                    elif blaziken.sattackmod == statdrop[i]:
                                        blaziken.sattackmod = statdrop[i-1]
                                        done = True 
                                        break
    
                               if done == True:
                                        log_text[log_text_top] = pygame.image.load('images/nptext2.png')
                                        log_text_top+=1
                               elif done == False:
                                        log_text[log_text_top] = pygame.image.load('images/nh.png')
                                        log_text_top+=1

                           elif move == COSMICPOWER:
                               log_text[log_text_top] = pygame.image.load('images/cptext.png')
                               log_text_top+=1
                               
                               for i in range(0,3):
                                    done = False
                                    if blaziken.defensemod == statboost[i] and blaziken.sdefensemod == statboost[i]:
                                        blaziken.defensemod = statboost[i+1]
                                        blaziken.sdefensemod = statboost[i+1]
                                        done = True 
                                        break
            
                               if done == True:
                                    log_text[log_text_top] = pygame.image.load('images/cptext2.png')
                                    log_text_top+=1
                               elif done == False:
                                    log_text[log_text_top] = pygame.image.load('images/nh.png')
                                    log_text_top+=1

                           elif move == HPUP:
                               log_text[log_text_top] = pygame.image.load('images/hutext.png')
                               log_text_top+=1

                               if blaziken.chp != blaziken.hp:
                                   blaziken.chp+=int(blaziken.hp/4)

                                   if blaziken.chp > blaziken.hp:
                                        blaziken.chp = blaziken.hp
                                    
                                   log_text[log_text_top] = pygame.image.load('images/hutext2.png')
                                   log_text_top+=1

                               else:
                                    log_text[log_text_top] = pygame.image.load('images/nh.png')
                                    log_text_top+=1

                           elif move == HJK:
                               log_text[log_text_top] = pygame.image.load('images/hjktext.png')
                               log_text_top+=1
                           
                               dc = damageCalc(blaziken, enemy, HJK)
                               enemy.chp-=dc 

                               #HJK Specifics (Crash)
                               if dc == 0:
                                   crash_d = ((((0.84 * (blaziken.attack/enemy.defense) * HJK.basepower) + 2) * crashModifier(enemy, HJK))/2)    
                                   if crash_d > (blaziken.hp/2): #cant do more than 50% of his total health as crash damage
                                       blaziken.chp-=(blaziken.hp/2)
                                   else:
                                       blaziken.chp-=crash_d

                           elif move == FLAREBLITZ:
                               log_text[log_text_top] = pygame.image.load('images/fbtext.png')
                               log_text_top+=1
                            
                               dc = damageCalc(blaziken, enemy, FLAREBLITZ)
                               enemy.chp-=dc

                               #Flare Blitz Recoil 
                               blaziken.chp-=(dc/3)
                               log_text[log_text_top] = pygame.image.load('images/recoil.png')
                               log_text_top+=1

                           elif move == STONEEDGE:
                                log_text[log_text_top] = pygame.image.load('images/setext.png')
                                log_text_top+=1
                            
                                dc = damageCalc(blaziken, enemy, STONEEDGE)
                                enemy.chp-=dc
                            
                           elif move == THUNDERPUNCH:
                               log_text[log_text_top] = pygame.image.load('images/tptext.png')
                               log_text_top+=1
                            
                               dc = damageCalc(blaziken, enemy, THUNDERPUNCH)
                               enemy.chp-=dc

                           elif move == VACUUMWAVE:
                               log_text[log_text_top] = pygame.image.load('images/vwtext.png')
                               log_text_top+=1
                            
                               dc = damageCalc(blaziken, enemy, VACUUMWAVE)
                               enemy.chp-=dc

                           elif move == FLAMETHROWER:
                               log_text[log_text_top] = pygame.image.load('images/fttext.png')
                               log_text_top+=1
                            
                               dc = damageCalc(blaziken, enemy, FLAMETHROWER)
                               enemy.chp-=dc

                           elif move == OVERHEAT:
                               log_text[log_text_top] = pygame.image.load('images/ohtext.png')
                               log_text_top+=1
                            
                               dc = damageCalc(blaziken, enemy, FLAMETHROWER)
                               enemy.chp-=dc
                                        
                               for i in range(0,3):
                                    done = False
                                    if blaziken.sattackmod == statdrop[i]:
                                        blaziken.sattackmod = statdrop[i+1]
                                        done = True 
                                        break
                                    elif blaziken.sattackmod == statboost[i]:
                                        blaziken.sattackmod = statboost[i-1]
                                        done = True 
                                        break
    
                               if done == True:
                                        log_text[log_text_top] = pygame.image.load('images/ohtext2.png')
                                        log_text_top+=1
                               elif done == False:
                                        log_text[log_text_top] = pygame.image.load('images/nh.png')
                                        log_text_top+=1

                           elif move == SOLARBEAM:
                               log_text[log_text_top] = pygame.image.load('images/sbtext2.png')
                               log_text_top+=1

                               dc = damageCalc(blaziken, enemy, SOLARBEAM)
                               enemy.chp-=dc                             
                            
                           #After Move Check Up 
                           if blaziken.chp < 0:
                              blaziken.chp = 0
                           if enemy.chp < 0:
                              enemy.chp = 0
                           
                           if blaziken.chp == 0 and enemy.chp == 0: #tie, you still lose though :p
                               log_text[log_text_top] = pygame.image.load('images/death.png')
                               log_text_top+=1
                               log_text[log_text_top] = pygame.image.load('images/faint.png')
                               log_text_top+=1
                               loadHelp('turnlog')
                               tie(enemy) 

                           if blaziken.chp == 0: #G-O
                               log_text[log_text_top] = pygame.image.load('images/death.png')
                               log_text_top+=1
                               loadHelp('turnlog')
                               gameOver(enemy)
                                              
def calcHealth(poke):
 
   #1. Show Blaziken HP
  if poke == blaziken:  
   DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (0, 26)) 
   health_string = str(int((blaziken.chp / blaziken.hp) * 100))
   if health_string == '0' and blaziken.chp != 0:
        health_string = str((blaziken.chp / blaziken.hp) * 100)
        textSurf = font.render(health_string[0:4] + "%" , True, BLACK)
   else:    
        textSurf = font.render(health_string + "%" , True, BLACK)
        
   textSurfRect = textSurf.get_rect() 
   textSurfRect.topleft = (35, 42)
   DISPLAYSURF.blit(textSurf, textSurfRect) 
   
   pygame.display.update()
   
   #2. Show Enemy HP
  else: 
   DISPLAYSURF.blit(pygame.image.load('images/hpfield.png'), (347, 26))
   
   health_string2 = str(int((poke.chp / poke.hp) * 100))
   if health_string2 == '0' and poke.chp != 0:
        health_string2 = str((poke.chp / poke.hp) * 100)
        textSurf2 = font.render(health_string2[0:4] + "%" , True, BLACK)
   else:    
        textSurf2 = font.render(health_string2 + "%" , True, BLACK)
            
   textSurfRect2 = textSurf2.get_rect() 
   textSurfRect2.topleft = (382, 42)
   DISPLAYSURF.blit(textSurf2, textSurfRect2)
   
   pygame.display.update()

                                             
if __name__ == '__main__':
    main()
