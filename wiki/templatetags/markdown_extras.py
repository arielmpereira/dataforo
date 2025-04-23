from django import template
import markdown2

register = template.Library()

@register.filter
def markdown(texto):
    return markdown2.markdown(
        texto,
        extras=[
            "fenced-code-blocks",
            "tables",
            "strike",
            "code-friendly"
        ]
    )

