# Sutra प.2.4.37: लुङ्सनोर्घसॢ
# (Samasa (compound formation)) — luNsanorGasx

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.37"
SUTRA_TEXT = "लुङ्सनोर्घसॢ"
SUTRA_DESC = "(Samasa (compound formation)) — luNsanorGasx"


class Sutra2437:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

