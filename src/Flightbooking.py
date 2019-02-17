#!/usr/bin/env python

###########################################################################
# - Flight Booking Test Cases methods
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

class Flightbooking:
    
    def __init__(self):
        self.objCommon = Common.Common()
        self.objhomepage = homepage.homepage()
        
    def test_onewayjourney(self, logger, driverhandler, Flight_day=0):
        """
        This method will find a element for oneway journey
        :param LogfileHandler: handler to log the execution data
        :param driverhandler: driver handler
        :return:
        """
        logger.info("Flights Booking")
        element = driverhandler.find_element_by_id("OneWay").click()
        driverhandler.find_element_by_id("FromTag").clear()
        driverhandler.find_element_by_id("FromTag").send_keys("Bangalore")
        # wait for the auto complete options to appear for the origin
        time.sleep(2)
        driverhandler.find_element_by_id("ToTag").clear()
        driverhandler.find_element_by_id("ToTag").send_keys("Ahmedabad")
        
        # Entering the DepartDate
        if Flight_day < 0:
            logger.error("Flights for older date cannot be booked")
            sys.exit(1)
        date = datetime.now() + timedelta(Flight_day)
        Ddate = date.strftime("%a, %d, %b, %Y")
        time.sleep(2)
        driverhandler.find_element_by_xpath(self.objhomepage.Product_Flights_DEPART_DATE_XPATH).send_keys(Ddate)
        driverhandler.find_element_by_xpath(self.objhomepage.Product_Flights_DEPART_DATE_XPATH).send_keys(Keys.RETURN)
        time.sleep(1)
        driverhandler.find_element_by_id(self.objhomepage.Product_Flights_SEARCH_BUTTON_ID).click()
        