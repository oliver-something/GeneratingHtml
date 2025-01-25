class Tag:
    def __init__(self, name, attributes=None, children=None):
        self.name = name
        self.attributes = attributes or {}
        self.children = children or []

    def render(self):
        """Render the tag and its children as HTML."""
        # Convert attributes to a string
        attributes_str = ' '.join([f'{key}="{value}"' for key, value in self.attributes.items()])
        if attributes_str:
            attributes_str = " " + attributes_str

        # Render children properly
        children_str = "".join(
            [child.render() if isinstance(child, Tag) else str(child) for child in self.children]
        )

        # Render tag with or without children
        if self.children:
            return f"<{self.name}{attributes_str}>{children_str}</{self.name}>"
        else:
            return f"<{self.name}{attributes_str} />"

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

# Example Usage
html = Html(lang="en")([
    Head()([
        Meta(charset="UTF-8"),
        Title("My Page")
    ]),
    Body()([
        Div()([
            P("This is a paragraph.", class_="intro"),
            P("This is a paragraph.", class_="intro")
        ])
    ])
])

# Print rendered HTML
print(html.render())