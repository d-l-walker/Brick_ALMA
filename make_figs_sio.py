"""
This script cycles through the RGB .png files made with make_rgb.py to
produce publication-quality 3-colour figures of the SiO emission.

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

os.chdir('./Moments_SiO/rgb_pngs/')

# Files to cycle through
pngs         = ['SiO_29_42__43_56.png', 'SiO_29_36__23_29__16_22.png', 'SiO_37_42__29_36__23_29.png',
                'SiO_56_62__50_56__43_49.png', 'SiO_56_69__43_56__29_42.png']

# Legend labels
lab_blue     = ['29 - 42', '16 - 22', '23 - 29', '43 - 49', '29 - 42']
lab_green    = ['       ', '23 - 29', '29 - 36', '50 - 56', '43 - 56']
lab_red      = ['43 - 56', '29 - 36', '37 - 42', '56 - 62', '56 - 69']

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

        if png == 'SiO_29_42__43_56.png':
            f.add_label(0.07, 0.97, lab_blue[index], relative=True, color='#069af3', size=12)
            f.add_label(0.07, 0.93, lab_red[index], relative=True, color='red', size=12)
            f.add_label(0.16, 0.95, 'km/s', relative=True, color='white', size=12)
        else:
            f.add_label(0.07, 0.97, lab_blue[index], relative=True, color='#069af3', size=12)
            f.add_label(0.07, 0.93, lab_green[index], relative=True, color='lightgreen', size=12)
            f.add_label(0.07, 0.89, lab_red[index], relative=True, color='red', size=12)
            f.add_label(0.16, 0.93, 'km/s', relative=True, color='white', size=12)

        f.savefig('./../rgb_figs/'+filename+'.pdf')
        f.close()
        i = i + 1

os.chdir('./../../')
