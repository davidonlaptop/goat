#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                        #Beatriz Kanzki
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------Modeles de la base de donnees hits-of-opti-tera cree pour logiciel "GOAT" avec Django--------------------------------------------------------------#
#-------------------------------------------------------------------------------------------13/05/2015---------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
from django.db import models

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class assoc(models.Model):
    idassoc=models.IntegerField(primary_key=True)
    phenotype=models.ForeignKey('self')
    covariates=models.CharField(max_length=45)
    dataset=models.ForeignKey('self')
    id_marqueur=models.ForeignKey('self')
    experiment=models.ForeignKey('self')
    user=models.CharField(max_length=45)
    experiment_approved=models.BooleanField()
    rs_id_assoc=models.CharField(max_length=45)
    chromosome=models.IntegerField()
    pos=models.BigIntegerField()
    allele_A=models.CharField(max_length=1)
    allele_B=models.CharField(max_length=1)
    av_max_post_call=models.FloatField()
    info_imp=models.DecimalField(max_digit=3, decimal_place=3)
    cohort_AA=models.DecimalField(max_digit=3, decimal_place=3)
    cohort_AB=models.DecimalField(max_digit=3, decimal_place=3)
    cohort_BB=models.DecimalField(max_digit=3, decimal_place=3)
    cohort_NULL=models.DecimalField(max_digit=3, decimal_place=3)
    cases_AA=models.DecimalField(max_digit=3, decimal_place=3)
    cases_AB=models.DecimalField(max_digit=3, decimal_place=3)
    cases_BB=models.DecimalField(max_digit=3, decimal_place=3)
    controls_AA=models.DecimalField(max_digit=3, decimal_place=3)
    controls_AB=models.DecimalField(max_digit=3, decimal_place=3)
    controls_BB=models.DecimalField(max_digit=3, decimal_place=3)
    allele_A_freq=models.FloatField()
    allele_B_freq=models.FloatField()
    maf=models.DecimalField(max_digit=3, decimal_place=3)
    cases_maf=models.DecimalField(max_digit=3, decimal_place=3)
    controls_maf=models.DecimalField(max_digit=3, decimal_place=3)
    miss_dat_prop=models.FloatField(max_digit=3, decimal_place=3)
    cohort_hwe=models.FloatField()
    cases_hwe=models.FloatField()
    controls_hwe=models.FloatField()
    het_OR=models.DecimalField(max_digit=3, decimal_place=3)
    het_OR_lower=models.DecimalField(max_digit=3, decimal_place=3)
    het_OR_upper=models.DecimalField(max_digit=3, decimal_place=3)
    all_OR=models.DecimalField(max_digit=3, decimal_place=3)
    all_OR_lower=models.DecimalField(max_digit=3, decimal_place=3)
    all_OR_upper=models.DecimalField(max_digit=3, decimal_place=3)
    pvalue_assoc=models.FloatField()
    info_assoc=models.DecimalField(max_digit=3, decimal_place=3)
    beta_assoc=models.FloatField()
    se_assoc=models.DecimalField(max_digit=3, decimal_place=3)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class marqueurs(models.Model):
    idmarqueurs=models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=20,primary_key=True)
    sorte=models.SmallIntegerField()
    chromosome=models.SmallIntegerField()
    position=models.ForeignKey('self')
    idgenes=models.IntegerField()
    build_Id=models.IntegerField(primary_key=True)
    remapped_from_hg18=models.CharField(max_length=20)
    refNCBI=models.CharField(max_length=5)
    observed=models.CharField(max_length=5)
    classe=models.CharField(max_length=15)
    func=models.CharField(max_length=15)
    frame=models.CharField(max_length=15)
    codons=models.CharField(max_length=10)
    peptides=models.CharField(max_length=5)
    gene=models.CharField(max_length=15)
    gene_strand=models.CharField(max_length=15)
    start_gen=models.BigIntegerField()
    end_gen=models.BigIntegerField()
    gene_before=models.CharField(max_length=15)
    gene_before_strand=models.CharField(max_length=15)
    dist_gen_before=models.IntegerField()
    start_gen_before=models.BigIntegerField()
    end_gen_before=models.BigIntegerField()
    gene_after=models.CharField(max_length=15)
    gene_after_strand=models.CharField(max_length=15)
    dist_gen_after=models.IntegerField()
    start_gen_after=models.BigIntegerField()
    end_gen_after=models.BigIntegerField()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class hg_rs_history(models.Model):
    idhg_rs=models.CharField(max_length=20,primary_key=True)
    rsHigh=models.CharField(max_length=20)
    rsLow=models.CharField(max_length=45)
    build_id=models.IntegerField(max_length=20)
    orien=models.BooleanField()
    create_time=models.DateTimeField()
    last_updated=models.DateTimeField()
    rsCurrent=models.CharField(max_length=20)
    orien2Current=models.BooleanField()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
class affy_s_rs(models.Model):
    id_s=models.CharField(max_length=20,primary_key=True)
    id_rs=models.CharField(max_length=20)
    affy_5=models.CharField(max_length=45)
    affy_6=models.CharField(max_length=45)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
class genes(models.Model):
    idgenes=models.IntegerField(primary_key=True)
    symbol=models.CharField(max_length=45)
    approved=models.CharField(max_length=45)
    type_field = models.CharField(db_column='type', max_length=45)
    longname=models.CharField(max_length=150)
    note=models.TextField()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
class experiment (models.Model):
    idexperiment=models.IntegerField(primary_key=True)
    idusers=models.ForeignKey('self')
    date_exp=models.DateTimeField()
    version_script=models.DecimalField(max_digit=3, decimal_place=3)
    verstion_algo=models.DecimalField(max_digit=3, decimal_place=3)
    post_process=models.TextField()
    note=models.models.TextField()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
class users(models.Model):
    idusers=models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=45)
    note=models.CharField(max_length=45)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
class phenotypes(models.Model):
    idphenotypes=models.IntegerField(primary_key=True)
    nom=models.CharField(max_length=45)
    nom_view=models.CharField(max_length=45)
    description=models.TextField()
    type_field = models.CharField(db_column='type', max_length=45)
    querry=models.TextField()
    covariable_choosing_table=models.CharField(max_length=200)
    characteristic_table=models.CharField(max_length=200)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class phen_id_val(models.Model):
    idphen_id_val=models.IntegerField(primary_key=True)
    idphenotypes=models.ForeignKey('self')
    idperson=models.ForeignKey('self')
    value=models.FloatField()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
class dataset(models.Model):
    iddataset=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    description_dataset=models.CharField(max_length=45)
    cohort=models.CharField(max_length=45)
    cohort_description=models.CharField(max_length=45)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
class person_dataset(models.Model):
    idperson_dataset=models.IntegerField(primary_key=True)
    idperson=models.ForeignKey('self')
    iddataset=models.ForeignKey('self')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
class person(models.Model):
    idperson=models.IntegerField(primary_key=True)
    sex=models.CharField(max_length=15)
    age=models.IntegerField()
    dob=models.DateTimeField()
    ethnic_code=models.IntegerField()
    country_name=models.CharField(max_length=45)
    region_name=models.CharField(max_length=45)
    centre_name=models.CharField(max_length=200)
    sample=models.IntegerField()
    comment=models.TextField()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                                                                                        #END
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#