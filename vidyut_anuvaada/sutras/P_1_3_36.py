# Sutra प.1.3.36: सम्माननोत्सञ्जनाचार्यकरणज्ञानभृतिविगणनव्ययेषु नियः
from P_1_3 import apply_1_3_36


class Sutra1336:
	def apply(self, word, pos):
		return apply_1_3_36(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_36:अग्निः'),
		('रामः', '', 'sutra_36:रामः'),
		('सीता', '', 'sutra_36:सीता'),
	]

