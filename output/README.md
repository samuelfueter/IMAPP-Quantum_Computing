# Corrected and completed lecture notes

Source: `../Lecture_Notes_2026-2027.pdf` (C. Kriegler, *Quantum Computing for Data Science DU*, UCA, Nov. 2026).

| File | Content |
|---|---|
| `Lecture_Notes_2026-2027_corrected.tex` | LaTeX source of the corrected and completed notes (single file) |
| `Lecture_Notes_2026-2027_corrected.pdf` | Compiled PDF (36 pages) |
| `verify_solutions.py` | Numerical checks of every computed exercise answer (`python3 verify_solutions.py`, needs numpy) |

## What was done
* The original numbering is kept (Def. 1.1 … Ex. 8.6). New auxiliary results get a letter suffix (Lemma 1.7a, 1.19a, 6.1a, 8.1a; Thm 8.7, Ex. 8.8).
* **Red boxes** explain each mistake. The statement in the main text is already the corrected one. A full errata table (34 entries) is on pp. 2–3 of the PDF.
* **Blue boxes** fill gaps: proofs that were omitted or only announced. These include Cauchy–Schwarz, Riesz, the adjoint, Gram–Schmidt, the tensor scalar product, the spectral theorem, the exponential law, uniqueness for the ODE, density matrices, the Bloch ball, the SNCF metric and Moore–Aronszajn.
* Every exercise has a full solution.

## Most important mathematical errors in the original
1. Ex. 1.12: the summation index is wrong, `Σ_k conj(x_n) y_n` → `Σ_k conj(x_k) y_k`.
2. Ex. 3.4: the variable defined there is *binomial* B(n,p), not "Bernoulli".
3. Def. 3.11: the expectation needs *absolute* convergence.
4. Prop. 4.1: `a_ij = <T e_j, f_i>` gives the complex conjugate. The correct formula is `a_ij = <f_i, T e_j>`.
5. Proof of Prop. 5.7: a factor `A` is lost in the estimate, so the bound is `|h| ||A||² e^{|h| ||A||}`. There is also a broken reference ("Lemma ??"), and `e^{hA}` is used for `h<0` although it is only defined for `t ≥ 0`.
6. Proof of Prop. 6.3: "positive definite" should be "positive *semi*-definite". The matrix of `T_x = |x><x|` is `(x_i conj(x_j))`, not `(conj(x_i) x_j)`.
7. Ex. 6.5 has three errors:
   * the printed A is not `T_x + T_y` (wrong sign of `a_12`);
   * `T_x + T_y` is singular, so it is only positive *semi*-definite;
   * the state must be `Φ(B) = tr(AB)/8` with values in ℂ, so `Φ(M) = 1/8`.
8. Def. 8.1: for positive definiteness the points must be pairwise distinct.

## Build
```
latexmk -pdf Lecture_Notes_2026-2027_corrected.tex
```
(packages: amsmath/amssymb/amsthm, mathtools, enumitem, longtable, booktabs, xcolor, tcolorbox, hyperref, lmodern)
