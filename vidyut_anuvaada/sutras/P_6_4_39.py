# Sutra प.6.4.39: न क्तिचि दीर्घश्च
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.39"
SUTRA_TEXT = "न क्तिचि दीर्घश्च"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6439:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.39: अग्निः'),
		('रामः', '', 'प.6.4.39: रामः'),
		('सीता', '', 'प.6.4.39: सीता'),
	]

