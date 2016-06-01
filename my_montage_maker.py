"""@file my_montage_maker.py
@brief the function needed for making a contact sheet
@author: Mehrdad Yazdani (modified by Shiyun Qiu & Siwen Tang)
@date April 29, 2016

This function is given by Professor Yazdani. We modified this document slightly
and updated the syntax to make it work in Python 3.5.
"""
import glob 
from PIL import Image

def make_contact_sheet(fnames,cols_rows,photow_h,marl_t_r_b,padding):
    #    """\
    #    Make a contact sheet from a group of filenames:
    #
    #    fnames       A list of names of the image files
    #    
    #    ncols        Number of columns in the contact sheet
    #    nrows        Number of rows in the contact sheet
    #    photow       The width of the photo thumbs in pixels
    #    photoh       The height of the photo thumbs in pixels
    #
    #    marl         The left margin in pixels
    #    mart         The top margin in pixels
    #    marr         The right margin in pixels
    #    marb         The bottom margin in pixels
    #
    #    padding      The padding between images in pixels
    #
    #    returns a PIL image object.
    #    """

    # Calculate the size of the output image, based on the
    #  photo thumb sizes, margins, and padding
    ncols, nrows = cols_rows
    photow,photoh = photow_h
    marl,mart,marr,marb = marl_t_r_b
    
    marw = marl+marr
    marh = mart+ marb

    padw = (ncols-1)*padding
    padh = (nrows-1)*padding
    isize = (ncols*photow+marw+padw,nrows*photoh+marh+padh)

    # Create the new image. The background doesn't have to be white
    white = (255,255,255)
    inew = Image.new('RGB',isize,white)

    count = 0
    # Insert each thumb:
    for irow in range(nrows):
        for icol in range(ncols):
            left = marl + icol*(photow+padding)
            right = left + photow
            upper = mart + irow*(photoh+padding)
            lower = upper + photoh
            bbox = (left,upper,right,lower)
            try:
                # Read in an image and resize appropriately
                img = Image.open(fnames[count]).resize((photow,photoh))
            except:
                break
            inew.paste(img,bbox)
            count += 1
    return inew

ncols, nrows = 5,4
ncr = (ncols, nrows)
files = glob.glob("../../data/*.jpg")
files = files[:20]

photow,photoh = 150,150
photo = (photow,photoh)

margins = [0,0,0,0]

padding = 0

inew = make_contact_sheet(files,ncr,photo,margins,padding)