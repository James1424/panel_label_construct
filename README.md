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
| tickers               | 531      |
| avg_source_count      |   1.0678 |
| max_source_count      |   2      |
| avg_source_weight_sum |   3.339  |
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
| raw_rows           | 64939               |
| clean_rows         | 64939               |
| raw_columns        | 136                 |
| clean_columns      | 125                 |
| raw_tickers        | 531                 |
| clean_tickers      | 531                 |
| months             | 128                 |
| first_month        | 2016-01-31 00:00:00 |
| last_month         | 2026-08-31 00:00:00 |
| candidate_features | 109                 |
| kept_features      | 109                 |
| dropped_features   | 0                   |

## Tail-label summary
| label                   |   positive_rows |   valid_future_rows | positive_rate   |   months_with_positive |   avg_positives_per_month |   min_positives_per_month |   max_positives_per_month |
|:------------------------|----------------:|--------------------:|:----------------|-----------------------:|--------------------------:|--------------------------:|--------------------------:|
| label_top10_1_3m        |            6505 |               64408 | 10.10%          |                    127 |                   50.8203 |                         0 |                        54 |
| label_top5_1_3m         |            3291 |               64408 | 5.11%           |                    127 |                   25.7109 |                         0 |                        27 |
| label_boom30_top10_1_3m |            3341 |               64408 | 5.19%           |                    126 |                   26.1016 |                         0 |                        53 |
| label_boom40_top10_1_3m |            1910 |               64408 | 2.97%           |                    125 |                   14.9219 |                         0 |                        53 |
| label_boom50_top5_1_3m  |            1092 |               64408 | 1.70%           |                    123 |                    8.5312 |                         0 |                        27 |
| label_mega100_1_3m      |             273 |               64408 | 0.42%           |                     72 |                    2.1328 |                         0 |                        22 |

## Recent monthly label distribution
| month      |   rows |   tickers | future_max_return_1_3m_mean   | future_max_return_1_3m_p90   | future_max_return_1_3m_p95   | future_max_return_1_3m_max   |   label_top10_1_3m_count |   label_top5_1_3m_count |   label_boom30_top10_1_3m_count |   label_boom40_top10_1_3m_count |   label_boom50_top5_1_3m_count |   label_mega100_1_3m_count |
|:-----------|-------:|----------:|:------------------------------|:-----------------------------|:-----------------------------|:-----------------------------|-------------------------:|------------------------:|--------------------------------:|--------------------------------:|-------------------------------:|---------------------------:|
| 2025-03-31 |    528 |       528 | 12.15%                        | 35.54%                       | 53.03%                       | 194.45%                      |                       53 |                      27 |                              53 |                              47 |                             27 |                          7 |
| 2025-04-30 |    528 |       528 | 18.25%                        | 44.18%                       | 62.97%                       | 222.62%                      |                       53 |                      27 |                              53 |                              53 |                             27 |                         10 |
| 2025-05-31 |    528 |       528 | 14.47%                        | 33.01%                       | 44.51%                       | 248.51%                      |                       53 |                      27 |                              53 |                              34 |                             23 |                          6 |
| 2025-06-30 |    528 |       528 | 12.23%                        | 29.49%                       | 46.30%                       | 253.55%                      |                       53 |                      27 |                              52 |                              30 |                             23 |                          7 |
| 2025-07-31 |    528 |       528 | 13.14%                        | 29.93%                       | 49.93%                       | 364.42%                      |                       53 |                      27 |                              53 |                              39 |                             27 |                          9 |
| 2025-08-31 |    528 |       528 | 10.43%                        | 28.53%                       | 49.75%                       | 325.54%                      |                       53 |                      27 |                              49 |                              33 |                             27 |                          8 |
| 2025-09-30 |    528 |       528 | 6.73%                         | 21.89%                       | 31.61%                       | 126.53%                      |                       53 |                      27 |                              30 |                              18 |                              9 |                          2 |
| 2025-10-31 |    529 |       529 | 9.23%                         | 23.31%                       | 31.15%                       | 189.09%                      |                       53 |                      27 |                              28 |                              14 |                             10 |                          1 |
| 2025-11-30 |    529 |       529 | 12.82%                        | 30.82%                       | 43.50%                       | 184.56%                      |                       53 |                      27 |                              53 |                              36 |                             19 |                          3 |
| 2025-12-31 |    529 |       529 | 11.40%                        | 31.83%                       | 44.57%                       | 167.66%                      |                       53 |                      27 |                              53 |                              33 |                             24 |                          1 |
| 2026-01-31 |    529 |       529 | 9.75%                         | 27.41%                       | 45.89%                       | 130.28%                      |                       53 |                      27 |                              45 |                              36 |                             23 |                          4 |
| 2026-02-28 |    529 |       529 | 9.75%                         | 35.20%                       | 61.48%                       | 188.52%                      |                       53 |                      27 |                              53 |                              48 |                             27 |                         15 |
| 2026-03-31 |    529 |       529 | 20.28%                        | 47.67%                       | 89.27%                       | 340.71%                      |                       53 |                      27 |                              53 |                              53 |                             27 |                         22 |
| 2026-04-30 |    529 |       529 | 12.85%                        | 36.38%                       | 53.05%                       | 148.03%                      |                       53 |                      27 |                              53 |                              44 |                             27 |                          7 |
| 2026-05-31 |    530 |       530 | 10.38%                        | 25.97%                       | 33.44%                       | 207.54%                      |                       54 |                      27 |                              36 |                              16 |                              5 |                          1 |
| 2026-06-30 |    531 |       531 | 5.96%                         | 25.51%                       | 30.93%                       | 107.24%                      |                       54 |                      27 |                              36 |                              11 |                              6 |                          1 |
| 2026-07-31 |    531 |       531 | 3.60%                         | 13.67%                       | 20.00%                       | 164.74%                      |                       54 |                      27 |                               7 |                               3 |                              1 |                          1 |
| 2026-08-31 |    531 |       531 |                               |                              |                              |                              |                        0 |                       0 |                               0 |                               0 |                              0 |                          0 |

