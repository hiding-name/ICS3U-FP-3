#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sep 2019
# This program draws a background on the PyBadge

import ugame
import stage

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
sprites = []
def main():
    # this function sets the background

    # sets the background to image 0 in the bank
    # backgrounds do not have magenta as a transparent color
    background = stage.Grid(image_bank_1, 10, 8)
    # changes (0,0) image to the 3rd image

    ship = stage.Sprite(image_bank_1, 5, 75, 56)
    sprites.append(ship)
    alien = stage.Sprite(image_bank_1, 9, 64, 56)
    sprites.append(alien)
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        #get user input
        
        #update game logic
        
        #redraw sprite list
        game.render_sprites(sprites)
        game.tick() #wait until refresh rate finishes
        


if __name__ == "__main__":
    main()