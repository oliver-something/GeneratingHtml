
BLOCK_LEVEL_TAGS = [
    'address', 'article', 'aside', 'blockquote','canvas',
    'dd', 'div', 'dl', 'dt', 'fieldset','figcaption', 'figure',
    'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'header', 'hr','li', 'main', 'nav', 'noscript', 'ol',
    'p', 'pre', 'section', 'table', 'tfoot', 'ul', 'video',
]

INLINE_LEVEL_TAGS = [
    'a', 'abbr', 'acronym', 'b', 'bdo', 'big',
    'button', 'cite', 'code', 'dfn', 'em', 'i',
    'input', 'kbd', 'label', 'map', 'object', 'output',
    'samp', 'script', 'select', 'small', 'span', 'strong',
    'sup', 'textarea', 'time', 'tt', 'var'
]

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
        # Validate each child
        for child in children:
            if self.name in INLINE_LEVEL_TAGS and child.name in BLOCK_LEVEL_TAGS:
                raise Exception(f"Block-level tag <{child.name}> cannot be added inside an inline-level tag <{self.name}>.")

        """Allow adding children with function-like syntax."""
        # Add valid children
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
    def __init__(self, text=None, **attributes):
        super().__init__('div', attributes)
        if text:
            self.children.append(text)


class P(Tag):
    def __init__(self, text=None, **attributes):
        super().__init__('p', attributes)
        if text:
            self.children.append(text)


class Image(Tag):
    def __init__(self, src=None, alt=None, **attributes):
        if not src:
            raise ValueError("The 'src' attribute is required for an 'Image' tag.")
        attributes['src'] = src

        if alt:
            attributes['alt'] = alt

        super().__init__('img', attributes)

    def __call__(self, children):
        raise TypeError("Cannot add children to an 'img' tag.")


class Section(Tag):
    def __init__(self, text=None, **attributes):
        super().__init__('section', attributes)
        if text:
            self.children.append(text)


class Span(Tag):
    def __init__(self, text=None, **attributes):
        super().__init__('span', attributes)
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
            P("This is a paragraph.", class_="intro"),
        ]),
        Div(class_="secondDiv")([
            P("This is a paragraph.", class_="intro", id_="test_id"),
            P("This is a paragraph.", class_="intro"),
            Image(src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHhtanZhaHVvcHplYnhpcGN3ajF0c3diYW91dTMzNTY5ZjRhdmJkOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kFgzrTt798d2w/giphy.gif", alt="rick roll", width_="480", height_="340")
        ])
    ])
])

# Print rendered HTML
print(html.render())

#Generate the rendered HTML
gen = Generate(html, "index.html")
gen.generate()