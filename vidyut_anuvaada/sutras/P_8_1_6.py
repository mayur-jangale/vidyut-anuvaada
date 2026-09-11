# Sutra प.8.1.6: प्रसमुपोदः पादपूरणे
# ṅamo lopaḥ — elision of ङम्

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.6"
SUTRA_TEXT = "प्रसमुपोदः पादपूरणे"
SUTRA_DESC = "ṅamo lopaḥ — elision of ङम्"


class Sutra816:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.6: अग्निः'),
		('रामः', '', 'प.8.1.6: रामः'),
		('सीता', '', 'प.8.1.6: सीता'),
	]

