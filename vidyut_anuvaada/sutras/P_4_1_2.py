# Sutra प.4.1.2: स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्भ्यस्ङसोसाङ्ङ्योस्सुप्
# sup-sthāna — add appropriate sup ending for vibhakti/vacana

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.2"
SUTRA_TEXT = "स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्भ्यस्ङसोसाङ्ङ्योस्सुप्"
SUTRA_DESC = "sup-sthāna — add appropriate sup ending for vibhakti/vacana"


class Sutra412:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

