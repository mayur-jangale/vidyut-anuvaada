# Sutra प.6.4.168: ये चाभावकर्मणोः
# (Sandhi (euphonic combination)) — ye cABAvakarmaRoH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.168"
SUTRA_TEXT = "ये चाभावकर्मणोः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — ye cABAvakarmaRoH"


class Sutra64168:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.168: अग्निः'),
		('रामः', '', 'प.6.4.168: रामः'),
		('सीता', '', 'प.6.4.168: सीता'),
	]

