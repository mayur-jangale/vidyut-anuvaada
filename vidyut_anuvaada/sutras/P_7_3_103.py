# Sutra प.7.3.103: बहुवचने झल्येत्
# (Taddhita (secondary derivations)) — bahuvacane Jalyet

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.103"
SUTRA_TEXT = "बहुवचने झल्येत्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — bahuvacane Jalyet"


class Sutra73103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.103: अग्निः'),
		('रामः', '', 'प.7.3.103: रामः'),
		('सीता', '', 'प.7.3.103: सीता'),
	]

