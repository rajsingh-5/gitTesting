from PIL import Image
import pytesseract


def searching_text_with_pos(searchText, pos=1):
    pos = str(pos)
    try:
        position = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}
        image = Image.open("flip.png")
        image = image.convert('L')
        data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
        occurrences = []
        searchTextList = searchText.split(" ")
        if len(searchTextList) > 1:
            for j in range(len(searchTextList)):
                for i in range(len(data['text'])):
                    if data['text'][i] == searchTextList[j]:
                        # print("19",searchTextList[j])
                        occurrence = {
                            'text': data['text'][i],
                            'x': data['left'][i],
                            'y': data['top'][i]
                        }
                        # print(occurrences)
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


print(searching_text_with_pos("2,999"))
