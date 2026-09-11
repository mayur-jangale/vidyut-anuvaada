# Sutra प.5.2.124: वाचो ग्मिनिः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vAco gminiH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.124"
SUTRA_TEXT = "वाचो ग्मिनिः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vAco gminiH"


class Sutra52124:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.124: अग्निः'),
		('रामः', '', 'प.5.2.124: रामः'),
		('सीता', '', 'प.5.2.124: सीता'),
	]

