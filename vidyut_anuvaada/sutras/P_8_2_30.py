# Sutra प.8.2.30: चोः कुः
# vibhāṣā senāsaṃyukteṣu — optional rules with army compounds

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.30"
SUTRA_TEXT = "चोः कुः"
SUTRA_DESC = "vibhāṣā senāsaṃyukteṣu — optional rules with army compounds"


class Sutra8230:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.30: अग्निः'),
		('रामः', '', 'प.8.2.30: रामः'),
		('सीता', '', 'प.8.2.30: सीता'),
	]

