# Sutra प.1.1.4: न धातुलोप आर्धधातुके
# A root ending in ṛ/ḷ (lṛdhātu) does not undergo elision before ardhādhātuka suffixes

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.4"
SUTRA_TEXT = "न धातुलोप आर्धधातुके"
SUTRA_DESC = "A root ending in ṛ/ḷ (lṛdhātu) does not undergo elision before ardhādhātuka suffixes"


class Sutra114:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_4
		return apply_1_1_4(word, pos)

	EXAMPLES = [
		('गमृ', '', 'lṛdhātu-keeps-ending:गमृ'),
		('पच', '', 'regular-root:पच'),
	]

