import re

#function checks html file and returns true or false, true if valid, false if invalid
def checkhtml(file):
    arr = []
    with open(file, 'r') as f:
        #formats the html file
        data = f.read().replace('\n', '')
        #gets each tag using re library
        tags = re.findall(r'(</?[a-z]*>)', data)

    #iterates through each tag found, searching for completeness, removing each complete pair
    for tag in tags:
        if tag.startswith("</"):
            if len(arr) == 0:
                return False
            else:
                arr.pop()
        elif tag.startswith("<"):
            arr.append(tag)
    #if each pairs match has been found , len(arr) = 0, and true is returned, valid html
    return len(arr) == 0

#runner code
def main():
    filename = input('Enter file name: ')
    if checkhtml(filename):
        print('Valid HTML')
    else:
        print('Invalid HTML, mismatched opening and closing braces')

main()
