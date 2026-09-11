# Sutra प.7.3.40: भियो हेतुभये षुक्
# (Taddhita (secondary derivations)) — Biyo hetuBaye zuk

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.40"
SUTRA_TEXT = "भियो हेतुभये षुक्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Biyo hetuBaye zuk"


class Sutra7340:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.40: अग्निः'),
		('रामः', '', 'प.7.3.40: रामः'),
		('सीता', '', 'प.7.3.40: सीता'),
	]

