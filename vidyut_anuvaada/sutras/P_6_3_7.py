# Sutra प.6.3.7: वैयाकरणाख्यायां चतुर्थ्याः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.7"
SUTRA_TEXT = "वैयाकरणाख्यायां चतुर्थ्याः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra637:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.7: अग्निः'),
		('रामः', '', 'प.6.3.7: रामः'),
		('सीता', '', 'प.6.3.7: सीता'),
	]

