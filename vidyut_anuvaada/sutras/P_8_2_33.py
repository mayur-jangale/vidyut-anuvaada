# Sutra प.8.2.33: वा द्रुहमुहष्णुहष्णिहाम्
# pūrvatrāsiddham — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.33"
SUTRA_TEXT = "वा द्रुहमुहष्णुहष्णिहाम्"
SUTRA_DESC = "pūrvatrāsiddham — repeated"


class Sutra8233:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.33: अग्निः'),
		('रामः', '', 'प.8.2.33: रामः'),
		('सीता', '', 'प.8.2.33: सीता'),
	]

