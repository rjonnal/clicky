# clicky

## Minimum working example

```python
import numpy as np
import clicky

images = []

for k in range(5):
    images.append(np.random.rand(100,100))
    
xclicks,yclicks,image_indices = clicky.collector(images)
```

## Gotchas

1. `image_indices` contains the index of the image in the input image list corresponding to the click.

2. There are no other gotchas.