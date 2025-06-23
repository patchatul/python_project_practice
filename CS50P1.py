input = input('choose stock\' industry[aerospace, ai, bank, blockchain, cybersecurity, gold, healthcare, nuclear, oil, quantum computing, anything]: ')
name = input.lower()
match name:
    case 'oil':
        print('invest in XOM, CVX, COP, EOG, TTE, BP, SLB, OXY, PXD')
    case 'aerospace':
        print('invest in GD, ESLT, NOC, LHX, HWM, TDG, TXT')    
    case 'ai':
            print('invest in NVDA, IBM, AMZN, AI, MU, GOOGL, META, AAPL, MSFT')
    case 'bank':
        print('invest in JPM, BAC, WFC, C, USB, BK, MS, GS')
    case 'blockchain':
        print('invest in HOOD, RIOT, COIN, MARA, PYPL, NVDA, CME, XYZ, MA')
    case 'cybersecurity':
        print('invest in ZS, FTNT, CRWD, PANW, OKTA, RPD, VRNS, CYBR, S')
    case 'gold':
        print('invest in B, NEM, KGC, SBSW, WPM, FNV, RIO, GORO, OR')
    case 'healthcare':
        print('invest in PFE, NVS, JNJ, RHHBY, ABT, LLY, CVS, UNH, TDOC')
    case 'nuclear':
        print('invest in SMR, VST, GEV, OKLO, BWXT, NNE, CORZ, CEG, TLN, WULF')
    case 'quantum computing':
        print('invest in IQNQ, RGTI, QUBT, QBTS, NVDA, BABA, RTX, GOOGL, MSFT')
    case 'anything':
        print('invest in MSTR BITCOIN, BABA CHINESE, COIN CRYPTO, SONY TOELY JAPANESE')