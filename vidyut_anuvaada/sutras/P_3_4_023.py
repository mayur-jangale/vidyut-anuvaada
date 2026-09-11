# Sutra प23: na yadyanAkANkze
# na yadi anAkANkze

from sutra_engines import apply_general
from P_3_4 import apply_3_4_23

SUTRA_CODE = "प23"
SUTRA_TEXT = "na yadyanAkANkze"
SUTRA_DESC = "na yadi anAkANkze"


class Sutra3423:
	def apply(self, word, pos):
		return apply_3_4_23(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-023:na yadi anAkANkze;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-023:na yadi anAkANkze;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-023:na yadi anAkANkze;input=सीता;stem=सीता;ending=-;pos='),
	]

