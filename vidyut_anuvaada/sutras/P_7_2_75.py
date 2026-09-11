# Sutra प.7.2.75: किरश्च पञ्चभ्यः
# (Taddhita (secondary derivations)) — kiraSca paYcaByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.75"
SUTRA_TEXT = "किरश्च पञ्चभ्यः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — kiraSca paYcaByaH"


class Sutra7275:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.75: अग्निः'),
		('रामः', '', 'प.7.2.75: रामः'),
		('सीता', '', 'प.7.2.75: सीता'),
	]

