from django.urls import path
from .views import *

urlpatterns = [
    
    path('',trial,name ='trial'),
    
    path('addpatient',add_patient_info,name='patient'),
    path('register',registerUser,name ='adduser'),
    path('login',opd_login,name ='ologin'),
    path('opd_graphview',opd_graphview, name ='opdgraph_view'),
    path('opd_dataview', opd_dataview,name = 'data'),
    path('opdmedical',medical_info,name='medical_info'),
    path('searchopd',searchUser,name = "searcher"),
    path('signout',signout,name = 'sout'),


    #pharmacy urls
    path('pharmlogin',pharmacy_login,name ="pharmacy_login"),
    path('pharm_data',pharmacy_dataview, name ="pharmacy_data"),
    path('pharm_graph',pharmacy_graphview,name = "pharmacy_graph"),

    #laboratory urls
    path('lablogin',lab_login,name ="lab_login"),
    path('lab_data',lab_dataview, name ="lab_data"),
    path('lab_graph',lab_graphview,name = "lab_graph"),

    #physician urls
    path('phylogin',physician_login,name ="phy_login"),
    path('phydata',physician_dataview, name ="phy_dara"),
    path('phygraph',physician_graphview,name = "phy_graph"),
]
