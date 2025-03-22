import marimo

__generated_with = "0.11.25"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Bullet Formatting""")
    return


@app.cell
def _():
    import io
    import itertools
    import re
    import textwrap

    def get_indentation(text: str):
        bullet_pattern = re.compile('^( *[*-] *)')
        if match := bullet_pattern.search(text):
            return match[1], ' ' * len(match[1])
        return '- ', '  '

    def format_bullet(text: str, width=72):
        initial_indent, subsequent_indent = get_indentation(text)
        buf = io.StringIO()
        separator = re.compile(r"^ *[*-] +", re.MULTILINE)
        bullets = separator.split(text)

        for bullet in bullets:
            bullet = textwrap.fill(
                bullet,
                width=width,
                initial_indent=initial_indent,
                subsequent_indent=subsequent_indent,
            )
            buf.write(bullet)
            buf.write("\n")

        return buf.getvalue()
    return format_bullet, get_indentation, io, itertools, re, textwrap


@app.cell
def _(format_bullet):
    text = """  * Lorem ipsum odor amet, consectetuer adipiscing elit.
    Fames vulputate - iaculis magna malesuada dignissim elementum ut maximus.
      * Magna habitant mi auctor facilisis
    urna nullam sapien. Curae donec mauris maximus morbi
    porttitor mus per auctor pretium.
      * Lacus ultrices congue pellentesque vel tempor convallis egestas. Faucibus aliquam risus diam faucibus; sit etiam ad hac.
      * Pellentesque praesent scelerisque sit litora class ultrices phasellus luctus. Semper quis eleifend quam morbi non hendrerit condimentum euismod.
    """.rstrip()
    print(text)
    print("-" * 80)
    print(format_bullet(text, 79))
    return (text,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
