import cv2
import pytesseract

global data


def SearchUsingImage(searchText, pos=1):
    pos = str(pos)

    try:
        position = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}
        image = cv2.imread("framm.png")

        occurrences = normalImg(searchText, data)

        if len(occurrences) < 1:
            print("Length less")
            occurrences = greyImage(searchText, data, image)
        return occurrences[position[pos]]['x'], occurrences[position[pos]]['y']
    except IndexError as e:
        for i in range(len(data['text']) - 1):
            if data['conf'][i] > (-1):
                print(data['text'][i], data['conf'][i])
        raise e


def normalImg(searchText, data):
    occurrences = []
    searchTextList = searchText.split(" ")

    if len(searchTextList) > 1:
        for i in range(len(data['text']) - 1):
            if (
                    data['text'][i] == searchTextList[0]
                    and data['text'][i + 1] == searchTextList[1]
                    and data['conf'][i] > 90  # Check confidence level
            ):
                occurrence = {
                    'x': data['left'][i],
                    'y': data['top'][i]
                }
                occurrences.append(occurrence)
    else:
        for i in range(len(data['text'])):
            if (
                    data['text'][i] == searchText
                    and data['conf'][i] > 90  # Check confidence level
            ):
                occurrence = {
                    'x': data['left'][i],
                    'y': data['top'][i]
                }
                occurrences.append(occurrence)
    return occurrences


def greyImage(searchText, data, image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh, img_bw = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)

    occurrences = []
    searchTextList = searchText.split(" ")

    if len(searchTextList) > 1:
        for i in range(len(data['text']) - 1):
            if (
                    data['text'][i] == searchTextList[0]
                    and data['text'][i + 1] == searchTextList[1]
                    and data['conf'][i] > 90  # Check confidence level
            ):
                occurrence = {
                    'x': data['left'][i],
                    'y': data['top'][i]
                }
                occurrences.append(occurrence)
    else:
        for i in range(len(data['text'])):
            if (
                    data['text'][i] == searchText
                    and data['conf'][i] > 90  # Check confidence level
            ):
                occurrence = {
                    'x': data['left'][i],
                    'y': data['top'][i]
                }
                occurrences.append(occurrence)
    return occurrences


print(SearchUsingImage("Calc"))
