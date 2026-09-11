# Sutra प.2.4.66: बह्वचः इञः प्राच्यभरतेषु
# (Samasa (compound formation)) — bahvacaH iYaH prAcyaBaratezu

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.66"
SUTRA_TEXT = "बह्वचः इञः प्राच्यभरतेषु"
SUTRA_DESC = "(Samasa (compound formation)) — bahvacaH iYaH prAcyaBaratezu"


class Sutra2466:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

