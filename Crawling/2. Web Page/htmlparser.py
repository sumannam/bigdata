from html.parser import HTMLParser
 
class Parse(HTMLParser):
    #Python3부터 __init__() 함수 호출 필요
    def __init__(self):
        super().__init__()
        self.reset()
 
    # HTMLParser에서 호출할 때 메서드가 출력해야 하는 내용 정의
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for a in attrs:
            print("Attributes of the tag: ", a)
 
    def handle_data(self, data):
        print("Here's the data: ", data)
 
    def handle_endtag(self, tag):
        print("End tag: ", tag)
 
 
parser = Parse()
parser.feed("<html><head><title>Testing Parser</title></head></html>")