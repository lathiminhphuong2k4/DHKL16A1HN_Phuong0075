#LATHIMINHPHUONG-22174600075
import xml.dom.minidom

def main():
    path="f:/Python Nâng Cao/Chương 2 . PT tập tin XML , JSON/Bài Tập Chương 2/sample.xml"
    doc=xml.dom.minidom.parse("sample.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    expertise=doc.getElementsByTagName("expertise")
    print("%d expertise.length")
    for skill in expertise:
        print(skill.getAttribute("name"))
if __name__=="__main__":
    main()