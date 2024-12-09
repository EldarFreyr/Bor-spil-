from machine import Pin, PWM
import random
from neopixel import NeoPixel
from time import sleep_ms
import math

neo = NeoPixel(Pin(45), 24)

shuffle_ljos = Pin(40, Pin.OUT)
bolvunar_ljos = Pin(12, Pin.OUT)
teninga_ljos = Pin(41, Pin.OUT)

shuffle_takki = Pin(39, Pin.IN, Pin.PULL_UP)
bolvunar_takki = Pin(13, Pin.IN, Pin.PULL_UP)
teninga_takki = Pin(42, Pin.IN, Pin.PULL_UP)

reed = Pin(2, Pin.IN, Pin.PULL_UP) 

hatalari = PWM(Pin(4), freq=1000)

hatalari.duty(0)
neo.fill([0, 0, 0])
neo.write()

teninga_ljos.value(0)
# Define a dictionary with note frequencies
note_frequencies = { 'C0': 16, 'C#0': 17, 'D0': 18, 'D#0': 19, 'E0': 21, 'F0': 22, 'F#0': 23, 'G0': 25, 'G#0': 26, 'A0': 28, 'A#0': 29, 'B0': 31,
                     'C1': 33, 'C#1': 35, 'D1': 37, 'D#1': 39, 'E1': 41, 'F1': 44, 'F#1': 46, 'G1': 49, 'G#1': 52, 'A1': 55, 'A#1': 58, 'B1': 62,
                     'C2': 65,'C#2': 69, 'D2': 73, 'D#2': 78, 'E2': 82, 'F2': 87, 'F#2': 93, 'G2': 98, 'G#2': 104, 'A2': 110, 'A#2': 117, 'B2': 123,
                     'C3': 131, 'C#3': 139, 'D3': 147, 'D#3': 156, 'E3': 165, 'F3': 175, 'F#3': 185, 'G3': 196, 'G#3': 208, 'A3': 220, 'A#3': 233, 'B3': 247,
                     'C4': 262, 'C#4': 277, 'D4': 294, 'D#4': 311, 'E4': 330, 'F4': 349, 'F#4': 370, 'G4': 392, 'G#4': 415, 'A4': 440, 'A#4': 466, 'B4': 494,
                     'C5': 523, 'C#5': 554, 'D5': 587, 'D#5': 622, 'E5': 659, 'F5': 698, 'F#5': 740, 'G5': 784, 'G#5': 831, 'A5': 880, 'A#5': 932, 'B5': 988,
                     'C6': 1047, 'C#6': 1109, 'D6': 1175, 'D#6': 1244, 'E6': 1319, 'F6': 1397, 'F#6': 1480, 'G6': 1568, 'G#6': 1661, 'A6': 1760, 'A#6': 1865, 'B6': 1976,
                     'C7': 2093, 'C#7': 2217, 'D7': 2349, 'D#7': 2489, 'E7': 2637, 'F7': 2794, 'F#7': 2960, 'G7': 3136, 'G#7': 3322, 'A7': 3520, 'A#7': 3730, 'B7': 3951,
                     'C8': 4186, 'C#8': 4435, 'D8': 4699, 'D#8': 4978, 'E8': 5274, 'F8': 5588, 'F#8': 5920, 'G8': 6272, 'G#8': 6645, 'A8': 7040, 'A#8': 7459, 'B8': 7902,
                     'S': 1000000
                     }

def get_frequencies(notes):
    # Split the input string into a list of notes
    note_list = notes.split()
    # Map each note to its corresponding frequency using the dictionary
    frequencies = [note_frequencies[note.upper()] for note in note_list]
    return frequencies

# Play tune
def play_tune():
    frequencies = get_frequencies(notes)
    hatalari.duty(512)
    for i in range(len(frequencies)):
        hatalari.freq(frequencies[i])
        sleep_ms(125)
    hatalari.duty(0)
    
