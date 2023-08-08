# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality_new(self):
        for item in self.items:
            self.update_single_item(item)

    def update_single_item(self, item):
        if item.name == "Backstage passes":
            self.do_backstage(item)
        elif item.name == "Aged Brie":
            self.do_aged(item)
        elif item.name == "Sulfuras":
            pass
        else:
            self.do_general(item)

    def do_general(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0 < item.quality:
            item.quality = item.quality - 1

    def do_aged(self, item):
        self.inc_fifty(item)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            self.inc_fifty(item)

    def do_backstage(self, item):
        self.inc_fifty(item)
        if item.sell_in < 11:
            self.inc_fifty(item)
        if item.sell_in < 6:
            self.inc_fifty(item)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = 0


    @staticmethod
    def inc_fifty(item):
        if item.quality < 50:
            item.quality = item.quality + 1


    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes":
                if item.quality > 0:
                    if item.name != "Sulfuras":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes":
                        if item.quality > 0:
                            if item.name != "Sulfuras":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
