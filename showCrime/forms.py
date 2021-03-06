from django import forms

BeatChoices = ( ('01X','01X'), ('02X','02X'), ('02Y','02Y'), ('03X','03X'), ('03Y','03Y'), ('04X','04X'), 
    ('05X','05X'), ('05Y','05Y'), ('06X','06X'), ('07X','07X'), ('08X','08X'), ('09X','09X'), ('10X','10X'), 
    ('10Y','10Y'), ('11X','11X'), ('12X','12X'), ('12Y','12Y'), ('13X','13X'), ('13Y','13Y'), ('13Z','13Z'), 
    ('14X','14X'), ('14Y','14Y'), ('15X','15X'), ('16X','16X'), ('16Y','16Y'), ('17X','17X'), ('17Y','17Y'), 
    ('18X','18X'), ('18Y','18Y'), ('19X','19X'), ('20X','20X'), ('21X','21X'), ('21Y','21Y'), ('22X','22X'), 
    ('22Y','22Y'), ('23X','23X'), ('24X','24X'), ('24Y','24Y'), ('25X','25X'), ('25Y','25Y'), ('26X','26X'), 
    ('26Y','26Y'), ('27X','27X'), ('27Y','27Y'), ('28X','28X'), ('29X','29X'), ('30X','30X'), ('30Y','30Y'), 
    ('31X','31X'), ('31Y','31Y'), ('31Z','31Z'), ('32X','32X'), ('32Y','32Y'), ('33X','33X'), ('34X','34X'), 
    ('35X','35X'), ('35Y','35Y') )

