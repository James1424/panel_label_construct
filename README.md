# ETF / Index Tail-Event Panel Builder

This repository builds a monthly machine-learning panel for detecting right-tail stock events: stocks that may enter an explosive 1–3 month return regime.

It uses ETF / index holdings as the seed universe rather than copying the full common-stock universe. The panel includes the dense feature set from the previous XGBoost boom project, plus ETF-source features, liquidity/size proxies, volatility amplitude/frequency features, future-return targets, and multiple tail-event labels.

## Run
```bash
pip install -r requirements.txt
python run_all.py
```

Step by step:
```bash
python -m src.get_holdings_universe
python -m src.download_data
python -m src.build_panel
python -m src.update_readme
```

## Important leakage rule
The future-return and label columns are generated for training targets and evaluation only. They must not be used as model input features.

Target / label columns include:
- `future_return_1m`
- `future_return_2m`
- `future_return_3m`
- `future_max_return_1_3m`
- `future_max_return_1_3m_pct_rank`
- `monthly_top10_threshold_1_3m`
- `monthly_top5_threshold_1_3m`
- `label_top10_1_3m`
- `label_top5_1_3m`
- `label_boom30_top10_1_3m`
- `label_boom40_top10_1_3m`
- `label_boom50_top5_1_3m`
- `label_mega100_1_3m`

## Source ETF / index list
| ticker   | category             |   source_weight | provider_hint   |
|:---------|:---------------------|----------------:|:----------------|
| QQQ      | core_growth          |               4 | invesco         |
| SPY      | large_cap_core       |               3 | wikipedia_sp500 |
| IVV      | large_cap_core       |               3 | ishares         |
| VOO      | large_cap_core       |               3 | vanguard        |
| VUG      | large_cap_growth     |               4 | vanguard        |
| IWF      | large_cap_growth     |               4 | ishares         |
| SCHG     | large_cap_growth     |               4 | schwab          |
| MGK      | large_cap_growth     |               4 | vanguard        |
| IWO      | small_mid_growth     |               3 | ishares         |
| VTWG     | small_mid_growth     |               3 | vanguard        |
| IJT      | small_mid_growth     |               3 | ishares         |
| IJK      | small_mid_growth     |               3 | ishares         |
| SMH      | semiconductor_ai     |               5 | vaneck          |
| SOXX     | semiconductor_ai     |               5 | ishares         |
| SOXQ     | semiconductor_ai     |               5 | invesco         |
| XSD      | semiconductor_ai     |               5 | spdr            |
| AIQ      | semiconductor_ai     |               4 | globalx         |
| BOTZ     | semiconductor_ai     |               4 | globalx         |
| ROBO     | semiconductor_ai     |               4 | robo            |
| ARKQ     | semiconductor_ai     |               4 | ark             |
| QTUM     | semiconductor_ai     |               4 | defiance        |
| IGV      | software_cloud       |               5 | ishares         |
| WCLD     | software_cloud       |               5 | wisdomtree      |
| SKYY     | software_cloud       |               5 | firsttrust      |
| CIBR     | cybersecurity        |               4 | firsttrust      |
| HACK     | cybersecurity        |               4 | amplify         |
| ARKK     | innovation_high_beta |               4 | ark             |
| ARKW     | innovation_high_beta |               4 | ark             |
| ARKG     | innovation_high_beta |               4 | ark             |
| XBI      | biotech              |               3 | spdr            |
| IBB      | biotech              |               3 | ishares         |
| TAN      | clean_energy         |               3 | invesco         |
| ICLN     | clean_energy         |               3 | ishares         |
| QCLN     | clean_energy         |               3 | firsttrust      |
| URA      | uranium_nuclear      |               3 | globalx         |
| BLOK     | blockchain_fintech   |               3 | amplify         |
| BKCH     | blockchain_fintech   |               3 | globalx         |
| FINX     | blockchain_fintech   |               3 | globalx         |
| IPO      | innovation_high_beta |               3 | renaissance     |

