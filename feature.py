class feature_value:
    def __init__(self):
        self.PM=0
        self.PA=0
        self.NM=0
        self.NA=0
        self.NP=0
        self.NN=0

class all_feature:
    def __init__(self, summary, review):
        self.SPM=summary.PM
        self.SPA=summary.PA
        self.SNM=summary.NM
        self.SNA=summary.NA
        self.SNP=summary.NP
        self.SNN=summary.NN
        self.RPM=review.PM
        self.RPA=review.PA
        self.RNM=review.NM
        self.RNA=review.NA
        self.RNP=review.NP
        self.RNN=review.NN
    

