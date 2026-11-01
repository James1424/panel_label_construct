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
| tickers               | 530      |
| avg_source_count      |   1.0698 |
| max_source_count      |   2      |
| avg_source_weight_sum |   3.3453 |
| max_source_weight_sum |   8      |

### Highest source-score seed tickers
| ticker   |   source_count |   source_weight_sum |   theme_count | sources    | categories                 |
|:---------|---------------:|--------------------:|--------------:|:-----------|:---------------------------|
| AAPL     |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| ADBE     |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| AMD      |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| AMZN     |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| AVGO     |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| CRM      |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| GOOG     |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| GOOGL    |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| META     |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| MSFT     |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| NFLX     |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| NOW      |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| NVDA     |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| ORCL     |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| TSLA     |              2 |                   8 |             2 | SPY,manual | large_cap_core,manual_core |
| AMAT     |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| ANET     |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| APP      |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| CEG      |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| COIN     |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| CRWD     |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| DDOG     |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| DELL     |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| GEV      |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| HOOD     |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| KLAC     |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| LRCX     |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| MPWR     |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| MRVL     |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |
| MU       |              2 |                   7 |             2 | SPY,manual | large_cap_core,manual_core |

## Panel summary
| metric             | value               |
|:-------------------|:--------------------|
| raw_rows           | 65785               |
| clean_rows         | 65785               |
| raw_columns        | 136                 |
| clean_columns      | 125                 |
| raw_tickers        | 530                 |
| clean_tickers      | 530                 |
| months             | 130                 |
| first_month        | 2016-01-31 00:00:00 |
| last_month         | 2026-10-31 00:00:00 |
| candidate_features | 109                 |
| kept_features      | 109                 |
| dropped_features   | 0                   |

## Tail-label summary
| label                   |   positive_rows |   valid_future_rows | positive_rate   |   months_with_positive |   avg_positives_per_month |   min_positives_per_month |   max_positives_per_month |
|:------------------------|----------------:|--------------------:|:----------------|-----------------------:|--------------------------:|--------------------------:|--------------------------:|
| label_top10_1_3m        |            6587 |               65255 | 10.09%          |                    129 |                   50.6692 |                         0 |                        53 |
| label_top5_1_3m         |            3331 |               65255 | 5.10%           |                    129 |                   25.6231 |                         0 |                        27 |
| label_boom30_top10_1_3m |            3374 |               65255 | 5.17%           |                    128 |                   25.9538 |                         0 |                        53 |
| label_boom40_top10_1_3m |            1931 |               65255 | 2.96%           |                    127 |                   14.8538 |                         0 |                        53 |
| label_boom50_top5_1_3m  |            1098 |               65255 | 1.68%           |                    124 |                    8.4462 |                         0 |                        27 |
| label_mega100_1_3m      |             272 |               65255 | 0.42%           |                     72 |                    2.0923 |                         0 |                        22 |