## Seed universe summary
| metric                |    value |
|:----------------------|---------:|
| tickers               | 664      |
| avg_source_count      |   1.2304 |
| max_source_count      |   3      |
| avg_source_weight_sum |   4.1762 |
| max_source_weight_sum |  12      |

### Highest source-score seed tickers
| ticker   |   source_count |   source_weight_sum |   theme_count | sources        | categories                             |
|:---------|---------------:|--------------------:|--------------:|:---------------|:---------------------------------------|
| AMD      |              3 |                  12 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| AVGO     |              3 |                  12 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| GOOG     |              3 |                  12 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| META     |              3 |                  12 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| NFLX     |              3 |                  12 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| ORCL     |              3 |                  12 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| TSLA     |              3 |                  12 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| APP      |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| CEG      |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| CRWD     |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| DDOG     |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| DELL     |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| KLAC     |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| LRCX     |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| MPWR     |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| MRVL     |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| MU       |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| PANW     |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| PLTR     |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| SMCI     |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| TER      |              3 |                  11 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| FSLR     |              3 |                  10 |             3 | QQQ,SPY,manual | core_growth,large_cap_core,manual_core |
| AAPL     |              2 |                   8 |             2 | SPY,manual     | large_cap_core,manual_core             |
| ADBE     |              2 |                   8 |             2 | SPY,manual     | large_cap_core,manual_core             |
| ALAB     |              2 |                   8 |             2 | QQQ,manual     | core_growth,manual_core                |
| AMZN     |              2 |                   8 |             2 | SPY,manual     | large_cap_core,manual_core             |
| ARM      |              2 |                   8 |             2 | QQQ,manual     | core_growth,manual_core                |
| ASML     |              2 |                   8 |             2 | QQQ,manual     | core_growth,manual_core                |
| CRM      |              2 |                   8 |             2 | SPY,manual     | large_cap_core,manual_core             |
| GOOGL    |              2 |                   8 |             2 | SPY,manual     | large_cap_core,manual_core             |

## Panel summary
| metric             | value               |
|:-------------------|:--------------------|
| raw_rows           | 51815               |
| clean_rows         | 51815               |
| raw_columns        | 137                 |
| clean_columns      | 126                 |
| raw_tickers        | 424                 |
| clean_tickers      | 424                 |
| months             | 127                 |
| first_month        | 2016-01-31 00:00:00 |
| last_month         | 2026-07-31 00:00:00 |
| candidate_features | 110                 |
| kept_features      | 110                 |
| dropped_features   | 0                   |

## Tail-label summary
| label                   |   positive_rows |   valid_future_rows | positive_rate   |   months_with_positive |   avg_positives_per_month |   min_positives_per_month |   max_positives_per_month |
|:------------------------|----------------:|--------------------:|:----------------|-----------------------:|--------------------------:|--------------------------:|--------------------------:|
| label_top10_1_3m        |            5214 |               51391 | 10.15%          |                    126 |                   41.0551 |                         0 |                        43 |
| label_top5_1_3m         |            2636 |               51391 | 5.13%           |                    126 |                   20.7559 |                         0 |                        22 |
| label_boom30_top10_1_3m |            2527 |               51391 | 4.92%           |                    124 |                   19.8976 |                         0 |                        43 |
| label_boom40_top10_1_3m |            1367 |               51391 | 2.66%           |                    122 |                   10.7638 |                         0 |                        43 |
| label_boom50_top5_1_3m  |             757 |               51391 | 1.47%           |                    117 |                    5.9606 |                         0 |                        22 |
| label_mega100_1_3m      |             154 |               51391 | 0.30%           |                     52 |                    1.2126 |                         0 |                        16 |

