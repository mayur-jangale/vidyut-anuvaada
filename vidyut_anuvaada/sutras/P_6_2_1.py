# Sutra प.6.2.1: बहुव्रीहौ प्रकृत्या पूर्वपदम्
# hal-sandhi — consonant-sandhi rules begin

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.1"
SUTRA_TEXT = "बहुव्रीहौ प्रकृत्या पूर्वपदम्"
SUTRA_DESC = "hal-sandhi — consonant-sandhi rules begin"


class Sutra621:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.1: अग्निः'),
		('रामः', '', 'प.6.2.1: रामः'),
		('सीता', '', 'प.6.2.1: सीता'),
	]

