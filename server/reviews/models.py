from django.db import models
from django.contrib.auth.models import User
from dealers.models import Dealer

class Review(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    purchase = models.BooleanField(default=False)
    purchase_date = models.DateField(blank=True, null=True)
    car_make = models.CharField(max_length=50, blank=True, null=True)
    car_model = models.CharField(max_length=50, blank=True, null=True)
    car_year = models.IntegerField(blank=True, null=True)
    sentiment = models.CharField(max_length=20, blank=True, null=True)  # positive, negative, neutral
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.dealer.name}"

    class Meta:
        db_table = 'reviews'
        ordering = ['-created_at']
