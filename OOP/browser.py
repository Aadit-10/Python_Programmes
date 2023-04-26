class webBrowsr:
    connected = True  # Class Attribute

    def __init__(self, page):
        self.history = [page]
        self.current_Page = page
        self.is_incognito=False

    def navigate(self,new_page):
        self.current_Page=new_page
        if not self.is_incognito:
            self.history.append(new_page)

    def clear_history(self):
        # remove everything upto last element
        self.history[:-1]=[]

    @classmethod
    def with_incognito(cls,page):
        instance=cls(page)
        instance.is_incognito=True
        instance.history=[]
        return instance

chrome = webBrowsr.with_incognito("google.com")
firefox = webBrowsr("youtube.com")
chrome.navigate('dictionary.com')
chrome.navigate('helo.com')
print(chrome.__dict__)
print(firefox.__dict__)
