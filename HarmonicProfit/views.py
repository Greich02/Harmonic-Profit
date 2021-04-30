from django.shortcuts import render, redirect
from HarmonicProfit.models import User, ActivateDeposit, AutopoolList, Voucher, PasswordReset, Withdrawal, Autopool1
from HarmonicProfit.forms import RegisterForm, LoginForm
from django.apps import apps
from django.template.loader import get_template
from django.core.mail import EmailMessage
from datetime import date
from django.db.models import Sum
import random
import string
import requests

# misc functions used inside views


def joinNextAutopool(investor, n=1):
    # A function I am quite proud about; it is the main function of the app and the global unilevel mlm system is based on it. It seems more obvious why it is on top :)
    # Check if the investor account is active
    if investor.accountStatus == True and n < 11:
        f = AutopoolList.objects.get(id=n)
        fee = f.fee
        # Place the investor on the appropriate autopool, by default it starts on Autopool1: Note that the functtion is recursive so...
        pool = "Autopool"+str(n)
        Autopool = apps.get_model("HarmonicProfit", pool)
        # Find in the aautopool the investor is joining the first member that has received a paymment less than 3 times; once it's done create the new investor instance in that pool
        sendTo = Autopool.objects.filter(receivedInvestment__lt=3).first()
        new = Autopool.objects.create(user=investor, receivedInvestment=0,)
        new.save()
        # If the sendTo returns empty result, which will not be the case:
        if sendTo == None:
            pass
        elif sendTo.receivedInvestment < 2:  # if user receiving payment have received less than 2
            sendTo.receivedInvestment += 1
            sendTo.save()
            sendToId = sendTo.user
            # save user who have recived payment Id in the user's "sentTo" field ???
            # Get user reciveing user instance
            sendToUser = User.objects.get(id=sendToId.id)
            sendToUser.balance += fee  # Add payment to his wallet
            sendToUser.save()
            investor.balance -= fee  # Withdraw payment to new  comer's balance
            investor.save()
        # This case means  he is receiving the third payment right now so  he have  to join next autopool
        else:
            sendTo.receivedInvestment += 1
            sendTo.save()
            sendToId = sendTo.user
            sendToUser = User.objects.get(id=sendToId.id)
            # We could have  make him join the next autopool quite easily but seems we add a functionality that generates a voucher code  on some level the user get
            # So if he is not on last level:
            if n != 10:
                # And if he is either on third level
                if n == 3:
                    createVoucher(sendToUser, 1)
                    sendToUser.balance -= 15
                    sendToUser.withdrawableBalance += fee
                    sendToUser.save()
                # Or sixth
                elif n == 6:
                    createVoucher(sendToUser, 2)
                    sendToUser.balance -= 30
                    sendToUser.save()
                    sendToUser.withdrawableBalance += fee
                    sendToUser.save()
                # Or nineth
                elif n == 9:
                    createVoucher(sendToUser, 3)
                    sendToUser.balance -= 45
                    sendToUser.save()
                    sendToUser.withdrawableBalance += fee
                    sendToUser.save()
                else:
                    pass
            # Then supposing he reached the last level
            else:
                sendToUser.withdrawableBalance += fee
                sendToUser.withdrawableBalance += (fee*2)
                sendToUser.balance -= (fee*2)
                sendToUser.save()
            sendToUser.sponsorshipStatus = n+1
            sendToUser.save()
            investor.balance -= fee
            investor.save()
            n += 1
            # Here we make the user join the next  autopool and do same while there is a user with upgrade posssibilities
            try:
                joinNextAutopool(sendToUser, n)
            except UnboundLocalError:
                pass
    else:
        pass


def testFunction(user):
    # This funtion has been used to test the function above
    lName = createCode(8)
    fName = createCode(8)
    uName = createCode(8)
    email = createCode(8)+"@"+createCode(4)+".com"
    password = createCode(8)
    balance = 15
    referredBy = user

    investor = User.objects.create(
        lastName=lName,
        firstName=fName,
        username=uName,
        email=email,
        password=password,
        balance=balance,
        referredBy=referredBy,
        accountStatus=1
    )
    investor.save()
    joinNextAutopool(investor)
    return (investor)


