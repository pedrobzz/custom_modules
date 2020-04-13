import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk
from PIL import Image

def get_pix_image(x=0, y=0, width=None, height=None):
    win = Gdk.get_default_root_window()
    if width == None:
        width = win.get_width()
    if height == None:
        height = win.get_height()
    pix_image = Gdk.pixbuf_get_from_window(win, x, y, width, height)
    return pix_image


def convert_to_PIL(pix):
    data = pix.get_pixels()
    w = pix.props.width
    h = pix.props.height
    stride = pix.props.rowstride
    mode = "RGB"
    if pix.props.has_alpha == True:
        mode = "RGBA"
    img = Image.frombytes(mode, (w, h), data, "raw", mode, stride)
    return img


def ImageGrab(x=0, y=0, width=None, height=None):
    return convert_to_PIL(get_pix_image(x, y, width, height))
