from matplotlib import pyplot as plt
import numpy as np
import sys,os

def collector(image_list,cmap='gray',interpolation='none',titles=[],print_code=True,plot_marker='k-',show_individual=True):
    global xclicks,yclicks,indices,subplot_axes,points
    xclicks = []
    yclicks = []
    indices = []
    subplot_axes = []
    points = [[]]*len(image_list)

    print len(titles),len(image_list)
    if len(titles)!=len(image_list):
        titles = ['%02d'%k for k in range(len(image_list))]
    
    nrows = int(np.floor(np.sqrt(len(image_list))))
    ncols = int(np.ceil(np.sqrt(len(image_list))))

    for idx,im in enumerate(image_list):
        plt.figure()
        plt.axes([0,0,1,1])
        plt.imshow(im,cmap=cmap,interpolation=interpolation)
        plt.grid(True)
        


    
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
        
        indices.append(subplot_index)
        points[subplot_index].append((xnewclick,ynewclick))
        
        plt.sca(event.inaxes)
        plt.plot(xnewclick,ynewclick,'go',markersize=10)
        plt.draw()
        #printclicks()

    cid = fig.canvas.mpl_connect('button_press_event',onclick)

    for idx,im in enumerate(image_list):
        plt.subplot(nrows,ncols,idx+1)
        if type(im)==tuple:
            plt.plot(im[0],im[1],plot_marker)
        else:
            plt.imshow(im,cmap=cmap,interpolation=interpolation)
        plt.title(titles[idx])
        plt.autoscale(False)
        subplot_axes.append(plt.gca())
        
    plt.show()
    if print_code:
        printclicks()
        
    return xclicks,yclicks,indices

