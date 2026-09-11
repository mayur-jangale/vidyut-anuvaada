# Sutra प.5.1.63: तद् अर्हति
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tad arhati

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.63"
SUTRA_TEXT = "तद् अर्हति"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tad arhati"


class Sutra5163:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.63: अग्निः'),
		('रामः', '', 'प.5.1.63: रामः'),
		('सीता', '', 'प.5.1.63: सीता'),
	]

