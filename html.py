class HTMLBuilder:
    def __init__(self):
        self.__body = ""

    def __add_element(self, name: str, content: str = "", pair: bool = True, **params):
        element = "<" + name
        option = [f'{key}="{value}"' for key, value in params.items()]
        if option:
            element += " " + " ".join(option)
        if pair:
            element += f">{content}</{name}>"
        else:
            element += ">"
        return element

    def set_title(self, title: str):
        self.__title = title

    def add_paragraph(self, text: str):
        self.__body += self.__add_element("p", text, True)

    def add_link(self, href: str, text: str):
        self.__body += self.__add_element("a", text, True, href=href)

    def add_div(self, text: str):
        self.__body += self.__add_element("div", text, True)

    def add_h(self, number: int, text: str):
        self.__body += self.__add_element(f"h{number}", text, True)

    def add_img(self, URL: str):
        self.__body += self.__add_element("img", "", False, src=URL)

    def add_list(self, tag: str, array: list):
        self.__body += self.__add_element(tag, "", False)
        for i in range(len(array)):
            self.__body += self.__add_element("li", array[i], True)
        self.__body += f"</{tag}>"

    def change_text(self, tag: str, text: str):
        self.__body += self.__add_element(tag, text, True)

    def get_body(self) -> str:
        return self.__body

    def render(self):
        return f"""
    <html>
        <head>
            {self.__add_element("title",self.__title, True)}
        </head>
        <body>
            {self.__body}
            </body>
    </html>
    """


html = HTMLBuilder()
html.set_title("Site")
html.add_paragraph("First paragraph")
html.add_link("https://rickowens.eu", "Жми на ссылку, покупай одежду")
html.add_div("fsdfd")
html.add_h(1, "Я stylist")
html.add_img("https://logodix.com/logo/1120105.jpg")
html.change_text("strong", "Я ношу ")
html.add_list("ol", ["Rick Owens", "336"])
print(html.render())
