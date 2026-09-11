# Sutra प.2.4.46: णौ गमिरबोधने
# (Samasa (compound formation)) — RO gamiraboDane

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.46"
SUTRA_TEXT = "णौ गमिरबोधने"
SUTRA_DESC = "(Samasa (compound formation)) — RO gamiraboDane"


class Sutra2446:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

