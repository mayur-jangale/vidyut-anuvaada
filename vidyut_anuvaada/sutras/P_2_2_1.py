# Sutra प.2.2.1: पूर्वापराधरोत्तरमेकदेशिनैकाधिकरणे
# (Samasa (compound formation)) — pUrvAparADarottaramekadeSinEkADikaraRe

from sutra_engines import apply_general

SUTRA_CODE = "प.2.2.1"
SUTRA_TEXT = "पूर्वापराधरोत्तरमेकदेशिनैकाधिकरणे"
SUTRA_DESC = "(Samasa (compound formation)) — pUrvAparADarottaramekadeSinEkADikaraRe"


class Sutra221:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

