from django.contrib import admin
from django.urls import path
from HarmonicProfit.views import (test, test2, home, reflink, login, register, logout, dashboard, apply, activateGiftCard, invest, activate, successpm, failpm, successpy, failpy, successcp, failcp, withdraw, downline, vouchers, investSuccesspm, investFailpm, investSuccesspy, investFailpy, investSuccesscp, investFailcp, invalid, valid, reset_password, password_reset_sent, password_reset_form, password_reset_done, checkmail )


urlpatterns = [
    path('admin', admin.site.urls),
    path('test', test, name='test'),
    path('test2', test2, name='test2'),
    path('', home, name='home'),
    path('ref/<ref>', reflink, name='reflink'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path('reset_password', reset_password, name='reset_password'),
    path('password_reset_sent', password_reset_sent, name='password_reset_sent'),
    path('password_reset_form', password_reset_form, name='password_reset_form'),
    path('password_reset_done', password_reset_done, name='password_reset_done'),
    path('invalid', invalid, name='invalid'),
    path('valid', valid, name='valid'),
    path('token/<token>', checkmail, name='checkmail'),
    path('dashboard', dashboard, name='dashboard'),
    path('apply', apply, name='apply'),
    path('activateGiftCard', activateGiftCard, name='activateGiftCard'),
    path('invest', invest, name='invest'),
    path('activate', activate, name='activate'),
    path('successpm', successpm, name='successpm'),
    path('failpm', failpm, name='failpm'),
    path('successpy', successpy, name='successpy'),
    path('failpy', failpy, name='failpy'),
    path('successcp', successcp, name='successcp'),
    path('failcp', failcp, name='failcp'),
    path('investSuccesspm', investSuccesspm, name='investSuccesspm'),
    path('investFailpm', investFailpm, name='investFailpm'),
    path('investSuccesspy', investSuccesspy, name='InvestSuccesspy'),
    path('investFailpy', investFailpy, name='investFailpy'),
    path('investSuccesscp', investSuccesscp, name='investSuccesscp'),
    path('investFailcp', investFailcp, name='investFailcp'),
    path('withdraw', withdraw, name='withdraw'),
    path('downline', downline, name='downline'),
    path('vouchers', vouchers, name='vouchers'),
]
