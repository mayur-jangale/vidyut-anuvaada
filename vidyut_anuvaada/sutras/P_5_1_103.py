# Sutra प.5.1.103: कर्मण उकञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — karmaRa ukaY

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.103"
SUTRA_TEXT = "कर्मण उकञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — karmaRa ukaY"


class Sutra51103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.103: अग्निः'),
		('रामः', '', 'प.5.1.103: रामः'),
		('सीता', '', 'प.5.1.103: सीता'),
	]

