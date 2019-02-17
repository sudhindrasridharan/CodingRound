#!/usr/bin/python

import os
import sys
import logging


class homepage:
        Product_Flights_XPATH = '//*[@class="flightApp"]'
        Product_Flights_DEPART_DATE_XPATH = '//*[@id="DepartDate"]'

        Product_Hotel_XPATH = '//*[@class="hotelApp "]'
        Poduct_Hotel_Where_XPATH = '//*[@id="Tags"]'
            #'//*[@id="SearchForm"]/section[1]/div/dl/dd' # '//*[@class="ui-widget"]'
        Product_Hotel_Checkin_XPATH = '//*[@id="CheckInDate"]'
        Product_Hotel_Checkout_XPATH = '//*[@id="CheckOutDate"]'
        
        # BUTTON ACTION
        Product_Flights_SEARCH_BUTTON_ID = "SearchBtn"
        Product_Hotel_SEARCH_BUTTON_ID = "SearchHotelsButton"
        
        