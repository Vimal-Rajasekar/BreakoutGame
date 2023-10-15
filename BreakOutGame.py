'''BreakOut Game Using Pygame.'''
import pygame

'''To Initialize all the pygame classes'''
pygame.init()
'''Giving Dimension for Screen Of Constant Sizes'''
WIDTH=700
HEIGHT=700
FPS=60#Frames per Second-->It'll erase and draw again and again for 60 times a second.
'''Creating Constant   Number of Rows and Columns'''
ROWS=6
COLS=10
'''Creating Constants of Color with rgb() values'''
WHITE=(255,255,255)#rgb
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(80,175,90)
BLUE=(60,160,200)
''' Creating Object for Screen Display by method'''
window_screen=pygame.display.set_mode((WIDTH,HEIGHT))
'''Setting Title to the Screen Tab'''
pygame.display.set_caption("BreakOutGame")
'''It'll return a time object '''
clock=pygame.time.Clock()

'''Creating Classess For drawing Paddle:'''

class Paddle:
    def __init__(self):
        self.width=int(WIDTH/COLS)
        self.height=20
        self.x = int(WIDTH/2)-int(self.width/2)
        self.y = HEIGHT-40
        self.speed = 10#How many pixels this paddle should move when clicking the button.
        '''Drawing this paddle first as a rectangle.It contains the datas of rectangle to be drawn'''
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)#(x,y coordinates,height,width of paddle)

    '''Method to Draw the Paddle'''
    def draw_paddle(self):
        pygame.draw.rect(window_screen,WHITE,self.rect)#rect() is a method to draw rectangle
    def move_paddle(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left>0:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT] and self.rect.right<WIDTH:
            self.rect.x += self.speed

'''Creating Class For Ball:'''
class Ball:
    def __init__(self,x,y):
        self.radius=10
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,self.radius*2,self.radius*2)
        self.dx = 3
        self.dy = -3
        self.game_status = 0

    '''Method For Drawing a Ball.'''
    def draw_ball(self):
        pygame.draw.circle(window_screen,BLUE,(self.rect.x,self.rect.y),self.radius)

    '''Method For Moving a Ball.'''
    def move_ball(self):
        #Wall Colllision
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.dx *= -1
        if self.rect.top < 0:
            self.dy *= -1
        if self.rect.bottom > HEIGHT:
            self.game_status=-1
            return self.game_status
        '''paddle collision'''
        if self.rect.colliderect(paddle) and self.dy>0:
            self.dy*=-1

        #Brick Collision
        all_done=True
        row_val=0
        for row in brick.bricks:
            col_val=0
            for br in row:
                if self.rect.colliderect(br):
                    if abs(self.rect.top-br.bottom) < 5 and self.dy<0:
                        self.dy*=-1
                    if abs(self.rect.bottom-br.top) < 5 and self.dy>0:
                        self.dy*=-1
                    if abs(self.rect.right-br.left) < 5 and self.dx>0:
                        self.dx*=-1
                    if abs(self.rect.left-br.right) < 5 and self.dx<0:
                        self.dx*=-1
                    brick.bricks[row_val][col_val] = (0, 0, 0, 0)
                if brick.bricks[row_val][col_val]!=(0,0,0,0):
                    all_done=False
                col_val+=1
            row_val+=1

        if all_done:
            self.game_status = 1

        self.rect.x += self.dx
        self.rect.y += self.dy

'''Creating Brick Class'''
class Brick:
    def __init__(self):
        self.width=int(WIDTH/COLS)
        self.height=30
    def create_bricks(self):
        self.bricks=[]
        for row in range(ROWS):
            brick_row=[]
            for col in range(COLS):
                bricks_x=col*self.width
                bricks_y=row*self.height
                br=pygame.Rect(bricks_x,bricks_y,self.width,self.height)
                brick_row.append(br)
            self.bricks.append(brick_row)

    def draw_bricks(self):
        for  row in self.bricks:
            for br in row:
                pygame.draw.rect(window_screen,GREEN,br)
                pygame.draw.rect(window_screen,BLACK,br,2)






'''Creating Object for Paddle Class'''
paddle=Paddle()
'''Creating Object for Ball Class'''
ball = Ball(paddle.x+int(paddle.width/2),paddle.y-10)
'''Creating Object for Brick Class'''
brick=Brick()
brick.create_bricks()
'''Setting Default Values to a variable as True so that program will by default.
when they cancel the game,we need to stop.It is done by taking every active events and comparing it with Quit action
If they click quit,run variable become false and program will stop.'''
run=True
while run:
    clock.tick(FPS)#Clock object will start with 60 frames per second.
    window_screen.fill(BLACK)
    paddle.draw_paddle()#Every time loop calls background of previous object will be black
    paddle.move_paddle()
    ball.draw_ball()
    brick.draw_bricks()
    game_status=ball.move_ball()
    if game_status==-1:
        window_screen.fill(BLACK)
        font=pygame.font.SysFont(None,50)
        text=font.render('GAME OVER',True,BLUE)
        text_rect=text.get_rect(center=(WIDTH/2,HEIGHT/2))
        window_screen.blit(text,text_rect)
        brick.draw_bricks()
    if game_status==1:
        window_screen.fill(BLACK)
        font=pygame.font.SysFont(None,50)
        text=font.render('YOU WIN',True,BLUE)
        text_rect=text.get_rect(center=(WIDTH/2,HEIGHT/2))
        window_screen.blit(text,text_rect)
        brick.draw_bricks()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
    pygame.display.update()

'''After executing code,we are quiting the program'''
pygame.quit()
