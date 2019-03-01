# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:14:48 2019

@author: Josh Weissmann
"""
import torch

class DicomImagePair():
    def __init__(self, preC, postC, bins = 255):
        self.extractionIndices = utils.removeBackgroundIndices(preC)
        self.preC, self.postC = utils.removeBackground(preC, postC)
        self.preC, self.postC = torch.Tensor(self.preC), torch.Tensor(self.postC)
        
        self.prob_preC = self.preC.histc(bins)
        self.prob_postC = self.postC.histc(bins)
        
        self.entropy_preC = \
            torch.sum(-1*self.prob_preC * torch.log(self.prob_preC))
        self.entropy_postC = \
            torch.sum(-1*self.prob_postC * torch.log(self.prob_postC))
                
        ## IMPORTANT NOTE:
        # initialize everything to start at 1, so that we can avoid 0 in log
#==============================================================================
#         jointHist = torch.ones(bins, bins)#       
#         d = torch.Tensor([bins])*.9999
#         for i in range(preC.shape[0]):
#             for j in range(preC.shape[1]):
#                 # place the two pixels into bins                
#                 binPreC = int(torch.floor(preC[i,j]*d))
#                 binPostC = int(torch.floor(postC[i,j]*d))
#                 jointHist[binPreC, binPostC] += 1
#         self.jointHist = jointHist
#              
#         self.jointEntropy = \
#             torch.sum(-1*self.jointHist * torch.log(self.jointHist))
#==============================================================================
        
    def backgroundIndices(self):
        return self.extractionIndices
    
    def prob_preC(self):
        return self.prob_preC
    
    def prob_postC(self):
        return self.prob_postC
    
    def entropy_preC(self):
        return self.entropy_preC
    
    def entropy_postC(self):
        return self.entropy_postC
    
#==============================================================================
#     def entropy_joint(self):
#         return self.jointEntropy
#==============================================================================
