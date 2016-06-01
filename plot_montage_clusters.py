'''
@file plot_montage_clusters.py
@brief plot montange clusters
@author: Mehrdad Yazdani (modified by Shiyun Qiu & Siwen Tang)
@date April 29, 2016

This document is given by Professor Yazdani. We modified this document slightly
and updated the syntax to make it work in Python 3.5.
'''
import csv
import operator
from my_montage_maker import *
import math
#from PIL import Image

#csv file missing
in_file = "/Users/myazdaniUCSD/Documents/kiev-instagram/results/kmeans_hog/Kmeans_RGB_HOG_lat_long_65.csv"
image_path = "/Users/qiushiyun/Documents/Lily Shiyun/Spring 2016/PIC 10C/pyImagePlot-master/sample_data/Rothko_images/"
output_path = "/Users/qiushiyun/Documents/Lily Shiyun/"


sample = open(in_file, "r")
csv1 = csv.reader(sample, delimiter = ',')
sorted_csv = sorted(csv1, key = operator.itemgetter(0,2))

#first col = cluster number
#second col = filename
#third col = distance from cluster center

for i in range(1,66):
    print ("cluster", i)
    cluster_filenames = [image_path + eachLine[1] for eachLine in sorted_csv if eachLine[0] == str(i)]
    if len(cluster_filenames) == 0: continue
    filedim = math.sqrt(len(cluster_filenames))
    if (filedim%int(filedim) == 0): ncols, nrows = int(filedim),int(filedim)
    else: ncols, nrows = int(filedim), int(filedim)+1
    if ncols == 0: continue
    photow,photoh = 150,150
    photo = (photow,photoh)
    nc_r = (ncols,nrows)
    margins = [0,0,0,0]
    padding = 0
    inew = make_contact_sheet(cluster_filenames,nc_r,photo,margins,padding)
    inew.save(output_path+"cluster_"+ str(i)+ ".jpg")
	
	