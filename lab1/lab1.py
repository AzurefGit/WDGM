from PIL import Image
import numpy as np

# obrazek = Image.open("inicjaly.bmp")
# print("---------- informacje o obrazie")
# print("tryb:", obrazek.mode)
# print("format:", obrazek.format)
# print("rozmiar:", obrazek.size)

# obrazek.show()

# dane_obrazka = np.asarray(obrazek)
# dane_obrazka1 = dane_obrazka.astype(np.uint8)
# print(dane_obrazka1)

# np.savetxt("inicjaly.txt", dane_obrazka1, fmt="%d")

# ob_d1 = Image.fromarray(dane_obrazka1)
# ob_d1.show()

# t3 = np.loadtxt("dane.txt", dtype=np.uint8)
# print("typ danych tablicy t3:", t3.dtype)
# print("rozmiar tablicy t3 :", t3.shape)
# print("wymiar tablicy t3 :", t3.ndim)


# Zadanie 4
# print(dane_obrazka1[30][50], dane_obrazka1[40][90], dane_obrazka1[0][99])


# Zadanie 5
# t1 = np.loadtxt("inicjaly.txt", dtype=np.bool_)
# print(t1)
# print("======================================")
# print(dane_obrazka)


# Zadanie 6
# t2 = np.loadtxt("inicjaly.txt", dtype=np.uint8)
# print(t2)
# print("======================================")
# print(dane_obrazka)
#
#
# ob_d1 = Image.fromarray(t2)
# ob_d1.show()

# Zadanie 7
# obrazek_png = Image.open("inicjaly.png")
# print("---------- informacje o obrazie")
# print("tryb:", obrazek_png.mode)
# print("format:", obrazek_png.format)
# print("rozmiar:", obrazek_png.size)
#
# dane_obrazka_png = np.asarray(obrazek_png)
# dane_obrazka_png1 = dane_obrazka_png.astype(np.uint8)
# print(dane_obrazka_png1)

#-----------------------------------------------------------

# obrazek_jpg = Image.open("inicjaly.jpg")
# print("---------- informacje o obrazie")
# print("tryb:", obrazek_jpg.mode)
# print("format:", obrazek_jpg.format)
# print("rozmiar:", obrazek_jpg.size)
#
# dane_obrazka_jpg = np.asarray(obrazek_jpg)
# dane_obrazka_jpg1 = dane_obrazka_jpg.astype(np.uint8)
# print(dane_obrazka_jpg1)

#-----------------------------------------------------------

# obrazek_gif = Image.open("inicjaly.gif")
# print("---------- informacje o obrazie")
# print("tryb:", obrazek_gif.mode)
# print("format:", obrazek_gif.format)
# print("rozmiar:", obrazek_gif.size)
#
# dane_obrazka_gif = np.asarray(obrazek_gif)
# dane_obrazka_gif1 = dane_obrazka_gif.astype(np.uint8)
# print(dane_obrazka_gif1)
