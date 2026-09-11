# Sutra प.2.2.11: पूरणगुणसुहितार्थसदव्ययतव्यसमानाधिकरणेन
# (Samasa (compound formation)) — pUraRaguRasuhitArTasadavyayatavyasamAnADikaraRena

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.11"
SUTRA_TEXT = "पूरणगुणसुहितार्थसदव्ययतव्यसमानाधिकरणेन"
SUTRA_DESC = "(Samasa (compound formation)) — pUraRaguRasuhitArTasadavyayatavyasamAnADikaraRena"


class Sutra2211:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

