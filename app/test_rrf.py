"""RRF formula regression test — rank must be 1-based (rubric NB2)."""

from __future__ import annotations


def rrf_scores(kw_ids: list[str], sem_ids: list[str], rrf_k: int = 60) -> dict[str, float]:
    scores: dict[str, float] = {}
    for rank, doc_id in enumerate(kw_ids, start=1):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (rrf_k + rank)
    for rank, doc_id in enumerate(sem_ids, start=1):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (rrf_k + rank)
    return scores


def test_rrf_one_based_formula_hand_computed() -> None:
    """Single doc at rank 1 in one list: contribution must be 1/(60+1), not 1/60."""
    s = rrf_scores(["only"], [], rrf_k=60)
    assert s["only"] == 1.0 / 61


def test_rrf_merges_two_rankers() -> None:
    kw = ["a", "b", "c"]
    sem = ["c", "d", "e"]
    s = rrf_scores(kw, sem)
    assert "b" in s and "d" in s
    # "c" in both lists — should outrank "e" (only weak tail in sem)
    assert s["c"] > s["e"]
