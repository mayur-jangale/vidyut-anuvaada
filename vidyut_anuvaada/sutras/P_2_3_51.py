# Sutra प.2.3.51: ज्ञोऽविदर्थस्य करणे
# (Samasa (compound formation)) — jYo'vidarTasya karaRe

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.51"
SUTRA_TEXT = "ज्ञोऽविदर्थस्य करणे"
SUTRA_DESC = "(Samasa (compound formation)) — jYo'vidarTasya karaRe"


class Sutra2351:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

