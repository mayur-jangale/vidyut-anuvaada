# Sutra प.5.3.113: व्रातच्फञोरस्त्रियाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vrAtacPaYorastriyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.113"
SUTRA_TEXT = "व्रातच्फञोरस्त्रियाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vrAtacPaYorastriyAm"


class Sutra53113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.113: अग्निः'),
		('रामः', '', 'प.5.3.113: रामः'),
		('सीता', '', 'प.5.3.113: सीता'),
	]

