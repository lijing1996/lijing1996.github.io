from PIL import Image, ImageOps
import os
images = os.listdir()
for image in images:
    if ".png" not in image or "256" in image:
        continue
    c = Image.open(image)
    w, h = c.size
    if w >= h:
        pad = (256 - int(h / w * 256)) // 2
        c = c.resize((256, int(h / w * 256)))
        c = ImageOps.expand(c, border=(0, pad, 0, pad))
    else:
        pad = (256 - int(w / h * 256)) // 2
        c = c.resize((int(w / h * 256), 256))
        c = ImageOps.expand(c, border=(pad, 0, pad, 0))
    c.save("256_" + image)