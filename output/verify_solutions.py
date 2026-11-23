"""Numerical sanity checks for the exercise solutions in
Lecture_Notes_2026-2027_corrected.tex (requires numpy only).
Run:  python3 verify_solutions.py
"""
import numpy as np

ip = np.vdot  # <x,y> = sum conj(x_k) y_k  (anti-linear in the first slot)
ok = lambda name, cond: print(f"[{'OK' if cond else 'FAIL'}] {name}")

# Ex 1.13
x, y, z = np.array([2, 1, -1]), np.array([-1, 1, 1j]), np.array([2, 1j, 0])
ok("1.13 <x,y>=-1-i, <y,z>=-2+i, <z,x>=4-i",
   np.allclose([ip(x, y), ip(y, z), ip(z, x)], [-1 - 1j, -2 + 1j, 4 - 1j]))
ok("1.13 norms sqrt6, sqrt3, sqrt5",
   np.allclose([np.linalg.norm(v) for v in (x, y, z)], np.sqrt([6, 3, 5])))
# Ex 1.24
ok("1.24 |phi><psi|xi> = (4,-2,0)",
   np.allclose(ip([5, 1, -1], [1, 0, 3]) * np.array([2, -1, 0]), [4, -2, 0]))
# Ex 2.7
r = np.kron([1, 2, 1], [2, 0, -1]) + np.kron([1, 1, 2], [3, 0, 2])
s = np.kron([1, -1, -1], [2, 1, 0])
ok("2.7 <r,s> = -20", r @ s == -20)
# Ex 4.2
ok("4.2 matrix of |phi><psi|",
   np.array_equal(np.outer([1, 2, -1], [0, 3, 2]), [[0, 3, 2], [0, 6, 4], [0, -3, -2]]))
# Ex 4.13
A = np.array([[1, -2/3, -2/3], [-2/3, 2/3, 0], [-2/3, 0, 4/3]])
U = np.array([[1, 2, 2], [-2, -1, 2], [2, -2, 1]]) / 3
D = np.diag([1, 2, 0])
ok("4.13 A self-adjoint, not unitary", np.allclose(A, A.T) and not np.allclose(A @ A, np.eye(3)))
ok("4.13 A = U D U^-1, U unitary", np.allclose(U @ D @ U.T, A) and np.allclose(U.T @ U, np.eye(3)))
# Ex 4.17 / 4.18
sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
P = [np.eye(2), sx, sy, sz]
G = np.array([[np.trace(a.conj().T @ b) for b in P] for a in P])
ok("4.17 {1,sx,sy,sz} HS-orthogonal (Gram = 2 I)", np.allclose(G, 2 * np.eye(4)))
def expm(M, terms=60):
    out, term = np.eye(len(M), dtype=complex), np.eye(len(M), dtype=complex)
    for k in range(1, terms):
        term = term @ M / k; out = out + term
    return out
zc = 0.7 + 0.3j
ok("4.18 exp(z sx) = cosh z 1 + sinh z sx", np.allclose(expm(zc * sx), np.cosh(zc) * np.eye(2) + np.sinh(zc) * sx))
# Ex 5.8 / Thm 5.9
Am = np.array([[0, 1], [0, 0]]); Bm = np.array([[0, 0], [1, 0]])
t = 1.3
ok("5.8 e^{tA}e^{tB} = [[1+t^2,t],[t,1]]", np.allclose(expm(t * Am) @ expm(t * Bm), [[1 + t**2, t], [t, 1]]))
E = expm(Am + Bm)
errs = [np.linalg.norm(np.linalg.matrix_power(expm(Am / n) @ expm(Bm / n), n) - E, 2) for n in (10, 100, 1000)]
ok("5.9 Trotter error ~ 0.59/n and below bound 2e^4/n",
   all(abs(n * e - 0.59) < 0.01 and e <= 2 * np.exp(4) / n for n, e in zip((10, 100, 1000), errs)))
# Ex 6.5
x, y = np.array([1, 2, 0]), np.array([1, -1, -1])
A = np.outer(x, x) + np.outer(y, y)
A_orig = np.array([[2, -1, -1], [-1, 5, 1], [-1, 1, 1]])
M = np.array([[3, 2, 0], [0, -1, -1], [1, 0, 0]])
ok("6.5 T_x+T_y = [[2,1,-1],[1,5,1],[-1,1,1]] != printed A", np.array_equal(A, [[2, 1, -1], [1, 5, 1], [-1, 1, 1]]) and not np.array_equal(A, A_orig))
ok("6.5 A psd, singular (kernel (-2,1,-3)), tr A = 8",
   np.all(np.linalg.eigvalsh(A) > -1e-12) and np.allclose(A @ [-2, 1, -3], 0) and np.trace(A) == 8)
ok("6.5 Phi(M) = tr(AM)/8 = 1/8", np.isclose(np.trace(A @ M) / 8, 1 / 8))
ok("6.5 printed A is positive definite, tr(A_orig M)/8 = -3/8",
   np.all(np.linalg.eigvalsh(A_orig) > 0) and np.isclose(np.trace(A_orig @ M) / 8, -3 / 8))
# Prop 6.6
a = np.array([0.3, -0.4, 0.5]); rho = 0.5 * (np.eye(2) + a[0] * sx + a[1] * sy + a[2] * sz)
ok("6.6 eigenvalues (1 +- |a|)/2", np.allclose(np.sort(np.linalg.eigvalsh(rho)), [(1 - np.linalg.norm(a)) / 2, (1 + np.linalg.norm(a)) / 2]))
# Ex 8.4
phi = lambda t: expm(-0.5j * t * sx) @ np.array([1, 0])
rho8 = lambda t: np.outer(phi(t), phi(t).conj())
s_, t_ = 0.4, 2.1
ok("8.4 k(s,t) = tr(rho(t)rho(s)) = cos^2((t-s)/2)", np.isclose(np.trace(rho8(t_) @ rho8(s_)).real, np.cos((t_ - s_) / 2) ** 2))
pts = np.random.default_rng(0).uniform(-5, 5, 8)
K = np.cos((pts[:, None] - pts[None, :]) / 2) ** 2
ok("8.4 kernel matrix psd with rank <= 3 (RKHS = span{1,cos,sin})",
   np.all(np.linalg.eigvalsh(K) > -1e-10) and np.linalg.matrix_rank(K, tol=1e-8) == 3)
