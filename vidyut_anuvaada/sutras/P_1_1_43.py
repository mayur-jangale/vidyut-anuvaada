# Sutra प.1.1.43: सुडनपुंसकस्य
# (Samjna (technical definitions)) — suqanapuMsakasya

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.43"
SUTRA_TEXT = "सुडनपुंसकस्य"
SUTRA_DESC = "(Samjna (technical definitions)) — suqanapuMsakasya"


class Sutra1143:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_43
		return apply_1_1_43(word, pos)

	EXAMPLES = [
		('सुट्', '', 'प.1.1.43:suḍ-anapuṃsakasya;input=सुट्'),
		('अग्नि', '', 'प.1.1.43:suḍ-anapuṃsakasya;input=अग्नि'),
	]

