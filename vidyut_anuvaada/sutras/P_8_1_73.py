# Sutra प.8.1.73: नामन्त्रिते समानाधिकरणे सामान्यवचनम्
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.73"
SUTRA_TEXT = "नामन्त्रिते समानाधिकरणे सामान्यवचनम्"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8173:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.73: अग्निः'),
		('रामः', '', 'प.8.1.73: रामः'),
		('सीता', '', 'प.8.1.73: सीता'),
	]

