# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def get_items_by_name(self, name: str):
        return [item for item in self.items if item.name == name]

    def update_quality(self):
        for item in self.items:
            # Define rules for updating each item's quality
            # Apply iterator pattern
            item_rules = {
                "Aged Brie": self.update_aged_brie,
                "Backstage passes to a TAFKAL80ETC concert": self.update_backstage_passes,
                "Sulfuras, Hand of Ragnaros": self.update_sulfuras,
                "Conjured Items": self.update_conjured
            }

            # Apply the rules based on the item's name
            if item.name in item_rules:
                item_rules[item.name](item)
            else:
                self.update_default(item)

            # Handle sell-in and quality degradation after sell date
            item.sell_in -= 1
            if item.sell_in < 0:
                if item.name not in ("Aged Brie", "Backstage passes to a TAFKAL80ETC concert"):
                    self.update_default(item)
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0

    def update_aged_brie(self, item):
        item.quality = min(50, item.quality + 1)

    def update_backstage_passes(self, item):
        item.quality = min(50, item.quality + (1 + min(2, max(0,
                           item.sell_in - 10), max(2, max(0, item.sell_in - 5)))))

    def update_sulfuras(self, item):
        pass

    def update_conjured(self, item):
        item.quality = max(0, item.quality - 2)

    def update_default(self, item):
        item.quality = max(0, item.quality - (1 if item.name !=
                           "Sulfuras, Hand of Ragnaros" else 0))
