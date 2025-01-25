
# Declarative HTML Framework

This project aims to create HTML files using a declarative syntax in Python.

> **Note:** This project is currently under development. If you are interested in collaborating or have any questions, please feel free to contact me.

**Contact Email:** [diablo31@live.co.uk](mailto:diablo31@live.co.uk)

---

## Roadmap

1. **Full HTML Tag and Attribute Support**  
   - Implement support for all HTML tags and attributes.
   
2. **Control Structures and Loops**  
   - Add support for control structures such as `ForEach`, `IF-ELSE`, and other programming constructs.

3. **DSL Compiler**  
   - Develop a compiler for the DSL to streamline the build process.

4. **Framework Integration**  
   - Integrate the framework with popular backend technologies such as Django, FastAPI, and Flask as a template engine.

---

## Example Usage

Here is an example of how to use the framework:

```python
from html import *

html = Html(lang="en")(
    Head()(
        Meta(charset="UTF-8"),
        Title("My Page")
    ),
    Body()(
        Div(class_="divClass")(
            P("This is a paragraph.", class_="intro"),
            P("This is a paragraph.", class_="intro"),
        ),
        Div(class_="secondDiv")(
            P("This is a paragraph.", class_="intro", id_="test_id"),
            P("This is a paragraph.", class_="intro"),
            Image(src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHhtanZhaHVvcHplYnhpcGN3ajF0c3diYW91dTMzNTY5ZjRhdmJkOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kFgzrTt798d2w/giphy.gif", alt="rick roll", width_="480", height_="340")
        ),
    ),
    Script()(
    """
        console.log('Hello, World!');
        let name = 'Oliver';
        console.log(`Hello, ${name}`);
    """,
    )
)

# Print rendered HTML
print(html.render())

#Generate the rendered HTML
gen = Generate(html, "index.html")
gen.generate()
```

---

## Generated HTML

The following HTML will be generated from the Python code:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>
      My Page
    </title>
  </head>
  <body>
    <div class="divClass">
      <p class="intro">
        This is a paragraph.
      </p>
      <p class="intro">
        This is a paragraph.
      </p>
    </div>
    <div class="secondDiv">
      <p class="intro" id="test_id">
        This is a paragraph.
      </p>
      <p class="intro">
        This is a paragraph.
      </p>
      <img width="480" height="340" src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHhtanZhaHVvcHplYnhpcGN3ajF0c3diYW91dTMzNTY5ZjRhdmJkOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kFgzrTt798d2w/giphy.gif" alt="rick roll" />
    </div>
  </body>
  <script type="text/javascript">
        console.log('Hello, World!');
        let name = 'Oliver';
        console.log(`Hello, ${name}`);
    </script>
</html>

```
> Inline JavaScript is not advised, and there are currently no syntax highlighting capabilities. To use external JavaScript files, add the src attribute. There is support for async and differ.
