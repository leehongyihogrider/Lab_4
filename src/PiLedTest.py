import hal.hal_led as LED
import hal.hal_input_switch as SWITCH
import time



def blink_led(delay):
    LED.init()
    
    LED.set_output(0,1)
    time.sleep(delay)

    LED.set_output(0,0)
    time.sleep(delay)

def main():
    SWITCH.init()
    LED.init()

    while(True):
        switch = SWITCH.read_slide_switch()
        if switch == 0:
            blink_led(0.1)
        elif switch == 1:
            blink_led(0.2)


if __name__=='__main__':
    main()