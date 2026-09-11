# Sutra प.3.4.72: गत्यर्थाकर्मकश्लिषशीङ्स्थाऽऽसवसजनरुहजीर्यतिभ्यश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — gatyarTAkarmakaSlizaSINsTA''savasajanaruhajIryatiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.72"
SUTRA_TEXT = "गत्यर्थाकर्मकश्लिषशीङ्स्थाऽऽसवसजनरुहजीर्यतिभ्यश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — gatyarTAkarmakaSlizaSINsTA''savasajanaruhajIryatiByaSca"


class Sutra3472:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

