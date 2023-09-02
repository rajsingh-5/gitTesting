import xml.etree.ElementTree as ET
import uiautomator2 as u2
import os
import cv2
import pytesseract

global data


def get_dump(deviceId):
    try:
        device = u2.connect(deviceId)
        xml_dump = device.dump_hierarchy()
        with open('dump.xml', 'w', encoding="utf-8") as file:
            file.write(xml_dump)
        dump_path = os.path.join(os.getcwd(), 'dump.xml')
        return dump_path
    except Exception as e:
        raise e


def get_text(text, partial=False, pos=1):
    try:
        pos = str(pos)
        position = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}
        tree = ET.parse(get_dump("RZCT30QFEMB"))
        root = tree.getroot()
        target_elements = []
        if "|" in text:
            locator, locatorBy = text.split("|")
            locatorBy = locatorBy.replace("//", "").replace("[", "").replace("]", "")
            if "@" in locatorBy:
                className, parameter2 = locatorBy.split("@")
                parameter2 = parameter2.split("=")
                for ele in root.iter():
                    if ele.get('class') == className and ele.get(parameter2[0]) == parameter2[1].replace("'", ""):
                        bounds = ele.get('bounds')
                        x, y = map(int, bounds[1:-1].split('][')[0].split(','))
                        target_elements.append((x, y))
            else:
                className = locatorBy
                for ele in root.iter():
                    if ele.get('class') == className:
                        bounds = ele.get('bounds')
                        print(bounds)
                        x, y = map(int, bounds[1:-1].split('][')[0].split(','))
                        target_elements.append((x, y))
        else:
            for element in root.iter():
                if element.get('text') and (partial and text in element.get('text')) or (
                        not partial and text == element.get('text')):
                    bounds = element.get('bounds')
                    x, y = map(int, bounds[1:-1].split('][')[0].split(','))
                    target_elements.append((x, y))
        if len(target_elements) > 0:
            x, y = target_elements[position[pos]]
            return x, y
        else:
            print(f"No element found with {'partial' if partial else 'exact'} text '{text}'")
    except IndexError as e:
        raise e


def SearchUsingImage(searchText, pos=1):
    pos = str(pos)
    try:
        position = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}
        image = cv2.imread("framm.png")
        data = pytesseract.image_to_data(image, lang="eng", output_type=pytesseract.Output.DICT)

        occurrences = normalImg(searchText, image)
        if len(occurrences) < 1:
            occurrences = greyImage(searchText, image)
        return occurrences[position[pos]]['x'], occurrences[position[pos]]['y']
    except IndexError as e:
        for i in range(len(data['text']) - 1):
            if data['conf'][i] > (-1):
                print(data['text'][i], data['conf'][i])
        raise e


def normalImg(searchText, image):
    data = pytesseract.image_to_data(image, lang="eng", output_type=pytesseract.Output.DICT)
    occurrences = []
    searchTextList = searchText.split(" ")
    if len(searchTextList) > 1:
        for i in range(len(data['text']) - 1):
            if data['text'][i] == searchTextList[0] and data['text'][i + 1] == searchTextList[1]:
                if data['conf'][i] > 90:
                    occurrence = {
                        'x': data['left'][i],
                        'y': data['top'][i]
                    }
                    occurrences.append(occurrence)
    else:
        for i in range(len(data['text'])):
            if data['text'][i] == searchText:
                if data['conf'][i] > 90:
                    occurrence = {
                        'x': data['left'][i],
                        'y': data['top'][i]
                    }
                    occurrences.append(occurrence)
    return occurrences


def greyImage(searchText, image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh, img_bw = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
    data = pytesseract.image_to_data(img_bw, lang="eng", output_type=pytesseract.Output.DICT)
    occurrences = []
    searchTextList = searchText.split(" ")
    if len(searchTextList) > 1:
        for i in range(len(data['text']) - 1):
            if data['text'][i] == searchTextList[0] and data['text'][i + 1] == searchTextList[1]:
                if data['conf'][i] > 90:
                    occurrence = {
                        'x': data['left'][i],
                        'y': data['top'][i]
                    }
                    occurrences.append(occurrence)
    else:
        for i in range(len(data['text'])):
            if data['text'][i] == searchText:
                if data['conf'][i] > 90:
                    occurrence = {
                        'x': data['left'][i],
                        'y': data['top'][i]
                    }
                    occurrences.append(occurrence)
    return occurrences


print(SearchUsingImage("Mumbai"))
