import machine
import time

from ubitstring import Bits



def xmit(data,gpio_pin = 16,delay_us = 160):
    pin = machine.Pin(gpio_pin, machine.Pin.OUT)
    for b in data:
        for bit in range(8):
            pin.value(1 if (b & 128 != 0) else 0)
            time.sleep_us(delay_us)
            b<<=1
            


def xmit_data(data,repeat_bits,pause_in_seconds_between_plays, num_of_plays):
    
    bitstring = Bits(hex=(data * repeat_bits))
    formatted_data = bitstring.tobytes()

    for play in range(num_of_plays):
        print("Transmitting...",play,"out of",num_of_plays) 
        xmit(formatted_data,gpio_pin=16,delay_us=170)
        print("Done")
        time.sleep(pause_in_seconds_between_plays)
    

repeat_bits = 4
pause_in_seconds_between = 4
number_of_plays = 10000000000

bell_data = "bec3e43e41e79041043079e43e41f0001041e4107df61f61f61f7d86186083efb0fb0f8000c30fb0c3efb0fb079079f61861861f7d87d87c0006187d861f7d87d87d87df60860860f3c83c83c0006187d861f7d87d87c83ef20c30c30fbec3ec3e00030c3ec30fbec3e41e41e7d86186187df61f20f0000820f20c"
xmit_data(bell_data, repeat_bits, pause_in_seconds_between, number_of_plays)
