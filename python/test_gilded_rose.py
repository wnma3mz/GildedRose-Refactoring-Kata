# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
import copy

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    @staticmethod
    def generate_grid_items(name_lst: list[str], sell_in_lst: list[int], quality_lst: list[int]) -> list[Item]:
        items = []
        for name in name_lst:
            for sell_in in sell_in_lst:
                for quality in quality_lst:
                    items.append(Item(name, sell_in, quality))
        return items

    def generate_examples(self) -> tuple[list[Item], list[Item]]:
        name_lst = ["foo", "Aged Brie", "Sulfuras", "Backstage passes"]
        sell_in_lst = [-1, 0, 1, 5, 10, 15]
        quality_lst = [-1, 0, 1, 5, 10, 15]
        items = self.generate_grid_items(name_lst, sell_in_lst, quality_lst)
        items_ori = copy.deepcopy(items)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        return items_ori, items

    def test_all(self):
        items_ori, items_ans = self.generate_examples()
        gilded_rose = GildedRose(items_ori)
        gilded_rose.update_quality_new()
        for item_o, item_n in zip(items_ori, items_ans):
            self.assertEqual(item_o.quality, item_n.quality)

    def test_Conjured(self):
        items = [Item("Conjured", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality_new()
        self.assertEqual(items[0].quality, 0)

        items = [Item("Conjured", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality_new()
        self.assertEqual(items[0].quality, 6)

        items = [Item("Conjured", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality_new()
        self.assertEqual(items[0].quality, 8)

if __name__ == '__main__':
    unittest.main()
