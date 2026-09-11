# Sutra प.5.1.96: तत्र च दीयते कार्यं भववत्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tatra ca dIyate kAryaM Bavavat

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.96"
SUTRA_TEXT = "तत्र च दीयते कार्यं भववत्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tatra ca dIyate kAryaM Bavavat"


class Sutra5196:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.96: अग्निः'),
		('रामः', '', 'प.5.1.96: रामः'),
		('सीता', '', 'प.5.1.96: सीता'),
	]

