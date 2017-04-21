import numpy as np
import clicky

images = []

for k in range(5):
    images.append(np.random.rand(100,100))


xclicks,yclicks,image_indices = clicky.collector(images)

print xclicks,yclicks,image_indices
