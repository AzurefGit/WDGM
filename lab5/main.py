from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()

def rysuj_histogram_L(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:])
    plt.show()

def zlicz_piksele(obraz, kolor):
    licznik = 0
    tab = np.array(obraz, dtype=np.uint8)
    if tab.ndim == 2:
        d1, d2 = tab.shape
        for i in range(d1):
            for j in range(d2):
                if tab[i][j] == kolor:
                    licznik += 1

    elif tab.ndim == 3:
        d1, d2, d3 = tab.shape
        for i in range(d1):
            for j in range(d2):
                for k in range(d3):
                    if (tab[i][j] == kolor).any:
                        licznik += 1

    return licznik


# Zad 1
# a)
im = Image.open("obraz.png")
# print("Statystyki obrazu(im):")
# print("tryb", im.mode)
# print("format", im.format)
# print("rozmiar", im.size)

r, g, b = im.split()

# statystyki(im)
# rysuj_histogram_RGB(im)
# rysuj_histogram_L(r)
# rysuj_histogram_L(g)
# rysuj_histogram_L(b)

# przedstawienie 4 obrazów w jednym oknie plt
# plt.figure(figsize=(16, 16))
# plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
# plt.imshow(im)
# plt.axis('off')
# plt.subplot(2,2,2)
# plt.imshow(r, "gray")
# plt.axis('off')
# plt.subplot(2,2,3)
# plt.imshow(g, "gray")
# plt.axis('off')
# plt.subplot(2,2,4)
# plt.imshow(b, "gray")
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('figura1.png')
# plt.show()

# b)
print("R:", zlicz_piksele(r, 155))
print("G:", zlicz_piksele(g, 155))
print("B:", zlicz_piksele(b, 155))

# c)
# print("Obraz:", zlicz_piksele(im, [155,155,155])) # poprawić

# ------------------------------------- zad 2 ------------------------------------- #
# a)
im.save("im.jpg")
