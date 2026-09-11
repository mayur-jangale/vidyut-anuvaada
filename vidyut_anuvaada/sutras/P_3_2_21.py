# Sutra प.3.2.21: दिवाविभानिशाप्रभाभास्कारान्तानन्तादिबहुनान्दीकिम्लिपिलिबिबलिभक्तिकर्तृचित्रक्षेत्रसंख्याजङ्घाबाह्वहर्यत्तत्धनुररुष्षु
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — divAviBAniSApraBABAskArAntAnantAdibahunAndIkimlipilibibaliBaktikartfcitrakzetrasaMKyAjaNGAbAhvaharyattatDanuraruzzu

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.21"
SUTRA_TEXT = "दिवाविभानिशाप्रभाभास्कारान्तानन्तादिबहुनान्दीकिम्लिपिलिबिबलिभक्तिकर्तृचित्रक्षेत्रसंख्याजङ्घाबाह्वहर्यत्तत्धनुररुष्षु"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — divAviBAniSApraBABAskArAntAnantAdibahunAndIkimlipilibibaliBaktikartfcitrakzetrasaMKyAjaNGAbAhvaharyattatDanuraruzzu"


class Sutra3221:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

