# analyticsAutomation
A more efficient way to run multiple web analytics reports.

Modules needed:
PyQT5
Pandas
Numpy
Matplotlib
GRPC/GRPCIO
Google.Analytics.Data.V1Beta

Run Report Steps:
1 - Run V100GUI.py
2 - Input data and press create report
3 - Exit GUI
4 - Run GraphMaker.py
5 - Paste graph images in presentation and analyze!

Inputs:
type = website (app coming soon!)
property_id = ######### (found here)
api = credentials.json (found here)
start date = a date in 20XX-XX-XX format
end date = a date in 20XX-XX-XX format

GA Dimensions Used:
- Date/ month
- Region/Country/City
- Session Source/Medium
- Landing page / page path/ title

GA Metrics Used:
- Events per session
- Average session duration
- Users
- Sessions

Metrics and Dimensions can be seen in the GUI code under "dimension_list"  and "metric_list"

Comment if you have any issues! A few initial problems that I had that you may come across might include folder naming, finding the right credentials, creating a procfile, and possible virtual environment issues.