## Feature missingness report
A feature is dropped if `missing_rate > 35%` or `non_null_rows < 1000`.

### Highest-missing candidate features
| feature                       | feature_group     |   missing_count | missing_rate   |   non_null_rows | non_null_rate   | first_valid_month   | last_valid_month   | dropped   |   drop_reason |
|:------------------------------|:------------------|----------------:|:---------------|----------------:|:----------------|:--------------------|:-------------------|:----------|--------------:|
| rel_mom_12m_vs_qqq            | relative_strength |             687 | 1.06%          |           64252 | 98.94%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_12m                       | other_momentum    |             687 | 1.06%          |           64252 | 98.94%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| up_day_volume_ratio_3m        | volume_flow       |             616 | 0.95%          |           64323 | 99.05%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| up_day_dollar_volume_ratio_3m | volume_flow       |             616 | 0.95%          |           64323 | 99.05%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_9m                        | other_momentum    |             507 | 0.78%          |           64432 | 99.22%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_7m                        | other_momentum    |             390 | 0.60%          |           64549 | 99.40%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_6m                        | core_momentum     |             332 | 0.51%          |           64607 | 99.49%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_4m_vs_6m                  | core_momentum     |             332 | 0.51%          |           64607 | 99.49%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_5m_vs_6m                  | core_momentum     |             332 | 0.51%          |           64607 | 99.49%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_6m_first3m                | core_momentum     |             332 | 0.51%          |           64607 | 99.49%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_6m_acceleration           | core_momentum     |             332 | 0.51%          |           64607 | 99.49%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| ret_lag_6m                    | sequence_path     |             332 | 0.51%          |           64607 | 99.49%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| rel_mom_6m_vs_qqq             | relative_strength |             332 | 0.51%          |           64607 | 99.49%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_3m_vs_6m                  | other_momentum    |             332 | 0.51%          |           64607 | 99.49%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| return_vol_ratio_6m           | risk_drawdown     |             332 | 0.51%          |           64607 | 99.49%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| drawdown_12m                  | risk_drawdown     |             331 | 0.51%          |           64608 | 99.49%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| drawdown_12m_abs              | risk_drawdown     |             331 | 0.51%          |           64608 | 99.49%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| volume_change_3m              | volume_flow       |             320 | 0.49%          |           64619 | 99.51%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| dollar_volume_change_3m       | volume_flow       |             320 | 0.49%          |           64619 | 99.51%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| ma100_slope_1m                | trend             |             319 | 0.49%          |           64620 | 99.51%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| volume_ma3_to_12m             | volume_flow       |             282 | 0.43%          |           64657 | 99.57%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_5m                        | core_momentum     |             277 | 0.43%          |           64662 | 99.57%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| core_mom_456_std              | core_momentum     |             277 | 0.43%          |           64662 | 99.57%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| ret_lag_5m                    | sequence_path     |             277 | 0.43%          |           64662 | 99.57%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| price_ma100_ratio             | trend             |             265 | 0.41%          |           64674 | 99.59%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| drawdown_change_3m            | drawdown_recovery |             244 | 0.38%          |           64695 | 99.62%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_4m                        | core_momentum     |             222 | 0.34%          |           64717 | 99.66%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| core_mom_456_avg              | core_momentum     |             222 | 0.34%          |           64717 | 99.66%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| core_mom_456_min              | core_momentum     |             222 | 0.34%          |           64717 | 99.66%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| core_mom_456_max              | core_momentum     |             222 | 0.34%          |           64717 | 99.66%          | 2016-01-31          | 2026-08-31         | False     |           nan |

