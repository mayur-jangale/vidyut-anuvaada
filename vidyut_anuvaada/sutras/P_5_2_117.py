# Sutra प.5.2.117: तुन्दादिभ्य इलच् च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tundAdiBya ilac ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.117"
SUTRA_TEXT = "तुन्दादिभ्य इलच् च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tundAdiBya ilac ca"


class Sutra52117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.117: अग्निः'),
		('रामः', '', 'प.5.2.117: रामः'),
		('सीता', '', 'प.5.2.117: सीता'),
	]