def play_tune2():
    litirR = [
        148, #Violet
        65,  #Indigo
        0, #Blue
        0, #Lightblue
        0, #Cyan
        0, # Green
        230, # Yellow
        255, # Orange
        255, # Red
        210 # Pink
    ]
    litirG = [
        0, #Violet
        0, #Indigo
        0, #Blue
        90, #Lightblue
        220, #Cyan
        230, # Green
        230, # Yellow
        50, # Orange
        0, # Red
        25 # Pink
    ]
    litirB = [
        211, #Violet
        210,  #Indigo
        255,  #Blue
        180, #Lightblue
        220, #Cyan
        0, # Green
        0, # Yellow
        0, # Orange
        0, # Red
        25 # Pink
    ]
    liturR = litirR[0]
    liturG = litirG[0]
    liturB = litirB[0]
    Brightness = 0.2
    num = 0
    frequencies = get_frequencies(notes)
    hatalari.duty(512)
    for i in range(len(frequencies)):
        hatalari.freq(frequencies[i])
        sleep_ms(125)
        num = num+1
        liturR = litirR[(num-1) % 8 +1]
        liturG = litirG[(num-1) % 8 +1]
        liturB = litirB[(num-1) % 8 +1]
        neo.fill([0, 0, 0])
        for i2 in range(24):
            liturR = litirR[((i2-num) % 8 +1)]
            liturG = litirG[((i2-num) % 8 +1)]
            liturB = litirB[((i2-num) % 8 +1)]
            neo[i2] = [round(liturR*Brightness), round(liturG*Brightness), round(liturB*Brightness)]
        neo.write()
        timi = 300
    for i in range(400):
        timi = math.floor(timi*0.99999)
        hatalari.freq(7000-timi*20)
        num = num+1
        liturR = litirR[(num-1) % 8 +1]
        liturG = litirG[(num-1) % 8 +1]
        liturB = litirB[(num-1) % 8 +1]
        neo.fill([0, 0, 0])
        for i2 in range(24):
            liturR = litirR[((i2-num) % 8 +1)]
            liturG = litirG[((i2-num) % 8 +1)]
            liturB = litirB[((i2-num) % 8 +1)]
            neo[i2] = [round(liturR*Brightness), round(liturG*Brightness), round(liturB*Brightness)]
        neo.write()
        sleep_ms(timi)
    neo.fill([0, 0, 0])
    neo.write()
    teninga_ljos.value(0)
    hatalari.duty(0)
    
    
