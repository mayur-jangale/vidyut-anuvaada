# Sutra प.2.3.38: षष्ठी चानादरे
# (Samasa (compound formation)) — zazWI cAnAdare

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.38"
SUTRA_TEXT = "षष्ठी चानादरे"
SUTRA_DESC = "(Samasa (compound formation)) — zazWI cAnAdare"


class Sutra2338:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

