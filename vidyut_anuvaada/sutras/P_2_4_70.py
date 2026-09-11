# Sutra प.2.4.70: आगस्त्यकौण्डिन्ययोरगस्तिकुण्डिनच्
# (Samasa (compound formation)) — AgastyakORqinyayoragastikuRqinac

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.70"
SUTRA_TEXT = "आगस्त्यकौण्डिन्ययोरगस्तिकुण्डिनच्"
SUTRA_DESC = "(Samasa (compound formation)) — AgastyakORqinyayoragastikuRqinac"


class Sutra2470:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

