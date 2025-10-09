from PIL import Image
import numpy as np

inicjaly = Image.open("inicjaly.bmp")

print("tryb", inicjaly.mode)
print("format", inicjaly.format)
print("rozmiar", inicjaly.size)

# t_inicjaly = np.asarray(inicjaly)
# print("typ danych tablicy", t_inicjaly.dtype)
# print("rozmiar tablicy", t_inicjaly.shape)


#--------------------- Zadanie 1 ----------------------#
def rysuj_paski_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape
    for i in range(h):
        for j in range(w):
            if i < grub or j < grub or i > h - grub or j > w - grub:
                tab_obraz[i][j] = 0

    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)

# rysuj_paski_w_obrazie(inicjaly, 6).show()

#---------------- Zadanie 2 -------------------#
# 1.1
def rysuj_ramki(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    c =  int(w/grub)

    for i in range(c):
        top = i * grub
        bottom = h - i * grub
        left = i * grub
        right = w - i * grub

        if i % 2 == 1:
            tab[top:bottom, left:right] = 1
        else:
            tab[top:bottom, left:right] = 0

    tab = tab * 255
    return Image.fromarray(tab)

# rysuj_ramki(250, 85, 10).show()

# 1.2
def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile =  int(h/grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                tab[i, j] = k % 2
    tab = tab * 255
    return Image.fromarray(tab)

rysuj_pasy_pionowe(180, 100, 20).show()
