# Sutra प.8.1.9: एकं बहुव्रीहिवत्
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.9"
SUTRA_TEXT = "एकं बहुव्रीहिवत्"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra819:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.9: अग्निः'),
		('रामः', '', 'प.8.1.9: रामः'),
		('सीता', '', 'प.8.1.9: सीता'),
	]

