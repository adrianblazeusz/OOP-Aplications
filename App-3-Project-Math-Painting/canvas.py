import numpy as np
from PIL import Image

data = np.zeros((5,4,3), dtype= np.unit8)
data[:] = [255, 255, 0]
print(data)

data[1:3] = [255,0,0]

img = Image.fromarray(data, "RGB")
img.save("canvas.png")