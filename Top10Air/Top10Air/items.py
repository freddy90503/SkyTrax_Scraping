# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Top10AirItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    AirName = scrapy.Field()
    OverallScore = scrapy.Field()
    ReviewTitle = scrapy.Field()
    ReviewrCountry = scrapy.Field()
    ReviewDate = scrapy.Field()
    AircraftModel = scrapy.Field()
    TravelType = scrapy.Field()
    SeatType = scrapy.Field()
    Route = scrapy.Field()
    DateFlown = scrapy.Field()
    SeatComfortRating = scrapy.Field()
    ServiceRating = scrapy.Field()
    FoodRating = scrapy.Field()
    EntertainmentRating = scrapy.Field()
    GroundServiceRating = scrapy.Field()
    WifiRating = scrapy.Field()
    ValueRating = scrapy.Field()
    Recommended = scrapy.Field()
    Comments = scrapy.Field()