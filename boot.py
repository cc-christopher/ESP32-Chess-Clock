from disp_clock import timer_var, pixel_var
from machine import Timer, Pin

W = False

Wm1 = 1
Wm2 = 0
Ws1 = 0
Ws2 = 0

Bm1 = 1
Bm2 = 0
Bs1 = 0
Bs2 = 0

flick = Timer(0)
button = Pin(4, Pin.IN)

def Bmain_timer(hdt):
    global Bm1, Bm2, Bs1, Bs2
    pixel_var(Wm1, Wm2, Ws1, Ws2, Bm1, Bm2, Bs1, Bs2)
    Bm1, Bm2, Bs1, Bs2 = timer_var(Bm1, Bm2, Bs1, Bs2)
    print(Bm1, Bm2, Bs1, Bs2)

def Wmain_timer(hdt):
    global Wm1, Wm2, Ws1, Ws2
    pixel_var(Wm1, Wm2, Ws1, Ws2, Bm1, Bm2, Bs1, Bs2)
    Wm1, Wm2, Ws1, Ws2 = timer_var(Wm1, Wm2, Ws1, Ws2)
    print(Wm1, Wm2, Ws1, Ws2)

def click(pin):
    global W
    W = not W
    if W:
        print("W")
        flick.deinit()
        flick.init(period=1000, mode=Timer.PERIODIC, callback=Wmain_timer)
    else:
        print("B")
        flick.deinit()
        flick.init(period=1000, mode=Timer.PERIODIC, callback=Bmain_timer)

button.irq(trigger=Pin.IRQ_FALLING, handler=click)