def test(request):
    # ... To reach the test page
    return render(request, 'dashboard/test2.html')


def test2(request):
    # ... Saame thing
    if request.method == "POST":
        if request.POST["number"]:
            n = request.POST["number"]
        else:
            n = 0
        if request.POST["number2"]:
            n2 = request.POST["number2"]
        else:
            n2 = 0
        loggedUser = getLoggedUser(request)
        createVoucher(loggedUser, n2)
        for i in range(int(n)):
            i = testFunction(loggedUser)
        return render(request, 'dashboard/test.html')
    else:
        return render(request, 'dashboard/test.html')


def getLoggedUser(request):
    # This function will be called to  check if user is  logged in using session variables
    if 'loggedUserId' in request.session:
        loggedUserId = request.session['loggedUserId']
        if len(User.objects.filter(id=loggedUserId)) == 1:
            return User.objects.get(id=loggedUserId)
        else:
            return None
    else:
        return None


def success(status, amount):
    # Function called for successful payment
    if status == "success" or status == "ok" or status == "U222021000" and amount == 15:
        return True
    else:
        return False


def fail(request):
    #  You guessed it
    error = "Failed payment"
    return render(request, 'activate.html', {'error': error})


def activation(loggedUser, paymentMethod):
    # We use this function to activate user account once paymennt has been processed
    userId = loggedUser.id
    deposit = ActivateDeposit(
        status=True,
        userId=userId,
        paymentMethod=paymentMethod,
        date=date.today()
    )
    deposit.save()
    l = loggedUser.referredBy
    g = User.objects.get(id=l)
    g.withdrawableBalance += 10
    g.earnedFromReferral += 10
    g.save()
    User.objects.filter(id=loggedUser.id).update(accountStatus=True)


def createCode(length):
    # choose from all upppercase letter
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return(result_str)


