# Sutra प.7.1.101: उपधायाश्च
# (Taddhita (secondary derivations)) — upaDAyASca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.101"
SUTRA_TEXT = "उपधायाश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — upaDAyASca"


class Sutra71101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.101: अग्निः'),
		('रामः', '', 'प.7.1.101: रामः'),
		('सीता', '', 'प.7.1.101: सीता'),
	]

