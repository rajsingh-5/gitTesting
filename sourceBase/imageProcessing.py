from PIL import Image
import pytesseract


def searching_text_with_pos(searchText,pos=1):
    pos = str(pos)
    try:
        position = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}
        image = Image.open("D:/Projects/MobileImageAutomation/sourceBase/flip.png")
        image = image.convert('L')
        data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
        occurrences = []
        searchTextList = searchText.split(" ")
        itemSearchList = []
        print(searchTextList)
        if len(searchTextList) > 1:
            for j in range(len(searchTextList)):
                for i in range(len(data['text'])):
                    if data['text'][i] == searchTextList[j]:
                        occurrence = {
                            'x': data['left'][i],
                            'y': data['top'][i]
                        }
                        occurrences.append(occurrence)
        else:
            for i in range(len(data['text'])):
                if data['text'][i] == searchText:
                    occurrence = {
                        'x': data['left'][i],
                        'y': data['top'][i]
                    }
                    occurrences.append(occurrence)
        return occurrences[position[pos]]['x'], occurrences[position[pos]]['y']
    except IndexError as e:
        raise e
        # print(f"Text \033[1m'{searchText}'\033[0m not found.")


print(searching_text_with_pos("Dressing"))
