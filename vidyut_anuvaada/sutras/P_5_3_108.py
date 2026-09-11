# Sutra प.5.3.108: अङ्गुल्यादिभ्यष्ठक्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aNgulyAdiByazWak

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.108"
SUTRA_TEXT = "अङ्गुल्यादिभ्यष्ठक्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aNgulyAdiByazWak"


class Sutra53108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.108: अग्निः'),
		('रामः', '', 'प.5.3.108: रामः'),
		('सीता', '', 'प.5.3.108: सीता'),
	]

