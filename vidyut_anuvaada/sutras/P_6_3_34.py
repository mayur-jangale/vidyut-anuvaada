# Sutra प.6.3.34: स्त्रियाः पुंवद्भाषितपुंस्कादनूङ् समानाधिकरणे स्त्रियामपूरणीप्रियाऽऽदिषु
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.34"
SUTRA_TEXT = "स्त्रियाः पुंवद्भाषितपुंस्कादनूङ् समानाधिकरणे स्त्रियामपूरणीप्रियाऽऽदिषु"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6334:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.34: अग्निः'),
		('रामः', '', 'प.6.3.34: रामः'),
		('सीता', '', 'प.6.3.34: सीता'),
	]

