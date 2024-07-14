import pytesseract
from pytesseract import Output
import numpy as np
import cv2


def process(images):
    processed_images = []
    for i, image in enumerate(images):
        img = np.array(image)
        ocr = pytesseract.image_to_data(img, output_type=Output.DICT)
        for i in range(len(ocr["text"])):
            if int(ocr["conf"][i]) > 0:
                (x, y, w, h) = (
                    ocr["left"][i],
                    ocr["top"][i],
                    ocr["width"][i],
                    ocr["height"][i],
                )
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        processed_images.append(img)
    return processed_images
