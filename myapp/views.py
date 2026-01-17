from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from http.client import HTTPResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator


global_image_variable = None


# Create your views here.
def dataform(request):
    return render(request, 'form.html')

def payment(request):
    return render(request, 'payment.html')


@csrf_exempt
def showcertificate(request):
    if request.method == "POST":
        enroll = request.POST.get('certi')
        reg_no = request.POST.get('reg_no')
        if enroll is None:
            try:
                check = certificate2.objects.get(regno=reg_no)
            except:
                check = None
            if check is not None:
                student = certificate2.objects.filter(regno=reg_no).all()
                return render(request, 'certificate.html', locals())
            else:
                messages.error(request, "No Data Found")
                return render(request, 'search.html')
        else:
            try:
                check = certificate2.objects.get(enroll=enroll)
            except:
                check = None
            if check is not None:
                student = certificate2.objects.filter(enroll=enroll).all()
                return render(request, 'certificate.html', locals())
            else:
                messages.error(request, "No Data Found")
                return render(request, 'search.html')
            
    else:
        return render(request, 'search.html')

def showid(request):
    if request.method == "POST":
        fno=request.POST.get('formnumber')
        try:
            check = admission.objects.get(formno=fno)
        except:
            check = None
        if check is not None:
            idstudent = admission.objects.filter(formno=fno).first()
            return render(request,'id.html', locals())
        else:
            messages.error(request,"Admission Not Found")
            return render(request,'searchid.html')
    else:
        return render(request, 'searchid.html')

@csrf_exempt
def showsearch(request):
    if request.method == "POST":
        enroll = request.POST.get('enroll')
        try:
            check = certificate2.objects.get(enroll=enroll)
        except:
            check = None
        if check is not None:
            education = certificate2.objects.filter(enroll=enroll).first()
            if education:
                messages.success(request, "Data Found")
            else:
                messages.error(request, "No Data Found")
            return render(request, 'verify.html', locals())
        else:
            messages.error(request, "No Data Found")
            return render(request, 'verify.html')
    else:
        return render(request, 'verify.html')

def index(request):
    return render(request,'index.html')


@method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='session_login'), name='dispatch')
class AllStudentsListView(ListView):
    model = admission
    context_object_name = 'students'
    template_name = 'students.html'
    paginate_by = 10 
    paginate_orphans = 5
    sort_field = [
        'formno',
        'usersname',
        'doa',
    ]

    def get_queryset(self):
        # will use filter and sorting here
        sort = self.request.GET.get("sort")
        ord = self.request.GET.get("ord", "asc")
        q = self.request.GET.get("q", "")
        
        qs = admission.objects.all().order_by('-id')
        if q:
            qs = qs.filter(
                Q(formno__icontains=q) |
                Q(usersname__icontains=q) |
                Q(course__icontains=q)
            )

        if sort and sort in self.sort_field:
            if ord == "desc":
                sort = "-" + sort
            qs = qs.order_by(sort)

        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Access paginator and page_obj from context
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')

        if paginator and page_obj:
            start_pos = (page_obj.number - 1) * self.paginate_by + 1
            end_pos = start_pos + len(context['students']) - 1
            page_list = f'Showing {start_pos} to {end_pos} of {paginator.count} students'
        else:
            page_list = ''

        context['page_list'] = page_list
        return context

def courses(request):
    getcourse = detailcourse.objects.all()
    return render(request,'courses.html',locals())

class AllCoursesListView(ListView):
    model = admission
    context_object_name = 'courses'
    template_name = 'courses.html'
    paginate_by = 10 
    paginate_orphans = 5

    def get_queryset(self):
        # will use filter and sorting here
        return detailcourse.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Access paginator and page_obj from context
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')

        if paginator and page_obj:
            start_pos = (page_obj.number - 1) * self.paginate_by + 1
            end_pos = start_pos + len(context['courses']) - 1
            page_list = f'Showing {start_pos} to {end_pos} of {paginator.count} courses'
        else:
            page_list = ''

        context['page_list'] = page_list
        return context

def vocationalcourse(request):
    getcourse = detailcourse.objects.filter(program='4')
    return render(request, 'courses.html', locals())

def AdvDiploma(request):
    getcourse = detailcourse.objects.filter(program='3')
    return render(request, 'courses.html', locals())

def Diploma(request):
    getcourse = detailcourse.objects.filter(program='2')
    print(getcourse)
    return render(request, 'courses.html', locals())

def Certificate(request):
    getcourse = detailcourse.objects.filter(program='1')
    return render(request, 'courses.html', locals())

def contactus(request):
    return render(request,'contactus.html')

def about(request):
    return render(request,'about.html')

def ccc(request):
    return render(request,'ccc.html')

def tally(request):
    return render(request,'tally.html')

def dca(request):
    return render(request,'dca.html')

def codding(request):
    return render(request,'codding.html')

def admissions(request):
    return render(request,'admission.html')


