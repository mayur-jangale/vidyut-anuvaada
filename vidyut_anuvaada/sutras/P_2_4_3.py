# Sutra प.2.4.3: अनुवादे चरणानाम्
# (Samasa (compound formation)) — anuvAde caraRAnAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.3"
SUTRA_TEXT = "अनुवादे चरणानाम्"
SUTRA_DESC = "(Samasa (compound formation)) — anuvAde caraRAnAm"


class Sutra243:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

