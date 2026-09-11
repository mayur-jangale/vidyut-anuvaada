# Sutra प.1.3.67: णेरणौ यत्कर्म णौ चेत् स कर्ताऽनाध्याने
from P_1_3 import apply_1_3_67


class Sutra1367:
	def apply(self, word, pos):
		return apply_1_3_67(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_67:अग्निः'),
		('रामः', '', 'sutra_67:रामः'),
		('सीता', '', 'sutra_67:सीता'),
	]

