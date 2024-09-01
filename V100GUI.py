# Steps:
# 1 - run all at the same time 
# 2 - input data
# 3 - exit GUI
# 4 - run graph maker
# 5 - put graphs into powerpoint slides

from PyQt5 import QtCore, QtGui, QtWidgets
import time
import csv
import pandas as pd
import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    MetricType,
    RunReportRequest
)
import numpy as np
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
from google.analytics.data_v1beta.types import OrderBy

userInput = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.reporttypebutton = QtWidgets.QPushButton(self.centralwidget)
        self.reporttypebutton.setGeometry(QtCore.QRect(410, 70, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.reporttypebutton.setFont(font)
        self.reporttypebutton.setObjectName("reporttypebutton")
        self.reporttypeline = QtWidgets.QLineEdit(self.centralwidget)
        self.reporttypeline.setGeometry(QtCore.QRect(100, 70, 271, 51))
        self.reporttypeline.setObjectName("reporttypeline")

        self.propertyidline = QtWidgets.QLineEdit(self.centralwidget)
        self.propertyidline.setGeometry(QtCore.QRect(100, 150, 271, 51))
        self.propertyidline.setObjectName("propertyidline")
        self.propertyidbutton = QtWidgets.QPushButton(self.centralwidget)
        self.propertyidbutton.setGeometry(QtCore.QRect(410, 150, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.propertyidbutton.setFont(font)
        self.propertyidbutton.setObjectName("propertyidbutton")

        self.apikeybutton = QtWidgets.QPushButton(self.centralwidget)
        self.apikeybutton.setGeometry(QtCore.QRect(410, 230, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.apikeybutton.setFont(font)
        self.apikeybutton.setObjectName("apikeybutton")
        self.apikeyline = QtWidgets.QLineEdit(self.centralwidget)
        self.apikeyline.setGeometry(QtCore.QRect(100, 230, 271, 51))
        self.apikeyline.setObjectName("apikeyline")

        self.startdatebutton = QtWidgets.QPushButton(self.centralwidget)
        self.startdatebutton.setGeometry(QtCore.QRect(410, 310, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.startdatebutton.setFont(font)
        self.startdatebutton.setObjectName("startdatebutton")
        self.startdateline = QtWidgets.QLineEdit(self.centralwidget)
        self.startdateline.setGeometry(QtCore.QRect(100, 310, 271, 51))
        self.startdateline.setObjectName("startdateline")

        self.enddatebutton = QtWidgets.QPushButton(self.centralwidget)
        self.enddatebutton.setGeometry(QtCore.QRect(410, 390, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.enddatebutton.setFont(font)
        self.enddatebutton.setObjectName("enddatebutton")
        self.enddateline = QtWidgets.QLineEdit(self.centralwidget)
        self.enddateline.setGeometry(QtCore.QRect(100, 390, 271, 51))
        self.enddateline.setObjectName("enddateline")

#create frame button
        self.createreportbutton = QtWidgets.QPushButton(self.centralwidget)
        self.createreportbutton.setGeometry(QtCore.QRect(255, 490, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.createreportbutton.setFont(font)
        self.createreportbutton.setObjectName("createreportbutton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.propertyidbutton.clicked.connect(self.add_id)
        self.apikeybutton.clicked.connect(self.add_key)
        self.reporttypebutton.clicked.connect(self.add_type)
        self.startdatebutton.clicked.connect(self.add_startdate)
        self.enddatebutton.clicked.connect(self.add_enddate)
        self.createreportbutton.clicked.connect(self.create_reports)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_id(self):
        userInput.append(self.propertyidline.text())
        print(userInput)
    
    def add_key(self):
        userInput.append(self.apikeyline.text())
        print(userInput)

    def add_type(self):
        userInput.append(self.reporttypeline.text())
        print(userInput)

    def add_startdate(self):
        userInput.append(self.startdateline.text())
        print(userInput)

    def add_enddate(self):
        userInput.append(self.enddateline.text())
        print(userInput)

    def create_reports(self):

    ############################
    #########REPORT ONE#########
    ############################

        #global variables
        print("setting global variables 1")
        time.sleep(.5)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(userInput[2])
        property_id = str(userInput[1])
        client = BetaAnalyticsDataClient()

        #format
        print("formatting 1")
        def format_report(request):
            #getting response
            response = client.run_report(request)
            
            #DIMENSIONS
            #setting dimension header names
            row_index_names = [header.name for header in response.dimension_headers]
            #empty list
            row_header = []
            #add/ append dimensions
            for i in range(len(row_index_names)):
                row_header.append([row.dimension_values[i].value for row in response.rows])

            #index setting from rows **(rows = dimensions, columns = metrics)**
            row_index_named = pd.MultiIndex.from_arrays(np.array(row_header), names = np.array(row_index_names))
            
            #METRICS
            #setting metric header names
            metric_names = [header.name for header in response.metric_headers]
            #empty list
            data_values = []
            #add/ append metrics
            for i in range(len(metric_names)):
                data_values.append([row.metric_values[i].value for row in response.rows])

            #make into MultiIndex dataframe
            output = pd.DataFrame(data = np.transpose(np.array(data_values, dtype = 'f')),
                                index = row_index_named, columns = metric_names)
            return output
        
        #request
        print("requesting 1")       
        request = RunReportRequest(
                property='properties/'+property_id,
                dimensions=[Dimension(name="month"),
                            Dimension(name="browser")],
                metrics=[Metric(name="averageSessionDuration"),
                        Metric(name="totalUsers")],
                #order_bys = [OrderBy(dimension = {'dimension_name': 'month'}),
                #            OrderBy(dimension = {'dimension_name': 'sessionMedium'})],
                date_ranges=[DateRange(start_date=str(userInput[3]), end_date=str(userInput[4]))],
            )

        #output df to csv
        print("outputting 1 to csv")
        output_df = format_report(request)
        output_df.to_csv('Example-Report-'+str(userInput[3])+'report1'+'.csv')
        
        #report done
        print('done with report 1')

    ############################
    #########REPORT TWO#########
    ############################

        #global variables
        print("setting global variables 2")
        time.sleep(.5)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(userInput[2])
        property_id = str(userInput[1])
        client = BetaAnalyticsDataClient()

        #format
        print("formatting 2")
        def format_report(request):
            response = client.run_report(request)
            row_index_names = [header.name for header in response.dimension_headers]
            row_header = []
            for i in range(len(row_index_names)):
                row_header.append([row.dimension_values[i].value for row in response.rows])
            row_index_named = pd.MultiIndex.from_arrays(np.array(row_header), names = np.array(row_index_names))
            metric_names = [header.name for header in response.metric_headers]
            data_values = []
            for i in range(len(metric_names)):
                data_values.append([row.metric_values[i].value for row in response.rows])
            output = pd.DataFrame(data = np.transpose(np.array(data_values, dtype = 'f')),
                                index = row_index_named, columns = metric_names)
            return output
        
        #request
        print("requesting 2")       
        request = RunReportRequest(
                property='properties/'+property_id,
                dimensions=[Dimension(name="month")],
                metrics=[Metric(name="averageSessionDuration")],
                #order_bys = [OrderBy(dimension = {'dimension_name': 'month'}),
                #            OrderBy(dimension = {'dimension_name': 'sessionMedium'})],
                date_ranges=[DateRange(start_date=str(userInput[3]), end_date=str(userInput[4]))],
            )

        #output df to csv
        print("outputting 2 to csv")
        output_df = format_report(request)
        output_df.to_csv('Example-Report-'+str(userInput[3])+'report2'+'.csv')
        
        #report done
        print('done with report 2')

    ############################
    #########REPORT THREE#######
    ############################

        #global variables
        print("setting global variables 3")
        time.sleep(.5)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(userInput[2])
        property_id = str(userInput[1])
        client = BetaAnalyticsDataClient()

        #format
        print("formatting 3")
        def format_report(request):
            response = client.run_report(request)
            row_index_names = [header.name for header in response.dimension_headers]
            row_header = []
            for i in range(len(row_index_names)):
                row_header.append([row.dimension_values[i].value for row in response.rows])
            row_index_named = pd.MultiIndex.from_arrays(np.array(row_header), names = np.array(row_index_names))
            metric_names = [header.name for header in response.metric_headers]
            data_values = []
            for i in range(len(metric_names)):
                data_values.append([row.metric_values[i].value for row in response.rows])
            output = pd.DataFrame(data = np.transpose(np.array(data_values, dtype = 'f')),
                                index = row_index_named, columns = metric_names)
            return output
        
        #request
        print("requesting 3")       
        request = RunReportRequest(
                property='properties/'+property_id,
                dimensions=[Dimension(name="region")],
                metrics=[Metric(name="eventsPerSession")],
                #order_bys = [OrderBy(dimension = {'dimension_name': 'month'}),
                #            OrderBy(dimension = {'dimension_name': 'sessionMedium'})],
                date_ranges=[DateRange(start_date=str(userInput[3]), end_date=str(userInput[4]))],
            )

        #output df to csv
        print("outputting 3 to csv")
        output_df = format_report(request)
        output_df.to_csv('Example-Report-'+str(userInput[3])+'report3'+'.csv')
        
        #report done
        print('done with report 3')

    ############################
    #########REPORT FOUR########
    ############################

        #global variables
        print("setting global variables 4")
        time.sleep(.5)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(userInput[2])
        property_id = str(userInput[1])
        client = BetaAnalyticsDataClient()

        #format
        print("formatting 4")
        def format_report(request):
            response = client.run_report(request)
            row_index_names = [header.name for header in response.dimension_headers]
            row_header = []
            for i in range(len(row_index_names)):
                row_header.append([row.dimension_values[i].value for row in response.rows])
            row_index_named = pd.MultiIndex.from_arrays(np.array(row_header), names = np.array(row_index_names))
            metric_names = [header.name for header in response.metric_headers]
            data_values = []
            for i in range(len(metric_names)):
                data_values.append([row.metric_values[i].value for row in response.rows])
            output = pd.DataFrame(data = np.transpose(np.array(data_values, dtype = 'f')),
                                index = row_index_named, columns = metric_names)
            return output
        
        #request
        print("requesting 4")       
        request = RunReportRequest(
                property='properties/'+property_id,
                dimensions=[Dimension(name="pagePath")],
                metrics=[Metric(name="sessions")],
                #order_bys = [OrderBy(dimension = {'dimension_name': 'month'}),
                #            OrderBy(dimension = {'dimension_name': 'sessionMedium'})],
                date_ranges=[DateRange(start_date=str(userInput[3]), end_date=str(userInput[4]))],
            )

        #output df to csv
        print("outputting 4 to csv")
        output_df = format_report(request)
        output_df.to_csv('Example-Report-'+str(userInput[3])+'report4'+'.csv')
        
        #report done
        print('done with report 4')

    ############################
    #########REPORT FIVE########
    ############################

        #global variables
        print("setting global variables 5")
        time.sleep(.5)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(userInput[2])
        property_id = str(userInput[1])
        client = BetaAnalyticsDataClient()

        #format
        print("formatting 5")
        def format_report(request):
            response = client.run_report(request)
            row_index_names = [header.name for header in response.dimension_headers]
            row_header = []
            for i in range(len(row_index_names)):
                row_header.append([row.dimension_values[i].value for row in response.rows])
            row_index_named = pd.MultiIndex.from_arrays(np.array(row_header), names = np.array(row_index_names))
            metric_names = [header.name for header in response.metric_headers]
            data_values = []
            for i in range(len(metric_names)):
                data_values.append([row.metric_values[i].value for row in response.rows])
            output = pd.DataFrame(data = np.transpose(np.array(data_values, dtype = 'f')),
                                index = row_index_named, columns = metric_names)
            return output
        
        #request
        print("requesting 5")       
        request = RunReportRequest(
                property='properties/'+property_id,
                dimensions=[Dimension(name="sessionSource")],
                metrics=[Metric(name="sessions")],
                #order_bys = [OrderBy(dimension = {'dimension_name': 'month'}),
                #            OrderBy(dimension = {'dimension_name': 'sessionMedium'})],
                date_ranges=[DateRange(start_date=str(userInput[3]), end_date=str(userInput[4]))],
            )

        #output df to csv
        print("outputting 5 to csv")
        output_df = format_report(request)
        output_df.to_csv('Example-Report-'+str(userInput[3])+'report5'+'.csv')
        
        #report done
        print('done with report 5')

        print('done with all reports')
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutomateMe!"))
        self.reporttypebutton.setText(_translate("MainWindow", "Report Type"))
        self.propertyidbutton.setText(_translate("MainWindow", "GA Property ID"))
        self.apikeybutton.setText(_translate("MainWindow", "API Credentials"))
        self.startdatebutton.setText(_translate("MainWindow", "Start Date"))
        self.enddatebutton.setText(_translate("MainWindow", "End Date"))
        self.createreportbutton.setText(_translate("MainWindow", "Create Report"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())