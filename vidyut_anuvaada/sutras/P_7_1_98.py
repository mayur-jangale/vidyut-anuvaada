# Sutra प.7.1.98: चतुरनडुहोरामुदात्तः
# (Taddhita (secondary derivations)) — caturanaquhorAmudAttaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.98"
SUTRA_TEXT = "चतुरनडुहोरामुदात्तः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — caturanaquhorAmudAttaH"


class Sutra7198:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.98: अग्निः'),
		('रामः', '', 'प.7.1.98: रामः'),
		('सीता', '', 'प.7.1.98: सीता'),
	]

