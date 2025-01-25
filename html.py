class Tag:
    def __init__(self, name, attributes=None, children=None):
        self.name = name
        self.attributes = attributes or {}
        self.children = children or []

    def render(self, indent=0):
        """Render the tag and its content as formatted HTML."""
        # Prepare the indentation string
        indent_str = "  " * indent
        newline = "\n"

        # Handle special attribute names like class_
        attributes_str = ' '.join([
            f'{key.rstrip("_")}="{value}"' for key, value in self.attributes.items()
        ])
        if attributes_str:
            attributes_str = " " + attributes_str

        # Render children with proper indentation
        children_str = ""
        if self.children:
            children_str = newline + "".join(
                [child.render(indent + 1) if isinstance(child, Tag) else f"{indent_str}  {child}{newline}"
                 for child in self.children]
            ) + indent_str

        # Render tag with or without children
        if self.children:
            return f"{indent_str}<{self.name}{attributes_str}>{children_str}</{self.name}>{newline}"
        else:
            return f"{indent_str}<{self.name}{attributes_str} />{newline}"

    def __call__(self, children):
        """Allow adding children with function-like syntax."""
        self.children.extend(children)
        return self


class Html(Tag):
    def __init__(self, **attributes):
        super().__init__('html', attributes)

class Head(Tag):
    def __init__(self, **attributes):
        super().__init__('head', attributes)

class Body(Tag):
    def __init__(self, **attributes):
        super().__init__('body', attributes)

class Meta(Tag):
    def __init__(self, **attributes):
        super().__init__('meta', attributes)

class Title(Tag):
    def __init__(self, text, **attributes):
        super().__init__('title', attributes)
        self.children.append(text)

class Div(Tag):
    def __init__(self, **attributes):
        super().__init__('div', attributes)

class P(Tag):
    def __init__(self, text=None, **attributes):
        super().__init__('p', attributes)
        if text:
            self.children.append(text)

class Generate:
    def __init__(self, html_input: Html, file_name: str):
        file_extension = ".html"
        if file_name.find(file_extension) != -1:
            self.file_name = file_name
        else:
            self.file_name = file_name.join(".html")

        self.html_input = html_input
    def generate(self):
        file = open(self.file_name, "w")
        file.write(self.html_input.render())
        print("File is written successfully")
        file.close()

# Example Usage
html = Html(lang="en")([
    Head()([
        Meta(charset="UTF-8"),
        Title("My Page")
    ]),
    Body()([
        Div(class_="divClass")([
            P("This is a paragraph.", class_="intro"),
            P("This is a paragraph.", class_="intro")
        ]),
        Div(class_="secondDiv")([
            P("This is a paragraph.", class_="intro"),
            P("This is a paragraph.", class_="intro")
        ])
    ])
])

# Print rendered HTML
print(html.render())

#Generate the rendered HTML
gen = Generate(html, "index.html")
gen.generate()