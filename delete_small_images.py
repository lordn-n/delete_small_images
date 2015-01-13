#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        delete_small_images.py
# Purpose:     Search and destroy, images under specified size
#
# Author:      Arturo Bruno (@Lordn__n <lord.the.gatekeeper@gmail.com>)
# Paulo Scardine (based on code from Emmanuel VAÏSSE)
#
# Created:     13/01/2015
# Copyright:   (c) Arturo Bruno 2015
# Licence:     GPL v3.0
#-------------------------------------------------------------------------------

import os
import re
import sys
from get_image_size import get_image_size, UnknownImageFormat

show_progress_bar = True

try:
    import progressbar
except ImportError:
    show_progress_bar = False

images_dir = sys.argv[1] if len(sys.argv) > 1 else raw_input('Images directory: ')

while os.path.isdir(images_dir) is not True:
    images_dir = raw_input('Images directory "' + images_dir + '" does not exists, select an existing directory: ')

min_width = unicode(sys.argv[2] if len(sys.argv) > 2 else raw_input('Min width: '))

while min_width.isnumeric() is not True:
    min_width = unicode(raw_input('Min width (must be a valid number): '))

min_height = unicode(sys.argv[3] if len(sys.argv) > 3 else raw_input('Max height: '))

while min_height.isnumeric() is not True:
    min_height = unicode(raw_input('Min height (must be a valid number): '))

images = [f for f in os.listdir(images_dir) if re.match(r'(.)+.*\.[jpg|png]', f)]
count = 1
deleted_images = []

if show_progress_bar:
    bar = progressbar.ProgressBar(maxval=1000, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

for image in images:
    full_image_path = images_dir + '/' + image

    try:
        width, height = get_image_size(full_image_path)
    except UnknownImageFormat:
        print 'Can\'t get the size of the image "' + full_image_path + '".'
        sys.exit(0)

    if height < min_height and width < min_width:
        deleted_images.insert(len(deleted_images), image)
        os.remove(full_image_path)

    progress = (count * 100) / len(images)

    if show_progress_bar:
        bar.update(progress)
    else:
        print progress, '%'

    count = count + 1

if show_progress_bar:
    bar.finish()

print 'Total images: ', len(images), ' | Deleted:', len(deleted_images)
sys.exit(0)
