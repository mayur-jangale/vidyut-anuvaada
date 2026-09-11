# Sutra प.3.4.84: ब्रुवः पञ्चानामादित आहो ब्रुवः
# lot — imperative endings

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.84"
SUTRA_TEXT = "ब्रुवः पञ्चानामादित आहो ब्रुवः"
SUTRA_DESC = "lot — imperative endings"


class Sutra3484:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

