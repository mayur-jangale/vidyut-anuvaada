# Sutra प12: Saki RamulkamulO
# Saki Ramul kamulO

from sutra_engines import apply_general
from P_3_4 import apply_3_4_12

SUTRA_CODE = "प12"
SUTRA_TEXT = "Saki RamulkamulO"
SUTRA_DESC = "Saki Ramul kamulO"


class Sutra3412:
	def apply(self, word, pos):
		return apply_3_4_12(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-012:Saki Ramul kamulO;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-012:Saki Ramul kamulO;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-012:Saki Ramul kamulO;input=सीता;stem=सीता;ending=-;pos='),
	]

