from gi.repository import Gdk
from PIL import Image
import time


win = Gdk.get_default_root_window()
h = win.get_height()
w = win.get_width()

print ("The size of the window is %d x %d" % (w, h))

init_time = time.time()
pb = Gdk.pixbuf_get_from_window(win, w/2, w/2, w, h)

def pixbuf2image(pix):
    """Convert gdkpixbuf to PIL image"""
    data = pix.get_pixels()
    w = pix.props.width
    h = pix.props.height
    stride = pix.props.rowstride
    mode = "RGB"
    if pix.props.has_alpha == True:
        mode = "RGBA"
    im = Image.frombytes(mode, (w, h), data, "raw", mode, stride)
    return im

if (pb != None):
    print(pixbuf2image(pb).getpixel((0,0)))
    print(time.time() - init_time)
else:
    print("Unable to get the screenshot.")
