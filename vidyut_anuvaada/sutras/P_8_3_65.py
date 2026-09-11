# Sutra प.8.3.65: उपसर्गात् सुनोतिसुवतिस्यतिस्तौतिस्तोभतिस्थासेनयसेधसिचसञ्जस्वञ्जाम्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.65"
SUTRA_TEXT = "उपसर्गात् सुनोतिसुवतिस्यतिस्तौतिस्तोभतिस्थासेनयसेधसिचसञ्जस्वञ्जाम्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8365:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.65: अग्निः'),
		('रामः', '', 'प.8.3.65: रामः'),
		('सीता', '', 'प.8.3.65: सीता'),
	]

