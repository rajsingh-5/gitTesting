import subprocess
import xml.etree.ElementTree as ET
import uiautomator2 as u2
import os

udid = "104e6ae3"


def get_dump(udid):
    try:
        device = u2.connect(udid)
        xml_dump = device.dump_hierarchy()
        with open('dump.xml', 'w', encoding="utf-8") as file:
            file.write(xml_dump)
        dump_path = os.path.join(os.getcwd(), 'dump.xml')
        return dump_path
    except Exception as e:
        raise e


def text_read_method_one(text, partial=False):
    try:
        tree = ET.parse(get_dump(udid))
        root = tree.getroot()
        target_element = None
        for element in root.iter():
            if element.get('text') and (partial and text in element.get('text')) or (
                    not partial and text == element.get('text')):
                target_element = element
                break

        if target_element is not None:
            bounds = target_element.get('bounds')
            x_start, y_start = map(int, bounds[1:-1].split('][')[0].split(','))
            x_end, y_end = 0, 0
            x = (x_start + x_end)
            y = (y_start + y_end)
            return x, y
        else:
            print(f"No element found with {'partial' if partial else 'exact'} text '{text}'")

    except Exception as e:
        raise e


def click(text, partial=False):
    try:
        x, y = text_read_method_one(text, partial)
        subprocess.run(["adb", "-s", udid, "shell", "input", "tap", str(x), str(y)], check=True, shell=True)
    except subprocess.CompletedProcess as e:
        raise e


def isPresent(text, partial=False):
    try:
        dump_result = text_read_method_one(text, partial)
        if dump_result is not None:
            print(f"'{text}' is present")
    except Exception as e:
        raise e


isPresent("Account Settings")
click("Notification", True)
