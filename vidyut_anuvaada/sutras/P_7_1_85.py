# Sutra प.7.1.85: पथिमथ्यृभुक्षामात्
# (Taddhita (secondary derivations)) — paTimaTyfBukzAmAt

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.85"
SUTRA_TEXT = "पथिमथ्यृभुक्षामात्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — paTimaTyfBukzAmAt"


class Sutra7185:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.85: अग्निः'),
		('रामः', '', 'प.7.1.85: रामः'),
		('सीता', '', 'प.7.1.85: सीता'),
	]

