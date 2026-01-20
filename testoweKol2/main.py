from PIL import Image, ImageDraw, ImageStat, ImageFont, ImageColor, ImageFilter
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt



#---------------------------------------- Zadanie 1 ----------------------------------------
wd2 = Image.open("WD2.jpg")
print("Wymiary obrazu WD2.jpg:", wd2.size)

w, h = wd2.size

kanal_alpha = Image.new('L', (w, h), 0)

draw = ImageDraw.Draw(kanal_alpha)

srodek_x = w // 2
srodek_y = h // 2
przesuniecie_x = w // 3
przesuniecie_y = h // 3

wierzcholki = [
    (srodek_x, 0),
    (srodek_x + przesuniecie_x, srodek_y),
    (srodek_x, srodek_y + przesuniecie_y),
    (0, 0)
]

draw.polygon(wierzcholki, fill=255)

if wd2.mode != 'RGB':
    wd2 = wd2.convert('RGB')

wd2.putalpha(kanal_alpha)

wd2.save("rgba.png")

print(f"- Kanał alpha: tryb {kanal_alpha.mode}, rozmiar {kanal_alpha.size}")
print(f"- Obraz rgba.png: tryb {wd2.mode}, rozmiar {wd2.size}")

wd2.show()


#---------------------------------------- Zadanie 3 ----------------------------------------
# obraz = Image.open("WD1.jpg")
#
# obraz_cmyk = obraz.convert("CMYK")
#
# c, m, y, k = obraz_cmyk.split()
#
# stat_c = ImageStat.Stat(c)
#
# srednia = stat_c.mean[0]
# mediana = stat_c.median[0]
#
# tablica_c = np.array(c)
# liczba_125 = np.sum(tablica_c == 125)
#
# print(f"Średnia: {srednia}")
# print(f"Mediana: {mediana}")
# print(f"Liczba pikseli o wartości 125: {liczba_125}")
#
# print(f"\nOdpowiedź: {srednia:.1f} / {mediana:.1f} / {liczba_125:.1f}")

#---------------------------------------- Zadanie 4 ----------------------------------------
# obraz = Image.open("WD1.jpg")
# w, h = obraz.size
#
# draw = ImageDraw.Draw(obraz)
#
# tekst_linie = [
#     "idź wyprostowany wśród tych",
#     "co na kolanach",
#     "wśród odwróconych plecami",
#     "i obalonych",
#     "w proch"
# ]
#
# kolor = "#663399"
#
# rozmiar_czcionki = 50
# while rozmiar_czcionki > 10:
#     font = ImageFont.truetype("DejaVuSans-BoldOblique.ttf", rozmiar_czcionki)
#
#     max_szerokosc = 0
#     calkowita_wysokosc = 0
#
#     for linia in tekst_linie:
#         bbox = draw.textbbox((0, 0), linia, font=font)
#         szerokosc = bbox[2] - bbox[0]
#         wysokosc = bbox[3] - bbox[1]
#         max_szerokosc = max(max_szerokosc, szerokosc)
#         calkowita_wysokosc += wysokosc
#
#     if max_szerokosc <= w - 20 and calkowita_wysokosc <= h - 20:
#         break
#
#     rozmiar_czcionki -= 1
#
# font = ImageFont.truetype("DejaVuSans-BoldOblique.ttf", rozmiar_czcionki)
#
# y = 10
# for linia in tekst_linie:
#     bbox = draw.textbbox((0, 0), linia, font=font)
#     wysokosc = bbox[3] - bbox[1]
#     draw.text((10, y), linia, fill=kolor, font=font)
#     y += wysokosc
#
# obraz.save("WD1_tekst.jpg")
# obraz.show()


#---------------------------------------- Zadanie 5 ----------------------------------------
# obraz = Image.open("steve.png").convert("RGB")
# w, h = obraz.size
#
# draw = ImageDraw.Draw(obraz)
#
# color_mediumaquamarine = ImageColor.getrgb("mediumaquamarine")
# color_negative = tuple(255 - c for c in color_mediumaquamarine)
#
# left_circle_box = [0, 0, h, h]
# right_circle_box = [w - h, 0, w, h]
#
# draw.ellipse(left_circle_box, outline=color_mediumaquamarine, width=3)
#
# draw.ellipse(right_circle_box, outline=color_negative, width=5)
#
# obraz.save("steve_z_okregami.png")

#---------------------------------------- Zadanie 6 ----------------------------------------
# royalblue_rgb = ImageColor.getrgb('royalblue')
# saddlebrown_rgb = ImageColor.getrgb('saddlebrown')
# ivory_rgb = ImageColor.getrgb('ivory')
#
# royalblue_hex = '#%02x%02x%02x' % royalblue_rgb
# saddlebrown_hex = '#%02x%02x%02x' % saddlebrown_rgb
# ivory_hex = '#%02x%02x%02x' % ivory_rgb
#
# print(f"'royalblue': {royalblue_rgb} -> {royalblue_hex}")
# print(f"'saddlebrown': {saddlebrown_rgb} -> {saddlebrown_hex}")
# print(f"'ivory': {ivory_rgb} -> {ivory_hex}")

#---------------------------------------- Zadanie 8 ----------------------------------------

# kwiaty = Image.open("kwiaty.png")
#
# draw = ImageDraw.Draw(kwiaty)
#
# draw.rectangle([622, 250, 800, 430], fill=(255, 255, 255))
#
# kwiaty.save("kwiaty_bez_kwiatka.png")
# kwiaty.show()

