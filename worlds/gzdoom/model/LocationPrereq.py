'''
Classes for modeling location/region access prerequisites.

This is a generalization of earlier, ad-hoc access modeling based on key and
weapon inventory. A leaf prereq models a requirement that a player have a
certain item in their inventory, or have access to a certain region or location.
A branch prereq models a combination of leaf prereqs.
'''

'''
When tune_location is called, we're passed:
- the set of keys used;
- the set of weapons held;
- the set of levels traversed to get here.

In all of these cases we want to apply the same basic algorithm: insert this
set into our set-of-sets, and remove any sets that it is a proper subset of.
'''

from typing import FrozenSet

class PrereqSet:
  # None means that we haven't received any tuning data, and need to use
  # whatever the default prereqs are.
  prereqs: FrozenSet[FrozenSet[str]] | None

  def tune(self, new_prereqs: FrozenSet[str]) -> None:
    if self.prereqs == frozenset():
       # Empty requirement cannot be further tuned.
       return

    if not new_prereqs:
       # Mark this requirement empty.
       self.prereqs = frozenset()
       return

    if self.prereqs is None:
      # First time we're getting tuned
      self.prereqs = frozenset([new_prereqs])
      return

    self.prereqs = frozenset([
      xs for xs in self.prereqs
      if not new_prereqs < xs
    ] + [new_prereqs])


class ItemPrereq(PrereqSet):
  def satisfied(self, world, state) -> bool:
