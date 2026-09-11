# Sutra प.7.3.47: भस्त्रैषाऽजाज्ञाद्वास्वानञ्पूर्वाणामपि
# (Taddhita (secondary derivations)) — BastrEzA'jAjYAdvAsvAnaYpUrvARAmapi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.47"
SUTRA_TEXT = "भस्त्रैषाऽजाज्ञाद्वास्वानञ्पूर्वाणामपि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — BastrEzA'jAjYAdvAsvAnaYpUrvARAmapi"


class Sutra7347:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.47: अग्निः'),
		('रामः', '', 'प.7.3.47: रामः'),
		('सीता', '', 'प.7.3.47: सीता'),
	]

