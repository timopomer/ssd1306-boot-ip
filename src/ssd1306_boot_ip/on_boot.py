import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

WIDTH = 128
HEIGHT = 32
BORDER = 5

def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)
    oled.fill(0)
    oled.show()
    font = ImageFont.load_default()

    while True:
        text = "Hello World!"
        (font_width, font_height) = font.getsize(text)
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)
        draw.text(
            (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
            text,
            font=font,
            fill=255,
        )

        oled.image(image)
        oled.show()
        time.sleep(1)

if __name__ == '__main__':
    main()