while reed.value() == 1:
    if shuffle_takki.value() == 0:
        shuffle_ljos.value(1)
        #Shuffle V2 Takki pressed
        litirR = [
            255,
            255,
            0,
            0
        ]
        litirG = [
            0,
            50,
            0,
            255
        ]
        litirB = [
            0,
            0,
            255,
            0
        ]
        litir = [1,2,3,4]
        litir2 = 0
        litir3 = []
        for i in range(4):
            litir2 = random.choice(litir)
            litir.remove(litir2)
            litir3.append(litir2)
        litir = litir3

        litur1 = litir[0]
        litur2 = litir[1]
        litur3 = litir[2]
        litur4 = litir[3]

        litur1R = litirR[litur1-1]
        litur1G = litirG[litur1-1]
        litur1B = litirB[litur1-1]

        litur2R = litirR[litur2-1]
        litur2G = litirG[litur2-1]
        litur2B = litirB[litur2-1]

        litur3R = litirR[litur3-1]
        litur3G = litirG[litur3-1]
        litur3B = litirB[litur3-1]

        litur4R = litirR[litur4-1]
        litur4G = litirG[litur4-1]
        litur4B = litirB[litur4-1]

        for i in range(15):
            for i in range(6):
                neo[i] = [litur1R, litur1G, litur1B]
                neo[i+6] = [litur2R, litur2G, litur2B]
                neo[i+12] = [litur3R, litur3G, litur3B]
                neo[i+18] = [litur4R, litur4G, litur4B]
                neo.write()
                hatalari.duty(512)
                if i == 0:
                    hatalari.freq(440)
                elif i == 1:
                    hatalari.freq(494)
                elif i == 2:
                    hatalari.freq(587)
                elif i == 3:
                    hatalari.freq(659)
                elif i == 4:
                    hatalari.freq(740)
                elif i == 5:
                    hatalari.freq(880)
                sleep_ms(150)
                hatalari.duty(0)
            sleep_ms(100)
            neo.fill([0, 0, 0])
        shuffle_ljos.value(0)

    if bolvunar_takki.value() == 0:
        bolvunar_ljos.value(1)
        #Bölvunartakki pressed
        litir = [1,2,3,4]
        banlist = []
        timi = 150
        peep = 0
        for i in range(random.randint(21, 23)):
            sleep_ms(round(timi/2))
            thing1 = litir[random.randint(0,len(litir)-1)]
            litir.remove(thing1)
            banlist.append(thing1)
            hatalari.duty(512)
            hatalari.freq(2400-peep)
            peep = peep+100
            if i < 10:
                timi = timi+20
            elif i < 14:
                timi = timi+40
            elif i < 16:
                timi = timi+50
            elif i < 18:
                timi = timi+60
            if thing1 == 1:
                neo.fill([255, 0, 0])
                neo.write()
            if thing1 == 2:
                neo.fill([255, 50, 0])
                neo.write()
            if thing1 == 3:
                neo.fill([0, 0, 255])
                neo.write()
            if thing1 == 4:
                neo.fill([0, 255, 0])
                neo.write()
            if len(banlist) == 2:
                thing1 = banlist[0]
                banlist.remove(thing1)
                litir.append(thing1)
                litir.sort()
            sleep_ms(round(timi/2))
            hatalari.duty(0)
        #Hátalari pípar hátt
        sleep_ms(500)
        for i in range(3):
            hatalari.duty(0)
            neo.fill([0, 0, 0])
            neo.write()
            sleep_ms(200)
            hatalari.duty(512)
            hatalari.freq(1047)
            if thing1 == 1:
                neo.fill([255, 0, 0])
                neo.write()
            if thing1 == 2:
                neo.fill([255, 50, 0])
                neo.write()
            if thing1 == 3:
                neo.fill([0, 0, 255])
                neo.write()
            if thing1 == 4:
                neo.fill([0, 255, 0])
                neo.write()
            sleep_ms(250)
        sleep_ms(500)
        hatalari.duty(0)
        neo.fill([0, 0, 0])
        neo.write()
        bolvunar_ljos.value(0)
        
    if teninga_takki.value() == 0:
        teninga_ljos.value(1)
        #Teningatakki pressed
        litirR = [
            148, #Violet
            65,  #Indigo
            0, #Blue
            0, #Lightblue
            0, #Cyan
            0, # Green
            230, # Yellow
            255, # Orange
            255, # Red
            210 # Pink
        ]
        litirG = [
            0, #Violet
            0, #Indigo
            0, #Blue
            90, #Lightblue
            220, #Cyan
            230, # Green
            230, # Yellow
            50, # Orange
            0, # Red
            25 # Pink
        ]
        litirB = [
            211, #Violet
            210,  #Indigo
            255,  #Blue
            180, #Lightblue
            220, #Cyan
            0, # Green
            0, # Yellow
            0, # Orange
            0, # Red
            25 # Pink
        ]
        tala = random.randint(1,6)*4
        liturR = litirR[0]
        liturG = litirG[0]
        liturB = litirB[0]
        num = 0
        Brightness = 0.2
        for i in range(tala):
            hatalari.duty(512)
            if i == 0:
                hatalari.freq(262)
            elif i == 1:
                hatalari.freq(277)
            elif i == 2:
                hatalari.freq(294)
            elif i == 3:
                hatalari.freq(311)
            elif i == 4:
                hatalari.freq(330)
            elif i == 5:
                hatalari.freq(349)
            elif i == 6:
                hatalari.freq(370)
            elif i == 7:
                hatalari.freq(392)
                Brightness = 0.3
            elif i == 8:
                hatalari.freq(415)
            elif i == 9:
                hatalari.freq(440)
            elif i == 10:
                hatalari.freq(466)
            elif i == 11:
                hatalari.freq(494)
                Brightness = 0.45
            elif i == 12:
                hatalari.freq(523)
            elif i == 13:
                hatalari.freq(554)
            elif i == 14:
                hatalari.freq(587)
            elif i == 15:
                hatalari.freq(622)
                Brightness = 0.6
            elif i == 16:
                hatalari.freq(659)
            elif i == 17:
                hatalari.freq(698)
            elif i == 18:
                hatalari.freq(740)
            elif i == 19:
                hatalari.freq(788)
                Brightness = 0.75
            elif i == 20:
                hatalari.freq(831)
            elif i == 21:
                hatalari.freq(880)
            elif i == 22:
                hatalari.freq(932)
            elif i == 23:
                Brightness = 1
                hatalari.freq(988)
            num = num+1
            liturR = litirR[(num-1) % 8 +1]
            liturG = litirG[(num-1) % 8 +1]
            liturB = litirB[(num-1) % 8 +1]
            neo.fill([0, 0, 0])
            for i2 in range(i+1):
                liturR = litirR[((i2-num) % 8 +1)]
                liturG = litirG[((i2-num) % 8 +1)]
                liturB = litirB[((i2-num) % 8 +1)]
                neo[i2] = [round(liturR*Brightness), round(liturG*Brightness), round(liturB*Brightness)]
            neo.write()
            sleep_ms(150)
            hatalari.duty(0)
            sleep_ms(25)

        for i in range(65):
            if (num-1) % 8 +1 < 3:
                notes = "C5"
            elif (num-1) % 8 +1 < 5:
                notes = "A4"
            elif (num-1) % 8 +1 < 8:
                notes = "B4"
            else:
                notes = "A4"
            play_tune()
            num = num+1
            liturR = litirR[(num-1) % 8 +1]
            liturG = litirG[(num-1) % 8 +1]
            liturB = litirB[(num-1) % 8 +1]
            neo.fill([0, 0, 0])
            for i2 in range(tala):
                liturR = litirR[((i2-num) % 8 +1)]
                liturG = litirG[((i2-num) % 8 +1)]
                liturB = litirB[((i2-num) % 8 +1)]
                neo[i2] = [round(liturR*Brightness), round(liturG*Brightness), round(liturB*Brightness)]
                if reed.value() == 0:
                    break
            if reed.value() == 0:
                break
            neo.write()
            sleep_ms(50)
        neo.fill([0, 0, 0])
        neo.write()
        teninga_ljos.value(0)


notes = "A4 B4 C#5 E5 S C#5 E5 E5 A#4 C5 D5 F5 S D5 F5 F5 A4 B4 C#5 E5 S C#5 E5 S E5 C5 D#5 B4 D5 A#4 A5 A5 A5 A5 S S S S"
play_tune2()
sleep_ms(5000)
