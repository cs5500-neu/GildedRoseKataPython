# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].quality)
    
    def test_backstage_passes(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 20),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].quality)

    def test_vest_item_should_decrease_after_one_day(self):

        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6), ]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.get_items_by_name(vest) == [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]
    
    def test_aged_brie_should_increase_in_quality(self):
        aged_brie = "Aged Brie"
        items = [Item(aged_brie, 2, 0)]
        gr = GildedRose(items)

        gr.update_quality()

        # This assertion should fail if the quality does not increase
        assert gr.get_items_by_name(aged_brie) == [Item(aged_brie, 1, 1)] 

    def test_sulfuras_never_decreases_quality(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 0, 80)]
        gr = GildedRose(items)

        gr.update_quality()

        # This assertion should fail if Sulfuras' properties are not handled correctly
        assert gr.get_items_by_name(sulfuras) == [Item(sulfuras, -1, 80)] 

    def test_backstage_passes_should_increase_quality_within_10_days(self):
        backstage_pass = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(backstage_pass, 9, 20)]
        gr = GildedRose(items)

        gr.update_quality()

        # This assertion should fail if the quality is not updated as expected
        assert gr.get_items_by_name(backstage_pass) == [Item(backstage_pass, 8, 21)] 



if __name__ == '__main__':
    unittest.main()
