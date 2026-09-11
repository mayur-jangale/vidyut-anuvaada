# Sutra प.3.1.141: श्याद्व्यधास्रुसंस्र्वतीणवसाऽवहृलिहश्लिषश्वसश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — SyAdvyaDAsrusaMsrvatIRavasA'vahflihaSlizaSvasaSca

from P_3_1 import apply_3_1_141

SUTRA_CODE = "प.3.1.141"
SUTRA_TEXT = "श्याद्व्यधास्रुसंस्र्वतीणवसाऽवहृलिहश्लिषश्वसश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — SyAdvyaDAsrusaMsrvatIRavasA'vahflihaSlizaSvasaSca"


class Sutra31141:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_141(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.141:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.141:root=रामः;pos='),
		('सीता', '', 'प.3.1.141:root=सीता;pos='),
	]