## Recent monthly label distribution
| month      |   rows |   tickers | future_max_return_1_3m_mean   | future_max_return_1_3m_p90   | future_max_return_1_3m_p95   | future_max_return_1_3m_max   |   label_top10_1_3m_count |   label_top5_1_3m_count |   label_boom30_top10_1_3m_count |   label_boom40_top10_1_3m_count |   label_boom50_top5_1_3m_count |   label_mega100_1_3m_count |
|:-----------|-------:|----------:|:------------------------------|:-----------------------------|:-----------------------------|:-----------------------------|-------------------------:|------------------------:|--------------------------------:|--------------------------------:|-------------------------------:|---------------------------:|
| 2025-02-28 |    421 |       421 | 2.91%                         | 15.47%                       | 22.59%                       | 55.18%                       |                       43 |                      22 |                              14 |                               8 |                              2 |                          0 |
| 2025-03-31 |    421 |       421 | 10.66%                        | 33.50%                       | 48.32%                       | 194.45%                      |                       43 |                      22 |                              43 |                              31 |                             20 |                          3 |
| 2025-04-30 |    421 |       421 | 16.55%                        | 40.99%                       | 55.89%                       | 210.87%                      |                       43 |                      22 |                              43 |                              43 |                             22 |                          5 |
| 2025-05-31 |    421 |       421 | 13.40%                        | 30.04%                       | 40.69%                       | 248.51%                      |                       43 |                      22 |                              43 |                              22 |                             15 |                          3 |
| 2025-06-30 |    421 |       421 | 10.36%                        | 25.49%                       | 37.42%                       | 175.67%                      |                       43 |                      22 |                              31 |                              17 |                             12 |                          4 |
| 2025-07-31 |    421 |       421 | 10.70%                        | 25.62%                       | 41.55%                       | 134.31%                      |                       43 |                      22 |                              35 |                              23 |                             14 |                          5 |
| 2025-08-31 |    421 |       421 | 8.26%                         | 25.08%                       | 38.15%                       | 117.31%                      |                       43 |                      22 |                              30 |                              18 |                             14 |                          1 |
| 2025-09-30 |    421 |       421 | 5.88%                         | 21.10%                       | 28.23%                       | 71.34%                       |                       43 |                      22 |                              18 |                               8 |                              4 |                          0 |
| 2025-10-31 |    422 |       422 | 8.90%                         | 23.23%                       | 29.36%                       | 85.48%                       |                       43 |                      22 |                              20 |                               8 |                              4 |                          0 |
| 2025-11-30 |    422 |       422 | 12.44%                        | 29.99%                       | 43.26%                       | 90.01%                       |                       43 |                      22 |                              42 |                              26 |                             13 |                          0 |
| 2025-12-31 |    422 |       422 | 11.44%                        | 31.88%                       | 42.10%                       | 88.31%                       |                       43 |                      22 |                              43 |                              24 |                             16 |                          0 |
| 2026-01-31 |    422 |       422 | 9.63%                         | 27.16%                       | 43.84%                       | 109.52%                      |                       43 |                      22 |                              35 |                              28 |                             15 |                          3 |
| 2026-02-28 |    422 |       422 | 8.93%                         | 28.71%                       | 55.41%                       | 188.52%                      |                       43 |                      22 |                              39 |                              32 |                             22 |                         13 |
| 2026-03-31 |    422 |       422 | 19.15%                        | 44.72%                       | 87.62%                       | 340.71%                      |                       43 |                      22 |                              43 |                              43 |                             22 |                         16 |
| 2026-04-30 |    422 |       422 | 11.05%                        | 30.20%                       | 51.93%                       | 148.03%                      |                       43 |                      22 |                              43 |                              30 |                             22 |                          4 |
| 2026-05-31 |    423 |       423 | 4.47%                         | 15.88%                       | 21.37%                       | 60.65%                       |                       43 |                      22 |                              10 |                               5 |                              2 |                          0 |
| 2026-06-30 |    424 |       424 | 1.11%                         | 6.97%                        | 8.05%                        | 15.92%                       |                       43 |                      22 |                               0 |                               0 |                              0 |                          0 |
| 2026-07-31 |    424 |       424 |                               |                              |                              |                              |                        0 |                       0 |                               0 |                               0 |                              0 |                          0 |

