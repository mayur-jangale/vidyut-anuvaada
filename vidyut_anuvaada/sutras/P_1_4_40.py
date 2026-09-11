# Sutra प.1.4.40: प्रत्याङ्भ्यां श्रुवः पूर्वस्य कर्ता
# (Samjna (technical definitions)) — pratyANByAM SruvaH pUrvasya kartA

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.40"
SUTRA_TEXT = "प्रत्याङ्भ्यां श्रुवः पूर्वस्य कर्ता"
SUTRA_DESC = "(Samjna (technical definitions)) — pratyANByAM SruvaH pUrvasya kartA"


class Sutra1440:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_40
		return apply_1_4_40(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-SruvaH-kartA:अग्निः'),
		('रामः', '', 'not-SruvaH-kartA:रामः'),
		('सीता', '', 'not-SruvaH-kartA:सीता'),
	]

