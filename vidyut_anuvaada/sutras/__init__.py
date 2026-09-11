"""vidyut-anuvaada sutras package -- Panini Ashtadhyayi sutra engine.

The engine discovers all chapter modules at runtime via
``SutraEngine`` / ``_load_sutra_table``. Consolidated chapter files
(P_1_1 through P_8_4) are *not* eagerly imported here because several
use bare intra-package imports that require the sutras directory on
``sys.path`` (handled by the runtime loader).

Exports
-------
- ``apply_general`` -- fallback sutra-applier (used by individual sutra files)
- ``SutraEngine`` -- high-level sutra-lookup orchestrator
"""
from __future__ import annotations

from vidyut_anuvaada.sutras.sutra_engines import apply_general, SutraEngine
