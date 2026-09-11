# Sutra प.1.1.68: स्वं रूपं शब्दस्याशब्दसंज्ञा
# (Samjna (technical definitions)) — svaM rUpaM SabdasyASabdasaMjYA

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.68"
SUTRA_TEXT = "स्वं रूपं शब्दस्याशब्दसंज्ञा"
SUTRA_DESC = "(Samjna (technical definitions)) — svaM rUpaM SabdasyASabdasaMjYA"


class Sutra1168:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_68
		return apply_1_1_68(word, pos)

	EXAMPLES = [
		('स्वरूप', '', 'प.1.1.68:svaṃ-rūpaṃ-śabdasya-āśabda-saṃjñā;input=स्वरूप'),
		('अग्नि', '', 'प.1.1.68:svaṃ-rūpaṃ-śabdasya-āśabda-saṃjñā;input=अग्नि'),
	]

