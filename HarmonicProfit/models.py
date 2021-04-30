from django.db import models

class User (models.Model):
    firstName = models.CharField(max_length=20, null=False)
    lastName = models.CharField(max_length=15, null=False)
    username = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=30, null=False)
    password = models.CharField(max_length=32, null=False)
    balance = models.FloatField(default=0, null=False)
    withdrawableBalance = models.FloatField(default=0, null=False)
    earnedFromReferral = models.FloatField(default=0, null=False)
    sponsorshipStatus = models.IntegerField(null=False, default=0)
    accountStatus = models.BooleanField(default=0)
    ambassador = models.BooleanField(default=0)
    referredBy = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    useLastNameFirstName = models.BooleanField(default=0)
    removeUsername = models.BooleanField(default=0)
    changeGender = models.BooleanField(default=0)
    
    def __str__(self):
        return self.firstName + " " + self.lastName


class ActivateDeposit (models.Model):
    status = models.BooleanField()
    paymentMethod = models.CharField(max_length=32, null=False)
    userId = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    paymentMethod = models.CharField(max_length=32, null=False)
    date = models.DateField()
    
    def __str__(self):
        return self.date


class Withdrawal (models.Model):
    userId = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    
    def __str__(self):
        return self.userId.username


class Message (models.Model):
    title =  models.CharField(max_length=60)
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField()
    
    def __str__(self):
        return self.title



class Voucher (models.Model):
    owner = models.ForeignKey('User', on_delete=models.CASCADE, null=False, default=0)
    code = models.CharField(max_length=60)
    status = models.BooleanField()
    
    def __str__(self):
        return self.code


class AutopoolList(models.Model):
    fee = models.IntegerField()
    level = models.CharField(max_length=20)
    
    def __str__(self):
        return self.level


class Autopool1(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    receivedInvestment =models.IntegerField()
    
    def __str__(self):
        return self.user.firstName

class Autopool2(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    receivedInvestment =models.IntegerField()
    
    def __str__(self):
        return self.user.firstName
    
class Autopool3(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    receivedInvestment =models.IntegerField()
    
    def __str__(self):
        return self.user.firstName
    
class Autopool4(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    receivedInvestment =models.IntegerField()
    
    def __str__(self):
        return self.user.firstName
    
class Autopool5(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    receivedInvestment =models.IntegerField()
    
    def __str__(self):
        return self.user.firstName
    
class Autopool6(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    receivedInvestment =models.IntegerField()
    
    def __str__(self):
        return self.user.firstName
    
class Autopool7(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    receivedInvestment =models.IntegerField()
    
    def __str__(self):
        return self.user.firstName
    
class Autopool8(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    receivedInvestment =models.IntegerField()
    
    def __str__(self):
        return self.user.firstName
    
class Autopool9(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    receivedInvestment =models.IntegerField()
    
    def __str__(self):
        return self.user.firstName
    
class Autopool10(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    receivedInvestment =models.IntegerField()
    
    def __str__(self):
        return self.user.firstName
    
class PasswordReset(models.Model):
    email = models.EmailField(max_length=30, null=False)
    token = models.CharField(max_length=35,null=False)
    status= models.BooleanField(default=1)
    
    def __str__(self):
        return self.email
