from django.contrib.auth import get_user_model
from django import template 
from django.utils.html import format_html

register = template.Library()
user_model = get_user_model()

@register.filter
def author_details(author, current_user):
  if not isinstance(author, user_model):
    return ''
    
  if author == current_user: 
    return format_html('<strong>me</strong>')

  author_name = str(author.username)
  if author.first_name and author.last_name: 
    author_name = f'{author.first_name} {author.last_name}'

  prefix, suffix = '', ''
  if author.email:
    prefix = format_html('<a href="mailto:{}">', author.email)
    suffix = format_html("</a>")

  return format_html('{}{}{}', prefix, author_name, suffix)