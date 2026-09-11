# Sutra प.7.3.95: तुरुस्तुशम्यमः सार्वधातुके
# (Taddhita (secondary derivations)) — turustuSamyamaH sArvaDAtuke

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.95"
SUTRA_TEXT = "तुरुस्तुशम्यमः सार्वधातुके"
SUTRA_DESC = "(Taddhita (secondary derivations)) — turustuSamyamaH sArvaDAtuke"


class Sutra7395:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.95: अग्निः'),
		('रामः', '', 'प.7.3.95: रामः'),
		('सीता', '', 'प.7.3.95: सीता'),
	]

