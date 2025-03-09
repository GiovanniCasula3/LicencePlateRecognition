from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import localization
from greycar import binary_car_imm

# connette assieme tutte le regioni connesse
label_image = measure.label(localization.binary_car_imm)

platedimensions = (0.08 * label_image.shape[0], 0.2 * label_image.shape[0], 0.15 * label_image.shape[1], 0.4 * label_image.shape[1])
min_height, max_height, min_width, max_width = platedimensions
plate_objects_cordinates = []
plate_like_objects = []
fig, (ax1) = plt.subplots(1, figsize=(10, 5))
ax1.imshow(localization.gray_car_imm, cmap="gray")

for region in regionprops(label_image):
    if region.area < 50:
        # Ignora le regioni piccole
        continue
    
    # box coordinate
    minrow, mincol, maxrow, maxcol = region.bbox
    region_height = maxrow - minrow
    region_width = maxcol - mincol
    
    # Disegna un rettangolo attorno alla regione
    if region_height >= min_height and region_height <= max_height and region_width >= min_width and region_width <= max_width and region_width > region_height:
        plate_like_objects.append(localization.binary_car_imm[minrow:maxrow, mincol:maxcol])
        plate_objects_cordinates.append((minrow, mincol, maxrow, maxcol))
        rectBorder = patches.Rectangle((mincol, minrow), maxcol - mincol, maxrow - minrow, edgecolor="red", linewidth=2, fill=False)
        ax1.add_patch(rectBorder)
    
plt.tight_layout()
plt.show()