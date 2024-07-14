import easyocr
import numpy as np
import cv2


def process(images):
    reader = easyocr.Reader(["en"])
    processed_images = []
    for i, image in enumerate(images):
        img = np.array(image)
        # width_ths is a threshold for width of the text.
        # docs: https://www.jaided.ai/easyocr/documentation/
        easyocr_parser = reader.readtext(img, paragraph=False, width_ths=0.1)
        for result in easyocr_parser:
            # result is a tuple of 3 points: top_left, top_right, bottom_right, bottom_left
            top_left = tuple(map(int, result[0][0]))
            bottom_right = tuple(map(int, result[0][2]))
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 3)
        processed_images.append(img)
    return processed_images
