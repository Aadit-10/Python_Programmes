class webBrowsr:
    connected = True  # Class Attribute
    counter_web = 0

    def __init__(self, page):
        self.history = [page]
        self.current_Page = page
        webBrowsr.counter_web += 1

print(webBrowsr.counter_web)
chrome = webBrowsr("google.com")
firefox = webBrowsr("youtube.com")
print(webBrowsr.counter_web)

