# Sutra प.2.4.27: पूर्ववदश्ववडवौ
# (Samasa (compound formation)) — pUrvavadaSvavaqavO

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.27"
SUTRA_TEXT = "पूर्ववदश्ववडवौ"
SUTRA_DESC = "(Samasa (compound formation)) — pUrvavadaSvavaqavO"


class Sutra2427:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

