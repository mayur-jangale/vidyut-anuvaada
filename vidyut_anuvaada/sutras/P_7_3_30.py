# Sutra प.7.3.30: नञः शुचीश्वरक्षेत्रज्ञकुशलनिपुणानाम्
# (Taddhita (secondary derivations)) — naYaH SucISvarakzetrajYakuSalanipuRAnAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.30"
SUTRA_TEXT = "नञः शुचीश्वरक्षेत्रज्ञकुशलनिपुणानाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — naYaH SucISvarakzetrajYakuSalanipuRAnAm"


class Sutra7330:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.30: अग्निः'),
		('रामः', '', 'प.7.3.30: रामः'),
		('सीता', '', 'प.7.3.30: सीता'),
	]

