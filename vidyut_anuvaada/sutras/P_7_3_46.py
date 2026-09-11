# Sutra प.7.3.46: उदीचामातः स्थाने यकपूर्वायाः
# (Taddhita (secondary derivations)) — udIcAmAtaH sTAne yakapUrvAyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.46"
SUTRA_TEXT = "उदीचामातः स्थाने यकपूर्वायाः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — udIcAmAtaH sTAne yakapUrvAyAH"


class Sutra7346:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.46: अग्निः'),
		('रामः', '', 'प.7.3.46: रामः'),
		('सीता', '', 'प.7.3.46: सीता'),
	]

