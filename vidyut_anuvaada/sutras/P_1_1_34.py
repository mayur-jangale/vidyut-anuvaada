# Sutra प.1.1.34: पूर्वपरावरदक्षिणोत्तरापराधराणि व्यवस्थायामसंज्ञायाम्
# (Samjna (technical definitions)) — pUrvaparAvaradakziRottarAparADarARi vyavasTAyAmasaMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.34"
SUTRA_TEXT = "पूर्वपरावरदक्षिणोत्तरापराधराणि व्यवस्थायामसंज्ञायाम्"
SUTRA_DESC = "(Samjna (technical definitions)) — pUrvaparAvaradakziRottarAparADarARi vyavasTAyAmasaMjYAyAm"


class Sutra1134:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_34
		return apply_1_1_34(word, pos)

	EXAMPLES = [
		('पूर्व', '', 'दिक्-keyword=yes:पूर्व'),
		('दक्षिण', '', 'दिक्-keyword=yes:दक्षिण'),
		('उत्तर', '', 'दिक्-keyword=yes:उत्तर'),
		('देव', '', 'दिक्-keyword=no:देव'),
	]

