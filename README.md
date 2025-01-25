# Declarative HTML
> This is a test project to create html files using declarative syntax in python.

> It is still in development process, If you are interested in the project please Email me.

> My email address is diablo31@live.co.uk


## Example usage : 

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

# Print rendered HTML
print(html.render())

#Generate the rendered HTML
gen = Generate(html, "index.html")
gen.generate()
   
```

## Generated HTML file : 

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
      <p class="intro">
        This is a paragraph.
      </p>
      <p class="intro">
        This is a paragraph.
      </p>
    </div>
  </body>
</html>

```