# Sutra प.6.1.170: अञ्चेश्छन्दस्यसर्वनामस्थानम्
# sandhi-sūtra प.6.1.170

from P_6_1 import apply_6_1_170

SUTRA_CODE = "प.6.1.170"
SUTRA_TEXT = "अञ्चेश्छन्दस्यसर्वनामस्थानम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.170"


class Sutra61170:
	def apply(self, word, pos):
		return apply_6_1_170(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.170:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.170:marker=padartha;input=रामः'),
		('सीता', '', '6.1.170:marker=padartha;input=सीता'),
	]
