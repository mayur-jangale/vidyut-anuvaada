# Sutra प87: ser hyap icca
# ASIrliN ser hyap icca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_87

SUTRA_CODE = "प87"
SUTRA_TEXT = "ser hyap icca"
SUTRA_DESC = "ASIrliN ser hyap icca"


class Sutra3487:
	def apply(self, word, pos):
		return apply_3_4_87(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-087:ASIrliN ser hyap icca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-087:ASIrliN ser hyap icca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-087:ASIrliN ser hyap icca;input=सीता;stem=सीता;ending=-;pos='),
	]

