# Sutra प24: viBAzA agra prathama
# viBAzA gre prathama pUrve

from sutra_engines import apply_general
from P_3_4 import apply_3_4_24

SUTRA_CODE = "प24"
SUTRA_TEXT = "viBAzA agra prathama"
SUTRA_DESC = "viBAzA gre prathama pUrve"


class Sutra3424:
	def apply(self, word, pos):
		return apply_3_4_24(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-024:viBAzA gre prathama pUrve;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-024:viBAzA gre prathama pUrve;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-024:viBAzA gre prathama pUrve;input=सीता;stem=सीता;ending=-;pos='),
	]

