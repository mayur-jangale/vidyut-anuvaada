# Sutra प.6.2.191: अतेरकृत्पदे
# (Sandhi (euphonic combination)) — aterakftpade

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.191"
SUTRA_TEXT = "अतेरकृत्पदे"
SUTRA_DESC = "(Sandhi (euphonic combination)) — aterakftpade"


class Sutra62191:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.191: अग्निः'),
		('रामः', '', 'प.6.2.191: रामः'),
		('सीता', '', 'प.6.2.191: सीता'),
	]

