# Sutra प.6.1.134: सोऽचि लोपे चेत् पादपूरणम्
# sandhi-sūtra प.6.1.134

from P_6_1 import apply_6_1_134

SUTRA_CODE = "प.6.1.134"
SUTRA_TEXT = "सोऽचि लोपे चेत् पादपूरणम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.134"


class Sutra61134:
	def apply(self, word, pos):
		return apply_6_1_134(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.134:input=अग्निः'),
		('रामः', '', '6.1.134:input=रामः'),
		('सीता', '', '6.1.134:input=सीता'),
	]
