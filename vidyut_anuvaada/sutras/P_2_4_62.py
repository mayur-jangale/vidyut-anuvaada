# Sutra प.2.4.62: तद्राजस्य बहुषु तेनैवास्त्रियाम्
# (Samasa (compound formation)) — tadrAjasya bahuzu tenEvAstriyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.62"
SUTRA_TEXT = "तद्राजस्य बहुषु तेनैवास्त्रियाम्"
SUTRA_DESC = "(Samasa (compound formation)) — tadrAjasya bahuzu tenEvAstriyAm"


class Sutra2462:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

