# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class QualityUpdater:
    """Strategy Pattern: Base class for quality update strategies."""
    def update(self, item: Item):
        raise NotImplementedError("This method should be overridden.")


class NormalItemUpdater(QualityUpdater):
    """Concrete strategy for normal items."""
    def update(self, item: Item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class AgedBrieUpdater(QualityUpdater):
    """Concrete strategy for Aged Brie."""
    def update(self, item: Item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class BackstagePassUpdater(QualityUpdater):
    """Concrete strategy for Backstage passes."""
    def update(self, item: Item):
        if item.sell_in > 10:
            item.quality += 1
        elif item.sell_in > 5:
            item.quality += 2
        elif item.sell_in > 0:
            item.quality += 3
        else:
            item.quality = 0

        # Ensure quality does not exceed 50
        if item.quality > 50:
            item.quality = 50
        
        item.sell_in -= 1


class UpdaterFactory:
    """Factory for creating quality updater instances."""
    @staticmethod
    def get_updater(item: Item) -> QualityUpdater:
        if item.name == "Aged Brie":
            return AgedBrieUpdater()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdater()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return None  # Sulfuras does not change
        else:
            return NormalItemUpdater()


class GildedRose:
    """Main class that uses the factory and strategies to update items."""
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = UpdaterFactory.get_updater(item)
            if updater:
                updater.update(item)

if __name__ == "__main__":
    items = [
        Item("Aged Brie", 2, 0),
        Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        Item("Normal Item", 10, 20),
        Item("Sulfuras, Hand of Ragnaros", 0, 80)
    ]
    gilded_rose = GildedRose(items)

    print("Before Update:")
    for item in gilded_rose.items:
        print(item)

    gilded_rose.update_quality()

    print("\nAfter Update:")
    for item in gilded_rose.items:
        print(item)
