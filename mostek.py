import math

d_drutu = 1000

pomiar_wzorcowy = [10,11, 12, 13, 14, 15, 16, 17, 9, 18]
dlugosci = [564, 537, 515, 494, 474, 446, 439, 424, 592, 412]

rx = [pomiar_wzorcowy[i] * dlugosci[i] / (d_drutu - dlugosci[i]) for i in range(len(pomiar_wzorcowy))]

srednia_rx = sum(rx) / len(rx)

niepewnosc_rx = math.sqrt(sum([math.pow(i - srednia_rx,2) for i in rx]) / (len(rx) * (len(rx) - 1)))

print("rx1: ")
print(rx)
print(srednia_rx)
print(niepewnosc_rx)

pomiar_wzorcowy2 = [i + 30 for i in range(10)]
dlugosci2 = [537, 528, 517, 510, 503, 496, 489, 481, 476, 469]



rx2 = [pomiar_wzorcowy2[i] * dlugosci2[i] / (d_drutu - dlugosci2[i]) for i in range(len(pomiar_wzorcowy2))]

srednia_rx2 = sum(rx2) / len(rx2)

niepewnosc_rx2 = math.sqrt(sum([math.pow(i - srednia_rx2,2) for i in rx2]) / (len(rx2) * (len(rx2) - 1)))
print("rx2: ")
print(rx2)
print(srednia_rx2)
print(niepewnosc_rx2)


pomiar_wzorcowy3 = [70 + (i * 2) for i in range(10)]
dlugosci3 = [503, 497, 490, 484, 475, 469, 463, 457, 452, 446]

rx3 = [pomiar_wzorcowy3[i] * dlugosci3[i] / (d_drutu - dlugosci3[i]) for i in range(len(pomiar_wzorcowy3))]

srednia_rx3 = sum(rx3) / len(rx3)

niepewnosc_rx3 = math.sqrt(sum([math.pow(i - srednia_rx3,2) for i in rx3]) / (len(rx3) * (len(rx3) - 1)))

print("rx3: ")
print(rx3)
print(srednia_rx3)
print(niepewnosc_rx3)


print("RX2 + RX3 = ", rx2 + rx3)


pomiar_wzorcowy4 = [90 + (i * 4) for i in range(10)]
dlugosci4 = [541, 530, 519, 510, 499, 489, 481, 471, 463, 455]

rx4 = [pomiar_wzorcowy4[i] * dlugosci4[i] / (d_drutu - dlugosci4[i]) for i in range(len(pomiar_wzorcowy4))]

srednia_rx4 = sum(rx4) / len(rx4)

niepewnosc_rx4 = math.sqrt(sum([math.pow(i - srednia_rx4,2) for i in rx4]) / (len(rx4) * (len(rx4) - 1)))

print("rx4: ")
print(rx4)
print(srednia_rx4)
print(niepewnosc_rx4)



pomiar_wzorcowy5 = [23 + i for i in range(10)]
dlugosci5 = [500, 490, 481, 472, 461, 452, 442, 431, 427, 418]

rx5 = [pomiar_wzorcowy5[i] * dlugosci5[i] / (d_drutu - dlugosci5[i]) for i in range(len(pomiar_wzorcowy5))]

srednia_rx5 = sum(rx5) / len(rx5)

niepewnosc_rx5 = math.sqrt(sum([math.pow(i - srednia_rx5,2) for i in rx5]) / (len(rx5) * (len(rx5) - 1)))

print("rx5: ")
print(rx5)
print(srednia_rx5)
print(niepewnosc_rx5)

print(srednia_rx2 * srednia_rx3 / (srednia_rx3 + srednia_rx2))