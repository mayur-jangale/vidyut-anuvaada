# Sutra प.5.1.93: तेन परिजय्यलभ्यकार्यसुकरम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tena parijayyalaByakAryasukaram

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.93"
SUTRA_TEXT = "तेन परिजय्यलभ्यकार्यसुकरम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tena parijayyalaByakAryasukaram"


class Sutra5193:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.93: अग्निः'),
		('रामः', '', 'प.5.1.93: रामः'),
		('सीता', '', 'प.5.1.93: सीता'),
	]

