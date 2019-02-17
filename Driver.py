#!/usr/bin/env python

###########################################################################
#
# - Main Script to execute Test Cases
# 
# - Main Script perform following Operations:
#   1 Input data validation
#   2 Log the Execution Steps
#   3 Test Case execution
############################################################################

import sys
import os
import argparse
import time
from pathlib import Path
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                'common/')))
import Common

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                'src/')))
import Flightbooking

class Driver:
    results = ""
    
    def __init__(self):
        self.objCommon = Common.Common()

    def _cli_parser(self, list_input_args):
        """
        Parse cli arguments and stores it in dictionary.
        :param list_input_args: Arguments passed by user from cli.
        :return: Dictionary storing information of cli arguments in required format.
        """

        # Args having "default" keyword, are either optional, or not valid in all execution modes
        cli_parser = argparse.ArgumentParser()
        cli_parser.add_argument('-i', '--config-file',
                                dest='config_file',
                                help='Provide the absolute path for configuration file. This is mandatory argument.')
        cli_parser.add_argument('-t', '--testsuite',
                                dest='test_suite_file',
                                help = 'Test file which consist list of test case to execute'
                                       'This is mandatory argument.')
        result = cli_parser.parse_args()
        
        # Validation
        if (len(list_input_args) == 1) or (not result.config_file) or (not result.test_suite_file):
            print("Invalid Input Parameter")
            sys.exit(1)
        print("Cli argument parsed successfully\n")
        return (result)
    
        
# Driver entry point
if __name__ == '__main__':
    objDriver = Driver()
    objcommon = Common.Common()
    objflightbooking = Flightbooking.Flightbooking()

    # Creation of Logger File
    CurrentEpochTime = objcommon.getCurrentEpochTime()
    
    # Logger Section
    LogFileName = "test_" + str( CurrentEpochTime ) + ".log"
    CurrentPath = os.getcwd()
    LogFilePath = os.path.join( CurrentPath, 'logs', str( LogFileName ) )
    logger = logging.getLogger('spam_application')
    logger.setLevel(logging.DEBUG)
    lfh = logging.FileHandler(LogFilePath)
    lfh.setLevel(logging.DEBUG)
    logger.addHandler(lfh)
    
    input_parameters = objDriver._cli_parser(sys.argv)
    
    # Validation of Input File exist
    status = objcommon.fileExists(input_parameters.config_file)
    if status:
        logger.info("Framework Config File is : %s " % input_parameters.config_file)
        # XML Parser
        Input_data = objcommon.config_parser(input_parameters.config_file)
    else:
        print("Input Config file is missing ")
        sys.exit(1)

    logger.info("Test Application Details")
    webdriverpath = Input_data['Configuration']['SetupConfiguration']['WebDriverConfiguration']['WebDriverPath']
    WebSite = Input_data[ 'Configuration' ][ 'SetupConfiguration' ][ 'WebsiteConfiguration' ][ 'Site' ]
    logger.info("Web Driver Location : %s " % webdriverpath)
    logger.info("Web Site Under Test : %s " % WebSite)
    
    # Command to open a web driver Open of chrome
    driverhandler = objcommon.openwebdriver(webdriverpath)
    driverhandler.get(WebSite)
    objflightbooking.test_onewayjourney(logger, driverhandler,2)
    