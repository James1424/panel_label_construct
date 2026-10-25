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
| label_boom30_top10_1_3m |            3373 |               65255 | 5.17%           |                    128 |                   25.9462 |                         0 |                        53 |
| label_boom40_top10_1_3m |            1930 |               65255 | 2.96%           |                    126 |                   14.8462 |                         0 |                        53 |
| label_boom50_top5_1_3m  |            1096 |               65255 | 1.68%           |                    123 |                    8.4308 |                         0 |                        27 |
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
| 2026-07-31 |    529 |       529 | 7.26%                         | 23.71%                       | 34.51%                       | 265.01%                      |                       53 |                      27 |                              37 |                              18 |                              8 |                          1 |
| 2026-08-31 |    529 |       529 | 1.48%                         | 13.14%                       | 16.71%                       | 42.58%                       |                       53 |                      27 |                               6 |                               2 |                              0 |                          0 |
| 2026-09-30 |    529 |       529 | 3.37%                         | 14.50%                       | 18.00%                       | 38.13%                       |                       53 |                      27 |                               5 |                               0 |                              0 |                          0 |
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
| yearly_top_future_return_examples | 2016-01-31 | TRGP     |    14.1286  | -59.11%  | -73.14%  | -63.68%            |            3.67481e+07 | 43.65%               | 9.52%                 | 69.28%             | 84.40%                   |                  1 |                         1 |                        1 |                    0 |
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
| historical_mega100_examples       | 2019-10-31 | PCG      |     6.0393  | -65.97%  | -72.60%  | -69.87%            |            1.31098e+08 | 50.00%               | 12.70%                | 81.47%             | 146.52%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-10-31 | TSLA     |    20.9947  | 30.34%   | 31.94%   | 47.65%             |            1.94498e+09 | 23.02%               | 3.17%                 | 96.81%             | 106.58%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | ENPH     |    21.87    | -26.29%  | 44.17%   | 13.94%             |            1.27686e+08 | 43.65%               | 11.90%                | 80.41%             | 123.91%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | PCG      |     7.30198 | -28.61%  | -56.37%  | -60.89%            |            1.33322e+08 | 52.38%               | 16.67%                | 81.48%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | TSLA     |    21.996   | 46.24%   | 78.19%   | 54.13%             |            2.36702e+09 | 19.84%               | 3.17%                 | 96.34%             | 102.46%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-02-29 | EQT      |     5.46579 | -32.38%  | -41.79%  | -43.68%            |            5.55426e+07 | 42.86%               | 8.73%                 | 67.55%             | 148.55%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | APA      |     3.53296 | -83.54%  | -83.36%  | -81.67%            |            1.29382e+08 | 31.75%               | 6.35%                 | 73.06%             | 223.92%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | CELH     |     1.40333 | -12.84%  | 20.98%   | 9.13%              |            2.39728e+06 | 38.10%               | 11.11%                | 63.68%             | 179.57%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | TRGP     |     6.04267 | -82.66%  | -81.97%  | -81.46%            |            7.26848e+07 | 21.43%               | 5.56%                 | 60.97%             | 192.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-04-30 | CELH     |     1.67333 | -7.04%   | 42.61%   | 16.68%             |            1.90872e+06 | 40.48%               | 12.70%                | 62.87%             | 192.23%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-04-30 | TWLO     |   112.3     | -9.68%   | 16.30%   | 13.10%             |            3.57971e+08 | 30.95%               | 5.56%                 | 60.35%             | 147.03%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-05-31 | PLUG     |     4.21    | -3.00%   | 7.95%    | 16.65%             |            4.86118e+07 | 42.86%               | 13.49%                | 62.64%             | 208.31%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-05-31 | TSLA     |    55.6667  | 25.00%   | 153.08%  | 93.68%             |            1.11066e+10 | 40.48%               | 17.46%                | 96.69%             | 198.40%                  |                  1 |                         1 |                        1 |                    1 |

