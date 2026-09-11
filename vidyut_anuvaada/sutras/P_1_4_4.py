# Sutra प.1.4.4: नेयङुवङ्स्थानावस्त्री
# (Samjna (technical definitions)) — neyaNuvaNsTAnAvastrI

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.4"
SUTRA_TEXT = "नेयङुवङ्स्थानावस्त्री"
SUTRA_DESC = "(Samjna (technical definitions)) — neyaNuvaNsTAnAvastrI"


class Sutra144:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_4
		return apply_1_4_4(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'maybe-stri:अग्निः'),
		('रामः', '', 'maybe-stri:रामः'),
		('सीता', '', 'maybe-stri:सीता'),
	]

