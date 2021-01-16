"""
This script cycles through the RGB .png files made with make_rgb.py to
produce publication-quality 3-colour figures of the 13CO emission.

Note: figures are high-quality, but file size is too large for manuscript.
Run the following to compress:

for f in *.pdf
do
    gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -q -o ./Compressed/$f $f
done
"""

from __future__ import division
import matplotlib.pyplot as plt
from astropy import units as u
import numpy as np
import aplpy
import os
from pathlib import Path
plt.style.use('classic')

d       = 8100*u.pc
pc_sc   = ((1/d.value)*u.rad).to(u.deg).value   # Converts 1 parsec to degrees at the distance of the Galactic centre

os.chdir('./Moments_13CO/rgb_pngs/')

# Files to cycle through
pngs         = ['13CO_m331_m338_m345.png', '13CO_346_333_345.png', '13CO_452_439_426.png',
                '13CO_505_492_479.png', '13CO_532_519_505.png', '13CO_592_578_565.png']

# Legend labels
lab_blue     = ['-34.5', '31.9', '42.6', '47.9', '50.5', '56.5']
lab_green    = ['-33.8', '33.3', '43.9', '49.2', '51.9', '57.8']
lab_red      = ['-33.1', '34.6', '45.2', '50.5', '53.2', '59.2']

for png in pngs:
    t = os.path.splitext(png)
    filename = str(t[0])
    index = pngs.index(png)

    if Path('./../rgb_figs/'+filename+'.pdf').exists() == False:
        f = aplpy.FITSFigure(png)
        f.show_rgb()
        f.add_scalebar(0.1*pc_sc)
        f.scalebar.show(0.1*pc_sc)
        f.scalebar.set_corner('bottom left')
        f.scalebar.set_color('white')
        f.scalebar.set_label('0.1 pc')
        f.scalebar.set_font(size=15)
        f.scalebar.set_linewidth(2)
        f.axis_labels.set_font(size=16)
        f.ticks.set_color('white')
        f.tick_labels.set_font(size=15)
        f.axis_labels.set_xtext('Right Ascension (J2000)')
        f.axis_labels.set_ytext('Declination (J2000)')
        f.axis_labels.set_ypad(-2)
        f.show_regions('./../../brick_regions_new.reg')

        f.add_label(0.07, 0.97, lab_blue[index], relative=True, color='#069af3', size=12)
        f.add_label(0.07, 0.93, lab_green[index], relative=True, color='lightgreen', size=12)
        f.add_label(0.07, 0.89, lab_red[index], relative=True, color='red', size=12)
        f.add_label(0.16, 0.93, 'km/s', relative=True, color='white', size=12)

        f.savefig('./../rgb_figs/'+filename+'.pdf')
        f.close()
        
os.chdir('./../../')
