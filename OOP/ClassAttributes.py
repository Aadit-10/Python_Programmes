class webBrowsr:
    connected = True  # Class Attribute

    def __init__(self, page):
        self.history = [page]
        self.current_Page = page


chrome = webBrowsr("google.com")
firefox = webBrowsr("youtube.com")

print(chrome.__dict__)
print(firefox.__dict__)

# Check class attribute
print(chrome.connected)
print(firefox.connected)
#  change value of class attr
webBrowsr.connected=False
# chrome.connected = False
print(chrome.__dict__)  # if class attr is changed then it is reflected in instance attribute
print(firefox.__dict__)
print("firfox connected ",firefox.connected)
print("Chrome connected ",chrome.connected)