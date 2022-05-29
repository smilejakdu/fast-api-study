import pytesseract
import cv2, re
import matplotlib.pyplot as plt

path = './test.png'

image = cv2.imread(path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(rgb_image, lang='kor+eng')

# tel = re.findall(r'(?:Tel )([\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9])', text)[0]
mobile = re.findall(r'(?:M )([\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9])', text)[0]
# emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)[0]
# addr = re.findall(r"[0-9\.\-+_]+\,.*", text)[0]
print("mobile:", mobile)
