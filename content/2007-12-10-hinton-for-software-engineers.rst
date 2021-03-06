Hinton for software engineers
#############################

:date: 2007-12-10
:Latex:

Elements
--------

- Input Nodes
- Hidden Nodes
- Biases (on each node)
- Weights
- States

The canonical model uses binary states but can be extended to support
multinominal states. This allows for states to have more values than just two.

Primitives
----------

Sigma
  .. image:: |filename|/images/sigma.png

Forward compute (compute hidden nodes)
  .. image:: |filename|/images/forward.png
  
::

  P = probabilty
  s = state
  w = weight
  b = bias
  i = index of input node
  j = index of hidden node

Reverse compute (compute input nodes):
  .. image:: |filename|/images/reverse.png

Adjust weights:
  .. image:: |filename|/images/adjust.png
  
::

  L = learning rate (typically 0.01)


Operations
----------

Learning
  This is composed of executing the Forward computation, followed by a +Adjust,
  then t cycles of Reverse/Forwards, and finally a -Adjust.

::

  F, +A, (R, F)^t, -A

Lookup
   This is simply a Forward then a Reverse computation.

Notes
-----

Selection of t (number of cycles) is dynamic as time goes on. When starting, t
is set to 1, because setting t to higher values is computationally a waste at
first, the error rate or amount of information learned in each round doesn't
change much. However, eventually a 'valley' is found and the algorithm won't
find any better choices. At this point, t is increased, to say 3. The error rate
goes down some more, until another valley is reached, and then t is increased
again. However, there are diminishing returns on t, so eventually the bottom is
reached.

Extension to multinominal states
--------------------------------

Each node must be binary, so obviously a multinominal state must allocate
multiple nodes. The trick, however, is that only some inputs are valid. Encoding
of these states is not as trivial as one might imagine. We need a way to
represent an invalid or unknown state. This must always be encoded with all
zeros (the math requires this).

Starting with the simplest case, we have a tri-state input. This can be done
like so:

::

  [0][0] = unknown
  [0][1] = 0
  [1][0] = 1
  [1][1] = unused

The portion unused means that the configuration of [1][1] is never used. This
might be slightly wasteful, but there's no way around it.

Now let's imagine a state that has 3 possible values, along with an unknown value. This is done with:

::

[0][0][0] = unknown
[0][0][1] = 1
[0][1][0] = 2
[1][0][0] = 3

Notice that each bit-field can be used for one and only one value. This is not a
typical encoding for numbers in binary form. What we are basically saying here
is that the first bit-field is only means the value 4. If other inputs were
turned on, then this would be a 'confused' sensor, because it's not clearly
telling the system which state it is in.

Because of the modification to the way input nodes look, we need to update the
math accordingly. Sigma gets replaced with:

  .. image:: |filename|/images/multinominal.png


Where here the A is the activation term. This is the portion of the above
equations for forward and reverse computations, that are within the sigma (think
of it as the argument passed to the sigma function).
