# Sutra प.5.3.115: वृकाट्टेण्यण्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vfkAwweRyaR

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.115"
SUTRA_TEXT = "वृकाट्टेण्यण्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vfkAwweRyaR"


class Sutra53115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.115: अग्निः'),
		('रामः', '', 'प.5.3.115: रामः'),
		('सीता', '', 'प.5.3.115: सीता'),
	]

