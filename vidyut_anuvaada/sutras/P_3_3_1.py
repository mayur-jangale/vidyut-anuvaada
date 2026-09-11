# Sutra प.3.3.1: उणादयो बहुलम्
# kṛdartha — kṛdanta has specific meaning in context

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.1"
SUTRA_TEXT = "उणादयो बहुलम्"
SUTRA_DESC = "kṛdartha — kṛdanta has specific meaning in context"


class Sutra331:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

