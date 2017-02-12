# DeterministicGrowthProcess
Code to explore the properties of the deterministic growth process described in the __init__ method of growth.py

In this repo, we hope to store prior calculated iterations so we don't have to keep recalculating them. Once we add more dimensions and iterations, this should be way more efficient. As of now, reading in the two-dimensional n = 1000 case is 4 times faster than calculating it.

In growth.py, we can also test conjectures towards the end. For example, running numerics seems to suggest that in two-dimensions, the density of this shape is 2/3.

If you're trying to make the code run faster, a useful line to run in terminal is: python -m cProfile -s cumtime growth.py
