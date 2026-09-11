# Sutra प.5.3.104: द्रव्यं च भव्ये
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dravyaM ca Bavye

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.104"
SUTRA_TEXT = "द्रव्यं च भव्ये"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dravyaM ca Bavye"


class Sutra53104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.104: अग्निः'),
		('रामः', '', 'प.5.3.104: रामः'),
		('सीता', '', 'प.5.3.104: सीता'),
	]

