# Sutra प.5.4.134: जायाया निङ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — jAyAyA niN

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.134"
SUTRA_TEXT = "जायाया निङ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — jAyAyA niN"


class Sutra54134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.134: अग्निः'),
		('रामः', '', 'प.5.4.134: रामः'),
		('सीता', '', 'प.5.4.134: सीता'),
	]

