import pytesseract
from pytesseract import Output
import cv2


def extract_layout(image_path):
    image = cv2.imread(image_path)
    data = pytesseract.image_to_data(image, output_type=Output.DICT)

    blocks = []
    n = len(data['text'])

    for i in range(n):
        try:
            conf = int(data['conf'][i])
        except:
            continue

        if conf > 60 and data['text'][i].strip() != "":
            blocks.append({
                "text": data['text'][i],
                "x": data['left'][i],
                "y": data['top'][i]
            })

    return blocks


def group_into_lines(blocks):
    blocks = sorted(blocks, key=lambda x: (x['y'], x['x']))

    lines = []
    current_line = []
    current_y = None

    for b in blocks:
        if current_y is None:
            current_y = b['y']

        if abs(b['y'] - current_y) < 10:
            current_line.append(b['text'])
        else:
            lines.append(" ".join(current_line))
            current_line = [b['text']]
            current_y = b['y']

    if current_line:
        lines.append(" ".join(current_line))

    return lines


def structure_lines(lines):
    structured_data = []

    for line in lines:
        if line.strip() == "":
            continue

        if line.isupper():
            structured_data.append({"type": "heading", "text": line})
        elif ":" in line:
            structured_data.append({"type": "field", "text": line})
        else:
            structured_data.append({"type": "paragraph", "text": line})

    return structured_data
