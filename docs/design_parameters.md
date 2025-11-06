# Design Parameters  
## Combustion Chamber Pressure (Pc)  
- A typical range for modern orbital liquid-propellant engines is ~15-25 MPa. :contentReference[oaicite:0]{index=0}  
- Higher Pc increases specific impulse and combustion efficiency, but also structural complexity and mass.  
- For a balanced design: **Pc ≈ 20 MPa**.

## Nozzle Expansion Ratio (Ae/At)  
- The ratio of exit area to throat area depends on ambient pressure.  
- For first-stage (atmospheric): Ae/At ~15-35.  
- For upper-stage (vacuum): Ae/At ~40-100.  
- Proposed values: ~30 for first stage, ~60 for upper stage.

## Thrust-to-Weight Ratio (T/W)  
- High T/W is critical for orbital launch performance. State-of-the-art values are ~70-100 N/kg.  
- For a concept model: **T/W ≈ 80 N/kg**.

## Propellant Choice  
- LOX + RP-1 for first stage: high density, simpler storage. :contentReference[oaicite:1]{index=1}  
- LOX + LH₂ for upper stage: highest specific impulse but cryogenic storage complexity. :contentReference[oaicite:2]{index=2}

## Baseline Specification  
| Parameter                    | Value                   | Notes                            |
|------------------------------|-------------------------|----------------------------------|
| Pc                           | ~20 MPa                 | Trade-off between performance & mass |
| Ae/At                        | ~30 (1st stage) / ~60 (upper) | Matches ambient pressure regime     |
| T/W                          | ~80 N/kg                | Balanced performance target       |
| Propellant                   | LOX + RP-1 / LOX + LH₂ | Two stage-specific options         |