## Recent monthly label distribution
| month      |   rows |   tickers | future_max_return_1_3m_mean   | future_max_return_1_3m_p90   | future_max_return_1_3m_p95   | future_max_return_1_3m_max   |   label_top10_1_3m_count |   label_top5_1_3m_count |   label_boom30_top10_1_3m_count |   label_boom40_top10_1_3m_count |   label_boom50_top5_1_3m_count |   label_mega100_1_3m_count |
|:-----------|-------:|----------:|:------------------------------|:-----------------------------|:-----------------------------|:-----------------------------|-------------------------:|------------------------:|--------------------------------:|--------------------------------:|-------------------------------:|---------------------------:|
| 2025-05-31 |    526 |       526 | 14.53%                        | 33.34%                       | 44.82%                       | 248.51%                      |                       53 |                      27 |                              53 |                              35 |                             23 |                          6 |
| 2025-06-30 |    526 |       526 | 12.17%                        | 29.53%                       | 45.46%                       | 253.55%                      |                       53 |                      27 |                              52 |                              30 |                             22 |                          7 |
| 2025-07-31 |    526 |       526 | 13.27%                        | 29.98%                       | 50.22%                       | 364.42%                      |                       53 |                      27 |                              53 |                              39 |                             27 |                          9 |
| 2025-08-31 |    526 |       526 | 10.51%                        | 28.57%                       | 48.66%                       | 325.54%                      |                       53 |                      27 |                              49 |                              32 |                             26 |                          7 |
| 2025-09-30 |    526 |       526 | 6.85%                         | 22.02%                       | 32.50%                       | 126.53%                      |                       53 |                      27 |                              31 |                              18 |                              9 |                          2 |
| 2025-10-31 |    527 |       527 | 9.22%                         | 23.06%                       | 31.15%                       | 189.09%                      |                       53 |                      27 |                              28 |                              14 |                             10 |                          1 |
| 2025-11-30 |    527 |       527 | 12.78%                        | 30.84%                       | 43.53%                       | 184.56%                      |                       53 |                      27 |                              53 |                              36 |                             19 |                          3 |
| 2025-12-31 |    527 |       527 | 11.41%                        | 31.84%                       | 44.69%                       | 167.66%                      |                       53 |                      27 |                              53 |                              33 |                             24 |                          1 |
| 2026-01-31 |    527 |       527 | 9.84%                         | 27.46%                       | 46.01%                       | 130.28%                      |                       53 |                      27 |                              45 |                              36 |                             23 |                          4 |
| 2026-02-28 |    527 |       527 | 10.04%                        | 35.80%                       | 61.54%                       | 188.52%                      |                       53 |                      27 |                              53 |                              49 |                             27 |                         15 |
| 2026-03-31 |    527 |       527 | 20.60%                        | 47.76%                       | 89.45%                       | 340.71%                      |                       53 |                      27 |                              53 |                              53 |                             27 |                         22 |
| 2026-04-30 |    527 |       527 | 13.09%                        | 37.44%                       | 54.37%                       | 148.03%                      |                       53 |                      27 |                              53 |                              45 |                             27 |                          7 |
| 2026-05-31 |    528 |       528 | 10.46%                        | 26.15%                       | 33.63%                       | 197.39%                      |                       53 |                      27 |                              34 |                              16 |                              6 |                          1 |
| 2026-06-30 |    529 |       529 | 7.53%                         | 28.63%                       | 37.66%                       | 174.98%                      |                       53 |                      27 |                              45 |                              23 |                             13 |                          1 |
| 2026-07-31 |    529 |       529 | 8.12%                         | 24.17%                       | 34.33%                       | 304.45%                      |                       53 |                      27 |                              36 |                              18 |                              9 |                          1 |
| 2026-08-31 |    529 |       529 | 2.51%                         | 14.66%                       | 19.22%                       | 57.99%                       |                       53 |                      27 |                               6 |                               2 |                              1 |                          0 |
| 2026-09-30 |    529 |       529 | 4.01%                         | 17.17%                       | 20.03%                       | 41.96%                       |                       53 |                      27 |                               7 |                               1 |                              0 |                          0 |
| 2026-10-31 |    530 |       530 |                               |                              |                              |                              |                        0 |                       0 |                               0 |                               0 |                              0 |                          0 |

## Feature missingness report
A feature is dropped if `missing_rate > 35%` or `non_null_rows < 1000`.

