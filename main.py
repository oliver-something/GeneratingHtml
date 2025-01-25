from html import *

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
        ]),
    ]),
    Script()([
    """
        console.log('Hello, World!');
        let name = 'Oliver';
        console.log(`Hello, ${name}`);
    """,
    ])
])

# Print rendered HTML
print(html.render())

#Generate the rendered HTML
gen = Generate(html, "index.html")
gen.generate()