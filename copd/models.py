
from django.db import models


# Create your models here.
from VAYU_MAIN.models import User
from copd.doctor_script import generate_report


def namefile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


class AbgAutoTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ph = models.FloatField()
    paco2 = models.FloatField()
    pao2 = models.FloatField()
    o2sat = models.FloatField(default=100.0)
    hco3 = models.FloatField()
    disorder = models.CharField(max_length=50, blank=True)

    def report(self):
        return generate_report(self)


class XrayTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=namefile, blank=True, null=True)
    report = models.CharField(max_length=20,)


class AbgTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ph = models.FloatField()
    paco2 = models.FloatField()
    pao2 = models.FloatField()
    o2sat = models.FloatField(default=100.0)
    hco3 = models.FloatField()
    na = models.FloatField()
    cl = models.FloatField()
    disorder = models.CharField(max_length=50, blank=True)
    is_metabolic_acidosis = models.BooleanField(blank=True, default=False)
    compensation = models.CharField(max_length=30, blank=True)
    anion_gap = models.FloatField(blank=True)
    delta_ratio = models.FloatField(blank=True)
    anion_gap_result = models.CharField(max_length=100, blank=True)
    delta_ratio_result = models.CharField(max_length=100, blank=True)

    def save(
        self, *args, **kwargs
    ):
        self.report = ""
        self.compensation = ""
        self.anion_gap = self.na - (self.cl + self.hco3)
        self.delta_ratio = (self.anion_gap - 12) / (24 - self.hco3)
        if self.ph < 7.40:
            self.disorder = "Acidosis"
            diff_paco2 = 0
            diff_hco3 = 0
            if self.paco2 > 45:
                diff_paco2 = self.paco2 - 45
            elif self.paco2 < 35:
                diff_paco2 = abs(self.paco2 - 35)
            if self.hco3 > 26:
                diff_hco3 = self.hco3 - 26
            elif self.paco2 < 22:
                diff_hco3 = abs(self.hco3 - 22)

            if self.hco3 <= 20 and self.paco2 >= 47:
                self.disorder = "Metabolic Acidosis with Respiratory Acidosis"
            else:
                if diff_hco3 > diff_paco2:
                    self.compensation = "No Compensation"
                    self.disorder = "Metabolic Acidosis"
                    self.is_metabolic_acidosis = True
                    if 4 <= self.anion_gap <= 12:
                        self.anion_gap_result = "Normal"
                    elif self.anion_gap < 4:
                        self.anion_gap_result = "Low"
                    else:
                        self.anion_gap_result = "High"
                        if 0.0 < self.delta_ratio <= 0.4:
                            self.delta_ratio_result = "Normal Anion Gap Metabolic Acidosis (NAGMA)"
                        elif 0.4 < self.delta_ratio <= 0.8:
                            self.delta_ratio_result = "Mixed Normal and High Metabolic Acidosis (NAGMA and HAGMA)"
                        elif 0.8 < self.delta_ratio <= 2.0:
                            self.delta_ratio_result = "Pure High Metabolic Acidosis (HAGMA)"
                        elif self.delta_ratio > 2.0:
                            self.delta_ratio_result = "Mixed High Metabolic Acidosis (HAGMA) with Metabolic Alkalosis "\
                                                    "or Respiratory Acidosis"
                else:
                    self.compensation = "No Compensation"
                    self.disorder = "Respiratory Acidosis"

        elif self.ph > 7.40:
            self.disorder = "Alkalosis"
            diff_paco2 = 0
            diff_hco3 = 0
            if self.paco2 > 45:
                diff_paco2 = self.paco2 - 45
            elif self.paco2 < 35:
                diff_paco2 = abs(self.paco2) - 35
            if self.hco3 > 26:
                diff_hco3 = self.hco3 - 26
            elif self.paco2 < 22:
                diff_hco3 = abs(self.hco3) - 22

            if diff_hco3 > 5 and diff_paco2 > 5:
                self.disorder = "Metabolic Alkalosis with Respiratory Alkalosis"
            else:
                if diff_hco3 > diff_paco2:
                    self.compensation = "No Compensation"
                    self.disorder = "Metabolic Alkalosis"
                else:
                    self.compensation = "No Compensation"
                    self.disorder = "Respiratory Alkalosis"

        if 7.35 <= self.ph <= 7.45:
            if (self.paco2 > 45 and self.hco3 > 26) or (self.paco2 < 35 and self.hco3 < 22):
                self.compensation = "Fully Compensation"
            else:
                if (self.paco2 > 45 and self.hco3 > 26) and (self.paco2 < 35 and self.hco3 < 22):
                    self.compensation = "Partial Compensation"

        super(AbgTest, self).save(*args, **kwargs)