### Highest-missing candidate features
| feature                       | feature_group     |   missing_count | missing_rate   |   non_null_rows | non_null_rate   | first_valid_month   | last_valid_month   | dropped   |   drop_reason |
|:------------------------------|:------------------|----------------:|:---------------|----------------:|:----------------|:--------------------|:-------------------|:----------|--------------:|
| rel_mom_12m_vs_qqq            | relative_strength |             690 | 1.05%          |           65095 | 98.95%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| mom_12m                       | other_momentum    |             690 | 1.05%          |           65095 | 98.95%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| up_day_volume_ratio_3m        | volume_flow       |             611 | 0.93%          |           65174 | 99.07%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| up_day_dollar_volume_ratio_3m | volume_flow       |             611 | 0.93%          |           65174 | 99.07%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| mom_9m                        | other_momentum    |             509 | 0.77%          |           65276 | 99.23%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| mom_7m                        | other_momentum    |             392 | 0.60%          |           65393 | 99.40%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| mom_6m                        | core_momentum     |             334 | 0.51%          |           65451 | 99.49%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| mom_4m_vs_6m                  | core_momentum     |             334 | 0.51%          |           65451 | 99.49%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| mom_5m_vs_6m                  | core_momentum     |             334 | 0.51%          |           65451 | 99.49%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| mom_6m_first3m                | core_momentum     |             334 | 0.51%          |           65451 | 99.49%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| mom_6m_acceleration           | core_momentum     |             334 | 0.51%          |           65451 | 99.49%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| ret_lag_6m                    | sequence_path     |             334 | 0.51%          |           65451 | 99.49%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| rel_mom_6m_vs_qqq             | relative_strength |             334 | 0.51%          |           65451 | 99.49%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| mom_3m_vs_6m                  | other_momentum    |             334 | 0.51%          |           65451 | 99.49%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| return_vol_ratio_6m           | risk_drawdown     |             334 | 0.51%          |           65451 | 99.49%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| drawdown_12m                  | risk_drawdown     |             333 | 0.51%          |           65452 | 99.49%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| drawdown_12m_abs              | risk_drawdown     |             333 | 0.51%          |           65452 | 99.49%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| ma100_slope_1m                | trend             |             320 | 0.49%          |           65465 | 99.51%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| volume_change_3m              | volume_flow       |             318 | 0.48%          |           65467 | 99.52%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| dollar_volume_change_3m       | volume_flow       |             318 | 0.48%          |           65467 | 99.52%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| volume_ma3_to_12m             | volume_flow       |             283 | 0.43%          |           65502 | 99.57%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| mom_5m                        | core_momentum     |             278 | 0.42%          |           65507 | 99.58%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| core_mom_456_std              | core_momentum     |             278 | 0.42%          |           65507 | 99.58%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| ret_lag_5m                    | sequence_path     |             278 | 0.42%          |           65507 | 99.58%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| price_ma100_ratio             | trend             |             265 | 0.40%          |           65520 | 99.60%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| drawdown_change_3m            | drawdown_recovery |             243 | 0.37%          |           65542 | 99.63%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| mom_4m                        | core_momentum     |             221 | 0.34%          |           65564 | 99.66%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| core_mom_456_avg              | core_momentum     |             221 | 0.34%          |           65564 | 99.66%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| core_mom_456_min              | core_momentum     |             221 | 0.34%          |           65564 | 99.66%          | 2016-01-31          | 2026-10-31         | False     |           nan |
| core_mom_456_max              | core_momentum     |             221 | 0.34%          |           65564 | 99.66%          | 2016-01-31          | 2026-10-31         | False     |           nan |

### Dropped high-missing features
_No features dropped by missingness filter._

## Committed first-20k panel slice
`outputs/panel_head_20000.csv` contains the first 20,000 rows of the cleaned panel. It is committed for quick inspection and future model-design reference; the full panel remains in the GitHub Actions artifact.
Columns in slice: 125

