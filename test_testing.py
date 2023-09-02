import xml.etree.ElementTree as ET

global bounds
tree = ET.parse("dump.xml")
root = tree.getroot()
target_elements = []
position = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}
pos = '1'

text = "xpath|//android.widget.EditText"
# text = "xpath|//android.widget.EditText[@content-desc='Enter Password']"
locator, locatorBy = text.split("|")
locatorBy = locatorBy.replace("//", "").replace("[", "").replace("]", "")
if "@" in locatorBy:
    className, parameter2 = locatorBy.split("@")
    parameter2 = parameter2.split("=")
    for ele in root.iter():
        if ele.get('class') == className and ele.get(parameter2[0]) == parameter2[1].replace("'", ""):
            bounds = ele.get('bounds')
else:
    className = locatorBy
    for ele in root.iter():
        if ele.get('class') == className:
            bounds = ele.get('bounds')
            x, y = map(int, bounds[1:-1].split('][')[0].split(','))
            target_elements.append((x, y))
if len(target_elements) > 0:
    x, y = target_elements[position[pos]]
    print(x, y)
