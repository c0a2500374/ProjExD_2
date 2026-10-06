import os
import sys
import pygame as pg
import random
import time

WIDTH, HEIGHT = 1100, 650

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#課題１
def game_over(screen: pg.Surface) -> None:
    
    """
    ゲームオーバー画面を表示する関数
    引数：画面Surface
    戻り値：なし
    """

    black = pg.Surface((WIDTH, HEIGHT))
    black.set_alpha(200)
    black.fill((0, 0, 0))
    screen.blit(black, (0, 0))

    kk_img8_1 = pg.image.load("fig/8.png")
    kk_img8_1 = pg.transform.rotozoom(kk_img8_1, 0, 0.9)
    kk_img8_2 = pg.image.load("fig/8.png")
    kk_img8_2 = pg.transform.rotozoom(kk_img8_2, 0, 0.9)
    screen.blit(kk_img8_1, [WIDTH/2-150, HEIGHT/2])
    screen.blit(kk_img8_2, [WIDTH/2+220, HEIGHT/2])
    
    

    font = pg.font.Font(None, 80)
    txt = font.render("Game Over", True, (255, 255, 255))
    screen.blit(txt, [WIDTH/2-100, HEIGHT/2])

    pg.display.update()
    time.sleep(5)

#課題2
def init_bb_imgs() -> tuple[list[pg.Surface], list[int]]


def check_bound(rect: pg.Rect) ->tuple[bool, bool]:
    """
    引数：こうかとんor爆弾Rect
    戻り値：横方向・縦方向の真理値タプル
    """
    yoko, tate = True, True
    if rect.left < 0 or WIDTH < rect.right:
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom:
        tate = False
    return yoko, tate  


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    clock = pg.time.Clock()
    tmr = 0
    move_jisyo={pg.K_UP:(0,-5),
              pg.K_DOWN:(0,5),
              pg.K_RIGHT:(5,0),
              pg.K_LEFT:(-5,0),}
    bb_img = pg.Surface((20,20))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    bb_img.set_colorkey((0, 0, 0))
    bb_rct = bb_img.get_rect()
    bb_rct.centerx = random.randint(0, WIDTH)
    bb_rct.centery = random.randint(0, HEIGHT)
    vx, vy =+5, +5
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 
        if kk_rct.colliderect(bb_rct):
            print("\n    GAME OVER\n")
            screen=game_over(screen)
            return
            

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]


        for i, tpl in move_jisyo.items():
            if key_lst[i]:
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]


        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], sum_mv[1])
        
        bb_rct.move_ip(vx,vy)
        yoko,tate = check_bound(bb_rct) 
        if not yoko:
            vx*=-1
        if not tate:
            vy*=-1
           

        screen.blit(kk_img, kk_rct)
        screen.blit(bb_img, bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
