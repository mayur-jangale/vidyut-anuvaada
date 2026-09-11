# Sutra प.5.2.130: वयसि पूरणात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vayasi pUraRAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.130"
SUTRA_TEXT = "वयसि पूरणात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vayasi pUraRAt"


class Sutra52130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.130: अग्निः'),
		('रामः', '', 'प.5.2.130: रामः'),
		('सीता', '', 'प.5.2.130: सीता'),
	]

