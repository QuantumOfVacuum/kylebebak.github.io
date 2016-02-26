---
layout: page
permalink: /sub-pages/visit-logarithmic-growth
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=AM_HTMLorMML-full"></script>

## Stretching of visits: worst case scenario

Here we describe a visit that gets stretched as records are added to it. We define the visit's diameter `d` as the largest distance between any pair of records in the visit, and the visit's center `c` as the distance from the center to the first record in the visit.

We consider a sequence starting with an arbitrarily placed record that instantiates a new visit `V`. The following records radiate out in one direction, such that as each record is added to `V`, the following record is at distance `R` from the previously calculated center of `V`. As each record is added, it stretches `V` as much as possible. The stretching slows down as `V` accumulates records and its "weight" increases. We want to know if this stretching is bounded, and if it's not, what function we can use to describe it.

We focus on the growth of `c`, and hence `d`, as a function of `n`, the number of records that have been added to `V`.

<ul>
  <li>
    `c_(n+1) = (n * c_n + (c_n + R))/(n + 1)` <code>in general</code>
  </li>
  <li>
    `c_1 = 0` <code>first record in visit</code>
  </li>
  <li>
    `c_2 = (1 * c_1 + (c_1 + R))/2 = (2 * c_1 + R)/2 = c_1 + R/2 = R/2`
  </li>
  <li>
    `c_3 = (2 * c_2 + (c_2 + R))/3 = (3 * c_2 + R)/3 = c_2 + R/3 = R/2 + R/3`
  </li>
  <li>
    `c_4 = (3 * c_3 + (c_3 + R))/4 = (4 * c_3 + R)/4 = c_3 + R/4 = R/2 + R/3 + R/4`
  </li>
</ul>

<div>
  It's clear that `AAn >= 2, c_n = R(1/2 + 1/3 + ... + 1/n)`. As for the diameter, the next record is always added at a distance <code>R</code> from the previously calculated center, so we have `AAn >= 2, d_n = R + c_(n-1) = Rsum_(i=1)^(n-1) 1/i`.  But this is just <a href="https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)">the harmonic series</a>. The growth of this series is logarithmic. Specifically, `AAn >= 2, d_n < R*ln(n)`.
</div>
