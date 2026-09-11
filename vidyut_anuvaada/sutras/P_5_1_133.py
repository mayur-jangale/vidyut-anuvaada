# Sutra प.5.1.133: द्वन्द्वमनोज्ञादिभ्यश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvandvamanojYAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.133"
SUTRA_TEXT = "द्वन्द्वमनोज्ञादिभ्यश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvandvamanojYAdiByaSca"


class Sutra51133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.133: अग्निः'),
		('रामः', '', 'प.5.1.133: रामः'),
		('सीता', '', 'प.5.1.133: सीता'),
	]

