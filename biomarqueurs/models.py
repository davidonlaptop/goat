from __future__ import unicode_literals

from django.db import models


class Advance(models.Model):
    id                  = models.AutoField(primary_key=True)
    sample              = models.CharField(max_length=10, blank=True, null=True)
    marq_id             = models.IntegerField(blank=True, null=True)
    method_id           = models.IntegerField(blank=True, null=True)
    pheno_id            = models.IntegerField(blank=True, null=True)
    covariates          = models.CharField(max_length=50, blank=True, null=True)
    pvalue              = models.FloatField(blank=True, null=True)
    or_all              = models.FloatField(blank=True, null=True)
    maf                 = models.FloatField(blank=True, null=True)
    effet               = models.FloatField(blank=True, null=True)
    effet_normalized    = models.FloatField(blank=True, null=True)
    betacorrected       = models.IntegerField(blank=True, null=True)
    phenocorrected      = models.IntegerField(blank=True, null=True)
    add_after_beta_corr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advance'


class Advance3501(models.Model):
    id                  = models.AutoField(primary_key=True)
    marq_id             = models.IntegerField(blank=True, null=True)
    method_id           = models.IntegerField(blank=True, null=True)
    pheno_id            = models.IntegerField(blank=True, null=True)
    covariates          = models.CharField(max_length=50, blank=True, null=True)
    pvalue              = models.FloatField(blank=True, null=True)
    beta                = models.FloatField(blank=True, null=True)
    maf                 = models.FloatField(blank=True, null=True)
    imputed             = models.IntegerField(db_column='Imputed', blank=True, null=True)  # Field name made lowercase.
    betacorrected       = models.IntegerField(blank=True, null=True)
    phenocorrected      = models.IntegerField(blank=True, null=True)
    add_after_beta_corr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advance_3501'


class Brevet(models.Model):
    id                  = models.AutoField(primary_key=True)
    marq_id             = models.IntegerField()
    brevet              = models.IntegerField()
    sample              = models.CharField(max_length=15, blank=True, null=True)
    method              = models.ForeignKey('Method', db_column='method', blank=True, null=True)
    phenotype           = models.ForeignKey('Phenotype', db_column='phenotype', blank=True, null=True)
    covar               = models.CharField(max_length=50, blank=True, null=True)
    pvalue              = models.FloatField(blank=True, null=True)
    or_all              = models.FloatField(blank=True, null=True)
    ma                  = models.CharField(max_length=1, blank=True, null=True)
    effet               = models.FloatField(blank=True, null=True)
    effet_normalized    = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brevet'


class CkdAllWadv(models.Model):
    id          = models.AutoField(primary_key=True)
    marq_id     = models.IntegerField(blank=True, null=True)
    allele1     = models.CharField(max_length=1, blank=True, null=True)
    allele2     = models.CharField(max_length=2, blank=True, null=True)
    effet       = models.CharField(max_length=10, blank=True, null=True)
    se          = models.CharField(max_length=10, blank=True, null=True)
    pvalue      = models.CharField(max_length=10, blank=True, null=True)
    direction   = models.CharField(max_length=50, blank=True, null=True)
    hetisq      = models.CharField(max_length=10, blank=True, null=True)
    idanalyses  = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ckd_all_wadv'


