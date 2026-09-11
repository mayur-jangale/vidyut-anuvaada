# Sutra प.2.3.43: साधुनिपुणाभ्यामर्चायां सप्तम्यप्रतेः
# (Samasa (compound formation)) — sADunipuRAByAmarcAyAM saptamyaprateH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.43"
SUTRA_TEXT = "साधुनिपुणाभ्यामर्चायां सप्तम्यप्रतेः"
SUTRA_DESC = "(Samasa (compound formation)) — sADunipuRAByAmarcAyAM saptamyaprateH"


class Sutra2343:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

