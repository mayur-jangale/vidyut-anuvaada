# Sutra प.1.4.109: परः सन्निकर्षः संहिता
# (Samjna (technical definitions)) — paraH sannikarzaH saMhitA

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.109"
SUTRA_TEXT = "परः सन्निकर्षः संहिता"
SUTRA_DESC = "(Samjna (technical definitions)) — paraH sannikarzaH saMhitA"


class Sutra14109:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_109
		return apply_1_4_109(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sandhi:saMhitA:para-sannikarSa;word=अग्निः'),
		('रामः', '', 'sandhi:saMhitA:para-sannikarSa;word=रामः'),
		('सीता', '', 'sandhi:saMhitA:para-sannikarSa;word=सीता'),
	]

