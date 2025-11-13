import random

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
                if (tab[i][j] == kolor).all:
                    licznik += 1

    return licznik

def negatyw(obraz):
    tab = np.asarray(obraz)
    h, w, d = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            for k in range(d):
                tab_neg[i, j, k] = 255 - tab_neg[i, j, k]
    return Image.fromarray(tab_neg)

def mieszaj_kanaly(obraz):
    obraz_n = negatyw(obraz)
    nr, ng, nb = obraz_n.split()
    r, g, b = obraz.split()
    tab1 = [r, g, b, nr, ng, nb]
    tab2 = []
    for i in range(3):
        rand = random.randrange(5)
        tab2.append(tab1[rand])

    return Image.merge("RGB", (tab2[0], tab2[1], tab2[2]))


# Zad 1
# a)
im = Image.open("obraz.png")
# print("Statystyki obrazu(im):")
# print("tryb", im.mode)
# print("format", im.format)
# print("rozmiar", im.size)
#
r, g, b = im.split()
#
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
# print("R:", zlicz_piksele(r, 155))
# print("G:", zlicz_piksele(g, 155))
# print("B:", zlicz_piksele(b, 155))

# c)
# print("Obraz:", zlicz_piksele(im, [155,155,155])) # poprawić

# ------------------------------------- zad 2 ------------------------------------- #
# a)
# im.save("im.jpg")
# im_jpg = Image.open("im.jpg")
# print("Statystyki obrazu(im):")
# statystyki(im)
#
# print("Statystyki obrazu(im_jpg):")
# statystyki(im_jpg)

# b)
# dif = ImageChops.difference(im, im_jpg)
# statystyki(dif)

# c)
# im_jpg.save("im2.jpg")
# im_jpg2 = Image.open("im2.jpg")
# im_jpg2.save("im3.jpg")
# im_jpg3 = Image.open("im3.jpg")
# dif2 = ImageChops.difference(im, im_jpg3)
# statystyki(dif2)

# ------------------------------------- zad 3 ------------------------------------- #

#a)
# t = np.array(im, dtype=np.uint8)
# t_r = t[:, :, 0]
# t_g = t[:, :, 1]
# t_b = t[:, :, 2]
# im_r = Image.fromarray(t_r)
# im_g = Image.fromarray(t_g)
# im_b = Image.fromarray(t_b)

# b)
# im_merged = Image.merge("RGB", (im_r, im_g, im_b))

# c)
# plt.figure(figsize=(16, 16))
# plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
# plt.title("im")
# plt.imshow(im)
# plt.axis('off')
# plt.subplot(2,2,2)
# plt.title("im1")
# plt.imshow(im_merged)
# plt.axis('off')
# plt.subplot(2,2,3)
# plt.title("Porównianie")
# plt.imshow(ImageChops.difference(im, im_merged))
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.25)
# plt.savefig('fig1.png')
# plt.show()

# d)
# Nie widać różnicy pomiędzy obrazami

# ------------------------------------- zad 4 ------------------------------------- #

# a)
mix = mieszaj_kanaly(im)
# mix.show()
# mix.save("mix.png")

# b)
# print(rozpoznaj_mix(im, mix)) #w domu

# ------------------------------------- zad 5 ------------------------------------- #
im = Image.open('beksinski1.png')
r, g, b, a = im.split() # ponieważ jest kanał alfa.
