database(
    thermoLibraries=['primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC', 'Florine'],
    reactionLibraries=['F2'],
    seedMechanisms=[],
    kineticsFamilies='default',
    kineticsDepositories='default',
    kineticsEstimator='rate rules',
    
)

species(
    label='O2',
    structure=SMILES("[O][O]"),
)

species(
    label='N2',
    reactive=False,
    structure=adjacencyList("""
    1 N u0 p1 c0 {2,T}
    2 N u0 p1 c0 {1,T}
    """),
)

species(
    label='CH2F2',
    reactive=True,
    structure=adjacencyList("""
    1 F u0 p3 c0 {2,S}
    2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
    3 F u0 p3 c0 {2,S}
    4 H u0 p0 c0 {2,S}
    5 H u0 p0 c0 {2,S}
    """),
)

simpleReactor(
    temperature=(1000, 'K'),
    pressure=(1, 'atm'),
    initialMoleFractions={
        'CH2F2': 0.1,
        'O2': 0.21,
        'N2': 0.79,
    },
    terminationConversion={
        'CH2F2': 0.99,
    },
    terminationTime=(10, 's'),
)

simulator(
    atol=1e-16,
    rtol=1e-8,
    # sens_atol=1e-6,
    # sens_rtol=1e-4,
)

model(
    toleranceMoveToCore = 0.1,
    toleranceKeepInEdge = 0.01,
    toleranceInterruptSimulation = 1e8,
    maximumEdgeSpecies = 1000,
    minCoreSizeForPrune = 50,
    minSpeciesExistIterationsForPrune = 10,
    filterReactions=True,
)

options(
    units='si',
    generateSeedEachIteration=True,
    generateOutputHTML=False,
    saveSeedToDatabase=False,
    generatePlots=True,
    saveSimulationProfiles=False,
    saveEdgeSpecies=False,
)
