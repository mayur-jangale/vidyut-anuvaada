# Sutra प.5.1.122: पृथ्वादिभ्य इमनिज्वा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pfTvAdiBya imanijvA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.122"
SUTRA_TEXT = "पृथ्वादिभ्य इमनिज्वा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pfTvAdiBya imanijvA"


class Sutra51122:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.122: अग्निः'),
		('रामः', '', 'प.5.1.122: रामः'),
		('सीता', '', 'प.5.1.122: सीता'),
	]

