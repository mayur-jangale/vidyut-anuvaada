# Sutra प.2.3.47: सम्बोधने च
# (Samasa (compound formation)) — samboDane ca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.47"
SUTRA_TEXT = "सम्बोधने च"
SUTRA_DESC = "(Samasa (compound formation)) — samboDane ca"


class Sutra2347:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

