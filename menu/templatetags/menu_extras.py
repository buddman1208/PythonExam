from django import template

register = template.Library()

@register.filter
def get_range(value):
	"""
	Filter - returns a list containing range made from given va
	lue
	Usage (in template):
	"""
	return range(int(value))