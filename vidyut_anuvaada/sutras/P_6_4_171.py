# Sutra प.6.4.171: ब्राह्मोऽजातौ
# (Sandhi (euphonic combination)) — brAhmo'jAtO

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.171"
SUTRA_TEXT = "ब्राह्मोऽजातौ"
SUTRA_DESC = "(Sandhi (euphonic combination)) — brAhmo'jAtO"


class Sutra64171:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.171: अग्निः'),
		('रामः', '', 'प.6.4.171: रामः'),
		('सीता', '', 'प.6.4.171: सीता'),
	]