class CkdAllWoadv(models.Model):
    id          = models.AutoField(primary_key=True)
    marq_id     = models.IntegerField(blank=True, null=True)
    allele1     = models.CharField(max_length=1, blank=True, null=True)
    allele2     = models.CharField(max_length=2, blank=True, null=True)
    effet       = models.CharField(max_length=10, blank=True, null=True)
    se          = models.CharField(max_length=10, blank=True, null=True)
    pvalue      = models.CharField(max_length=10, blank=True, null=True)
    direction   = models.CharField(max_length=50, blank=True, null=True)
    hetisq      = models.CharField(max_length=10, blank=True, null=True)
    idanalyses  = models.ForeignKey('MetaAnalyse', db_column='idanalyses', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ckd_all_woadv'


class EgfrAllWadv(models.Model):
    id          = models.AutoField(primary_key=True)
    marq_id     = models.IntegerField(blank=True, null=True)
    allele1     = models.CharField(max_length=1, blank=True, null=True)
    allele2     = models.CharField(max_length=2, blank=True, null=True)
    effet       = models.CharField(max_length=10, blank=True, null=True)
    se          = models.CharField(max_length=10, blank=True, null=True)
    pvalue      = models.CharField(max_length=10, blank=True, null=True)
    direction   = models.CharField(max_length=50, blank=True, null=True)
    hetisq      = models.CharField(max_length=10, blank=True, null=True)
    idanalyses  = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'egfr_all_wadv'


class EgfrAllWoadv(models.Model):
    id          = models.AutoField(primary_key=True)
    marq_id     = models.IntegerField(blank=True, null=True)
    allele1     = models.CharField(max_length=1, blank=True, null=True)
    allele2     = models.CharField(max_length=2, blank=True, null=True)
    effet       = models.CharField(max_length=10, blank=True, null=True)
    se          = models.CharField(max_length=10, blank=True, null=True)
    pvalue      = models.CharField(max_length=10, blank=True, null=True)
    direction   = models.CharField(max_length=50, blank=True, null=True)
    hetisq      = models.CharField(max_length=10, blank=True, null=True)
    idanalyses  = models.ForeignKey('MetaAnalyse', db_column='idanalyses', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'egfr_all_woadv'


class EgfrDmWadv(models.Model):
    id          = models.AutoField(primary_key=True)
    marq_id     = models.IntegerField(blank=True, null=True)
    allele1     = models.CharField(max_length=1, blank=True, null=True)
    allele2     = models.CharField(max_length=2, blank=True, null=True)
    effet       = models.CharField(max_length=10, blank=True, null=True)
    se          = models.CharField(max_length=10, blank=True, null=True)
    pvalue      = models.CharField(max_length=10, blank=True, null=True)
    direction   = models.CharField(max_length=50, blank=True, null=True)
    hetisq      = models.CharField(max_length=10, blank=True, null=True)
    idanalyses  = models.ForeignKey('MetaAnalyse', db_column='idanalyses', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'egfr_dm_wadv'


class EgfrDmWoadv(models.Model):
    id          = models.AutoField(primary_key=True)
    marq_id     = models.IntegerField(blank=True, null=True)
    allele1     = models.CharField(max_length=1, blank=True, null=True)
    allele2     = models.CharField(max_length=2, blank=True, null=True)
    effet       = models.CharField(max_length=10, blank=True, null=True)
    se          = models.CharField(max_length=10, blank=True, null=True)
    pvalue      = models.CharField(max_length=10, blank=True, null=True)
    direction   = models.CharField(max_length=50, blank=True, null=True)
    hetisq      = models.CharField(max_length=10, blank=True, null=True)
    idanalyses  = models.ForeignKey('MetaAnalyse', db_column='idanalyses', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'egfr_dm_woadv'


class Gene(models.Model):
    id              = models.AutoField(primary_key=True)
    symbol          = models.CharField(unique=True, max_length=50, blank=True, null=True)
    nom             = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genes'


class GeneBak(models.Model):
    id              = models.AutoField(primary_key=True)
    symbol          = models.CharField(unique=True, max_length=50, blank=True, null=True)
    nom             = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genes_bak'


class IncidentMacroAlbuminuria(models.Model):
    id                  = models.AutoField(primary_key=True)
    marq_id             = models.IntegerField(blank=True, null=True)
    method              = models.ForeignKey('Method', blank=True, null=True)
    pheno               = models.ForeignKey('Phenotype', blank=True, null=True)
    pvalue              = models.FloatField(blank=True, null=True)
    or_all              = models.FloatField(blank=True, null=True)
    ma                  = models.CharField(max_length=1, blank=True, null=True)
    maf                 = models.FloatField(blank=True, null=True)
    effet               = models.FloatField(blank=True, null=True)
    effet_normalized    = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incident_macro_albuminuria'


class Marqueur(models.Model):
    id                  = models.AutoField(primary_key=True)
    nom                 = models.CharField(unique=True, max_length=15, blank=True, null=True)
    sorte               = models.ForeignKey('SorteMarqueur', db_column='sorte', blank=True, null=True)
    chromosome          = models.CharField(max_length=2, blank=True, null=True)
    position            = models.IntegerField(blank=True, null=True)
    id_genes            = models.ForeignKey(Gene, db_column='id_genes', blank=True, null=True)
    hg                  = models.IntegerField(blank=True, null=True)
    remapped_fromhg18   = models.CharField(unique=True, max_length=15, blank=True, null=True)
    refncbi             = models.CharField(db_column='refNCBI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    observed            = models.CharField(max_length=15, blank=True, null=True)
    classe              = models.CharField(max_length=15, blank=True, null=True)
    func                = models.CharField(max_length=15, blank=True, null=True)
    frame               = models.CharField(max_length=15, blank=True, null=True)
    codons              = models.CharField(max_length=15, blank=True, null=True)
    peptides            = models.CharField(max_length=15, blank=True, null=True)
    gene                = models.CharField(max_length=15, blank=True, null=True)
    gene_strand         = models.CharField(max_length=15, blank=True, null=True)
    start_gen           = models.IntegerField(blank=True, null=True)
    end_gen             = models.IntegerField(blank=True, null=True)
    gene_before         = models.CharField(max_length=15, blank=True, null=True)
    gene_before_strand  = models.CharField(max_length=15, blank=True, null=True)
    dist_gen_before     = models.IntegerField(blank=True, null=True)
    start_gen_before    = models.IntegerField(blank=True, null=True)
    end_gen_before      = models.IntegerField(blank=True, null=True)
    gene_after          = models.CharField(max_length=15, blank=True, null=True)
    gene_after_strand   = models.CharField(max_length=15, blank=True, null=True)
    dist_gen_after      = models.IntegerField(blank=True, null=True)
    start_gen_after     = models.IntegerField(blank=True, null=True)
    end_gen_after       = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marqueurs'
        unique_together = (('nom', 'remapped_fromhg18'),)


class MarqueurBak(models.Model):
    id          = models.AutoField(primary_key=True)
    nom         = models.CharField(unique=True, max_length=15, blank=True, null=True)
    sorte       = models.ForeignKey('SorteMarqueur', db_column='sorte', blank=True, null=True)
    chromosome  = models.CharField(max_length=2, blank=True, null=True)
    position    = models.IntegerField(blank=True, null=True)
    id_genes    = models.ForeignKey(GeneBak, db_column='id_genes', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marqueurs_bak'


class MetaAnalyse(models.Model):
    id          = models.AutoField(primary_key=True)
    analyse     = models.CharField(unique=True, max_length=50, blank=True, null=True)
    nom         = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metaanalyses'


class Method(models.Model):
    id          = models.AutoField(primary_key=True)
    nom         = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'method'


class Monica(models.Model):
    id                  = models.AutoField(primary_key=True)
    marq_id             = models.IntegerField(blank=True, null=True)
    method              = models.ForeignKey(Method, blank=True, null=True)
    pheno               = models.ForeignKey('Phenotypes', blank=True, null=True)
    covariates          = models.CharField(max_length=50, blank=True, null=True)
    pvalue              = models.FloatField(blank=True, null=True)
    or_all              = models.FloatField(blank=True, null=True)
    maf                 = models.FloatField(blank=True, null=True)
    effet               = models.FloatField(blank=True, null=True)
    effet_normalized    = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monica'


class Phenotype(models.Model):
    id          = models.AutoField(primary_key=True)
    nom         = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'phenotypes'


class PreviousGeneHugo(models.Model):
    id          = models.AutoField(primary_key=True)
    symbol      = models.CharField(unique=True, max_length=50, blank=True, null=True)
    approved    = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'previous_gene_hugo'


class SorteMarqueur(models.Model):
    id      = models.AutoField(primary_key=True)
    nom     = models.CharField(unique=True, max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sorte_marqueurs'


class SynonymGeneHugo(models.Model):
    id          = models.AutoField(primary_key=True)
    symbol      = models.CharField(unique=True, max_length=50, blank=True, null=True)
    approved    = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'synonym_gene_hugo'


class TmpAdvance(models.Model):
    id          = models.AutoField(primary_key=True)
    sample      = models.CharField(max_length=10, blank=True, null=True)
    nom         = models.CharField(max_length=20)
    method_id   = models.IntegerField(blank=True, null=True)
    pheno_id    = models.IntegerField(blank=True, null=True)
    covariates  = models.CharField(max_length=50, blank=True, null=True)
    pvalue      = models.FloatField(blank=True, null=True)
    or_all      = models.FloatField(blank=True, null=True)
    maf         = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_advance'
        unique_together = (('nom', 'method_id', 'pheno_id'),)


class TmpAdvance3501(models.Model):
    id          = models.AutoField(primary_key=True)
    nom         = models.CharField(max_length=20)
    method_id   = models.IntegerField(blank=True, null=True)
    pheno_id    = models.IntegerField(blank=True, null=True)
    covariates  = models.CharField(max_length=50, blank=True, null=True)
    pvalue      = models.FloatField(blank=True, null=True)
    beta        = models.FloatField(blank=True, null=True)
    maf         = models.FloatField(blank=True, null=True)
    Imputed     = models.IntegerField(db_column='Imputed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_advance_3501'


class UacrAllWadv(models.Model):
    id          = models.AutoField(primary_key=True)
    marq_id     = models.IntegerField(blank=True, null=True)
    allele1     = models.CharField(max_length=1, blank=True, null=True)
    allele2     = models.CharField(max_length=2, blank=True, null=True)
    effet       = models.CharField(max_length=10, blank=True, null=True)
    se          = models.CharField(max_length=10, blank=True, null=True)
    pvalue      = models.CharField(max_length=10, blank=True, null=True)
    direction   = models.CharField(max_length=50, blank=True, null=True)
    hetisq      = models.CharField(max_length=10, blank=True, null=True)
    idanalyses  = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uacr_all_wadv'


class UacrAllWoadv(models.Model):
    id          = models.AutoField(primary_key=True)
    marq_id     = models.IntegerField(blank=True, null=True)
    allele1     = models.CharField(max_length=1, blank=True, null=True)
    allele2     = models.CharField(max_length=2, blank=True, null=True)
    effet       = models.CharField(max_length=10, blank=True, null=True)
    se          = models.CharField(max_length=10, blank=True, null=True)
    pvalue      = models.CharField(max_length=10, blank=True, null=True)
    direction   = models.CharField(max_length=50, blank=True, null=True)
    hetisq      = models.CharField(max_length=10, blank=True, null=True)
    idanalyses  = models.ForeignKey(MetaAnalyse, db_column='idanalyses', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uacr_all_woadv'


class UacrDmWadv(models.Model):
    id          = models.AutoField(primary_key=True)
    marq_id     = models.IntegerField(blank=True, null=True)
    allele1     = models.CharField(max_length=1, blank=True, null=True)
    allele2     = models.CharField(max_length=2, blank=True, null=True)
    effet       = models.CharField(max_length=10, blank=True, null=True)
    se          = models.CharField(max_length=10, blank=True, null=True)
    pvalue      = models.CharField(max_length=10, blank=True, null=True)
    direction   = models.CharField(max_length=50, blank=True, null=True)
    hetisq      = models.CharField(max_length=10, blank=True, null=True)
    idanalyses  = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uacr_dm_wadv'


class UacrDmWoadv(models.Model):
    id          = models.AutoField(primary_key=True)
    marq_id     = models.IntegerField(blank=True, null=True)
    allele1     = models.CharField(max_length=1, blank=True, null=True)
    allele2     = models.CharField(max_length=2, blank=True, null=True)
    effet       = models.CharField(max_length=10, blank=True, null=True)
    se          = models.CharField(max_length=10, blank=True, null=True)
    pvalue      = models.CharField(max_length=10, blank=True, null=True)
    direction   = models.CharField(max_length=50, blank=True, null=True)
    hetisq      = models.CharField(max_length=10, blank=True, null=True)
    idanalyses  = models.ForeignKey(MetaAnalyse, db_column='idanalyses', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uacr_dm_woadv'


class User(models.Model):
    id     = models.AutoField(primary_key=True)
    iduser = models.CharField(unique=True, max_length=20)
    mdp    = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'user'
