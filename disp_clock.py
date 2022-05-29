import pcd8544
from machine import Pin, SPI

spi = SPI(1)
spi.init(baudrate=2000000, polarity=0, phase=0)
cs = Pin(2)
dc = Pin(15)
rst = Pin(0)
bl = Pin(12, Pin.OUT, value=1)

lcd = pcd8544.PCD8544(spi, cs, dc, rst)

import framebuf
buffer = bytearray((pcd8544.HEIGHT // 8) * pcd8544.WIDTH)
framebuf = framebuf.FrameBuffer(buffer, pcd8544.WIDTH, pcd8544.HEIGHT, framebuf.MONO_VLSB)

def timer_var(m1, m2, s1, s2):
    if s2 > 0:
        s2 = s2-1
    else:
        if s1 > 0:
            s1 = s1-1
            s2 = 9
        else:
            if m2 > 0:
                m2 = m2-1
                s1 = 5
                s2 = 9
            else:
                if m1 > 0:
                    m1 = m1-1
                    m2 = 9
                    s1 = 5
                    s2 = 9
    return (m1, m2, s1, s2)

def zeroB(x, y):
    framebuf.hline(x+1, y+0, 12, 0)
    framebuf.hline(x+0, y+1, 14, 0)
    framebuf.hline(x+5, y+3, 2, 0)
    framebuf.hline(x+6, y+4, 2, 0)
    framebuf.hline(x+7, y+5, 2, 0)
    framebuf.hline(x+0, y+7, 14, 0)
    framebuf.hline(x+1, y+8, 12, 0)
    framebuf.vline(x+0, y+2, 5, 0) 
    framebuf.vline(x+1, y+2, 5, 0)
    framebuf.vline(x+12, y+2, 5, 0) 
    framebuf.vline(x+13, y+2, 5, 0)
    
def oneB(x, y):
    framebuf.vline(x+0, y+0, 6, 0)
    framebuf.vline(x+1, y+0, 6, 0)
    framebuf.hline(x+2, y+2, 10, 0)
    framebuf.hline(x+2, y+3, 10, 0)
    framebuf.vline(x+12, y+0, 4, 0)
    framebuf.vline(x+13, y+1, 3, 0)
    
def twoB(x, y):
    framebuf.vline(x+0, y+0, 9, 0)
    framebuf.vline(x+1, y+0, 9, 0)
    ni = 0
    for ni in range (7):
        framebuf.vline(x+ni+2, y+ni+0, 3, 0)
    framebuf.hline(x+9, y+7, 3, 0)
    framebuf.hline(x+9, y+8, 3, 0)
    framebuf.vline(x+11, y+0, 2, 0)
    framebuf.vline(x+12, y+0, 9, 0)
    framebuf.vline(x+13, y+1, 7, 0)
    
def threeB(x,y):
    framebuf.vline(x+0, y+1, 7, 0)
    framebuf.vline(x+1, y+0, 9, 0)
    framebuf.hline(x+2, y+7, 4, 0)
    framebuf.hline(x+2, y+8, 4, 0)
    framebuf.vline(x+6, y+2, 7, 0)
    framebuf.vline(x+7, y+2, 6, 0)
    ni = 0
    for ni in range (4):
        framebuf.vline(x+ni+8, y+ni+3, 3, 0)
    framebuf.vline(x+12, y+0, 9, 0)
    framebuf.vline(x+13, y+0, 9, 0)

def fourB(x,y):
    framebuf.hline(x+0, y+6, 14, 0)
    framebuf.hline(x+0, y+7, 14, 0)
    framebuf.vline(x+3, y+0, 10, 0)
    framebuf.vline(x+4, y+0, 10, 0)
    ni = 0
    for ni in range (5):
        framebuf.vline(x+ni+3, y+ni+0, 2, 0)
        framebuf.vline(x+ni+4, y+ni+0, 2, 0)
    framebuf.pixel(x+13, y+4, 1)

def fiveB(x,y):
    framebuf.vline(x+0, y+1, 7, 0)
    framebuf.vline(x+1, y+0, 9, 0)
    framebuf.vline(x+2, y+0, 2, 0)
    framebuf.hline(x+2, y+7, 4, 0)
    framebuf.hline(x+2, y+8, 4, 0)
    framebuf.vline(x+7, y+1, 8, 0)
    framebuf.vline(x+8, y+0, 8, 0)
    framebuf.hline(x+9, y+0, 4, 0)
    framebuf.hline(x+9, y+1, 4, 0)
    framebuf.vline(x+12, y+0, 9, 0)
    framebuf.vline(x+13, y+0, 9, 0)

def sixB(x,y) :
    framebuf.hline(x+1, y+0, 5, 0)
    framebuf.hline(x+8, y+0, 5, 0)
    ni = 0
    for ni in range (7):
        framebuf.hline(x+0, y+ni+1, 14, 0)
    ni = 0
    for ni in range (5):
        framebuf.hline(x+2, y+ni+2, 10, 1)
    ni = 0
    for ni in range (2):
        framebuf.vline(x+ni+6, y+2, 5, 0)
    framebuf.hline(x+1, y+8, 5, 0)
    framebuf.hline(x+8, y+8, 5, 0)
    framebuf.hline(x+8, y+7, 3, 1)
    framebuf.hline(x+7, y+8, 4, 1)

def sevenB(x,y) :
    framebuf.vline(x+0, y+2, 2, 0)
    ni = 0
    for ni in range (6):
        framebuf.vline(x+2*ni+1, y+ni+2, 2, 0)
        framebuf.vline(x+2*ni+2, y+ni+2, 2, 0)
    for ni in range(2):
        framebuf.vline(x+ni+12, y+0, 9, 0)

def eightB(x,y) :
    framebuf.hline(x+1, y+0, 5, 0)
    framebuf.hline(x+8, y+0, 5, 0)
    ni = 0
    for ni in range (7):
        framebuf.hline(x+0, y+ni+1, 14, 0)
    ni = 0
    for ni in range (5):
        framebuf.hline(x+2, y+ni+2, 10, 1)
    ni = 0
    for ni in range (2):
        framebuf.vline(x+ni+6, y+2, 5, 0)
    framebuf.hline(x+1, y+8, 5, 0)
    framebuf.hline(x+8, y+8, 5, 0)

def nineB(x,y) :
    framebuf.hline(x+1, y+0, 5, 0)
    framebuf.hline(x+8, y+0, 5, 0)
    ni = 0
    for ni in range (7):
        framebuf.hline(x+0, y+ni+1, 14, 0)
    ni = 0
    for ni in range (5):
        framebuf.hline(x+2, y+ni+2, 10, 1)
    ni = 0
    for ni in range (2):
        framebuf.vline(x+ni+6, y+2, 5, 0)
    framebuf.hline(x+1, y+8, 5, 0)
    framebuf.hline(x+8, y+8, 5, 0)
    framebuf.hline(x+3, y+0, 4, 1)
    framebuf.hline(x+3, y+1, 3, 1)

def zeroW(x, y):
    framebuf.hline(x+1, y+0, 12, 1)
    framebuf.hline(x+0, y+1, 14, 1)
    framebuf.hline(x+5, y+3, 2, 1)
    framebuf.hline(x+6, y+4, 2, 1)
    framebuf.hline(x+7, y+5, 2, 1)
    framebuf.hline(x+0, y+7, 14, 1)
    framebuf.hline(x+1, y+8, 12, 1)
    framebuf.vline(x+0, y+2, 5, 1) 
    framebuf.vline(x+1, y+2, 5, 1)
    framebuf.vline(x+12, y+2, 5, 1) 
    framebuf.vline(x+13, y+2, 5, 1)
    
def oneW(x, y):
    framebuf.vline(x+0, y+2, 3, 1)
    framebuf.vline(x+1, y+2, 4, 1)
    framebuf.hline(x+2, y+2, 10, 1)
    framebuf.hline(x+2, y+3, 10, 1)
    framebuf.vline(x+12, y+0, 6, 1)
    framebuf.vline(x+13, y+0, 6, 1)
    
def twoW(x, y):
    framebuf.vline(x+0, y+1, 7, 1)
    framebuf.vline(x+1, y+0, 9, 1)
    framebuf.vline(x+2, y+7, 2, 1)
    ni = 0
    for ni in range (2):
        framebuf.hline(x+2, y+ni+0, 3, 1)
    for ni in range (7):
        framebuf.vline(x+ni+5, y+ni+0, 3, 1)
    for ni in range (2):
        framebuf.vline(x+ni+12, y+0, 9, 1)

    
def threeW(x,y):
    ni = 0
    for ni in range (2):
        framebuf.vline(x+ni+0, y+0, 9, 1)
    for ni in range (4):
        framebuf.vline(x+ni+2, y+ni+0, 3, 1)
    for ni in range (2):
        framebuf.vline(x+ni+6, y+1, 6, 1)
    for ni in range (2):
        framebuf.hline(x+7, y+ni+0, 5, 1)
    framebuf.vline(x+11, y+7, 2, 1)
    framebuf.vline(x+12, y+0, 9, 1)
    framebuf.vline(x+13, y+1, 7, 1)

def fourW(x,y):
    framebuf.hline(x+0, y+2, 14, 1)
    framebuf.hline(x+0, y+3, 14, 1)
    framebuf.vline(x+9, y+0, 10, 1)
    framebuf.vline(x+10, y+0, 10, 1)
    ni = 0
    for ni in range (5):
        framebuf.vline(x+2*ni+0, y+ni+4, 2, 1)
        framebuf.vline(x+2*ni+1, y+ni+4, 2, 1)
    framebuf.pixel(x+0, y+5, 1)

def fiveW(x,y):
    framebuf.hline(x+1, y+0, 5, 1)
    framebuf.hline(x+8, y+0, 5, 1)
    ni = 0
    for ni in range (7):
        framebuf.hline(x+0, y+ni+1, 14, 1)
    ni = 0
    for ni in range (5):
        framebuf.hline(x+2, y+ni+2, 10, 0)
    ni = 0
    for ni in range (2):
        framebuf.vline(x+ni+6, y+2, 5, 1)
    framebuf.hline(x+1, y+8, 5, 1)
    framebuf.hline(x+8, y+8, 5, 1)
    framebuf.hline(x+8, y+7, 3, 0)
    framebuf.hline(x+7, y+8, 4, 0)
    ni = 0
    for ni in range (2):
        framebuf.hline(x+2, y+ni+0, 4, 0)
    framebuf.pixel(x+6, y+0, 0)
    framebuf.pixel(x+0, y+0, 1)
    framebuf.pixel(x+0, y+8, 1)


def sixW(x,y) :
    framebuf.hline(x+1, y+0, 5, 1)
    framebuf.hline(x+8, y+0, 5, 1)
    ni = 0
    for ni in range (7):
        framebuf.hline(x+0, y+ni+1, 14, 1)
    ni = 0
    for ni in range (5):
        framebuf.hline(x+2, y+ni+2, 10, 0)
    ni = 0
    for ni in range (2):
        framebuf.vline(x+ni+6, y+2, 5, 1)
    framebuf.hline(x+1, y+8, 5, 1)
    framebuf.hline(x+8, y+8, 5, 1)
    framebuf.hline(x+3, y+0, 4, 0)
    framebuf.hline(x+3, y+1, 3, 0)

def sevenW(x,y) :
    ni = 0
    for ni in range (6):
        framebuf.vline(x+2*ni+1, y+ni+0, 2, 1)
        framebuf.vline(x+2*ni+2, y+ni+0, 2, 1)
    for ni in range(2):
        framebuf.vline(x+ni+0, y+0, 9, 1)
    framebuf.vline(x+14, y+5, 2, 1)

def eightW(x,y) :
    framebuf.hline(x+1, y+0, 5, 1)
    framebuf.hline(x+8, y+0, 5, 1)
    ni = 0
    for ni in range (7):
        framebuf.hline(x+0, y+ni+1, 14, 1)
    ni = 0
    for ni in range (5):
        framebuf.hline(x+2, y+ni+2, 10, 0)
    ni = 0
    for ni in range (2):
        framebuf.vline(x+ni+6, y+2, 5, 1)
    framebuf.hline(x+1, y+8, 5, 1)
    framebuf.hline(x+8, y+8, 5, 1)

def nineW(x,y) :
    framebuf.hline(x+1, y+0, 5, 1)
    framebuf.hline(x+8, y+0, 5, 1)
    ni = 0
    for ni in range (7):
        framebuf.hline(x+0, y+ni+1, 14, 1)
    ni = 0
    for ni in range (5):
        framebuf.hline(x+2, y+ni+2, 10, 0)
    ni = 0
    for ni in range (2):
        framebuf.vline(x+ni+6, y+2, 5, 1)
    framebuf.hline(x+1, y+8, 5, 1)
    framebuf.hline(x+8, y+8, 5, 1)
    framebuf.hline(x+8, y+7, 3, 0)
    framebuf.hline(x+7, y+8, 4, 0)

def showDigit(num, xloc, yloc):
    if xloc == 69:
        if num == 1:
            oneW(xloc, yloc)
        elif num == 2:
            twoW(xloc, yloc)
        elif num == 3:
            threeW(xloc, yloc)
        elif num == 4:
            fourW(xloc, yloc)
        elif num == 5:
            fiveW(xloc, yloc)
        elif num == 6:
            sixW(xloc, yloc)
        elif num == 7:
            sevenW(xloc, yloc)
        elif num == 8:
            eightW(xloc, yloc)
        elif num == 9:
            nineW(xloc, yloc)
        elif num == 0:
            zeroW(xloc, yloc)
    else:
        if num == 1:
            oneB(xloc, yloc)
        elif num == 2:
            twoB(xloc, yloc)
        elif num == 3:
            threeB(xloc, yloc)
        elif num == 4:
            fourB(xloc, yloc)
        elif num == 5:
            fiveB(xloc, yloc)
        elif num == 6:
            sixB(xloc, yloc)
        elif num == 7:
            sevenB(xloc, yloc)
        elif num == 8:
            eightB(xloc, yloc)
        elif num == 9:
            nineB(xloc, yloc)
        elif num == 0:
            zeroB(xloc, yloc)
    
def pixel_var(m1, m2, s1, s2, em1, em2, es1, es2):
    global buffer
    lcd.clear()
    lcd.reset()
    lcd.init()
    framebuf.fill_rect(0,0,47,47,1)
    framebuf.fill_rect(48,0,47,47,0)
    numlist = [m1, m2, s1, s2, em1, em2, es1, es2]
    y_list = [36, 24, 12, 0, 0, 12, 24, 36]
    x_list = [69, 69, 69, 69, 1, 1, 1, 1]
    zippeds = zip(numlist, x_list, y_list)
    for zipped in zippeds:
        num, xloc, yloc = zipped
        showDigit(num, xloc, yloc)
    lcd.data(buffer)
        

