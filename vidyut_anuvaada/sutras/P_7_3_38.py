# Sutra प.7.3.38: वो विधूनने जुक्
# (Taddhita (secondary derivations)) — vo viDUnane juk

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.38"
SUTRA_TEXT = "वो विधूनने जुक्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — vo viDUnane juk"


class Sutra7338:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.38: अग्निः'),
		('रामः', '', 'प.7.3.38: रामः'),
		('सीता', '', 'प.7.3.38: सीता'),
	]