### Dropped high-missing features
_No features dropped by missingness filter._

## Committed first-20k panel slice
`outputs/panel_head_20000.csv` contains the first 20,000 rows of the cleaned panel. It is committed for quick inspection and future model-design reference; the full panel remains in the GitHub Actions artifact.
Columns in slice: 125

## Model-design panel sample
This small committed sample contains historical labeled rows and recent examples for model-design inspection. The full panel is uploaded as a GitHub Actions artifact.
| sample_source                     | month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_top10_1_3m |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |   label_mega100_1_3m |
|:----------------------------------|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|-------------------:|--------------------------:|-------------------------:|---------------------:|
| historical_mega100_examples       | 2016-01-31 | FCX      |     4.14292 | -60.92%  | -60.70%  | -56.55%            |            2.91478e+08 | 53.97%               | 11.90%                | 94.10%             | 204.35%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2016-01-31 | LEU      |     1.37    | -49.26%  | -65.23%  | -61.39%            |        74400.9         | 46.83%               | 10.32%                | 64.68%             | 229.20%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-01-31 | TRGP     |    14.1286  | -59.11%  | -73.14%  | -63.68%            |            3.67481e+07 | 43.65%               | 9.52%                 | 69.27%             | 84.40%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2016-02-29 | LEU      |     1.32    | -21.43%  | -65.17%  | -57.67%            |        58517.2         | 51.59%               | 11.11%                | 64.76%             | 241.67%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-02-29 | AMD      |     2.14    | -9.32%   | 18.23%   | 14.53%             |            3.01533e+07 | 40.48%               | 7.94%                 | 66.57%             | 113.55%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-02-29 | DVN      |    13.5148  | -56.94%  | -53.27%  | -50.87%            |            2.14737e+08 | 44.44%               | 7.14%                 | 88.77%             | 85.36%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-04-30 | AMD      |     3.55    | 61.36%   | 67.45%   | 47.19%             |            4.55973e+07 | 46.83%               | 12.70%                | 70.90%             | 93.24%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-08-31 | LEU      |     3.46    | 14.19%   | 162.12%  | 49.10%             |       150004           | 42.86%               | 11.90%                | 65.20%             | 88.15%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-01-31 | PLUG     |     1.06    | -30.72%  | -40.78%  | -36.80%            |            4.82764e+06 | 25.40%               | 3.97%                 | 64.14%             | 111.32%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2017-02-28 | PLUG     |     1.08    | -21.17%  | -30.32%  | -32.19%            |            7.26119e+06 | 32.54%               | 5.56%                 | 65.38%             | 107.41%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2017-04-30 | CVNA     |     2.22    |          |          |                    |                        |                      |                       | 0.00%              | 84.41%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-05-31 | CVNA     |     2.01    |          |          |                    |                        |                      |                       | 0.00%              | 103.68%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2017-08-31 | ENPH     |     0.92    | 21.05%   | -48.60%  | -34.71%            |       600677           | 44.44%               | 7.14%                 | 65.18%             | 215.22%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2017-09-30 | ENPH     |     1.52    | 74.71%   | 10.95%   | 46.23%             |       821362           | 43.65%               | 10.32%                | 65.28%             | 90.79%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-10-31 | ENPH     |     1.53    | 62.77%   | 28.57%   | 68.58%             |       845932           | 46.03%               | 11.90%                | 65.37%             | 89.54%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-12-31 | ENPH     |     2.41    | 58.55%   | 177.01%  | 165.12%            |            2.1306e+06  | 50.00%               | 15.08%                | 65.56%             | 89.63%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-01-31 | ENPH     |     2.2     | 43.79%   | 134.04%  | 105.97%            |            2.52291e+06 | 52.38%               | 16.67%                | 65.58%             | 107.73%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-03-31 | TKO      |    32.5899  | 18.14%   | 53.98%   | 39.32%             |            2.7319e+07  | 7.94%                | 1.59%                 | 56.33%             | 102.62%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-04-30 | TKO      |    36.0109  | 12.92%   | 51.03%   | 40.74%             |            2.86848e+07 | 7.14%                | 0.79%                 | 47.37%             | 99.21%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-05-31 | CVNA     |     5.77    | 43.96%   | 77.98%   | 60.00%             |            2.393e+07   | 38.89%               | 11.11%                | 66.54%             | 124.40%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-06-30 | AMD      |    14.99    | 49.15%   | 45.82%   | 26.23%             |            7.8752e+08  | 28.57%               | 3.97%                 | 96.73%             | 106.07%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-12-31 | ENPH     |     4.73    | -2.47%   | -29.72%  | -17.83%            |            8.59184e+06 | 44.44%               | 9.52%                 | 64.89%             | 95.14%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | PLUG     |     1.24    | -35.42%  | -38.61%  | -37.89%            |            4.00456e+06 | 20.63%               | 3.17%                 | 61.27%             | 93.55%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | SE       |    11.32    | -18.15%  | -24.53%  | -21.60%            |            1.70236e+07 | 33.33%               | 7.14%                 | 64.08%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-04-30 | ENPH     |    10.04    | 38.87%   | 121.15%  | 106.44%            |            1.86016e+07 | 39.68%               | 11.11%                | 64.98%             | 180.38%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-09-30 | BE       |     3.25    | -73.51%  | -74.85%  | -73.63%            |            1.35115e+07 | 44.44%               | 9.52%                 | 65.40%             | 129.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | BE       |     3.06    | -70.72%  | -77.53%  | -74.75%            |            1.11875e+07 | 43.65%               | 8.73%                 | 65.43%             | 157.52%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | PCG      |     6.0642  | -65.97%  | -72.60%  | -69.87%            |            1.31638e+08 | 50.00%               | 12.70%                | 81.75%             | 146.52%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-10-31 | TSLA     |    20.9947  | 30.34%   | 31.94%   | 47.65%             |            1.94498e+09 | 23.02%               | 3.17%                 | 96.78%             | 106.58%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | ENPH     |    21.87    | -26.29%  | 44.17%   | 13.94%             |            1.27686e+08 | 43.65%               | 11.90%                | 80.42%             | 123.91%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | PCG      |     7.33208 | -28.61%  | -56.37%  | -60.89%            |            1.33872e+08 | 52.38%               | 16.67%                | 81.69%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | TSLA     |    21.996   | 46.24%   | 78.19%   | 54.13%             |            2.36702e+09 | 19.84%               | 3.17%                 | 96.20%             | 102.46%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-02-29 | EQT      |     5.46579 | -32.38%  | -41.79%  | -43.68%            |            5.55426e+07 | 42.86%               | 8.73%                 | 67.53%             | 148.55%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | APA      |     3.55084 | -83.54%  | -83.36%  | -81.67%            |            1.30037e+08 | 31.75%               | 6.35%                 | 72.92%             | 223.92%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | CELH     |     1.40333 | -12.84%  | 20.98%   | 9.13%              |            2.39728e+06 | 38.10%               | 11.11%                | 63.68%             | 179.57%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | TRGP     |     6.04267 | -82.66%  | -81.97%  | -81.46%            |            7.26848e+07 | 21.43%               | 5.56%                 | 60.80%             | 192.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-04-30 | CELH     |     1.67333 | -7.04%   | 42.61%   | 16.68%             |            1.90872e+06 | 40.48%               | 12.70%                | 62.85%             | 192.23%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-05-31 | PLUG     |     4.21    | -3.00%   | 7.95%    | 16.65%             |            4.86118e+07 | 42.86%               | 13.49%                | 62.57%             | 208.31%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-05-31 | TSLA     |    55.6667  | 25.00%   | 153.08%  | 93.68%             |            1.11066e+10 | 40.48%               | 17.46%                | 96.62%             | 198.40%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-09-30 | LEU      |     8.37    | -16.63%  | 65.09%   | 29.24%             |            1.80603e+06 | 55.56%               | 19.84%                | 64.35%             | 176.34%                  |                  1 |                         1 |                        1 |                    1 |