## Feature missingness report
A feature is dropped if `missing_rate > 35%` or `non_null_rows < 1000`.

### Highest-missing candidate features
| feature                       | feature_group     |   missing_count | missing_rate   |   non_null_rows | non_null_rate   | first_valid_month   | last_valid_month   | dropped   |   drop_reason |
|:------------------------------|:------------------|----------------:|:---------------|----------------:|:----------------|:--------------------|:-------------------|:----------|--------------:|
| rel_mom_12m_vs_qqq            | relative_strength |             450 | 0.87%          |           51365 | 99.13%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_12m                       | other_momentum    |             450 | 0.87%          |           51365 | 99.13%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| up_day_volume_ratio_3m        | volume_flow       |             382 | 0.74%          |           51433 | 99.26%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| up_day_dollar_volume_ratio_3m | volume_flow       |             382 | 0.74%          |           51433 | 99.26%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_9m                        | other_momentum    |             334 | 0.64%          |           51481 | 99.36%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_7m                        | other_momentum    |             259 | 0.50%          |           51556 | 99.50%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_6m                        | core_momentum     |             222 | 0.43%          |           51593 | 99.57%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_4m_vs_6m                  | core_momentum     |             222 | 0.43%          |           51593 | 99.57%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_5m_vs_6m                  | core_momentum     |             222 | 0.43%          |           51593 | 99.57%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_6m_first3m                | core_momentum     |             222 | 0.43%          |           51593 | 99.57%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_6m_acceleration           | core_momentum     |             222 | 0.43%          |           51593 | 99.57%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| ret_lag_6m                    | sequence_path     |             222 | 0.43%          |           51593 | 99.57%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| rel_mom_6m_vs_qqq             | relative_strength |             222 | 0.43%          |           51593 | 99.57%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_3m_vs_6m                  | other_momentum    |             222 | 0.43%          |           51593 | 99.57%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| return_vol_ratio_6m           | risk_drawdown     |             222 | 0.43%          |           51593 | 99.57%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| drawdown_12m                  | risk_drawdown     |             221 | 0.43%          |           51594 | 99.57%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| drawdown_12m_abs              | risk_drawdown     |             221 | 0.43%          |           51594 | 99.57%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| ma100_slope_1m                | trend             |             213 | 0.41%          |           51602 | 99.59%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_5m                        | core_momentum     |             185 | 0.36%          |           51630 | 99.64%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| core_mom_456_std              | core_momentum     |             185 | 0.36%          |           51630 | 99.64%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| ret_lag_5m                    | sequence_path     |             185 | 0.36%          |           51630 | 99.64%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| volume_ma3_to_12m             | volume_flow       |             185 | 0.36%          |           51630 | 99.64%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| price_ma100_ratio             | trend             |             177 | 0.34%          |           51638 | 99.66%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| volume_change_3m              | volume_flow       |             174 | 0.34%          |           51641 | 99.66%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| dollar_volume_change_3m       | volume_flow       |             174 | 0.34%          |           51641 | 99.66%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| drawdown_change_3m            | drawdown_recovery |             163 | 0.31%          |           51652 | 99.69%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_4m                        | core_momentum     |             148 | 0.29%          |           51667 | 99.71%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| core_mom_456_avg              | core_momentum     |             148 | 0.29%          |           51667 | 99.71%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| core_mom_456_min              | core_momentum     |             148 | 0.29%          |           51667 | 99.71%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| core_mom_456_max              | core_momentum     |             148 | 0.29%          |           51667 | 99.71%          | 2016-01-31          | 2026-07-31         | False     |           nan |

### Dropped high-missing features
_No features dropped by missingness filter._

