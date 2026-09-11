# Sutra प.3.4.78: तिप्तस्झिसिप्थस्थमिब्वस्मस् तातांझथासाथांध्वमिड्वहिमहिङ्
# tiṅ — the 18 verbal endings ( तिप्, तस्, झि, etc.)

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.78"
SUTRA_TEXT = "तिप्तस्झिसिप्थस्थमिब्वस्मस् तातांझथासाथांध्वमिड्वहिमहिङ्"
SUTRA_DESC = "tiṅ — the 18 verbal endings ( तिप्, तस्, झि, etc.)"


class Sutra3478:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

