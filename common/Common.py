#!/usr/bin/env python

##############################################
# Common Library includes all common functions
##############################################

import datetime
import time
import os
import re
import xmltodict
import json
import logging
import xml.dom.minidom as dom
from selenium import webdriver

class Common:

    def fileExists(self, fileName):
        """
        This function checks whether file exists or not
        Argument : Absolute file path
        Return : True if Success, else False
        """
        try:
            if os.path.isfile(fileName):
                return True
            else:
                return False
        except Exception as err:
            logging.error("file validation error %s " % err)
            return False

    def dirExists(self, dirName):
        """
        This function checks whether directory exists or not
        Argument : Absolute directory path
        Return : True if success, else False
        """
        try:
            if os.path.isdir(dirName):
                return True
            else:
                return False
        except Exception as err:
            logging.error("dirctory validation error %s " % err)
            return False

    def xmlValidator(self, fileName):
        """
        This function validates the syntax of a XML file
        Argument : Absolute file path with file name
        Return : True if Success, else False
        """
        if self.fileExists(fileName):
            with open(fileName) as f:
                try:
                    dom.parse(fileName)
                    return True
                except Exception as err:
                    logging.error("Error : XML File format is incorrect !! %s " % err)
                    return False
        else:
            return False

    def config_parser(self, fileName):
        try:
            dict_configuration_xml_json = {}
            with open(fileName, encoding="utf8") as fd:
                curr_line = fd.read()
                if curr_line:
                    object_configuration_xml = xmltodict.parse(curr_line)
                    str_config_xml = json.dumps(object_configuration_xml)
                    dict_configuration_xml_json = json.loads(str_config_xml)
                if not dict_configuration_xml_json:
                    logging.error(fileName + " file is empty.")
                    sys.exit()
            return dict_configuration_xml_json
        except (FileNotFoundError, PermissionError) as e:
            logging.error(fileName + " file doesn't exist. Please provide correct file with absolute path")
            sys.exit()

    def openFile(self, fileName, fileMode='a'):
        """
        Open File at given path
        Argument: File Name and file open mode
        Return: File pointer
        """
        try:
            filePtr = open(fileName, fileMode, encoding="utf8")
            return filePtr
        except Exception as err:
            print("ERROR : ", err)
            return False

    def removeWhiteSpace(self, inputStr):
        """
        Remove White Space of device name
        """
        try:
            return inputStr.strip().rstrip()
        except Exception as err:
            print("ERROR: ", err)
            return False

    def getCurrentEpochTime ( self ):
        """
        This function get the current EpochTime of the system.
        Return: Current Epoch time , False when exception.
        """
        try:
            temp = datetime.datetime.now()
            currentEpochTime = int( time.mktime( temp.timetuple() ) )
            return currentEpochTime
        except Exception as err:
            print( "Error:", err )
            return False
        
    def openwebdriver(self, webdriverpath):
        """
        This function will start/open the specific web driver
        :param webdriverpath:
        :return: driver oblject
        """
        try:
            driver = webdriver.Chrome(webdriverpath)
            driver.maximize_window()
            return driver
        except Exception as err:
            print("ERROR:", err)
            return False
        