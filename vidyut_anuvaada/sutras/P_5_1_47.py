# Sutra प.5.1.47: तदस्मिन् वृद्ध्यायलाभशुल्कोपदा दीयते
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasmin vfdDyAyalABaSulkopadA dIyate

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.47"
SUTRA_TEXT = "तदस्मिन् वृद्ध्यायलाभशुल्कोपदा दीयते"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasmin vfdDyAyalABaSulkopadA dIyate"


class Sutra5147:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.47: अग्निः'),
		('रामः', '', 'प.5.1.47: रामः'),
		('सीता', '', 'प.5.1.47: सीता'),
	]

