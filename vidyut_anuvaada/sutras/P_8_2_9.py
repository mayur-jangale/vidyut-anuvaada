# Sutra प.8.2.9: मादुपधायाश्च मतोर्वोऽयवादिभ्यः
# paraḥ paraṃ — each later rule applies to prior

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.9"
SUTRA_TEXT = "मादुपधायाश्च मतोर्वोऽयवादिभ्यः"
SUTRA_DESC = "paraḥ paraṃ — each later rule applies to prior"


class Sutra829:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.9: अग्निः'),
		('रामः', '', 'प.8.2.9: रामः'),
		('सीता', '', 'प.8.2.9: सीता'),
	]

