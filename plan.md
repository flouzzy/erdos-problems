1.  **Select the Problem**:
    The user requested choosing an open problem from Paul Erdős's conjectures based on difficulty (from least to most difficult) and applicability to the real world.
    I will choose the **Erdős-Gyárfás conjecture**. It's a graph theory problem with intermediate difficulty. It states that every graph with minimum degree at least 3 contains a cycle whose length is a power of 2. It has practical applications in network topology and computer science (e.g., hypercube routing).
    There is a directory `inprogress/04-Erdos-Gyarfas` that contains some files, but I will overwrite them or create new ones in an organized way, focusing on generating a rigorous proof structure. I will use a probability of resolution below 95%, so it will stay in `inprogress/04-Erdos-Gyarfas`.

2.  **Define the Script to Generate LaTeX (English)**:
    Create a python script `inprogress/04-Erdos-Gyarfas/gen_proof_en.py` to generate `proof.tex`. The script will output a rigorous LaTeX document.
    The document will include:
    - Axiomatic definitions (Graph $G=(V,E)$, minimum degree $δ(G) \ge 3$, cycle $C$, length $\ell(C) = 2^k$). Typing of variables.
    - Contextual literature research (using the results from the arXiv query: e.g., "A 60-Vertex Lower Bound for Cubic Bipartite Counterexamples", "On the Erdős-Gyárfás conjecture in claw-free graphs"). Analogies with other graph theory problems (like the existence of even cycles).
    - Proof Strategy & Isolation of Lemmas: Decomposition into intermediate problems (e.g., Lemma 1: Properties of longest paths in graphs with $δ \ge 3$. Lemma 2: Probabilistic bounds on cycle lengths).
    - Informal Proof (Zero Ellipse): Step-by-step mathematical derivation for the lemmas.
    - Architecture for Autoformalization: Lean 4/Aristotle blocks with types and explicit hypotheses.
    - Signature: "Charles EDOU NZE, chercheur indépendant" in the abstract footer.
    - Strict adherence to NO META-COMMENTARY rule.

3.  **Define the Script to Generate LaTeX (French)**:
    Create a python script `inprogress/04-Erdos-Gyarfas/gen_proof_fr.py` to generate `proof.fr.tex`. This will be the French equivalent of the English document, following all the same rules, including `\usepackage[french]{babel}` and `\usepackage[T1]{fontenc}`.

4.  **Execute Scripts and Compile LaTeX**:
    Execute `gen_proof_en.py` and `gen_proof_fr.py` to generate `proof.tex` and `proof.fr.tex`.
    Compile both `.tex` files using `pdflatex` to generate `04-Erdos-Gyarfas.pdf` and `04-Erdos-Gyarfas.fr.pdf`.
    Clean up auxiliary files.

5.  **Write Tests**:
    Write tests in `inprogress/04-Erdos-Gyarfas/test_gen_proof.py` to verify that the generated `.tex` files are correct, do not contain meta-commentary, and contain the required signature.
    Use `mock_open` to avoid writing to disk.

6.  **Run Tests**:
    Run `pytest inprogress/04-Erdos-Gyarfas/test_gen_proof.py`.

7.  **Pre-commit Step**:
    Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.

8.  **Complete Task**:
    Call `plan_step_complete` for the final submission.
