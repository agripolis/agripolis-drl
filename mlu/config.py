################################################
# Reinforcement Learning extension for AgriPoliS
# C.Dong, 2023
################################################

runs=9
#agpy="agpCC.exe"
agpy="agpCC-rlfarmid.exe"

#inputfiles="./inputfiles/"
inputfiles="./inputfiles-fid/"

temp_scenario="scenario-temp.txt"

nInvs = 47
epochs = 1000 #3000
simus = 30 #50
topn = 5
QSIZE = simus

#discount
gamma = 1/0.95
