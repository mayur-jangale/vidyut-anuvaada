# Sutra प.5.1.28: अध्यर्धपूर्वद्विगोर्लुगसंज्ञायाम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — aDyarDapUrvadvigorlugasaMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.28"
SUTRA_TEXT = "अध्यर्धपूर्वद्विगोर्लुगसंज्ञायाम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — aDyarDapUrvadvigorlugasaMjYAyAm"


class Sutra5128:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.28: अग्निः'),
		('रामः', '', 'प.5.1.28: रामः'),
		('सीता', '', 'प.5.1.28: सीता'),
	]

