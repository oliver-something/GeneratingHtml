
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

# Print the rendered HTML
print(html.render())

# Generate the HTML file
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
    <title>My Page</title>
  </head>
  <body>
    <div class="divClass">
      <p class="intro">This is a paragraph.</p>
      <p class="intro">This is a paragraph.</p>
    </div>
    <div class="secondDiv">
      <p class="intro">This is a paragraph.</p>
      <p class="intro">This is a paragraph.</p>
    </div>
  </body>
</html>
```
