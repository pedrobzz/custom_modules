import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk
from PIL import Image

def get_pix_image(width=0, height=0, final_width=None, final_height=None):
    win = Gdk.get_default_root_window()
    if final_width == None:
        final_width = win.get_width()
    if final_height == None:
        final_height = win.get_height()
    pix_image = Gdk.pixbuf_get_from_window(win, width, height, final_width, final_height)
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


def ImageGrab(width=0, height=0, final_width=None, final_height=None):
    return convert_to_PIL(get_pix_image(width, height, final_width, final_height))
