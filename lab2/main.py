from PIL import Image
import numpy as np

inicjaly = Image.open("inicjaly.bmp")

# print("tryb", inicjaly.mode)
# print("format", inicjaly.format)
# print("rozmiar", inicjaly.size)
#
# t_inicjaly = np.asarray(inicjaly)
# print("typ danych tablicy", t_inicjaly.dtype)
# print("rozmiar tablicy", t_inicjaly.shape)


#--------------------- Zadanie 1 ----------------------#
tablica = np.loadtxt("tablica.txt", dtype=np.bool)
obraz = Image.fromarray(tablica)

def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape
    for i in range(h):
        for j in range(w):
            if i < grub or j < grub or i > h - grub or j > w - grub:
                tab_obraz[i][j] = 0

    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)

# rrwo = rysuj_ramke_w_obrazie(obraz, 50)
# rrwo.save("rrwo.bmp")

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

        if i % 2 == 0:
            tab[top:bottom, left:right] = 0
        else:
            tab[top:bottom, left:right] = 1

    tab = tab * 255
    return Image.fromarray(tab)

# rysuj_ramki(80, 130, 5)
# rr = rysuj_ramki(80, 130, 5)
# rr.save("rr.bmp")

# rr = Image.open("rr.bmp")
#
# print("tryb", rr.mode)
# print("format", rr.format)
# print("rozmiar", rr.size)
#
# t_inicjaly = np.asarray(rr)
# print("typ danych tablicy", t_inicjaly.dtype)
# print("rozmiar tablicy", t_inicjaly.shape)
# print("rozmiar tablicy", t_inicjaly.ndim)

# 1.2
def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile =  int(w/grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                tab[i, j] = k % 2
    tab = tab * 255
    return Image.fromarray(tab)

# rpp = rysuj_pasy_pionowe(200, 100, 10)
# rpp.save("rpp.bmp")
# rpp = Image.open("rpp.bmp")

# print("tryb", rpp.mode)
# print("format", rpp.format)
# print("rozmiar", rpp.size)
#
# t_inicjaly = np.asarray(rpp)
# print("typ danych tablicy", t_inicjaly.dtype)
# print("rozmiar tablicy", t_inicjaly.shape)
# p_rpp = rpp.getpixel((97,20))
# print(p_rpp)

# 1.3 Funkcja rysuje linię pionową i poziomą na raz, czyli wychodzi kratka.
def rysuj_kratke(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)

    ile_pion = int(w / grub)
    ile_poz = int(h / grub)

    for k in range(ile_pion):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                if j < w:
                    tab[i, j] = k % 2

    for k in range(ile_poz):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                if i < h:
                    if k % 2 == 0:
                        tab[i, j] = 0

    tab = tab * 255
    return Image.fromarray(tab)


rk = rysuj_kratke(220, 100, 20)
rk.save("kratka.bmp")

# Zadanie 3
def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tablica_baza = np.asarray(obraz_bazowy).astype(bool)
    tablica_wstawka = np.asarray(obraz_wstawiany).astype(bool)

    h, w = tablica_baza.shape
    h0, w0 = tablica_wstawka.shape

    poczatek_y = max(0, n)
    poczatek_x = max(0, m)
    koniec_y = min(h, n + h0)
    koniec_x = min(w, m + w0)

    for wiersz in range(poczatek_y, koniec_y):
        for kolumna in range(poczatek_x, koniec_x):
            tablica_baza[wiersz, kolumna] = tablica_wstawka[wiersz - n][kolumna - m]

    return Image.fromarray(tablica_baza)

# obraz_bazowy = rysuj_pasy_pionowe(300, 200, 15)

# wowo1 = wstaw_obraz_w_obraz(obraz_bazowy, inicjaly, 250, 100)
# wowo1.save("wowo1.bmp")
#
# wowo2 = wstaw_obraz_w_obraz(obraz_bazowy, inicjaly, 0, 50)
# wowo2.save("wowo2.bmp")