from scrapy import Spider
from Top10Air.items import Top10AirItem
import re


class TopTenAirSpider(Spider):
    name = "Top10AirSpider"
    allowed_urls = ['https://www.airlinequality.com/']
    start_urls = ['https://www.airlinequality.com/airline-reviews/singapore-airlines/page/' + str(i) for i in range(40)]

    def parse(self, response):
        reviews = response.xpath('//article[@itemprop="review"]')
        for review in reviews:
            #OverallScore

            try:
                OverallScore = review.xpath('./div/span[1]/text()').extract_first()
            except:
                OverallScore = ''


            #ReviewTitle
            try:
                ReviewTitle = review.xpath('././div/h2/text()').extract_first()
            except:
                ReviewTitle = ''


            #ReviewrCountry
            try:
                ReviewrCountry = response.xpath('//article[@itemprop="review"]/div/h3/text()').extract()[1]
            except:
                ReviewrCountry = ''


            #ReviewDate
            try:
                ReviewDate = review.xpath('././div/h3/time/text()').extract_first()
            except:
                ReviewDate = ''


            #AircraftModel
            try:
                AircraftModel = review.xpath('.//td[@class="review-rating-header aircraft "]/../td[2]/text()').extract_first()
            except:
                AircraftModel = ''

            #TravelType
            try:
                TravelType = review.xpath('.//td[@class="review-rating-header type_of_traveller "]/../td[2]/text()').extract_first()
            except:
                TravelType = ''

            #SeatType
            try:
                SeatType = review.xpath('.//td[@class="review-rating-header cabin_flown "]/../td[2]/text()').extract_first()
            except:
                SeatType = ''

            #Route
            try:
                Route = review.xpath('.//td[@class="review-rating-header route "]/../td[2]/text()').extract_first()
            except:
                Route = ''

            #DateFlown
            try:
                DateFlown = review.xpath('.//td[@class="review-rating-header date_flown "]/../td[2]/text()').extract_first()
            except:
                DateFlown = ''

            #SeatComfortRating
            try:
                SeatComfortRatingPrep = review.xpath('.//td[@class="review-rating-header seat_comfort"]/../td[2]/span/@class').extract()
                SeatComfortRating = SeatComfortRatingPrep.count('star fill')
            except:
                SeatComfortRating = ''

            #ServiceRating
            try:
                ServiceRatingPrep = review.xpath('.//td[@class="review-rating-header cabin_staff_service"]/../td[2]/span/@class').extract()
                ServiceRating = ServiceRatingPrep.count('star fill')
            except:
                ServiceRating = ''

            #FoodRating
            try:
                FoodRatingPrep = review.xpath('.//td[@class="review-rating-header food_and_beverages"]/../td[2]/span/@class').extract()
                FoodRating = FoodRatingPrep.count('star fill')
            except:
                FoodRating = ''

            #EntertainmentRating
            try:
                EntertainmentRatingPrep = review.xpath('.//td[@class="review-rating-header inflight_entertainment"]/../td[2]/span/@class').extract()
                EntertainmentRating = EntertainmentRatingPrep.count('star fill')
            except:
                EntertainmentRating = ''

            #GroundServiceRating
            try:
                GroundServiceRatingPrep = review.xpath('.//td[@class="review-rating-header ground_service"]/../td[2]/span/@class').extract()
                GroundServiceRating = GroundServiceRatingPrep.count('star fill')
            except:
                GroundServiceRating = ''

            #WifiRating
            try:
                WifiRatingPrep = review.xpath('.//td[@class="review-rating-header wifi_and_connectivity"]/../td[2]/span/@class').extract()
                WifiRating = WifiRatingPrep.count('star fill')
            except:
                WifiRating = ''

            #ValueRating
            try:
                ValueRatingPrep = review.xpath('.//td[@class="review-rating-header value_for_money"]/../td[2]/span/@class').extract()
                ValueRating = ValueRatingPrep.count('star fill')
            except:
                ValueRating = ''

            #Recommended
            try:
                Recommended = review.xpath('.//td[@class="review-value rating-yes"]/text()').extract_first() 
            except:
                Recommended = 'no'

            #Comments
            try:
                Comments = response.xpath('//*[@id="anchor666219"]/div/div[1]/text()').extract_first()
            except:
                Comments = ''


            item = Top10AirItem()
            item['AirName'] = 'Singapore Airlines'
            item['OverallScore'] = OverallScore
            item['ReviewTitle'] = ReviewTitle
            item['ReviewrCountry'] = ReviewrCountry
            item['ReviewDate'] = ReviewDate
            item['AircraftModel'] = AircraftModel
            item['TravelType'] = TravelType
            item['SeatType'] = SeatType
            item['Route'] = Route
            item['DateFlown'] = DateFlown
            item['SeatComfortRating'] = SeatComfortRating
            item['ServiceRating'] = ServiceRating
            item['FoodRating'] = FoodRating
            item['EntertainmentRating'] = EntertainmentRating
            item['GroundServiceRating'] = GroundServiceRating
            item['WifiRating'] = WifiRating
            item['ValueRating'] = ValueRating
            item['Recommended'] = Recommended
            item['Comments'] = Comments

            yield item
#[@id="anchor666219"]/div/div[2]/table/tbody/tr[1]/td[2]
