################################################
# Reinforcement Learning extension for AgriPoliS
# C.Dong, 2023
################################################

runs=9
#agpy="agpCC-rlfarmid.exe"
agpy="agripolis-drl/build/src/agp24"

inputfiles="agripolis-drl/inputfiles/"
#inputfiles="./inputfiles-fid/"

temp_scenario="scenario-temp.txt"

nInvs = 47
epochs = 100 #3000
simus = 20 #50
topn = 5
QSIZE = simus

