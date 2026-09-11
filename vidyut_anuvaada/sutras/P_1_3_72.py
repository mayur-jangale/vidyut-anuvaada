# Sutra प.1.3.72: स्वरितञितः कर्त्रभिप्राये क्रियाफले
from P_1_3 import apply_1_3_72


class Sutra1372:
	def apply(self, word, pos):
		return apply_1_3_72(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'svaritaYitaH-kartraBiprAye-kriyAPale:अग्निः;not-applicable'),
		('रामः', '', 'svaritaYitaH-kartraBiprAye-kriyAPale:रामः;not-applicable'),
		('सीता', '', 'svaritaYitaH-kartraBiprAye-kriyAPale:सीता;not-applicable'),
	]

