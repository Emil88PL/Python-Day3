# PIL

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:  # argv  original name of the program
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "customes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)

# python .\pillow_py.py star1.gif star2.gif