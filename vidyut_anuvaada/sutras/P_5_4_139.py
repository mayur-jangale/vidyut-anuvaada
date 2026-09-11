# Sutra प.5.4.139: कुम्भपदीषु च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kumBapadIzu ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.139"
SUTRA_TEXT = "कुम्भपदीषु च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kumBapadIzu ca"


class Sutra54139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.139: अग्निः'),
		('रामः', '', 'प.5.4.139: रामः'),
		('सीता', '', 'प.5.4.139: सीता'),
	]

