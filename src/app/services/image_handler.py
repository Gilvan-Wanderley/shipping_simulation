from PIL import Image, ImageTk

class ImageSource():
    source = {
        'ship_menu': 'src\\app\\assets\\images\\ship_menu.png',
        'port_menu': 'src\\app\\assets\\images\\port_menu.png',
        'ship_flow': 'src\\app\\assets\\images\\ship_flow.png',
    }

    def get_photo_image(name: str, size: tuple[int, int]) -> ImageTk:
        image = ImageSource.get_image(name, size)
        return ImageTk.PhotoImage(image)
    
    def get_image(name: str, size: tuple[int, int]) -> Image:
        path = ImageSource.source[name]
        image = Image.open(path).resize(size)
        return image