## Model-design panel sample
This small committed sample contains historical labeled rows and recent examples for model-design inspection. The full panel is uploaded as a GitHub Actions artifact.
| sample_source                     | month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_top10_1_3m |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |   label_mega100_1_3m |
|:----------------------------------|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|-------------------:|--------------------------:|-------------------------:|---------------------:|
| historical_mega100_examples       | 2016-01-31 | FCX      |     4.134   | -60.92%  | -60.70%  | -56.55%            |            2.9085e+08  | 53.97%               | 11.90%                | 93.94%             | 204.35%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2016-01-31 | LEU      |     1.37    | -49.26%  | -65.23%  | -61.39%            |        74400.9         | 46.83%               | 10.32%                | 64.68%             | 229.20%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-01-31 | TRGP     |    14.072   | -59.11%  | -73.14%  | -63.68%            |            3.6601e+07  | 43.65%               | 9.52%                 | 69.28%             | 84.40%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2016-02-29 | LEU      |     1.32    | -21.43%  | -65.17%  | -57.67%            |        58517.2         | 51.59%               | 11.11%                | 64.76%             | 241.67%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-02-29 | AMD      |     2.14    | -9.32%   | 18.23%   | 14.53%             |            3.01533e+07 | 40.48%               | 7.94%                 | 66.62%             | 113.55%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-02-29 | DVN      |    13.4278  | -56.94%  | -53.27%  | -50.87%            |            2.13355e+08 | 44.44%               | 7.14%                 | 88.58%             | 85.36%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-04-30 | AMD      |     3.55    | 61.36%   | 67.45%   | 47.19%             |            4.55973e+07 | 46.83%               | 12.70%                | 70.99%             | 93.24%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-08-31 | LEU      |     3.46    | 14.19%   | 162.12%  | 49.10%             |       150004           | 42.86%               | 11.90%                | 65.20%             | 88.15%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-01-31 | PLUG     |     1.06    | -30.72%  | -40.78%  | -36.80%            |            4.82764e+06 | 25.40%               | 3.97%                 | 64.09%             | 111.32%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2017-02-28 | PLUG     |     1.08    | -21.17%  | -30.32%  | -32.19%            |            7.26119e+06 | 32.54%               | 5.56%                 | 65.39%             | 107.41%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2017-04-30 | CVNA     |     2.22    |          |          |                    |                        |                      |                       | 0.00%              | 84.41%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-05-31 | CVNA     |     2.01    |          |          |                    |                        |                      |                       | 0.00%              | 103.68%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2017-08-31 | ENPH     |     0.92    | 21.05%   | -48.60%  | -34.71%            |       600677           | 44.44%               | 7.14%                 | 65.18%             | 215.22%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2017-09-30 | ENPH     |     1.52    | 74.71%   | 10.95%   | 46.23%             |       821362           | 43.65%               | 10.32%                | 65.28%             | 90.79%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-10-31 | ENPH     |     1.53    | 62.77%   | 28.57%   | 68.58%             |       845932           | 46.03%               | 11.90%                | 65.37%             | 89.54%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-12-31 | ENPH     |     2.41    | 58.55%   | 177.01%  | 165.12%            |            2.1306e+06  | 50.00%               | 15.08%                | 65.56%             | 89.63%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-01-31 | ENPH     |     2.2     | 43.79%   | 134.04%  | 105.97%            |            2.52291e+06 | 52.38%               | 16.67%                | 65.65%             | 107.73%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-03-31 | TKO      |    32.457   | 18.14%   | 53.98%   | 39.32%             |            2.72076e+07 | 7.94%                | 1.59%                 | 56.28%             | 102.62%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-04-30 | TKO      |    35.8641  | 12.92%   | 51.03%   | 40.74%             |            2.85679e+07 | 7.14%                | 0.79%                 | 47.28%             | 99.21%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-05-31 | CVNA     |     5.77    | 43.96%   | 77.98%   | 60.00%             |            2.393e+07   | 38.89%               | 11.11%                | 66.52%             | 124.40%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-06-30 | AMD      |    14.99    | 49.15%   | 45.82%   | 26.23%             |            7.8752e+08  | 28.57%               | 3.97%                 | 96.68%             | 106.07%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-12-31 | ENPH     |     4.73    | -2.47%   | -29.72%  | -17.83%            |            8.59184e+06 | 44.44%               | 9.52%                 | 64.85%             | 95.14%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | PLUG     |     1.24    | -35.42%  | -38.61%  | -37.89%            |            4.00456e+06 | 20.63%               | 3.17%                 | 61.31%             | 93.55%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | SE       |    11.32    | -18.15%  | -24.53%  | -21.60%            |            1.70236e+07 | 33.33%               | 7.14%                 | 64.08%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-04-30 | ENPH     |    10.04    | 38.87%   | 121.15%  | 106.44%            |            1.86016e+07 | 39.68%               | 11.11%                | 64.91%             | 180.38%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-09-30 | BE       |     3.25    | -73.51%  | -74.85%  | -73.63%            |            1.35115e+07 | 44.44%               | 9.52%                 | 65.40%             | 129.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | BE       |     3.06    | -70.72%  | -77.53%  | -74.75%            |            1.11875e+07 | 43.65%               | 8.73%                 | 65.43%             | 157.52%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | PCG      |     6.0393  | -65.97%  | -72.60%  | -69.87%            |            1.31098e+08 | 50.00%               | 12.70%                | 81.54%             | 146.52%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-10-31 | TSLA     |    20.9947  | 30.34%   | 31.94%   | 47.65%             |            1.94498e+09 | 23.02%               | 3.17%                 | 96.81%             | 106.58%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | ENPH     |    21.87    | -26.29%  | 44.17%   | 13.94%             |            1.27686e+08 | 43.65%               | 11.90%                | 80.41%             | 123.91%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | PCG      |     7.30198 | -28.61%  | -56.37%  | -60.89%            |            1.33322e+08 | 52.38%               | 16.67%                | 81.55%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | TSLA     |    21.996   | 46.24%   | 78.19%   | 54.13%             |            2.36702e+09 | 19.84%               | 3.17%                 | 96.34%             | 102.46%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-02-29 | EQT      |     5.46579 | -32.38%  | -41.79%  | -43.68%            |            5.55426e+07 | 42.86%               | 8.73%                 | 67.55%             | 148.55%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | APA      |     3.53296 | -83.54%  | -83.36%  | -81.67%            |            1.29382e+08 | 31.75%               | 6.35%                 | 73.06%             | 223.92%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | CELH     |     1.40333 | -12.84%  | 20.98%   | 9.13%              |            2.39728e+06 | 38.10%               | 11.11%                | 63.68%             | 179.57%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | TRGP     |     6.01849 | -82.66%  | -81.97%  | -81.46%            |            7.2394e+07  | 21.43%               | 5.56%                 | 60.95%             | 192.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-04-30 | CELH     |     1.67333 | -7.04%   | 42.61%   | 16.68%             |            1.90872e+06 | 40.48%               | 12.70%                | 62.87%             | 192.23%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-04-30 | TWLO     |   112.3     | -9.68%   | 16.30%   | 13.10%             |            3.57971e+08 | 30.95%               | 5.56%                 | 60.35%             | 147.03%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-05-31 | PLUG     |     4.21    | -3.00%   | 7.95%    | 16.65%             |            4.86118e+07 | 42.86%               | 13.49%                | 62.64%             | 208.31%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-05-31 | TSLA     |    55.6667  | 25.00%   | 153.08%  | 93.68%             |            1.11066e+10 | 40.48%               | 17.46%                | 96.69%             | 198.40%                  |                  1 |                         1 |                        1 |                    1 |

