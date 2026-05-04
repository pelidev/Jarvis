from PIL import Image, ImageDraw, ImageFont
from combFunctions.openTasks import upcomingtasks
import base64
import io


def createBackground():

    tasks = upcomingtasks(0, "_")

    img = Image.new("RGB", (1320, 2868), (240,230,140))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Galafera.ttf", 90)
    starter = 1100
    if tasks:
        for task in tasks:
            draw.text((10, starter), task, font=font, fill=(0,0,0))
            starter = starter + 90

    img.save("background.png")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")

    print(encoded)