## Committed first-20k panel slice
`outputs/panel_head_20000.csv` contains the first 20,000 rows of the cleaned panel. It is committed for quick inspection and future model-design reference; the full panel remains in the GitHub Actions artifact.
Columns in slice: 126

## Model-design panel sample
This small committed sample contains historical labeled rows and recent examples for model-design inspection. The full panel is uploaded as a GitHub Actions artifact.
| sample_source                     | month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_top10_1_3m |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |   label_mega100_1_3m |
|:----------------------------------|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|-------------------:|--------------------------:|-------------------------:|---------------------:|
| historical_mega100_examples       | 2016-01-31 | FCX      |     4.15298 | -60.92%  | -60.70%  | -56.55%            |            2.92186e+08 | 53.97%               | 11.90%                | 93.55%             | 204.35%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2016-01-31 | LEU      |     1.37    | -49.26%  | -65.23%  | -61.39%            |        74400.9         | 46.83%               | 10.32%                | 64.39%             | 229.20%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-01-31 | TRGP     |    14.1947  | -59.11%  | -73.14%  | -63.68%            |            3.69201e+07 | 43.65%               | 9.52%                 | 69.31%             | 84.40%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2016-02-29 | AMD      |     2.14    | -9.32%   | 18.23%   | 14.53%             |            3.01533e+07 | 40.48%               | 7.94%                 | 66.65%             | 113.55%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2016-02-29 | LEU      |     1.32    | -21.43%  | -65.17%  | -57.67%            |        58517.2         | 51.59%               | 11.11%                | 64.43%             | 241.67%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-02-29 | DVN      |    13.5148  | -56.94%  | -53.27%  | -50.87%            |            2.14737e+08 | 44.44%               | 7.14%                 | 88.41%             | 85.36%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-04-30 | AMD      |     3.55    | 61.36%   | 67.45%   | 47.19%             |            4.55973e+07 | 46.83%               | 12.70%                | 70.84%             | 93.24%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-08-31 | LEU      |     3.46    | 14.19%   | 162.12%  | 49.10%             |       150004           | 42.86%               | 11.90%                | 64.97%             | 88.15%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2017-01-31 | PLUG     |     1.06    | -30.72%  | -40.78%  | -36.80%            |            4.82764e+06 | 25.40%               | 3.97%                 | 64.08%             | 111.32%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2017-02-28 | PLUG     |     1.08    | -21.17%  | -30.32%  | -32.19%            |            7.26119e+06 | 32.54%               | 5.56%                 | 65.27%             | 107.41%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2017-04-30 | CVNA     |     2.22    |          |          |                    |                        |                      |                       | 0.00%              | 84.41%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-05-31 | CVNA     |     2.01    |          |          |                    |                        |                      |                       | 0.00%              | 103.68%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2017-08-31 | ENPH     |     0.92    | 21.05%   | -48.60%  | -34.71%            |       600677           | 44.44%               | 7.14%                 | 65.05%             | 215.22%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2017-09-30 | ENPH     |     1.52    | 74.71%   | 10.95%   | 46.23%             |       821362           | 43.65%               | 10.32%                | 65.10%             | 90.79%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-10-31 | ENPH     |     1.53    | 62.77%   | 28.57%   | 68.58%             |       845932           | 46.03%               | 11.90%                | 65.19%             | 89.54%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-12-31 | ENPH     |     2.41    | 58.55%   | 177.01%  | 165.12%            |            2.1306e+06  | 50.00%               | 15.08%                | 65.33%             | 89.63%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2018-01-31 | ENPH     |     2.2     | 43.79%   | 134.04%  | 105.97%            |            2.52291e+06 | 52.38%               | 16.67%                | 65.35%             | 107.73%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-03-31 | TKO      |    32.5899  | 18.14%   | 53.98%   | 39.32%             |            2.7319e+07  | 7.94%                | 1.59%                 | 57.40%             | 102.62%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-04-30 | TKO      |    36.0109  | 12.92%   | 51.03%   | 40.74%             |            2.86848e+07 | 7.14%                | 0.79%                 | 48.50%             | 99.21%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2018-05-31 | CVNA     |     5.77    | 43.96%   | 77.98%   | 60.00%             |            2.393e+07   | 38.89%               | 11.11%                | 66.33%             | 124.40%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-06-30 | AMD      |    14.99    | 49.15%   | 45.82%   | 26.23%             |            7.8752e+08  | 28.57%               | 3.97%                 | 96.65%             | 106.07%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-12-31 | ENPH     |     4.73    | -2.47%   | -29.72%  | -17.83%            |            8.59184e+06 | 44.44%               | 9.52%                 | 64.80%             | 95.14%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | LEU      |     1.69    | -37.17%  | -50.87%  | -40.69%            |        57707           | 47.62%               | 11.90%                | 65.05%             | 84.02%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | PLUG     |     1.24    | -35.42%  | -38.61%  | -37.89%            |            4.00456e+06 | 20.63%               | 3.17%                 | 61.34%             | 93.55%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2019-03-31 | ENPH     |     9.23    | 95.14%   | 90.31%   | 88.18%             |            1.57355e+07 | 40.48%               | 11.11%                | 64.62%             | 97.51%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2019-04-30 | ENPH     |    10.04    | 38.87%   | 121.15%  | 106.44%            |            1.86016e+07 | 39.68%               | 11.11%                | 65.01%             | 180.38%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-05-31 | ENPH     |    15.17    | 67.25%   | 180.93%  | 170.49%            |            3.08737e+07 | 39.68%               | 10.32%                | 66.27%             | 95.58%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2019-10-31 | PCG      |     6.0642  | -65.97%  | -72.60%  | -69.87%            |            1.31638e+08 | 50.00%               | 12.70%                | 81.31%             | 146.52%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-10-31 | TSLA     |    20.9947  | 30.34%   | 31.94%   | 47.65%             |            1.94498e+09 | 23.02%               | 3.17%                 | 97.16%             | 106.58%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-11-30 | ENPH     |    21.87    | -26.29%  | 44.17%   | 13.94%             |            1.27686e+08 | 43.65%               | 11.90%                | 80.00%             | 123.91%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-11-30 | PCG      |     7.33207 | -28.61%  | -56.37%  | -60.89%            |            1.33872e+08 | 52.38%               | 16.67%                | 81.15%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | TSLA     |    21.996   | 46.24%   | 78.19%   | 54.13%             |            2.36702e+09 | 19.84%               | 3.17%                 | 96.63%             | 102.46%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-01-31 | EQT      |     5.61896 | -43.51%  | -59.75%  | -47.69%            |            5.80267e+07 | 39.68%               | 7.14%                 | 68.24%             | 142.54%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-02-29 | EQT      |     5.48294 | -32.38%  | -41.79%  | -43.68%            |            5.57168e+07 | 42.86%               | 8.73%                 | 67.64%             | 148.55%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | CVNA     |    11.018   | -40.15%  | -16.53%  | -30.26%            |            1.95395e+08 | 42.06%               | 11.11%                | 81.53%             | 118.19%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | DDOG     |    35.98    | -4.76%   | 6.10%    | 0.49%              |            1.42601e+08 | 42.86%               | 11.90%                | 75.36%             | 141.66%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | PLUG     |     3.54    | 12.03%   | 34.60%   | 19.65%             |            7.59733e+07 | 46.83%               | 15.87%                | 68.25%             | 131.92%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | SHOP     |    41.693   | 4.87%    | 33.78%   | 30.18%             |            1.16644e+09 | 33.33%               | 9.52%                 | 91.77%             | 127.66%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | TRGP     |     6.07095 | -82.66%  | -81.97%  | -81.46%            |            7.3025e+07  | 21.43%               | 5.56%                 | 60.88%             | 192.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-04-30 | DDOG     |    45.12    | -2.36%   | 34.33%   | 21.47%             |            1.4381e+08  | 33.33%               | 6.35%                 | 60.09%             | 108.02%                  |                  1 |                         1 |                        1 |                    1 |

