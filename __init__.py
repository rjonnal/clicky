from matplotlib import pyplot as plt
import numpy as np
import sys,os

def collector(image_list,cmap='gray',interpolation='none'):
    global xclicks,yclicks,indices,subplot_axes,points
    xclicks = []
    yclicks = []
    indices = []
    subplot_axes = []
    points = [[]]*len(image_list)
    
    nrows = int(np.floor(np.sqrt(len(image_list))))
    ncols = int(np.ceil(np.sqrt(len(image_list))))
    fig = plt.figure()

    def printclicks():
        outstr = 'xclicks = ['
        for xc in xclicks:
            outstr = outstr + '%0.1f,'%xc
        if outstr[-1]==',':
            outstr = outstr[:-1]
        outstr = outstr + ']'
        print outstr
        outstr = 'yclicks = ['
        for yc in yclicks:
            outstr = outstr + '%0.1f,'%yc
        if outstr[-1]==',':
            outstr = outstr[:-1]
        outstr = outstr + ']'
        print outstr
        outstr = 'indices = ['
        for idx in indices:
            outstr = outstr + '%d,'%idx
        if outstr[-1]==',':
            outstr = outstr[:-1]
        outstr = outstr + ']'
        print outstr

    def onclick(event):
        if event.inaxes is None:
            printclicks()
            return
        
        global xclicks,yclicks,indices,subplot_axes,points
        xnewclick = event.xdata
        ynewclick = event.ydata
        xclicks.append(xnewclick)
        yclicks.append(ynewclick)

        subplot_index = subplot_axes.index(event.inaxes)
        
        indices.append(subplot_index+1)
        print 'appending'
        print subplot_index
        points[subplot_index].append((xnewclick,ynewclick))
        print points
        
        plt.sca(event.inaxes)
        plt.plot(xnewclick,ynewclick,'go',markersize=10)
        plt.draw()
        #printclicks()
        
    cid = fig.canvas.mpl_connect('button_press_event',onclick)

    for idx,im in enumerate(image_list):
        plt.subplot(nrows,ncols,idx+1)
        plt.imshow(im,cmap=cmap,interpolation=interpolation)
        plt.autoscale(False)
        subplot_axes.append(plt.gca())
        
    plt.show()
    return xclicks,yclicks,indices
