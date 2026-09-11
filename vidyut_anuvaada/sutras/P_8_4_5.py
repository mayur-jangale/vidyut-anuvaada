# Sutra प.8.4.5: प्रनिरन्तःशरेक्षुप्लक्षाम्रकार्ष्यखदिरपीयूक्षाभ्योऽसंज्ञायामपि
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.5"
SUTRA_TEXT = "प्रनिरन्तःशरेक्षुप्लक्षाम्रकार्ष्यखदिरपीयूक्षाभ्योऽसंज्ञायामपि"
SUTRA_DESC = "final transformations — continued"


class Sutra845:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.5: अग्निः'),
		('रामः', '', 'प.8.4.5: रामः'),
		('सीता', '', 'प.8.4.5: सीता'),
	]

