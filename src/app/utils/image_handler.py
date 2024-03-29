from PIL import Image, ImageTk

class ImageSource():
    source = {
        'ship_menu': 'src\\app\\assets\\images\\ship_menu.png',
        'port_menu': 'src\\app\\assets\\images\\port_menu.png'
    }

    def get_image(name: str, size: tuple[int, int]) -> ImageTk:
        path = ImageSource.source[name]
        return ImageTk.PhotoImage(Image.open(path).resize(size))