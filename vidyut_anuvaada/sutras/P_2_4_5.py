# Sutra प.2.4.5: अध्ययनतोऽविप्रकृष्टाख्यानाम्
# (Samasa (compound formation)) — aDyayanato'viprakfzwAKyAnAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.5"
SUTRA_TEXT = "अध्ययनतोऽविप्रकृष्टाख्यानाम्"
SUTRA_DESC = "(Samasa (compound formation)) — aDyayanato'viprakfzwAKyAnAm"


class Sutra245:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

