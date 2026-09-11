# Sutra प.5.4.11: किमेत्तिङव्ययघादाम्वद्रव्यप्रकर्षे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kimettiNavyayaGAdAmvadravyaprakarze

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.11"
SUTRA_TEXT = "किमेत्तिङव्ययघादाम्वद्रव्यप्रकर्षे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kimettiNavyayaGAdAmvadravyaprakarze"


class Sutra5411:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.11: अग्निः'),
		('रामः', '', 'प.5.4.11: रामः'),
		('सीता', '', 'प.5.4.11: सीता'),
	]

