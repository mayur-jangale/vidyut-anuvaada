# Sutra प.2.4.13: विप्रतिषिद्धं चानधिकरणवाचि
# (Samasa (compound formation)) — vipratizidDaM cAnaDikaraRavAci

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.13"
SUTRA_TEXT = "विप्रतिषिद्धं चानधिकरणवाचि"
SUTRA_DESC = "(Samasa (compound formation)) — vipratizidDaM cAnaDikaraRavAci"


class Sutra2413:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

