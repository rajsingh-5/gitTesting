from PIL import Image
import pytesseract

image = Image.open("D:/Projects/MobileImageAutomation/sourceBase/flip.png")

text = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
# print(text['text'])
search_text = "Dining set"
search_text_list = search_text.split(" ")
oc = []
if len(search_text_list) > 1:
    for item in search_text_list:
        for i in range(len(text['text'])):
            if text['text'][i] == item:
                oce = {
                    'x': text['left'][i],
                    'y': text['top'][i]
                }
                oc.append(oce)
else:
    for i in range(len(text['text'])):
        if text['text'][i] == search_text:
            oce = {
                'x': text['left'][i],
                'y': text['top'][i]
            }
            oc.append(oce)
print(oc)
