#!/usr/bin/env python

###########################################################################
# - Hotel Booking Test Cases methods
############################################################################

import sys
import os
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import date
from datetime import datetime
from datetime import timedelta
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'common/')))
import Common
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../constants/')))
import homepage

class Hotelbooking:
    
    def __init__(self):
        self.objCommon = Common.Common()
        self.objhomepage = homepage.homepage()
        
    def test_hoteljourney(self, logger, driverhandler, Checkin_day=0, Checkout_day=1):
        """
        This method will find a element for hotel room for
        a) 1 room 1 adult
        b) 1 room 2 adult
        :param LogfileHandler: handler to log the execution data
        :param driverhandler: driver handler
        :return:
        """
        logger.info("Hotel Room Booking")
        time.sleep(2)
        # link = driverhandler.find_element_by_link_text('/hotels')
        # link.click()
        driverhandler.find_element_by_xpath(self.objhomepage.Product_Hotel_XPATH).click()
        time.sleep(2)
        driverhandler.find_element_by_xpath(self.objhomepage.Poduct_Hotel_Where_XPATH).send_keys("Whitefield, Bangalore")
        driverhandler.find_element_by_xpath(self.objhomepage.Poduct_Hotel_Where_XPATH).send_keys(Keys.RETURN)
        time.sleep(2)
        
        # Entering the DepartDate
        if (Checkin_day < 0 and Checkout_day == 0):
            print("Hotel cannot be booked")
            sys.exit(1)
        elif (Checkout_day == 0):
            print( "Hotel room cannot be for same day ")
            sys.exit(1)
        date = datetime.now() + timedelta(Checkin_day)
        Checkin_date = date.strftime("%a, %d, %b, %Y")
        date = datetime.now() + timedelta(Checkout_day)
        Checkout_date = date.strftime("%a, %d, %b, %Y")
        time.sleep(2)
        driverhandler.find_element_by_xpath(self.objhomepage.Product_Hotel_Checkin_XPATH).send_keys(Checkin_date)
        driverhandler.find_element_by_xpath(self.objhomepage.Product_Hotel_Checkin_XPATH).send_keys(Keys.RETURN)
        time.sleep(2)
        driverhandler.find_element_by_xpath(self.objhomepage.Product_Hotel_Checkout_XPATH).send_keys(Checkout_date)
        driverhandler.find_element_by_xpath(self.objhomepage.Product_Hotel_Checkout_XPATH).send_keys(Keys.RETURN)
        time.sleep(2)
        driverhandler.find_element_by_id(self.objhomepage.Product_Hotel_SEARCH_BUTTON_ID).click()
        