@user_passes_test(lambda u: u.is_superuser, login_url='session_login')
def addadmission(request):
    if request.method == 'POST':
        usersname = request.POST.get('usname')
        dateofadmission = request.POST.get('udoa')
        formno = request.POST.get('formno')
        dateofbirth = request.POST.get('udob')
        mobileno = request.POST.get('umob')
        usercourse = request.POST.get('ucourse')
        userimage = request.FILES['uimage']
        timing = request.POST.get('timing')
        total_fees = request.POST.get('t_fees')
        paid_fees = request.POST.get('p_fees')
        due_fees = int(total_fees) - int(paid_fees)
        add = admission(usersname=usersname,image=userimage,mobile=mobileno,doa=dateofadmission,formno=formno,dob=dateofbirth,course=usercourse,batch_time=timing)
        add.save()
        fee = fees(form_no=formno,total=total_fees,paid=paid_fees,due=due_fees)
        fee.save()
        payment = paid_log(form_no=formno,fee=paid_fees,fee_date=dateofadmission)
        payment.save()
        messages.info(request, "Admission Confirmed")
    else:
        messages.error(request, "Error Occured Try Again")

    return redirect('admission')

def session_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        upass = request.POST.get('pass')
        
        user = authenticate(request, username=uname, password=upass)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully")
            return redirect(index)
        else:
            messages.error(request, "Invalid Login")
            return redirect(session_login)
        
    return render(request,'login.html')

@user_passes_test(lambda u: u.is_superuser, login_url='session_login')
@csrf_exempt
def fees_status(request):
    if request.method == "POST":
        form_no = request.POST.get('form_no')
        try:
            user = admission.objects.get(formno=form_no)
            fee_structure = fees.objects.get(form_no=form_no)
            
        except:
            user = None
            fee_structure = None
            
        if user is not None and fee_structure is not None:
            payroll = paid_log.objects.filter(form_no=form_no).all()
            total_amount = fee_structure.total
            paid_amount = fee_structure.paid
            due_amount = int(total_amount) - int(paid_amount)
            if due_amount==0:
                fee_left = "false"
            else:
                fee_left = "true"
            return render(request, "feedetails.html", locals())
        else:
            messages.error(request, "No details related to this Form No")
            return render(request, "feesearch.html")
    else:
        return render(request, "feesearch.html")
            

def session_logout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect(index)

@user_passes_test(lambda u: u.is_superuser, login_url='session_login')
@csrf_exempt
def do_payment(request):
    if request.method == "POST":
        form_no = request.POST.get('form_no')
        amount = request.POST.get('fee')
        date = request.POST.get('date')
        log = paid_log(form_no=form_no,fee=amount,fee_date=date)
        log.save()
        try:
            fee_obj = fees.objects.get(form_no=form_no)
        except:
            fee_obj = None
        if fee_obj is not None:
            total_amount = fee_obj.total
            paid_amount = fee_obj.paid
            due_amount = fee_obj.due
            paid_amount = int(paid_amount) + int(amount)
            due_amount = int(total_amount) - int(paid_amount)
            fee_obj.paid = paid_amount
            fee_obj.due = due_amount
            fee_obj.save()
            messages.info(request, "Fee Payment Successful ")
            return redirect(fees_status)
        else:
            messages.error(request, "Error in Fee Payment !!!!")
            return render(request, "feesearch.html")
    else:
        messages.error(request, "Error in Fee Payment !!!")
        return render(request, "feesearch.html")

@user_passes_test(lambda u: u.is_superuser, login_url='session_login')
def generate_certificate(request):
    global global_image_variable
    if request.method == "POST":
        form_no = request.POST.get('form_no')
        try:
            user = admission.objects.get(formno=form_no)
        except:
            user = None
        if user is not None:
            global_image_variable = user.image
            return render(request,'certificate-data.html', locals())
        else:
            messages.error(request, "No Admission Related to this Form No !!!!")
            return redirect(generate_certificate)
    else:
        return render(request, "generate.html")

@user_passes_test(lambda u: u.is_superuser, login_url='session_login')
def certi_generated(request):
    global global_image_variable
    if request.method == "POST":
        regno = request.POST.get('regno')
        name = request.POST.get('uname')
        course = request.POST.get('course')
        course_details = request.POST.get('detail')
        enrollment = request.POST.get('enroll_no')
        grade = request.POST.get('grade')
        course_duration = request.POST.get('duration')
        certi_date = request.POST.get('date')
        if 'uimage' in request.FILES:
            user_image = request.FILES['uimage']
        else:
            user_image = global_image_variable
            global_image_variable = None
        add_certificate = certificate2(regno=regno,name=name,course=course,detail=course_details,enroll=enrollment,grade=grade,duration=course_duration,date=certi_date,image=user_image)
        add_certificate.save()
        messages.info(request, "Certified Successfully")
        return redirect(certi_generated)
    else:
        return redirect(generate_certificate)
        
# 404 handler
def handler404(request, exception):
    return render(request, '404.html', status=404)

# 500 handler
def handler500(request):
    return render(request, '500.html', status=500)

# Couse Detail View
class CourseDetailView(View):
    def get(self, request, course_name):
        course = get_object_or_404(
            Course,
            course_alias = course_name
        )
        techs_list = course.techs.split(',')
        eligibility_list = course.eligibility.split(',')
        
        return render(request, 'detail_course.html', locals())


