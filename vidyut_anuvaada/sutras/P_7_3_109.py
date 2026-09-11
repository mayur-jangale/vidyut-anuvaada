# Sutra प.7.3.109: जसि च
# (Taddhita (secondary derivations)) — jasi ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.109"
SUTRA_TEXT = "जसि च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — jasi ca"


class Sutra73109:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.109: अग्निः'),
		('रामः', '', 'प.7.3.109: रामः'),
		('सीता', '', 'प.7.3.109: सीता'),
	]

