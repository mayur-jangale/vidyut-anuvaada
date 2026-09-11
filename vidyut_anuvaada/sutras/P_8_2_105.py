# Sutra प.8.2.105: अनन्त्यस्यापि प्रश्नाख्यानयोः
# (Final transformations (tripāḍī)) — anantyasyApi praSnAKyAnayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.105"
SUTRA_TEXT = "अनन्त्यस्यापि प्रश्नाख्यानयोः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — anantyasyApi praSnAKyAnayoH"


class Sutra82105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.105: अग्निः'),
		('रामः', '', 'प.8.2.105: रामः'),
		('सीता', '', 'प.8.2.105: सीता'),
	]

