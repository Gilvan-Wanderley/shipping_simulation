from PIL import Image

class ImageSource():
    source = {
        'ship_menu': 'src\app\assets\images\ship_menu.png',
        'port_menu': 'src\app\assets\images\port_menu.png'
    }

    def get_image(name: str, size: tuple[int, int]) -> Image:
        path = ImageSource.source[name]
        return Image.open(path).resize(size)