# Sutra प.1.4.76: मध्ये पदे निवचने च
# (Samjna (technical definitions)) — maDye pade nivacane ca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.76"
SUTRA_TEXT = "मध्ये पदे निवचने च"
SUTRA_DESC = "(Samjna (technical definitions)) — maDye pade nivacane ca"


class Sutra1476:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_76
		return apply_1_4_76(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-maDya-nivacana:अग्निः'),
		('रामः', '', 'not-maDya-nivacana:रामः'),
		('सीता', '', 'not-maDya-nivacana:सीता'),
	]

