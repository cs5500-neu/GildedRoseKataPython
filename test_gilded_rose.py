# -*- coding: utf-8 -*-
import unittest

from gilded_rose_refactored import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("fixme", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual([(item.name, item.sell_in, item.quality) for item in gr.get_items_by_name(vest)],
                         [(vest, 0, 1), (vest, 8, 18), (vest, 3, 5)])

    def test_vest_item_past_sellin_degrade_doubles(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 0, 19), Item(vest, 0, 19), Item(vest, 5, 8)]
        gr = GildedRose(items)

        gr.update_quality()
        self.assertEqual([(item.name, item.sell_in, item.quality) for item in gr.get_items_by_name(vest)],
                         [(vest, -1, 17), (vest, -1, 17), (vest, 4, 7)])

        gr.update_quality()
        self.assertEqual([(item.name, item.sell_in, item.quality) for item in gr.get_items_by_name(vest)],
                         [(vest, -2, 15), (vest, -2, 15), (vest, 3, 6)])

        gr.update_quality()
        self.assertEqual([(item.name, item.sell_in, item.quality) for item in gr.get_items_by_name(vest)],
                         [(vest, -3, 13), (vest, 0-3, 13), (vest, 2, 5)])

    def test_brie_item_should_increase_in_quality_with_age(self):
        brie = "Aged Brie"
        items = [Item(brie, 10, 20), Item(brie, 5, 40), Item(brie, 0, 50)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual([(item.name, item.sell_in, item.quality) for item in gr.get_items_by_name(brie)],
                         [(brie, 9, 21), (brie, 4, 41), (brie, -1, 50)])

    def test_conjured_item_degrades_twice_as_fast(self):
        conjured = "Conjured Items"
        items = [Item(conjured, 5, 42)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual([(item.name, item.sell_in, item.quality) for item in gr.get_items_by_name(conjured)],
                         [(conjured, 4, 40)])

        gr.update_quality()

        self.assertEqual([(item.name, item.sell_in, item.quality) for item in gr.get_items_by_name(conjured)],
                         [(conjured, 3, 38)])


if __name__ == '__main__':

    unittest.main()
