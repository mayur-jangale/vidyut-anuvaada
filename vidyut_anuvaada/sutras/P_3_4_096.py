# Sutra प96: vEto nyatra
# vEto'nyatra

from sutra_engines import apply_general
from P_3_4 import apply_3_4_96

SUTRA_CODE = "प96"
SUTRA_TEXT = "vEto nyatra"
SUTRA_DESC = "vEto'nyatra"


class Sutra3496:
	def apply(self, word, pos):
		return apply_3_4_96(word, pos)

	EXAMPLES = [
	('अग्निः', '', "p34-096:vEto'nyatra;input=अग्निः;stem=अग्निः;ending=-;pos="),
		('रामः', '', "p34-096:vEto'nyatra;input=रामः;stem=रामः;ending=-;pos="),
		('सीता', '', "p34-096:vEto'nyatra;input=सीता;stem=सीता;ending=-;pos="),
	]

