#!/usr/bin/env python

###########################################################################
# - Hotel Booking Test Cases methods
############################################################################

import sys
import os
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import time
from datetime import date
from datetime import datetime
from datetime import timedelta
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'common/')))
import Common
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../constants/')))
import homepage

class Signin:
    
    def __init__(self):
        self.objCommon = Common.Common()
        self.objhomepage = homepage.homepage()
        
    def test_signin(self, logger, driverhandler):
        """
        This method will click on Signin button
        :param LogfileHandler: handler to log the execution data
        :param driverhandler: driver handler
        :return:
        """
        logger.info("Sign In ")
        time.sleep(2)
        
        driverhandler.find_element_by_id(self.objhomepage.Product_Yourtrip_ID).click()
        time.sleep(1)
        driverhandler.find_element_by_id( self.objhomepage.Product_Signin_ID).click()
        time.sleep(5)
        driverhandler.find_element_by_id(self.objhomepage.Product_Signin_BUTTON_ID).click()
        #driverhandler.find_element_by_xpath(self.objhomepage.Product_Signin_BUTTON_ID).click()
        # try:
        #     wait = WebDriverWait(driverhandler, 10000)
        #     confirm = wait.until(EC.element_to_be_clickable((By.ID, self.objhomepage.Product_Signin_BUTTON_ID)))
        #     confirm.click()
        # except Exception as err:
        #     print ("Timeout Exception")
        
        time.sleep(1)
        Error_Element = driverhandler.find_element_by_id( self.objhomepage.Product_Error_ID)
        print(Error_Element.text)
