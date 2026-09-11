# Sutra प.3.2.158: स्पृहिगृहिपतिदयिनिद्रातन्द्राश्रद्धाभ्य आलुच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — spfhigfhipatidayinidrAtandrASradDABya Aluc

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.158"
SUTRA_TEXT = "स्पृहिगृहिपतिदयिनिद्रातन्द्राश्रद्धाभ्य आलुच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — spfhigfhipatidayinidrAtandrASradDABya Aluc"


class Sutra32158:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