## Latest clean panel sample
| month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |
|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|--------------------------:|-------------------------:|
| 2026-10-31 | A        |      173.07 | 25.26%   | 50.29%   | 36.30%             |            354,034,240 | 13.49%               | 0.79%                 | 51.64%             |                          |                         0 |                        0 |
| 2026-10-31 | AAPL     |      347.73 | 12.66%   | 28.38%   | 20.06%             |         14,285,980,700 | 7.14%                | 0.00%                 | 50.54%             |                          |                         0 |                        0 |
| 2026-10-31 | ABBV     |      285.64 | 14.53%   | 36.97%   | 28.31%             |          1,272,216,100 | 7.94%                | 0.79%                 | 50.97%             |                          |                         0 |                        0 |
| 2026-10-31 | ABNB     |      172.01 | 13.52%   | 22.55%   | 23.93%             |            811,147,440 | 12.70%               | 1.59%                 | 65.73%             |                          |                         0 |                        0 |
| 2026-10-31 | ABT      |      103.7  | -1.29%   | 15.74%   | 18.10%             |            941,446,378 | 6.35%                | 0.79%                 | 50.43%             |                          |                         0 |                        0 |
| 2026-10-31 | ACGL     |      101.69 | 1.15%    | 7.65%    | 8.75%              |            278,385,141 | 5.56%                | 0.00%                 | 22.85%             |                          |                         0 |                        0 |
| 2026-10-31 | ACN      |      249.37 | 51.50%   | 42.35%   | 60.92%             |          1,236,769,924 | 30.16%               | 9.52%                 | 86.21%             |                          |                         0 |                        0 |
| 2026-10-31 | ADBE     |      263.82 | 5.36%    | 7.20%    | 12.55%             |          1,261,322,204 | 27.78%               | 6.35%                 | 82.89%             |                          |                         0 |                        0 |
| 2026-10-31 | ADI      |      391.07 | 6.76%    | -2.22%   | -2.80%             |          1,337,904,795 | 20.63%               | 2.38%                 | 75.06%             |                          |                         0 |                        0 |
| 2026-10-31 | ADM      |       80.14 | 1.74%    | 8.91%    | 5.19%              |            294,439,589 | 10.32%               | 0.79%                 | 37.00%             |                          |                         0 |                        0 |
| 2026-10-31 | ADP      |      304.16 | 14.88%   | 45.53%   | 40.41%             |            598,079,169 | 12.70%               | 2.38%                 | 58.56%             |                          |                         0 |                        0 |
| 2026-10-31 | ADSK     |      252.2  | 7.69%    | 6.41%    | 15.05%             |            482,622,137 | 23.81%               | 4.76%                 | 70.66%             |                          |                         0 |                        0 |
| 2026-10-31 | AEE      |      108.04 | -0.73%   | -3.59%   | -1.95%             |            181,881,046 | 1.59%                | 0.00%                 | 10.11%             |                          |                         0 |                        0 |
| 2026-10-31 | AEP      |      129.69 | 2.21%    | -4.00%   | -1.77%             |            457,623,007 | 2.38%                | 0.00%                 | 26.16%             |                          |                         0 |                        0 |
| 2026-10-31 | AES      |       15    | 2.18%    | 6.35%    | 4.46%              |            121,032,675 | 0.00%                | 0.00%                 | 4.78%              |                          |                         0 |                        0 |
| 2026-10-31 | AFL      |      120.51 | -4.99%   | 7.10%    | 6.05%              |            233,726,472 | 0.79%                | 0.00%                 | 12.32%             |                          |                         0 |                        0 |
| 2026-10-31 | AIG      |       81.26 | 4.10%    | 10.08%   | 10.25%             |            314,257,412 | 3.97%                | 0.79%                 | 28.44%             |                          |                         0 |                        0 |
| 2026-10-31 | AIZ      |      284.75 | 2.31%    | 21.31%   | 14.28%             |            104,816,826 | 2.38%                | 0.79%                 | 13.92%             |                          |                         0 |                        0 |
| 2026-10-31 | AJG      |      268.04 | 7.75%    | 30.64%   | 27.27%             |            351,872,162 | 14.29%               | 2.38%                 | 54.50%             |                          |                         0 |                        0 |
| 2026-10-31 | AKAM     |       93.53 | -18.80%  | -9.18%   | -22.50%            |            491,018,199 | 36.51%               | 7.14%                 | 78.60%             |                          |                         0 |                        0 |
| 2026-10-31 | ALAB     |      257.16 | -17.37%  | 32.05%   | -13.23%            |          1,302,182,152 | 59.52%               | 19.05%                | 94.57%             |                          |                         0 |                        0 |
| 2026-10-31 | ALB      |       93.67 | -20.11%  | -52.10%  | -43.03%            |            277,490,795 | 28.57%               | 4.76%                 | 63.36%             |                          |                         0 |                        0 |
| 2026-10-31 | ALGN     |      154.51 | -8.66%   | -12.22%  | -10.76%            |            145,957,764 | 20.63%               | 2.38%                 | 47.70%             |                          |                         0 |                        0 |
| 2026-10-31 | ALL      |      253.19 | -3.72%   | 17.64%   | 16.17%             |            480,654,053 | 9.52%                | 0.00%                 | 39.94%             |                          |                         0 |                        0 |
| 2026-10-31 | ALLE     |      178.98 | 14.11%   | 31.19%   | 32.57%             |            191,291,108 | 7.94%                | 1.59%                 | 37.33%             |                          |                         0 |                        0 |
| 2026-10-31 | AMAT     |      377.24 | -25.61%  | -4.15%   | -22.67%            |          3,356,767,215 | 46.03%               | 10.32%                | 93.13%             |                          |                         0 |                        0 |
| 2026-10-31 | AMCR     |       46.11 | 4.22%    | 25.00%   | 17.79%             |            154,881,701 | 10.32%               | 0.79%                 | 30.24%             |                          |                         0 |                        0 |
| 2026-10-31 | AMD      |      516.79 | 8.54%    | 45.78%   | 11.63%             |         11,641,421,445 | 49.21%               | 14.29%                | 95.94%             |                          |                         0 |                        0 |
| 2026-10-31 | AME      |      240.03 | -0.55%   | 2.23%    | 2.72%              |            335,474,163 | 6.35%                | 0.00%                 | 28.04%             |                          |                         0 |                        0 |
| 2026-10-31 | AMGN     |      439.26 | 14.71%   | 28.57%   | 27.26%             |          1,156,982,298 | 10.32%               | 0.00%                 | 51.66%             |                          |                         0 |                        0 |

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