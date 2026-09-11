# Sutra प.8.2.70: अम्नरूधरवरित्युभयथा छन्दसि
# (Final transformations (tripāḍī)) — amnarUDaravarityuBayaTA Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.70"
SUTRA_TEXT = "अम्नरूधरवरित्युभयथा छन्दसि"
SUTRA_DESC = "(Final transformations (tripāḍī)) — amnarUDaravarityuBayaTA Candasi"


class Sutra8270:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.70: अग्निः'),
		('रामः', '', 'प.8.2.70: रामः'),
		('सीता', '', 'प.8.2.70: सीता'),
	]

