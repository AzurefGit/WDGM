from PIL import Image
import numpy as np

obrazek = Image.open("inicjaly.bmp")
# print("---------- informacje o obrazie")
# print("tryb:", obrazek.mode)
# print("format:", obrazek.format)
# print("rozmiar:", obrazek.size)

# obrazek.show()

dane_obrazka = np.asarray(obrazek)
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
t2 = np.loadtxt("inicjaly.txt", dtype=np.uint8)
