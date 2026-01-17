from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),      #new done
    path('courses',views.AllCoursesListView.as_view(),name='courses'),   # new done
    path('course-detail/<str:course_name>/',views.CourseDetailView.as_view(),name='course_detail'),  # new done
    path('ccc',views.ccc,name='ccc'),
    path('tally',views.tally,name='tally'),
    path('dca',views.dca,name='dca'),
    path('codding',views.codding,name='codding'),
    path('admission', views.admissions, name='admission'),
    path('insertadmission',views.addadmission, name='insertadmission'),     # done
    path('session-login',views.session_login,name='session_login'),
    # path('fetch',views.fetch,name='fetch'),
    path('logout',views.session_logout,name='logout'),
    
    # path('data',views.dataform,name="data"),
    path('showsearch',views.showsearch,name="showsearch"),  # form done
    path('showcertificate',views.showcertificate,name="showcertificate"),       # form done
    path('vocational',views.vocationalcourse,name='vocational'),    # Done
    path('advdiploma', views.AdvDiploma, name='advdiploma'),    # Done
    path('diploma', views.Diploma, name='diploma'),     # Done
    path('certificate', views.Certificate, name='certificate'), # Done
    path('payment',views.payment,name='payment'),   # done
    path('showid',views.showid,name='showid'),      # form done
    path('feestatus',views.fees_status,name='feestatus'),   # form done
    path('do_payment',views.do_payment,name='do_payment'),
    path('generate-certificate',views.generate_certificate,name='generate-certificate'),        # form done
    path('certi-generated',views.certi_generated,name='certi-generated'),
    path('all-students',views.AllStudentsListView.as_view(),name='all-students'),   # done

]
