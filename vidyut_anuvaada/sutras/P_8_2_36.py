# Sutra प.8.2.36: व्रश्चभ्रस्जसृजमृजयजराजभ्राजच्छशां षः
# aparatvaṃ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.36"
SUTRA_TEXT = "व्रश्चभ्रस्जसृजमृजयजराजभ्राजच्छशां षः"
SUTRA_DESC = "aparatvaṃ — repeated"


class Sutra8236:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.36: अग्निः'),
		('रामः', '', 'प.8.2.36: रामः'),
		('सीता', '', 'प.8.2.36: सीता'),
	]