## Latest clean panel sample
| month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |
|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|--------------------------:|-------------------------:|
| 2026-08-31 | A        |      159    | 17.54%   | 31.55%   | 36.39%             |            307,352,515 | 12.70%               | 0.79%                 | 44.22%             |                          |                         0 |                        0 |
| 2026-08-31 | AAPL     |      309.35 | -0.78%   | 17.31%   | 17.87%             |         17,330,591,650 | 7.14%                | 0.00%                 | 49.78%             |                          |                         0 |                        0 |
| 2026-08-31 | ABBV     |      264.96 | 22.56%   | 15.93%   | 21.97%             |          1,616,081,916 | 8.73%                | 0.79%                 | 51.79%             |                          |                         0 |                        0 |
| 2026-08-31 | ABNB     |      187.3  | 40.50%   | 38.63%   | 40.13%             |            645,089,552 | 13.49%               | 3.17%                 | 64.69%             |                          |                         0 |                        0 |
| 2026-08-31 | ABT      |      116.64 | 37.23%   | 1.60%    | 15.37%             |          1,139,809,605 | 7.94%                | 0.79%                 | 51.17%             |                          |                         0 |                        0 |
| 2026-08-31 | ACGL     |       99.39 | 11.25%   | -0.76%   | 2.67%              |            197,003,171 | 5.56%                | 0.00%                 | 14.79%             |                          |                         0 |                        0 |
| 2026-08-31 | ACN      |      185.28 | 0.23%    | -9.40%   | -3.04%             |          1,257,709,742 | 25.40%               | 7.94%                 | 82.76%             |                          |                         0 |                        0 |
| 2026-08-31 | ADBE     |      275.3  | 6.21%    | 4.91%    | 10.01%             |          1,466,165,530 | 30.16%               | 4.76%                 | 81.62%             |                          |                         0 |                        0 |
| 2026-08-31 | ADI      |      373.09 | -9.60%   | 5.48%    | 5.36%              |          1,834,374,194 | 23.02%               | 3.97%                 | 78.23%             |                          |                         0 |                        0 |
| 2026-08-31 | ADM      |       80.3  | 1.29%    | 17.82%   | 12.95%             |            291,515,594 | 7.94%                | 1.59%                 | 35.33%             |                          |                         0 |                        0 |
| 2026-08-31 | ADP      |      280.81 | 27.54%   | 33.08%   | 35.28%             |            634,068,363 | 13.49%               | 2.38%                 | 57.52%             |                          |                         0 |                        0 |
| 2026-08-31 | ADSK     |      253.83 | 9.74%    | 3.24%    | 5.46%              |            574,717,233 | 23.81%               | 3.17%                 | 68.21%             |                          |                         0 |                        0 |
| 2026-08-31 | AEE      |      106.13 | -1.01%   | -5.01%   | -4.58%             |            188,315,685 | 2.38%                | 0.00%                 | 10.46%             |                          |                         0 |                        0 |
| 2026-08-31 | AEP      |      120.94 | -3.80%   | -8.28%   | -8.37%             |            608,161,686 | 2.38%                | 0.00%                 | 28.30%             |                          |                         0 |                        0 |
| 2026-08-31 | AES      |       14.77 | 1.89%    | -12.43%  | -0.11%             |            113,417,075 | 1.59%                | 0.79%                 | 15.79%             |                          |                         0 |                        0 |
| 2026-08-31 | AFL      |      116.07 | 3.77%    | 3.83%    | 4.62%              |            285,297,622 | 0.79%                | 0.00%                 | 14.49%             |                          |                         0 |                        0 |
| 2026-08-31 | AIG      |       76.12 | 3.23%    | -4.24%   | 0.01%              |            286,370,727 | 3.97%                | 0.79%                 | 23.98%             |                          |                         0 |                        0 |
| 2026-08-31 | AIZ      |      284.04 | 14.52%   | 24.14%   | 25.21%             |            107,796,458 | 2.38%                | 0.79%                 | 12.43%             |                          |                         0 |                        0 |
| 2026-08-31 | AJG      |      263.81 | 31.61%   | 16.34%   | 22.27%             |            379,407,352 | 12.70%               | 0.79%                 | 43.82%             |                          |                         0 |                        0 |
| 2026-08-31 | AKAM     |      110.42 | -26.16%  | 12.23%   | 5.20%              |            483,073,926 | 34.13%               | 6.35%                 | 76.53%             |                          |                         0 |                        0 |
| 2026-08-31 | ALAB     |      284.97 | -16.88%  | 139.81%  | 115.39%            |          1,897,152,362 | 57.94%               | 23.02%                | 95.20%             |                          |                         0 |                        0 |
| 2026-08-31 | ALB      |      143.25 | -18.59%  | -19.42%  | -22.14%            |            324,609,226 | 31.75%               | 8.73%                 | 68.80%             |                          |                         0 |                        0 |
| 2026-08-31 | ALGN     |      162.55 | -7.09%   | -14.49%  | -9.11%             |            173,421,892 | 26.19%               | 3.17%                 | 51.52%             |                          |                         0 |                        0 |
| 2026-08-31 | ALL      |      253.83 | 23.81%   | 19.55%   | 20.02%             |            427,225,081 | 7.14%                | 0.00%                 | 31.87%             |                          |                         0 |                        0 |
| 2026-08-31 | ALLE     |      162.31 | 25.30%   | 1.52%    | 10.75%             |            175,545,087 | 8.73%                | 0.79%                 | 28.46%             |                          |                         0 |                        0 |
| 2026-08-31 | AMAT     |      492.32 | 9.51%    | 32.54%   | 34.00%             |          5,305,246,905 | 46.03%               | 10.32%                | 93.47%             |                          |                         0 |                        0 |
| 2026-08-31 | AMCR     |       48.59 | 25.17%   | 2.00%    | 18.71%             |            157,609,714 | 15.08%               | 1.59%                 | 39.25%             |                          |                         0 |                        0 |
| 2026-08-31 | AMD      |      473.25 | -8.30%   | 136.38%  | 100.84%            |         14,653,489,805 | 52.38%               | 17.46%                | 96.17%             |                          |                         0 |                        0 |
| 2026-08-31 | AME      |      239.55 | 6.22%    | 0.45%    | 4.75%              |            289,386,497 | 5.56%                | 0.79%                 | 27.94%             |                          |                         0 |                        0 |
| 2026-08-31 | AMGN     |      439.33 | 31.21%   | 14.70%   | 23.28%             |            989,266,641 | 7.14%                | 0.00%                 | 41.18%             |                          |                         0 |                        0 |

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