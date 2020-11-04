import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from application.EvoDataAnalyzeScenario import *

evoDataAnalyzeScenario = EvoDataAnalyzeScenario()
evoDataAnalyzeScenario.execute()

