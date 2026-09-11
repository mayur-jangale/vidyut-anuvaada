# Sutra प.2.3.70: अकेनोर्भविष्यदाधमर्ण्ययोः
# (Samasa (compound formation)) — akenorBavizyadADamarRyayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.70"
SUTRA_TEXT = "अकेनोर्भविष्यदाधमर्ण्ययोः"
SUTRA_DESC = "(Samasa (compound formation)) — akenorBavizyadADamarRyayoH"


class Sutra2370:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

