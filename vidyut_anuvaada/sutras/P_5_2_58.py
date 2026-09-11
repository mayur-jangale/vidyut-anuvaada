# Sutra प.5.2.58: षष्ट्यादेश्चासंख्यादेः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — zazwyAdeScAsaMKyAdeH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.58"
SUTRA_TEXT = "षष्ट्यादेश्चासंख्यादेः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — zazwyAdeScAsaMKyAdeH"


class Sutra5258:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.58: अग्निः'),
		('रामः', '', 'प.5.2.58: रामः'),
		('सीता', '', 'प.5.2.58: सीता'),
	]

