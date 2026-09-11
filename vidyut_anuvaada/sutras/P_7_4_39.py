# Sutra प.7.4.39: कव्यध्वरपृतनस्यर्चि लोपः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.39"
SUTRA_TEXT = "कव्यध्वरपृतनस्यर्चि लोपः"
SUTRA_DESC = "taddhita — continued"


class Sutra7439:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.39: अग्निः'),
		('रामः', '', 'प.7.4.39: रामः'),
		('सीता', '', 'प.7.4.39: सीता'),
	]

