# Get all the names on this page 
from utils import *

infos = get_lex_links()
for name, _ in infos.items():
    name_lower = to_lower_name(name)
    parse_lex_transcript(name_lower)