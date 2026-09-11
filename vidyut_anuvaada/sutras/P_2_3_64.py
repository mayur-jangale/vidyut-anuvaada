# Sutra प.2.3.64: कृत्वोऽर्थप्रयोगे कालेऽधिकरणे
# (Samasa (compound formation)) — kftvo'rTaprayoge kAle'DikaraRe

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.64"
SUTRA_TEXT = "कृत्वोऽर्थप्रयोगे कालेऽधिकरणे"
SUTRA_DESC = "(Samasa (compound formation)) — kftvo'rTaprayoge kAle'DikaraRe"


class Sutra2364:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