## Latest clean panel sample
| month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |
|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|--------------------------:|-------------------------:|
| 2026-10-31 | A        |      174.87 | 26.57%   | 51.85%   | 37.72%             |            361,362,105 | 12.70%               | 0.79%                 | 51.00%             |                          |                         0 |                        0 |
| 2026-10-31 | AAPL     |      344.63 | 11.66%   | 27.23%   | 18.99%             |         13,555,059,519 | 6.35%                | 0.00%                 | 49.56%             |                          |                         0 |                        0 |
| 2026-10-31 | ABBV     |      294.89 | 18.24%   | 41.40%   | 32.47%             |          1,238,070,228 | 6.35%                | 0.79%                 | 48.69%             |                          |                         0 |                        0 |
| 2026-10-31 | ABNB     |      164.39 | 8.49%    | 17.12%   | 18.44%             |            801,521,240 | 12.70%               | 1.59%                 | 65.10%             |                          |                         0 |                        0 |
| 2026-10-31 | ABT      |      106.2  | 1.09%    | 18.53%   | 20.95%             |            916,082,679 | 6.35%                | 0.79%                 | 49.94%             |                          |                         0 |                        0 |
| 2026-10-31 | ACGL     |      106.36 | 5.80%    | 12.60%   | 13.74%             |            279,093,084 | 4.76%                | 0.00%                 | 22.38%             |                          |                         0 |                        0 |
| 2026-10-31 | ACN      |      258.24 | 56.89%   | 47.41%   | 66.65%             |          1,236,739,456 | 32.54%               | 9.52%                 | 86.63%             |                          |                         0 |                        0 |
| 2026-10-31 | ADBE     |      250.23 | -0.07%   | 1.68%    | 6.76%              |          1,203,662,779 | 28.57%               | 6.35%                 | 82.80%             |                          |                         0 |                        0 |
| 2026-10-31 | ADI      |      417.11 | 13.87%   | 4.29%    | 3.67%              |          1,351,781,367 | 22.22%               | 2.38%                 | 75.85%             |                          |                         0 |                        0 |
| 2026-10-31 | ADM      |       76.91 | -2.36%   | 4.52%    | 0.95%              |            279,003,185 | 9.52%                | 0.79%                 | 34.92%             |                          |                         0 |                        0 |
| 2026-10-31 | ADP      |      293.84 | 10.98%   | 40.59%   | 35.65%             |            590,170,276 | 11.90%               | 1.59%                 | 54.57%             |                          |                         0 |                        0 |
| 2026-10-31 | ADSK     |      249.61 | 6.58%    | 5.32%    | 13.87%             |            464,854,000 | 23.81%               | 4.76%                 | 70.31%             |                          |                         0 |                        0 |
| 2026-10-31 | AEE      |      110.54 | 1.56%    | -1.36%   | 0.32%              |            177,540,569 | 1.59%                | 0.00%                 | 10.39%             |                          |                         0 |                        0 |
| 2026-10-31 | AEP      |      130.21 | 2.62%    | -3.61%   | -1.38%             |            453,786,088 | 2.38%                | 0.00%                 | 26.62%             |                          |                         0 |                        0 |
| 2026-10-31 | AES      |       14.83 | 2.22%    | 6.39%    | 4.49%              |            123,552,379 | 0.00%                | 0.00%                 | 5.15%              |                          |                         0 |                        0 |
| 2026-10-31 | AFL      |      123.89 | -2.33%   | 10.11%   | 9.02%              |            231,007,993 | 0.79%                | 0.00%                 | 12.56%             |                          |                         0 |                        0 |
| 2026-10-31 | AIG      |       81.9  | 4.92%    | 10.95%   | 11.12%             |            313,905,977 | 3.17%                | 0.00%                 | 21.82%             |                          |                         0 |                        0 |
| 2026-10-31 | AIZ      |      292.8  | 5.20%    | 24.74%   | 17.51%             |            102,544,768 | 2.38%                | 0.79%                 | 14.14%             |                          |                         0 |                        0 |
| 2026-10-31 | AJG      |      276.07 | 10.98%   | 34.56%   | 31.08%             |            364,424,152 | 14.29%               | 2.38%                 | 55.30%             |                          |                         0 |                        0 |
| 2026-10-31 | AKAM     |       92.72 | -19.50%  | -9.96%   | -23.17%            |            495,754,631 | 36.51%               | 7.94%                 | 79.00%             |                          |                         0 |                        0 |
| 2026-10-31 | ALAB     |      258.7  | -16.88%  | 32.84%   | -12.71%            |          1,276,267,679 | 58.73%               | 19.05%                | 94.40%             |                          |                         0 |                        0 |
| 2026-10-31 | ALB      |       91    | -22.38%  | -53.46%  | -44.65%            |            274,121,643 | 27.78%               | 4.76%                 | 62.58%             |                          |                         0 |                        0 |
| 2026-10-31 | ALGN     |      149.89 | -11.39%  | -14.84%  | -13.43%            |            142,044,711 | 19.84%               | 2.38%                 | 46.73%             |                          |                         0 |                        0 |
| 2026-10-31 | ALL      |      259.87 | -1.18%   | 20.74%   | 19.23%             |            472,745,116 | 9.52%                | 0.00%                 | 40.14%             |                          |                         0 |                        0 |
| 2026-10-31 | ALLE     |      186.44 | 18.87%   | 36.66%   | 38.09%             |            195,272,735 | 7.94%                | 1.59%                 | 36.43%             |                          |                         0 |                        0 |
| 2026-10-31 | AMAT     |      390.09 | -23.08%  | -0.89%   | -20.04%            |          3,239,376,612 | 46.03%               | 11.11%                | 93.20%             |                          |                         0 |                        0 |
| 2026-10-31 | AMCR     |       47.39 | 7.11%    | 28.47%   | 21.06%             |            149,414,536 | 10.32%               | 0.79%                 | 29.55%             |                          |                         0 |                        0 |
| 2026-10-31 | AMD      |      504.8  | 6.02%    | 42.40%   | 9.04%              |         11,452,651,724 | 48.41%               | 14.29%                | 95.95%             |                          |                         0 |                        0 |
| 2026-10-31 | AME      |      241.12 | -0.10%   | 2.69%    | 3.19%              |            338,849,907 | 6.35%                | 0.00%                 | 28.78%             |                          |                         0 |                        0 |
| 2026-10-31 | AMGN     |      466.01 | 21.70%   | 36.40%   | 35.00%             |          1,160,392,131 | 9.52%                | 0.00%                 | 50.17%             |                          |                         0 |                        0 |

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