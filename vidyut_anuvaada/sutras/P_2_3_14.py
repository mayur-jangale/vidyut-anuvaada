# Sutra प.2.3.14: क्रियार्थोपपदस्य च कर्मणि स्थानिनः
# (Samasa (compound formation)) — kriyArTopapadasya ca karmaRi sTAninaH

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.14"
SUTRA_TEXT = "क्रियार्थोपपदस्य च कर्मणि स्थानिनः"
SUTRA_DESC = "(Samasa (compound formation)) — kriyArTopapadasya ca karmaRi sTAninaH"


class Sutra2314:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

