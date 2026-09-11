# Sutra प74: BImAdayo apAdAne
# BImAdayo'apAdAne

from sutra_engines import apply_general
from P_3_4 import apply_3_4_74

SUTRA_CODE = "प74"
SUTRA_TEXT = "BImAdayo apAdAne"
SUTRA_DESC = "BImAdayo'apAdAne"


class Sutra3474:
	def apply(self, word, pos):
		return apply_3_4_74(word, pos)

	EXAMPLES = [
	('अग्निः', '', "p34-074:BImAdayo'apAdAne;input=अग्निः;stem=अग्निः;ending=-;pos="),
		('रामः', '', "p34-074:BImAdayo'apAdAne;input=रामः;stem=रामः;ending=-;pos="),
		('सीता', '', "p34-074:BImAdayo'apAdAne;input=सीता;stem=सीता;ending=-;pos="),
	]

