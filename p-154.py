import matplotlib.pyplot as plt

data = [
        [3,3,3,1,1,1,1,1,1,10,10,10],
        [3,3,3,1,1,1,1,1,1,10,10,10],
        [5,5,5,1,5,5,5,5,1,5,5,5],
        [5,5,5,1,5,5,5,5,1,5,5,5],
        [3,3,3,1,5,5,5,5,1,10,10,10],
        [5,3,5,1,5,5,5,5,1,5,10,5],
        [3,5,3,1,1,1,1,1,1,10,5,10],
        [3,3,3,1,1,1,1,1,1,10,10,10]]

plt.imshow(data, cmap= 'seismic')
plt.show()
