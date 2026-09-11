# Sutra प.7.1.42: ध्वमो ध्वात्
# (Taddhita (secondary derivations)) — Dvamo DvAt

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.42"
SUTRA_TEXT = "ध्वमो ध्वात्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Dvamo DvAt"


class Sutra7142:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.42: अग्निः'),
		('रामः', '', 'प.7.1.42: रामः'),
		('सीता', '', 'प.7.1.42: सीता'),
	]

