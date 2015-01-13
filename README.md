Search images from a specified directory and remove does who are smaller than the
given height and width

Requirements
------------
* get_image_size from [scardine](https://github.com/scardine/image_size)
* [progressbar](https://code.google.com/p/python-progressbar/) (_optional_)

Usage
-----

Can set the parameters as arguments or wait to the script to ask for them.

    ./delete_small_images.py
    ./delete_small_images.py [<images directory> [ <min width> [<min height>]]]


Example:

    ./delete_small_images.py /home/lord/Pictures/wallpapers 1920 1080
