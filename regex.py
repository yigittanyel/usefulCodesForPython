from typing import MutableMapping, MutableSequence, MutableSet


"""
[abc] -> aralıktaki değerler.    ac 2 eşleşme  abc de ca -> 5 eşleşme
^ab -> ab ile başlayan.  abc -> 1 eşleşme  acb -> 0 eşleşme
a$ -> a ile biten.   formula -> 1 eşleşme cab -> 0 eşleşme
ma*n -> a dan 0 veya fazla   mn -> 1 eşleşme  maaan -> 1 eşleşme main -> 0 eşleşme
ma+n *> a dan 1 veya fazla   mn -> 0 eşleşme woman -> 1 eşleşme 
ma?n -> a dan 0 veya 1 man-> 1 eşleşme maan -> 0 eşleşme 
"""