## Latest clean panel sample
| month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |
|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|--------------------------:|-------------------------:|
| 2026-07-31 | AAPL     |      308.63 | 13.84%   | 19.16%   | 19.27%             |         15,409,358,283 | 7.94%                | 0.00%                 | 50.15%             |                          |                         0 |                        0 |
| 2026-07-31 | ABNB     |      148.93 | 6.11%    | 15.12%   | 14.43%             |            521,229,002 | 12.70%               | 2.38%                 | 57.36%             |                          |                         0 |                        0 |
| 2026-07-31 | ADBE     |      219.72 | -10.72%  | -25.07%  | -16.98%            |          1,459,481,642 | 21.43%               | 2.38%                 | 76.75%             |                          |                         0 |                        0 |
| 2026-07-31 | ADI      |      377.16 | -6.24%   | 21.70%   | 15.53%             |          1,821,055,724 | 21.43%               | 3.97%                 | 78.95%             |                          |                         0 |                        0 |
| 2026-07-31 | ADP      |      242.27 | 15.18%   | -0.28%   | 11.56%             |            632,463,325 | 11.11%               | 2.38%                 | 56.14%             |                          |                         0 |                        0 |
| 2026-07-31 | AEP      |      138.51 | 1.75%    | 17.40%   | 9.36%              |            594,040,649 | 2.38%                | 0.00%                 | 28.91%             |                          |                         0 |                        0 |
| 2026-07-31 | AKAM     |      113.17 | 9.90%    | 16.49%   | 10.02%             |            684,952,442 | 34.92%               | 4.76%                 | 82.70%             |                          |                         0 |                        0 |
| 2026-07-31 | ALAB     |      406.42 | 108.70%  | 169.83%  | 227.56%            |          1,749,460,074 | 58.73%               | 23.02%                | 95.58%             |                          |                         0 |                        0 |
| 2026-07-31 | ALGN     |      184.52 | 4.83%    | 13.18%   | 5.96%              |            184,090,518 | 26.98%               | 4.76%                 | 56.48%             |                          |                         0 |                        0 |
| 2026-07-31 | AMAT     |      603.04 | 53.06%   | 87.56%   | 75.46%             |          4,424,156,195 | 41.27%               | 11.11%                | 94.45%             |                          |                         0 |                        0 |
| 2026-07-31 | AMD      |      517.82 | 46.07%   | 118.74%  | 143.97%            |         15,113,608,614 | 48.41%               | 15.08%                | 96.46%             |                          |                         0 |                        0 |
| 2026-07-31 | AMZN     |      242.67 | -8.45%   | 1.41%    | 11.16%             |         12,629,056,980 | 14.29%               | 0.79%                 | 64.81%             |                          |                         0 |                        0 |
| 2026-07-31 | ANET     |      159.99 | -7.36%   | 12.88%   | 21.01%             |          1,491,780,906 | 43.65%               | 8.73%                 | 90.05%             |                          |                         0 |                        0 |
| 2026-07-31 | APP      |      527.06 | 18.08%   | 11.40%   | 21.69%             |          2,419,188,727 | 50.00%               | 15.87%                | 94.67%             |                          |                         0 |                        0 |
| 2026-07-31 | ARM      |      315.28 | 49.90%   | 199.24%  | 151.67%            |          3,155,394,988 | 46.03%               | 16.67%                | 96.16%             |                          |                         0 |                        0 |
| 2026-07-31 | ASML     |     1769.32 | 22.96%   | 24.77%   | 27.09%             |          3,135,905,115 | 33.33%               | 8.73%                 | 91.07%             |                          |                         0 |                        0 |
| 2026-07-31 | AVGO     |      360.45 | -13.51%  | 9.20%    | 13.02%             |         10,556,884,055 | 30.16%               | 3.97%                 | 87.03%             |                          |                         0 |                        0 |
| 2026-07-31 | AXON     |      597.04 | 48.61%   | 23.46%   | 24.71%             |            521,999,380 | 36.51%               | 12.70%                | 81.82%             |                          |                         0 |                        0 |
| 2026-07-31 | BEN      |       34.11 | 14.96%   | 31.31%   | 36.30%             |            143,689,727 | 11.11%               | 1.59%                 | 33.52%             |                          |                         0 |                        0 |
| 2026-07-31 | BF-B     |       26.16 | 2.40%    | -2.70%   | -3.54%             |            105,007,954 | 19.05%               | 3.17%                 | 47.97%             |                          |                         0 |                        0 |
| 2026-07-31 | BG       |      106.46 | -15.72%  | -5.41%   | -10.82%            |            203,788,180 | 10.32%               | 1.59%                 | 35.45%             |                          |                         0 |                        0 |
| 2026-07-31 | BIIB     |      216.12 | 14.18%   | 20.14%   | 16.90%             |            231,425,799 | 13.49%               | 2.38%                 | 47.86%             |                          |                         0 |                        0 |
| 2026-07-31 | BKNG     |      184.56 | 9.90%    | -7.31%   | 3.97%              |          1,358,014,360 | 17.46%               | 3.97%                 | 76.00%             |                          |                         0 |                        0 |
| 2026-07-31 | BKR      |       52.78 | -23.99%  | -5.15%   | -12.42%            |            517,507,449 | 19.84%               | 1.59%                 | 60.47%             |                          |                         0 |                        0 |
| 2026-07-31 | BLDR     |       84.69 | 7.08%    | -25.97%  | -13.97%            |            207,464,381 | 37.30%               | 7.94%                 | 65.07%             |                          |                         0 |                        0 |
| 2026-07-31 | BLK      |      995.73 | -6.03%   | -10.01%  | -3.73%             |            754,336,493 | 10.32%               | 0.79%                 | 51.28%             |                          |                         0 |                        0 |
| 2026-07-31 | BMY      |       58.13 | -2.98%   | 7.89%    | 0.35%              |            649,115,882 | 7.14%                | 0.79%                 | 43.99%             |                          |                         0 |                        0 |
| 2026-07-31 | BNY      |      146.62 | 9.12%    | 22.75%   | 23.48%             |            532,949,842 | 3.97%                | 0.00%                 | 30.69%             |                          |                         0 |                        0 |
| 2026-07-31 | BR       |      143.95 | -5.88%   | -26.07%  | -19.49%            |            228,040,168 | 14.29%               | 0.00%                 | 34.15%             |                          |                         0 |                        0 |
| 2026-07-31 | BRK-B    |      507.78 | 7.22%    | 5.67%    | 4.07%              |          2,462,618,216 | 0.79%                | 0.00%                 | 35.50%             |                          |                         0 |                        0 |

## Output files
- `data/seed_universe.csv`: ETF/index holdings universe with source metadata.
- `data/daily_prices.csv.gz`: downloaded historical daily OHLCV data, ignored by Git because it can be large.
- `outputs/raw_monthly_panel.csv`: full monthly panel before missingness feature deletion.
- `outputs/clean_monthly_panel.csv`: training-ready panel after high-missing feature deletion.
- `outputs/feature_missing_report.csv`: missingness statistics for candidate model features.
- `outputs/dropped_features.csv`: removed high-missing features.
- `outputs/label_summary.csv`: right-tail label distribution summary.
- `outputs/label_distribution_by_month.csv`: monthly tail-label distribution.
- `outputs/feature_manifest.txt`: final kept features and target columns.

## Notes
- ETF holdings URLs can change. If a source fails, check `data/holding_source_failures.csv` and add tickers to `data/manual_tickers.csv`.
- This project builds the panel only. Model training should read `outputs/clean_monthly_panel.csv`, choose a target label, and exclude all future/label columns from `X_train`.