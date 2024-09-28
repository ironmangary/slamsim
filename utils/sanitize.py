# sanitize.py - Sanitization functions
# for SlamSim

import bleach

def sanitize_input(input_string):
    return bleach.clean(input_string, tags=[], strip=True)

def sanitize_limit_html(input_string):
    allowed_tags = ['b', 'i', 'u', 'strong', 'em', 'br', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'center', 'ol', 'ul', 'li']
    return bleach.clean(input_string, tags=allowed_tags, strip=True)

def sanitize_number(value, allow_empty=False):
    if value == '' and allow_empty:
        return None
    if value.isdigit():
        return int(value)
    return None
