from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageStat as stat
import numpy as np


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # średnia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


postac = Image.open("postac.png")


# ------------------------------- Zad 1 ------------------------------- #
# s_w = 0.15
# s_h = 0.27

# new_width = int(postac.size[0] * s_w)
# new_height = int(postac.size[1] * s_h)
# new_size = (new_width, new_height)

# metody = {
#     'NEAREST': Image.Resampling.NEAREST,
#     'LANCZOS': Image.Resampling.LANCZOS,
#     'BILINEAR': Image.Resampling.BILINEAR,
#     'BICUBIC': Image.Resampling.BICUBIC,
#     'BOX': Image.Resampling.BOX,
#     'HAMMING': Image.Resampling.HAMMING
# }
#
# obrazy = {}
# for nazwa, metoda in metody.items():
#     obrazy[nazwa] = postac.resize(new_size, metoda)
#
# fig, axes = plt.subplots(4, 3, figsize=(15, 20))
#
# ref_img = obrazy['NEAREST']
#
# idx = 0
# for i, (nazwa, obraz) in enumerate(obrazy.items()):
#     row = i // 3
#     col = (i % 3)
#     if col == 0:
#         axes[row * 2, col].imshow(obraz)
#         axes[row * 2, col].set_title(f'{nazwa}', fontsize=12, fontweight='bold')
#         axes[row * 2, col].axis('off')
#     else:
#         axes[row * 2, col].imshow(obraz)
#         axes[row * 2, col].set_title(f'{nazwa}', fontsize=12, fontweight='bold')
#         axes[row * 2, col].axis('off')
#
#     if nazwa != 'NEAREST':
#         arr_ref = np.array(ref_img)
#         arr_current = np.array(obraz)
#
#         diff = np.abs(arr_ref.astype(int) - arr_current.astype(int))
#
#         if diff.ndim == 3 and diff.shape[2] == 4:
#             diff = diff[:, :, :3]
#
#         axes[row * 2 + 1, col].imshow(diff.astype(np.uint8))
#         axes[row * 2 + 1, col].set_title(f'Różnica: {nazwa} - NEAREST', fontsize=10)
#         axes[row * 2 + 1, col].axis('off')
#     else:
#         axes[row * 2 + 1, col].axis('off')
#
# plt.tight_layout()
# plt.savefig('fig1.png')
# plt.show()
#
# for nazwa, obraz in obrazy.items():
#     if nazwa != 'NEAREST':
#         arr_ref = np.array(ref_img)
#         arr_current = np.array(obraz)
#
#         diff = np.abs(arr_ref.astype(int) - arr_current.astype(int))
#
#         if diff.ndim == 3 and diff.shape[2] == 4:
#             diff_rgb = diff[:, :, :3]
#         else:
#             diff_rgb = diff
#
#         diff_img = Image.fromarray(diff_rgb.astype(np.uint8))
#
#         print(f"\nStatystyki dla {nazwa}:")
#         statystyki(diff_img)

# ------------------------------- Zad 2 ------------------------------- #
# w, h = postac.size
# box_glowa = (int(0.35*w), int(0.05*h), int(0.65*w), int(0.35*h))
#
# resampling = Image.Resampling.BICUBIC
#
# # a) resize fragmentu w obrazie
# fragment = postac.crop(box_glowa)
# resize_a = fragment.resize(
#     (fragment.size[0]*2, fragment.size[1]*3),
#     resampling
# )
#
# # b) crop -> resize
# resize_b = fragment.resize(
#     (fragment.size[0]*2, fragment.size[1]*3),
#     resampling
# )
#
# # różnica
# diff2 = np.abs(
#     np.array(resize_a).astype(int) -
#     np.array(resize_b).astype(int)
# ).astype(np.uint8)
#
# diff2_img = Image.fromarray(diff2)
#
# print("\nStatystyki różnicy Zad 2:")
# statystyki(diff2_img)
#
# plt.figure(figsize=(10,4))
# plt.subplot(1,3,1)
# plt.imshow(resize_a); plt.title("Resize fragmentu"); plt.axis('off')
#
# plt.subplot(1,3,2)
# plt.imshow(resize_b); plt.title("Crop + resize"); plt.axis('off')
#
# plt.subplot(1,3,3)
# plt.imshow(diff2_img); plt.title("Różnica"); plt.axis('off')
# plt.tight_layout()
# plt.show()

# # ------------------------------- Zad 3 ------------------------------- #
#
# a) 60° w lewo, cały obraz widoczny, tło czerwone
# rot_left = postac.rotate(
#     60,
#     expand=True,
#     fillcolor=(255, 0, 0)
# )
# rot_left.save("rot_left_60.png")
#
# # b) 60° w prawo, bez zmiany rozmiaru, tło zielone
# rot_right = postac.rotate(
#     -60,
#     expand=False,
#     fillcolor=(0, 255, 0)
# )
# rot_right.save("rot_right_60.png")
#
# plt.figure(figsize=(8,4))
# plt.subplot(1,2,1)
# plt.imshow(rot_left); plt.title("60° w lewo (expand)"); plt.axis('off')
#
# plt.subplot(1,2,2)
# plt.imshow(rot_right); plt.title("60° w prawo (bez expand)"); plt.axis('off')
# plt.show()

# # ------------------------------- Zad 4 ------------------------------- #

# w, h = postac.size
#
# new_w, new_h = w*2, h*2
# canvas = Image.new("RGB", (new_w, new_h), (0, 0, 0))
#
# canvas.paste(postac, (new_w//4, new_h//4))
#
# rot_00 = canvas.rotate(45, expand=True, fillcolor=(0,0,0))
# rot_00.show()
# rot_00.save("obrot.png")

# # ------------------------------- Zad 5 ------------------------------- #
#
# # TRANSPOSE = obrót 90° + flip L/R
# transpose_alt = postac.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
# transpose_alt.show()
# # TRANSVERSE = obrót -90° + flip L/R
# transverse_alt = postac.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
# transverse_alt.show()
# # ------------------------------- Zad 6 ------------------------------- #

postac = postac.convert("RGBA")
motyl = Image.open("motylek.png").convert("RGBA")
tlo = Image.open("kolorowe_tlo.png").convert("L")

# zmiana rozmiaru motylka
motyl = motyl.resize((60, 60))
tlo = tlo.resize((60, 60))

# obroty
motyl_left = motyl.rotate(60, expand=True)
motyl_right = motyl.rotate(-60, expand=True)


mask_left = tlo.rotate(60, expand=True)
mask_right = tlo.rotate(-60, expand=True)

# pozycje
positions = [
    (120, 50),
    (-10, 0),
    (-20, 200)
]

# wklejanie Z MASKĄ
postac.paste(motyl, positions[0], tlo)
postac.paste(motyl_left, positions[1], mask_left)
postac.paste(motyl_right, positions[2], mask_right)

postac.save("postac_motylki.png")
postac.show()