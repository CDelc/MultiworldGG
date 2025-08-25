

from . import PoeTestBase
from .. import Items, Locations


class TestEmpty(PoeTestBase):

    def test_empty(self) -> None:
        self.assertEqual(0, 0)


class TestPoeGem(PoeTestBase):

    def test_get_main_skill_gems_by_required_level(self):
        gems = Items.get_main_skill_gems_by_required_level(1, 10)
        names = [item["name"] for item in gems]
        assert "Crushing Fist" in names  # reqLevel 4
        assert "Artillery Ballista" not in names  # reqLevel 28