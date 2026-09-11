# Sutra प.5.1.24: विंशतित्रिंशद्भ्यां ड्वुन्नसंज्ञायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — viMSatitriMSadByAM qvunnasaMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.24"
SUTRA_TEXT = "विंशतित्रिंशद्भ्यां ड्वुन्नसंज्ञायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — viMSatitriMSadByAM qvunnasaMjYAyAm"


class Sutra5124:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.24: अग्निः'),
		('रामः', '', 'प.5.1.24: रामः'),
		('सीता', '', 'प.5.1.24: सीता'),
	]

