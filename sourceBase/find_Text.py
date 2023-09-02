import xml.etree.ElementTree as ET
import uiautomator2 as u2
import os


class FindText:

    @staticmethod
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

    @staticmethod
    def get_text(text, partial=False, pos=1):
        try:
            # Using XML
            pos = str(pos)
            position = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}
            tree = ET.parse(FindText.get_dump("104e6ae3"))
            root = tree.getroot()
            target_elements = []
            for element in root.iter():
                if element.get('text') and (partial and text in element.get('text')) or (
                        not partial and text == element.get('text')):
                    bounds = element.get('bounds')
                    x_start, y_start = map(int, bounds[1:-1].split('][')[0].split(','))
                    x_end, y_end = 0, 0
                    x = (x_start + x_end)
                    y = (y_start + y_end)
                    target_elements.append((x, y))
            if len(target_elements) > 0:
                x, y = target_elements[position[pos]]
                return x, y
            else:
                print(f"No element found with {'partial' if partial else 'exact'} text '{text}'")
        except IndexError as e:
            raise e
