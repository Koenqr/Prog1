import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum


bgColor = (0, 0, 0)
redColor = (255, 0, 0)


def createText(text,fontSize,color,background):
    """create surface with text"""
    font=pygame.freetype.SysFont("Comic Sans MS",fontSize,bold=True)
    surface,_=font.render(text,color,background)
    return surface


class uiElement(Sprite):
    """user interface element that can be added to a surface"""
    
    def __init__(self,centerPos,text,fontSize,bg,color,action=None):
        """
              Args:
                 centerPos (tuple): x and y position of center of element
                text (str): text to display
                fontSize (int): size of font
                bg (tuple): background color
                  color (tuple): text color
        """
        self.mouseOver=False

  
        normalText=createText(text,fontSize,color,bg)
        hoverText=createText(text,fontSize*1.3,redColor,bg)
        
        self.images=[normalText,hoverText]
  
        self.rects=[
            normalText.get_rect(center=centerPos),
            hoverText.get_rect(center=centerPos)
        ]

        self.action=action

        super().__init__()
  
    def image(self):
        """return image based on mouse state"""
        return self.images[1] if self.mouseOver else self.images[0]

    def rect(self):
        """return rect based on mouse state"""
        return self.rects[1] if self.mouseOver else self.rects[0]
    
    def update(self,mousePos,click):
        """update mouse state"""
        self.mouseOver=self.rect().collidepoint(mousePos)
        if click:
            return self.action
        
    def draw(self,surface):
        """draw element to surface"""
        surface.blit(self.image(),self.rect())
        
class GameState(Enum):
    START = 0
    SETTINGS = 1
    QUIT = -1

        
        
#title screen function


def titleScreen():
    """title screen"""
    
    start=uiElement((400,300),"Start",50,bgColor,redColor,action=GameState.START)
    settings=uiElement((400,400),"Settings",50,bgColor,redColor,action=GameState.SETTINGS)
    stop=uiElement((400,500),"Stop",50,bgColor,redColor,action=GameState.QUIT)
    
    buttons=[start,settings,stop]
    
    while True:
        click=False
        
        for event in pygame.event.get():
            
            if event.type==pygame.MOUSEBUTTONUP and event.button==1:
                click=True
            
        screen.fill(bgColor)
        
        for button in buttons:
            state=button.update(pygame.mouse.get_pos(),click)
            if state is not None:
                return state
            button.draw(screen)
        
        pygame.display.flip()
        
#pygame main function


screen=pygame.display.set_mode((800,600))

def main():
    pygame.init()
    
    

    titleScreen()
        
        
        
        
        
if __name__=="__main__":
    main()