CrimeCatChoices = ( ("ARSON","ARSON"),
    ("ASSAULT","ASSAULT"),
    ("ASSAULT_FIREARM","ASSAULT_FIREARM"),
    ("ASSAULT_FIREARM_FELONY","ASSAULT_FIREARM_FELONY"),
    ("ASSAULT_FIREARM_MISDEMEANOR","ASSAULT_FIREARM_MISDEMEANOR"),
    ("ASSAULT_HANDS-FISTS-FEET","ASSAULT_HANDS-FISTS-FEET"),
    ("ASSAULT_HANDS-FISTS-FEET_FELONY","ASSAULT_HANDS-FISTS-FEET_FELONY"),
    ("ASSAULT_HANDS-FISTS-FEET_MISDEMEANOR","ASSAULT_HANDS-FISTS-FEET_MISDEMEANOR"),
    ("ASSAULT_KNIFE","ASSAULT_KNIFE"),
    ("ASSAULT_KNIFE_FELONY","ASSAULT_KNIFE_FELONY"),
    ("ASSAULT_KNIFE_MISDEMEANOR","ASSAULT_KNIFE_MISDEMEANOR"),
    ("ASSAULT_OTHER-SIMPLE","ASSAULT_OTHER-SIMPLE"),
    ("ASSAULT_OTHER-SIMPLE_FELONY","ASSAULT_OTHER-SIMPLE_FELONY"),
    ("ASSAULT_OTHER-SIMPLE_MISDEMEANOR","ASSAULT_OTHER-SIMPLE_MISDEMEANOR"),
    ("ASSAULT_OTHER-WEAPON","ASSAULT_OTHER-WEAPON"),
    ("ASSAULT_OTHER-WEAPON_FELONY","ASSAULT_OTHER-WEAPON_FELONY"),
    ("ASSAULT_OTHER-WEAPON_MISDEMEANOR","ASSAULT_OTHER-WEAPON_MISDEMEANOR"),
    ("ASSAULT_PEACE-OFFICER","ASSAULT_PEACE-OFFICER"),
    ("ASSAULT_PEACE-OFFICER_FELONY","ASSAULT_PEACE-OFFICER_FELONY"),
    ("ASSAULT_PEACE-OFFICER_MISDEMEANOR","ASSAULT_PEACE-OFFICER_MISDEMEANOR"),
    ("ASSAULT_THREATS","ASSAULT_THREATS"),
    ("COURT","COURT"),
    ("COURT_CONTEMPT","COURT_CONTEMPT"),
    ("COURT_PROBATION","COURT_PROBATION"),
    ("COURT_WARRANT","COURT_WARRANT"),
    ("COURT_WARRANT_FELONY","COURT_WARRANT_FELONY"),
    ("COURT_WARRANT_MISDEMEANOR","COURT_WARRANT_MISDEMEANOR"),
    ("DOM-VIOL","DOM-VIOL"),
    ("DOM-VIOL_BATTERY-SPOUSE","DOM-VIOL_BATTERY-SPOUSE"),
    ("DOM-VIOL_COURT-ORDER","DOM-VIOL_COURT-ORDER"),
    ("DOM-VIOL_DOMESTIC-DISPUTE","DOM-VIOL_DOMESTIC-DISPUTE"),
    ("DOM-VIOL_PHONE","DOM-VIOL_PHONE"),
    ("HOMICIDE","HOMICIDE"),
    ("LARCENY","LARCENY"),
    ("LARCENY_BURGLARY","LARCENY_BURGLARY"),
    ("LARCENY_BURGLARY_AUTO","LARCENY_BURGLARY_AUTO"),
    ("LARCENY_BURGLARY_COMMERCIAL","LARCENY_BURGLARY_COMMERCIAL"),
    ("LARCENY_BURGLARY_OTHER","LARCENY_BURGLARY_OTHER"),
    ("LARCENY_BURGLARY_RESIDENTIAL","LARCENY_BURGLARY_RESIDENTIAL"),
    ("LARCENY_FORGERY-COUNTERFEIT","LARCENY_FORGERY-COUNTERFEIT"),
    ("LARCENY_FRAUD","LARCENY_FRAUD"),
    ("LARCENY_THEFT","LARCENY_THEFT"),
    ("LARCENY_THEFT_GRAND","LARCENY_THEFT_GRAND"),
    ("LARCENY_THEFT_PETTY","LARCENY_THEFT_PETTY"),
    ("LARCENY_THEFT_VEHICLE","LARCENY_THEFT_VEHICLE"),
    ("LARCENY_THEFT_VEHICLE_AUTO","LARCENY_THEFT_VEHICLE_AUTO"),
    ("LARCENY_THEFT_VEHICLE_CAR-JACKING","LARCENY_THEFT_VEHICLE_CAR-JACKING"),
    ("LARCENY_THEFT_VEHICLE_OTHER","LARCENY_THEFT_VEHICLE_OTHER"),
    ("LARCENY_THEFT_VEHICLE_TRUCK-BUS","LARCENY_THEFT_VEHICLE_TRUCK-BUS"),
    ("MENTAL-ILLNESS","MENTAL-ILLNESS"),
    ("OTHER","OTHER"),
    ("OTHER_FOUND","OTHER_FOUND"),
    ("OTHER_LOST","OTHER_LOST"),
    ("OTHER_MISSING-PERSON","OTHER_MISSING-PERSON"),
    ("QUALITY","QUALITY"),
    ("QUALITY_CURFEW-LOITERING","QUALITY_CURFEW-LOITERING"),
    ("QUALITY_DISORDERLY-CONDUCT","QUALITY_DISORDERLY-CONDUCT"),
    ("QUALITY_DRUG","QUALITY_DRUG"),
    ("QUALITY_DRUG_POSSESSION","QUALITY_DRUG_POSSESSION"),
    ("QUALITY_DRUG_POSSESSION_MARIJUANA","QUALITY_DRUG_POSSESSION_MARIJUANA"),
    ("QUALITY_DRUG_POSSESSION_NARCOTICS","QUALITY_DRUG_POSSESSION_NARCOTICS"),
    ("QUALITY_DRUG_POSSESSION_OTHER","QUALITY_DRUG_POSSESSION_OTHER"),
    ("QUALITY_DRUG_SALE-MFCTR","QUALITY_DRUG_SALE-MFCTR"),
    ("QUALITY_DRUG_SALE-MFCTR_NARCOTICS","QUALITY_DRUG_SALE-MFCTR_NARCOTICS"),
    ("QUALITY_LIQUOR","QUALITY_LIQUOR"),
    ("SEX","SEX"),
    ("SEX_OFFENDER","SEX_OFFENDER"),
    ("SEX_OTHER","SEX_OTHER"),
    ("SEX_PROSTITUTION","SEX_PROSTITUTION"),
    ("SEX_RAPE","SEX_RAPE"),
    ("ROBBERY","ROBBERY"),
    ("ROBBERY_FIREARM","ROBBERY_FIREARM"),
    ("ROBBERY_INHABITED-DWELLING","ROBBERY_INHABITED-DWELLING"),
    ("ROBBERY_KNIFE","ROBBERY_KNIFE"),
    ("ROBBERY_OTHER-WEAPON","ROBBERY_OTHER-WEAPON"),
    ("ROBBERY_STRONG-ARM","ROBBERY_STRONG-ARM"),
    ("TRAFFIC","TRAFFIC"),
    ("TRAFFIC_DUI","TRAFFIC_DUI"),
    ("TRAFFIC_HIT-RUN","TRAFFIC_HIT-RUN"),
    ("TRAFFIC_MISC","TRAFFIC_MISC"),
    ("TRAFFIC_TOWED-VEHICLE","TRAFFIC_TOWED-VEHICLE"),
    ("VANDALISM","VANDALISM"),
    ("WEAPONS","WEAPONS") )

class simpleQ(forms.Form):
    
    # idx = forms.IntegerField()
    beat = forms.ChoiceField(choices=BeatChoices)
    
    # 2do: replace with hierarchic widget
    ## django-mptt, jquery, ...?
    crimeCat = forms.ChoiceField(choices=CrimeCatChoices)  
    
    def __unicode__(self):
        return '%s+%s' % (self.beat,self.crimeCat)


class twoTypeQ(forms.Form):
    
    # idx = forms.IntegerField()
    beat = forms.ChoiceField(choices=BeatChoices)
    
    # 2do: replace with hierarchic widget
    ## django-mptt, jquery, ...?
    crimeCat = forms.ChoiceField(choices=CrimeCatChoices)  

    secondCatChoice = ( (None, '<none>'), ) + CrimeCatChoices
    
    crimeCat2 = forms.ChoiceField(choices=secondCatChoice)  
    
    def __unicode__(self):
        if self.crimeCat2:
            return '%s+%s+%s' % (self.beat,self.crimeCat,self.crimeCat2)
        else:
            return '%s+%s' % (self.beat,self.crimeCat)