#---------------------------------------- Zadanie 9 ----------------------------------------
# mmaska3 = Image.open("mmaska3.jpg")
# maska = mmaska3.convert("L")
#
# wd2 = Image.open("WD2.jpg")
# obraz = Image.open("obraz.png")
#
# w, h = wd2.size
#
# maska = maska.resize((w, h))
# obraz = obraz.resize((w, h))
#
# obraz.paste(wd2, (0, 0), maska)
#
# obraz.save("wynik_maska.png")
# obraz.show()

#---------------------------------------- Zadanie 10 ----------------------------------------
# wd1 = Image.open("WD1.jpg")
# obraz_L = wd1.convert("L")
#
# obraz_emboss = obraz_L.filter(ImageFilter.EMBOSS)
#
# sobel1_kernel = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
# obraz_sobel1 = obraz_L.filter(ImageFilter.Kernel(size=(3, 3), kernel=sobel1_kernel, scale=1))
#
# fig, axes = plt.subplots(1, 3, figsize=(15, 5))
#
# axes[0].imshow(obraz_L, cmap='gray')
# axes[0].set_title('Obraz oryginalny (tryb L)')
# axes[0].axis('off')
#
# axes[1].imshow(obraz_emboss, cmap='gray')
# axes[1].set_title('Filtr EMBOSS')
# axes[1].axis('off')
#
# axes[2].imshow(obraz_sobel1, cmap='gray')
# axes[2].set_title('Filtr SOBEL1')
# axes[2].axis('off')
#
# plt.tight_layout()
# plt.savefig('diagram_filtry.png', dpi=150, bbox_inches='tight')
# plt.show()

#---------------------------------------- Zadanie 11 ----------------------------------------
# wd3 = Image.open("WD3.jpg")
#
# obraz_ycbcr = wd3.convert("YCbCr")
#
# piksel = obraz_ycbcr.getpixel((200, 100))
#
# print(f"Wartość piksela o adresie (200, 100): {piksel}")

#---------------------------------------- Zadanie 13 ----------------------------------------
# wd1 = Image.open("WD1.jpg")
#
# obraz_resize = wd1.resize((500, 400), Image.Resampling.BILINEAR)
#
# srodek_x = 190
# srodek_y = 120
# bok = 81
# polowa = bok // 2
#
# left = srodek_x - polowa
# top = srodek_y - polowa
# right = srodek_x + polowa + 1
# bottom = srodek_y + polowa + 1
#
# kwadrat = obraz_resize.crop((left, top, right, bottom))
#
# stat = ImageStat.Stat(kwadrat)
# mediana = stat.median
#
# print(f"Rozmiar kwadratu: {kwadrat.size}")
# print(f"Mediana: {mediana}")

#---------------------------------------- Zadanie 14 ----------------------------------------
# steve = Image.open("steve.png")
#
# if steve.mode != "RGBA":
#     steve = steve.convert("RGBA")
#
# kolor_piksela = steve.getpixel((100, 50))
#
# if len(kolor_piksela) == 4:
#     kolor = (kolor_piksela[0], kolor_piksela[1], kolor_piksela[2], 100)
# else:
#     kolor = (kolor_piksela[0], kolor_piksela[1], kolor_piksela[2], 100)
#
# draw = ImageDraw.Draw(steve)
#
# font = ImageFont.truetype("DejaVuSansMono.ttf", 20)
#
# tekst = "Łukasz Malinowski"
#
# bbox = draw.textbbox((0, 0), tekst, font=font)
# szerokosc_tekstu = bbox[2] - bbox[0]
# wysokosc_tekstu = bbox[3] - bbox[1]
#
# w, h = steve.size
# x = w - szerokosc_tekstu - 10
# y = h - wysokosc_tekstu - 10
#
# draw.text((x, y), tekst, fill=kolor, font=font)
#
# steve.save("steve_podpis.png")
# steve.show()

#---------------------------------------- Zadanie 15 ----------------------------------------
#
# broken_leg = Image.open("broken-leg2.jpg")
#
# obraz_L = broken_leg.convert("L")
#
# hist = obraz_L.histogram()
#
# n_pikseli = obraz_L.size[0] * obraz_L.size[1]
# hist_norm = [h / n_pikseli for h in hist]
#
# hist_kumul = []
# suma = 0
# for h in hist_norm:
#     suma += h
#     hist_kumul.append(suma)
#
# plt.figure(figsize=(10, 6))
# plt.plot(range(256), hist_kumul)
# plt.title("Histogram skumulowany")
# plt.xlabel("Wartość piksela")
# plt.ylabel("Skumulowana częstość")
# plt.grid(True)
# plt.savefig("histogram_skumulowany.png")
# plt.show()
#
# print(f"Rozmiar obrazu: {obraz_L.size}")
# print(f"Tryb: {obraz_L.mode}")
# print(f"Wartość końcowa histogramu skumulowanego: {hist_kumul[-1]}")

#---------------------------------------- Zadanie 16 ----------------------------------------
# choinka = Image.open("choinka2.jpg")
# w, h = choinka.size
# choinka_resize = choinka.resize((w//3, h//3), Image.Resampling.HAMMING)
# choinka_rot = choinka_resize.rotate(-30, expand=True, fillcolor=(255, 255, 0))
#
# choinka_rot.show()

