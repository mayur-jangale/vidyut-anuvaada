# Sutra प.6.3.75: नभ्राण्नपान्नवेदानासत्यानमुचिनकुलनखनपुंसकनक्षत्रनक्रनाकेषु प्रकृत्या
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.75"
SUTRA_TEXT = "नभ्राण्नपान्नवेदानासत्यानमुचिनकुलनखनपुंसकनक्षत्रनक्रनाकेषु प्रकृत्या"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6375:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.75: अग्निः'),
		('रामः', '', 'प.6.3.75: रामः'),
		('सीता', '', 'प.6.3.75: सीता'),
	]

