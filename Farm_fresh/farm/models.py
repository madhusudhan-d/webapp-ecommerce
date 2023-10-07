from django.db import models

# Create your models here.
STATE_CHOICES = (
   ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
   ("Andhra Pradesh","Andhra Pradesh"),
   ("Arunachal Pradesh","Arunachal Pradesh"),
   ("Assam","Assam"),
   ("Bihar","Bihar"),
   ("Chhattisgarh","Chhattisgarh"),
   ("Chandigarh","Chandigarh"),
   ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
   ("Daman and Diu","Daman and Diu"),
   ("Delhi","Delhi"),
   ("Goa","Goa"),
   ("Gujarat","Gujarat"),
   ("Haryana","Haryana"),
   ("Himachal Pradesh","Himachal Pradesh"),
   ("Jammu and Kashmir","Jammu and Kashmir"),
   ("Jharkhand","Jharkhand"),
   ("Karnataka","Karnataka"),
   ("Kerala","Kerala"),
   ("Ladakh","Ladakh"),
   ("Lakshadweep","Lakshadweep"),
   ("Madhya Pradesh","Madhya Pradesh"),
   ("Maharashtra","Maharashtra"),
   ("Manipur","Manipur"),
   ("Meghalaya","Meghalaya"),
   ("Mizoram","Mizoram"),
   ("Nagaland","Nagaland"),
   ("Odisha","Odisha"),
   ("Punjab","Punjab"),
   ("Pondicherry","Pondicherry"),
   ("Rajasthan","Rajasthan"),
   ("Sikkim","Sikkim"),
   ("Tamil Nadu","Tamil Nadu"),
   ("Telangana","Telangana"),
   ("Tripura","Tripura"),
   ("Uttar Pradesh","Uttar Pradesh"),
   ("Uttarakhand","Uttarakhand"),
   ("West Bengal","West Bengal")
)


class Register(models.Model):

    username = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150, null=False, blank=False)
    confirm_password = models.CharField(max_length=150, null=False, blank=False)
    otp = models.CharField(max_length=20)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_username(username):
        try:
            return Register.objects.get(username=username)
        except:
            return False



    def isExists(self):
        if Register.objects.filter(email = self.email):
            return True
        return False


    def __str__(self):
        return self.username


class Profile(models.Model):

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    zipcode = models.IntegerField(null=False, blank=False)
    state = models.CharField(choices=STATE_CHOICES, max_length=100)

    def __str__(self):
        return self.name


class Complaints(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=12)
    subject = models.CharField(max_length=200, null=False, blank=False)
    reason = models.TextField()

    def __str__(self):
        return self.name




class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    Action = models.BooleanField(default=True)

    def __self__(self):
        return self.Name