def createToken(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return(result_str)


def createVoucher(user, n=1):
    # Earlier we created vouchers; we used this function to achieve it
    if int(n) > 1:
        o = user
        c = createCode(10)
        new = Voucher.objects.create(code=c, owner=o, status=True)
        new.save()
        i = int(n)
        i -= 1
        createVoucher(o, i)
    else:
        pass


# End misc functions used in views

# home-register-login functions


def home(request):
    #  Not much to say if not it renders home  with somme variables
    us = User.objects.all().count()
    t = Autopool1.objects.all().count()
    ti = t*30
    tw = Withdrawal.objects.all().aggregate(w=Sum('amount')).get('w')
    v1 = us/10
    v2 = v1 + random.randint(0, 10)
    return render(request, 'home.html', {'us': us, 'ti': ti, 'tw': tw, 'v2': v2})


def reflink(request, ref):
    # To track referral links; quite  useful function
    if len(ref) == 0:
        return render("home")
    else:
        request.session["ref"] = ref
        return redirect("home")


def login(request):
    # Another classic to for authentication. Let's move on
    loggedUser = getLoggedUser(request)
    if loggedUser:
        return redirect('dashboard')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                if User.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
                    loggedUser = User.objects.get(
                        email=request.POST['email'], password=request.POST['password'])
                    request.session["loggedUserId"] = loggedUser.id
                    # request.session.set_expiry(10)
                    # it shows home page
                    return render(request, "dashboard/dashboard.html", {"loggedUser": loggedUser})
                elif User.objects.filter(email=request.POST['email']).exists():
                    return render(request, 'login.html', {
                        'form': form,
                        'error_message': 'Password does not match.'
                    })
                else:
                    return render(request, 'login.html', {
                        'form': form,
                        'error_message': 'User not found.'})
        # it shows again login page
        return render(request, "Login.html")


def register(request):
    # Obvious
    loggedUser = getLoggedUser(request)
    if loggedUser:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = RegisterForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # referral instanciation
                r = User.objects.filter(
                    username=form.cleaned_data['referredBy']).exists()
                if User.objects.filter(username=form.cleaned_data['username']).exists():
                    return render(request, 'register.html', {
                        'form': form,
                        'error_message': 'This username is already taken. Please choose another one'
                    })
                elif User.objects.filter(email=form.cleaned_data['email']).exists():
                    return render(request, 'register.html', {
                        'form': form,
                        'error_message': 'This Email is already registered.'
                    })
                elif form.cleaned_data['password'] != form.cleaned_data['confirmPassword']:
                    return render(request, 'register.html', {
                        'form': form,
                        'error_message': 'Passwords do not match.'
                    })
                elif r == False:
                    return render(request, 'register.html', {
                        'form': form,
                        'error_message': "Enter a referral ID or enter Harmonic-profit as default in the 'Referred by' field "})
                else:
                    # Create the user:
                    ref = User.objects.get(
                        username=form.cleaned_data['referredBy'])
                    user = User.objects.create(
                        firstName=form.cleaned_data['firstName'],
                        lastName=form.cleaned_data['lastName'],
                        username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'],
                        password=form.cleaned_data['password'],
                        referredBy=ref
                    )
                    user.save()
                    return redirect('login')
        else:
            form = RegisterForm()
            r = request.session.get('ref')
        return render(request, 'register.html', {'form': form, 'r': r})


def logout(request):
    # Classic
    del request.session["loggedUserId"]
    return redirect('login')

# Password reset


def reset_password(request):
    # ...
    return render(request, 'reset/reset_password.html')


def password_reset_sent(request):
    # It send password reset link via  mail to the email retrieved from POST request
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            sendmail(request.POST["email"])
            return render(request, 'reset/password_reset_sent.html')
        except User.DoesNotExist:
            error_message = 'Email not registered'
            return render(request, 'reset/reset_password.html', {'error_message': error_message})
    else:
        return render(request, 'reset/reset_password.html')


def password_reset_form(request):
    # A form to get and check email we are going to  reset password of
    if request.method == 'POST':
        if request.POST["newPassword"] == request.POST["confirmNewPassword"]:
            u = User.objects.get(email=request.session["resetEmail"])
            u.password = request.POST["newPassword"]
            u.save()
            return redirect('password_reset_done')
        else:
            error_message = "Password should match"
            return render(request, 'reset/password_reset_form.html', {'error_message': error_message})
    else:
        return render(request, 'reset/password_reset_form.html')


def password_reset_done(request):
    # successfully reset password
    return render(request, 'reset/password_reset_done.html')


def sendmail(mail):
    # This function... send mails ... to reset email
    token = createToken(30)
    PasswordReset.objects.create(email=mail, token=token, status=True)
    u = User.objects.get(email=mail)
    user = u.firstName
    ctx = {'token': token, 'user': user}
    message = get_template('reset/mail.html').render(ctx)
    msg = EmailMessage(
        'Password reset',
        message,
        'Harmonic-profit',
        [mail],
    )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()


def checkmail(request, token):
    # Ok this one check the token send with reset link in order to allow  reset email
    if request.method == "GET":
        try:
            p = PasswordReset.objects.get(token=token, status=True)
            request.session["resetEmail"] = p.email
            p.status = False
            p.save()
            return redirect('valid')
        except PasswordReset.DoesNotExist:
            return redirect('invalid')
    else:
        return redirect('invalid')


def invalid(request):
    # Returns error page
    error_message = "Invalid reset link"
    return render(request, 'reset/reset_password.html', {'error_message': error_message})


def valid(request):
    #  All right
    return render(request, 'reset/password_reset_form.html')

# End home-register-login functions
# End password reset

# dashboard functions


def dashboard(request):
    # Renders dashboard  with appropriates var
    loggedUser = getLoggedUser(request)
    if loggedUser:
        if loggedUser.sponsorshipStatus == 0:
            s = "BRONZE"
        elif loggedUser.sponsorshipStatus in range(1, 4):
            s = "SILVER"
        elif loggedUser.sponsorshipStatus in range(4, 7):
            s = "GOLD"
        elif loggedUser.sponsorshipStatus in range(7, 10):
            s = "PLATINIUM"
        else:
            s = "TITANIUM"
        re = User.objects.filter(referredBy=loggedUser)
        if len(re) < 5:
            r = "PARTNER"
        elif len(re) in range(5, 10):
            r = "AMBASSADOR II"
        else:
            r = "DIRECTOR"
        return render(request, 'dashboard/dashboard.html', {"loggedUser": loggedUser, "s": s, "r": r})
    else:
        return redirect('login')


def apply(request):
    # Intersting functionality  to  change business card appearence on dashboard
    if request.method == 'POST':
        loggedUser = getLoggedUser(request)
        User.objects.filter(id=loggedUser.id).update(
            useLastNameFirstName=request.POST.get(
                "useLastNameFirstName", False),
            removeUsername=request.POST.get("removeUsername", False),
            changeGender=request.POST.get("changeGender", False)
        )
        return redirect('dashboard')


def activateGiftCard(request):
    #  Use this to activate account with gift card. I set a builtin gift card named "AMBASSADOR"
    if request.method == 'POST':
        loggedUser = getLoggedUser(request)
        if Voucher.objects.filter(code=request.POST["code"], status=True).exists():
            User.objects.filter(id=loggedUser.id).update(accountStatus=True)
            message = "Account activated"
            Voucher.objects.filter(
                code=request.POST["code"]).update(status=False)
            return redirect('dashboard')
        elif request.POST["code"] == "AMBASSADOR":
            User.objects.filter(id=loggedUser.id).update(
                accountStatus=True, ambassador=True)
            return redirect('dashboard')
        else:
            message = {"message": "Gift code not valid"}
            return render(request, 'dashboard/activate.html', message)
    else:
        return redirect('activate')


def invest(request):
    #  Renders invest page
    loggedUser = getLoggedUser(request)
    if loggedUser:
        return render(request, 'dashboard/invest.html', {"loggedUser": loggedUser})
    else:
        return redirect('login')


def activate(request):
    # ...
    loggedUser = getLoggedUser(request)
    if loggedUser:
        return render(request, 'dashboard/activate.html', {"loggedUser": loggedUser})
    else:
        return redirect('login')


def withdraw(request):
    # ...
    loggedUser = getLoggedUser(request)
    if loggedUser:
        return render(request, 'dashboard/withdraw.html', {"loggedUser": loggedUser})
    else:
        return redirect('login')


def downline(request):
    # Returns the list of all users we referred
    loggedUser = getLoggedUser(request)
    if loggedUser:
        try:
            referrals = User.objects.all().filter(referredBy=loggedUser.id)
        except User.DoesNotExist:
            return render(request, 'dashboard/downline.html', {"loggedUser": loggedUser, 'referrals': referrals})
        return render(request, 'dashboard/downline.html', {"loggedUser": loggedUser, 'referrals': referrals})
    else:
        return redirect('login')


def vouchers(request):
    # Displays the list of gift card  owned by  user
    loggedUser = getLoggedUser(request)
    if loggedUser:
        if loggedUser.sponsorshipStatus == 0:
            s = "BRONZE"
        elif loggedUser.sponsorshipStatus in range(1, 4):
            s = "SILVER"
        elif loggedUser.sponsorshipStatus in range(4, 7):
            s = "GOLD"
        elif loggedUser.sponsorshipStatus in range(7, 10):
            s = "PLATINIUM"
        else:
            s = "TITANIUM"
        re = User.objects.filter(referredBy=loggedUser)
        if len(re) < 5:
            r = "PARTNER"
        elif len(re) in range(5, 10):
            r = "AMBASSADOR II"
        else:
            r = "DIRECTOR"
        if Voucher.objects.filter(owner=loggedUser.id, status=True).exists():
            v = True
        else:
            v = False
        try:
            vouchers = Voucher.objects.all().filter(owner=loggedUser.id, status=True)
        except Voucher.DoesNotExist:
            return render(request, 'dashboard/vouchers.html', {"loggedUser": loggedUser, 'vouchers': vouchers, 'v': v, "s": s, "r": r})
        return render(request, 'dashboard/vouchers.html', {"loggedUser": loggedUser, 'vouchers': vouchers, 'v': v, "s": s, "r": r})
    else:
        return redirect('login')


# End dashboard functions

# Payment gateways views

# Activation


def successpm(request):
    paymentMethod = "Perfect Money"
    s = success(request.POST["PAYEE_ACCOUNT"], request.POST["PAYMENT_AMOUNT"])
    if s == True:
        loggedUser = request.session["loggedUser"]
        activation(loggedUser, paymentMethod)
        return redirect('dashboard')


def failpm(request):
    return redirect(request, 'fail')


def successpy(request):
    paymentMethod = "Payeer"
    m_status = request.POST["m_status"]
    m_amount = request.POST["m_amount"]
    s = success(m_status, m_amount)
    if s == True:
        loggedUser = request.session["loggedUser"]
        activation(loggedUser, paymentMethod)
        return redirect('dashboard')


def failpy(request):
    return redirect(request, 'fail')


def successcp(request):
    paymentMethod = "Coinpayments"
    response = requests.get('https://www.coinpayments.net/api.php')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    m_status = jsonResponse["error"]
    m_amount = jsonResponse["result"]["m_amount"]
    s = success(m_status, m_amount)
    if s == True:
        loggedUser = request.session["loggedUser"]
        activation(loggedUser, paymentMethod)
        return redirect('dashboard')


def failcp(request):
    return redirect(request, 'fail')

# End Activation

# Investment
# Those functions are used to proceed to investment. Not much to say about


def errorInvest(request):
    loggedUser = request.session["loggedUser"]
    if loggedUser.accountStatus == False:
        error_message = "Activate your account first"
        if request.POST["pmethod"] == "pm":
            return render(request, "invest.html", {"loggedUser": loggedUser, "error_messagepm": error_message})
        elif request.POST["pmethod"] == "py":
            return render(request, "invest.html", {"loggedUser": loggedUser, "error_messagepy": error_message})
        else:
            return render(request, "invest.html", {"loggedUser": loggedUser, "error_messagecp": error_message})


def investSuccesspm(request):
    s = success(request.POST["PAYEE_ACCOUNT"], request.POST["PAYMENT_AMOUNT"])
    if s == True:
        loggedUser = request.session["loggedUser"]
        joinNextAutopool(loggedUser)
        return redirect('dashboard')


def investFailpm(request):
    return redirect(request, 'fail')


def investSuccesspy(request):
    m_status = request.POST["m_status"]
    m_amount = request.POST["m_amount"]
    s = success(m_status, m_amount)
    if s == True:
        loggedUser = request.session["loggedUser"]
        joinNextAutopool(loggedUser)
        return redirect('dashboard')


def investFailpy(request):
    return redirect(request, 'fail')


def investSuccesscp(request):
    response = requests.get('https://www.coinpayments.net/api.php')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    m_status = jsonResponse["error"]
    m_amount = jsonResponse["result"]["m_amount"]
    s = success(m_status, m_amount)
    if s == True:
        loggedUser = request.session["loggedUser"]
        joinNextAutopool(loggedUser)
        return redirect('dashboard')


def investFailcp(request):
    return redirect(request, 'fail')

# End Activation

# Withdraw
# Same as investment functions


def withdrawProcess(request):
    loggedUser = request.session["loggedUser"]
    message = "Invalid amount"
    if loggedUser.withdrawableBalance >= request.POST["amount"] and request.POST["amount"] > 10:
        if request.POST["pmethod"] == "pm":
            request.POST["amount"] = request.POST["sumIn"]
            request.POST["apiPass"] = "49365846"
            return render(request, "https://payeer.com/merchant/")
        elif request.POST["pmethod"] == "py":
            request.POST["amount"] = request.POST["sum"]
            request.POST["apiPass"] = "49365846"
            return render(request, "https://payeer.com/merchant/")
        else:
            request.POST["amount"] = request.POST["sum"]
            return render(request, "https://www.coinpayments.net/api.php")
        loggedUser.withdrawableBalance -= request.POST["amount"]
        loggedUser.save()
        Withdrawal.objects.create(
            userId=loggedUser, amount=request.POST["amount"])
    else:
        return render(request, "withdraw.html", {"loggedUser": loggedUser, "message": message})

# End withdraw
# End Payment gateways views
