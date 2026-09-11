# Sutra प.5.1.79: तेन निर्वृत्तम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tena nirvfttam

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.79"
SUTRA_TEXT = "तेन निर्वृत्तम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tena nirvfttam"


class Sutra5179:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.79: अग्निः'),
		('रामः', '', 'प.5.1.79: रामः'),
		('सीता', '', 'प.5.1.79: सीता'),
	]

