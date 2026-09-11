# Sutra प.1.4.90: लक्षणेत्थम्भूताख्यानभागवीप्सासु प्रतिपर्यनवः
# (Samjna (technical definitions)) — lakzaRetTamBUtAKyAnaBAgavIpsAsu pratiparyanavaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.90"
SUTRA_TEXT = "लक्षणेत्थम्भूताख्यानभागवीप्सासु प्रतिपर्यनवः"
SUTRA_DESC = "(Samjna (technical definitions)) — lakzaRetTamBUtAKyAnaBAgavIpsAsu pratiparyanavaH"


class Sutra1490:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_90
		return apply_1_4_90(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-pratipar-context:अग्निः'),
		('रामः', '', 'not-pratipar-context:रामः'),
		('सीता', '', 'not-pratipar-context:सीता'),
	]

