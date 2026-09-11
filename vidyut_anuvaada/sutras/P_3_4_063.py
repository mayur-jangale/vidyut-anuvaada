# Sutra प63: ktin tuSNImi
# tuSNImi BuvuH ktin

from sutra_engines import apply_general
from P_3_4 import apply_3_4_63

SUTRA_CODE = "प63"
SUTRA_TEXT = "ktin tuSNImi"
SUTRA_DESC = "tuSNImi BuvuH ktin"


class Sutra3463:
	def apply(self, word, pos):
		return apply_3_4_63(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-063:tuSNImi BuvuH ktin;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-063:tuSNImi BuvuH ktin;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-063:tuSNImi BuvuH ktin;input=सीता;stem=सीता;ending=-;pos='),
	]

