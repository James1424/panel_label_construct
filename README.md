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
| raw_rows           | 65470               |
| clean_rows         | 65470               |
| raw_columns        | 136                 |
| clean_columns      | 125                 |
| raw_tickers        | 531                 |
| clean_tickers      | 531                 |
| months             | 129                 |
| first_month        | 2016-01-31 00:00:00 |
| last_month         | 2026-09-30 00:00:00 |
| candidate_features | 109                 |
| kept_features      | 109                 |
| dropped_features   | 0                   |

## Tail-label summary
| label                   |   positive_rows |   valid_future_rows | positive_rate   |   months_with_positive |   avg_positives_per_month |   min_positives_per_month |   max_positives_per_month |
|:------------------------|----------------:|--------------------:|:----------------|-----------------------:|--------------------------:|--------------------------:|--------------------------:|
| label_top10_1_3m        |            6559 |               64939 | 10.10%          |                    128 |                   50.845  |                         0 |                        54 |
| label_top5_1_3m         |            3318 |               64939 | 5.11%           |                    128 |                   25.7209 |                         0 |                        27 |
| label_boom30_top10_1_3m |            3358 |               64939 | 5.17%           |                    127 |                   26.031  |                         0 |                        53 |
| label_boom40_top10_1_3m |            1918 |               64939 | 2.95%           |                    125 |                   14.8682 |                         0 |                        53 |
| label_boom50_top5_1_3m  |            1102 |               64939 | 1.70%           |                    123 |                    8.5426 |                         0 |                        27 |
| label_mega100_1_3m      |             273 |               64939 | 0.42%           |                     72 |                    2.1163 |                         0 |                        22 |

## Recent monthly label distribution
| month      |   rows |   tickers | future_max_return_1_3m_mean   | future_max_return_1_3m_p90   | future_max_return_1_3m_p95   | future_max_return_1_3m_max   |   label_top10_1_3m_count |   label_top5_1_3m_count |   label_boom30_top10_1_3m_count |   label_boom40_top10_1_3m_count |   label_boom50_top5_1_3m_count |   label_mega100_1_3m_count |
|:-----------|-------:|----------:|:------------------------------|:-----------------------------|:-----------------------------|:-----------------------------|-------------------------:|------------------------:|--------------------------------:|--------------------------------:|-------------------------------:|---------------------------:|
| 2025-04-30 |    528 |       528 | 18.25%                        | 44.18%                       | 62.97%                       | 222.62%                      |                       53 |                      27 |                              53 |                              53 |                             27 |                         10 |
| 2025-05-31 |    528 |       528 | 14.47%                        | 33.01%                       | 44.51%                       | 248.51%                      |                       53 |                      27 |                              53 |                              34 |                             23 |                          6 |
| 2025-06-30 |    528 |       528 | 12.23%                        | 29.49%                       | 46.30%                       | 253.55%                      |                       53 |                      27 |                              52 |                              30 |                             23 |                          7 |
| 2025-07-31 |    528 |       528 | 13.14%                        | 29.93%                       | 49.93%                       | 364.42%                      |                       53 |                      27 |                              53 |                              39 |                             27 |                          9 |
| 2025-08-31 |    528 |       528 | 10.44%                        | 28.53%                       | 49.75%                       | 325.54%                      |                       53 |                      27 |                              49 |                              33 |                             27 |                          8 |
| 2025-09-30 |    528 |       528 | 6.73%                         | 21.89%                       | 31.61%                       | 126.53%                      |                       53 |                      27 |                              30 |                              18 |                              9 |                          2 |
| 2025-10-31 |    529 |       529 | 9.23%                         | 23.31%                       | 31.15%                       | 189.09%                      |                       53 |                      27 |                              28 |                              14 |                             10 |                          1 |
| 2025-11-30 |    529 |       529 | 12.82%                        | 30.82%                       | 43.50%                       | 184.56%                      |                       53 |                      27 |                              53 |                              36 |                             19 |                          3 |
| 2025-12-31 |    529 |       529 | 11.40%                        | 31.83%                       | 44.57%                       | 167.66%                      |                       53 |                      27 |                              53 |                              33 |                             24 |                          1 |
| 2026-01-31 |    529 |       529 | 9.75%                         | 27.41%                       | 45.89%                       | 130.28%                      |                       53 |                      27 |                              45 |                              36 |                             23 |                          4 |
| 2026-02-28 |    529 |       529 | 9.75%                         | 35.20%                       | 61.48%                       | 188.52%                      |                       53 |                      27 |                              53 |                              48 |                             27 |                         15 |
| 2026-03-31 |    529 |       529 | 20.28%                        | 47.67%                       | 89.27%                       | 340.71%                      |                       53 |                      27 |                              53 |                              53 |                             27 |                         22 |
| 2026-04-30 |    529 |       529 | 12.85%                        | 36.38%                       | 53.05%                       | 148.03%                      |                       53 |                      27 |                              53 |                              44 |                             27 |                          7 |
| 2026-05-31 |    530 |       530 | 10.33%                        | 26.10%                       | 33.48%                       | 197.39%                      |                       54 |                      27 |                              33 |                              16 |                              6 |                          1 |
| 2026-06-30 |    531 |       531 | 6.82%                         | 27.84%                       | 34.63%                       | 119.96%                      |                       54 |                      27 |                              41 |                              15 |                             13 |                          1 |
| 2026-07-31 |    531 |       531 | 3.69%                         | 16.80%                       | 26.48%                       | 180.99%                      |                       54 |                      27 |                              21 |                               7 |                              3 |                          1 |
| 2026-08-31 |    531 |       531 | -3.08%                        | 3.86%                        | 6.79%                        | 32.46%                       |                       54 |                      27 |                               1 |                               0 |                              0 |                          0 |
| 2026-09-30 |    531 |       531 |                               |                              |                              |                              |                        0 |                       0 |                               0 |                               0 |                              0 |                          0 |

## Feature missingness report
A feature is dropped if `missing_rate > 35%` or `non_null_rows < 1000`.

### Highest-missing candidate features
| feature                       | feature_group     |   missing_count | missing_rate   |   non_null_rows | non_null_rate   | first_valid_month   | last_valid_month   | dropped   |   drop_reason |
|:------------------------------|:------------------|----------------:|:---------------|----------------:|:----------------|:--------------------|:-------------------|:----------|--------------:|
| rel_mom_12m_vs_qqq            | relative_strength |             690 | 1.05%          |           64780 | 98.95%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| mom_12m                       | other_momentum    |             690 | 1.05%          |           64780 | 98.95%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| up_day_volume_ratio_3m        | volume_flow       |             616 | 0.94%          |           64854 | 99.06%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| up_day_dollar_volume_ratio_3m | volume_flow       |             616 | 0.94%          |           64854 | 99.06%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| mom_9m                        | other_momentum    |             509 | 0.78%          |           64961 | 99.22%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| mom_7m                        | other_momentum    |             392 | 0.60%          |           65078 | 99.40%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| mom_6m                        | core_momentum     |             334 | 0.51%          |           65136 | 99.49%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| mom_4m_vs_6m                  | core_momentum     |             334 | 0.51%          |           65136 | 99.49%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| mom_5m_vs_6m                  | core_momentum     |             334 | 0.51%          |           65136 | 99.49%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| mom_6m_first3m                | core_momentum     |             334 | 0.51%          |           65136 | 99.49%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| mom_6m_acceleration           | core_momentum     |             334 | 0.51%          |           65136 | 99.49%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| ret_lag_6m                    | sequence_path     |             334 | 0.51%          |           65136 | 99.49%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| rel_mom_6m_vs_qqq             | relative_strength |             334 | 0.51%          |           65136 | 99.49%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| mom_3m_vs_6m                  | other_momentum    |             334 | 0.51%          |           65136 | 99.49%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| return_vol_ratio_6m           | risk_drawdown     |             334 | 0.51%          |           65136 | 99.49%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| drawdown_12m                  | risk_drawdown     |             333 | 0.51%          |           65137 | 99.49%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| drawdown_12m_abs              | risk_drawdown     |             333 | 0.51%          |           65137 | 99.49%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| ma100_slope_1m                | trend             |             321 | 0.49%          |           65149 | 99.51%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| volume_change_3m              | volume_flow       |             320 | 0.49%          |           65150 | 99.51%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| dollar_volume_change_3m       | volume_flow       |             320 | 0.49%          |           65150 | 99.51%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| volume_ma3_to_12m             | volume_flow       |             284 | 0.43%          |           65186 | 99.57%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| mom_5m                        | core_momentum     |             279 | 0.43%          |           65191 | 99.57%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| core_mom_456_std              | core_momentum     |             279 | 0.43%          |           65191 | 99.57%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| ret_lag_5m                    | sequence_path     |             279 | 0.43%          |           65191 | 99.57%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| price_ma100_ratio             | trend             |             267 | 0.41%          |           65203 | 99.59%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| drawdown_change_3m            | drawdown_recovery |             246 | 0.38%          |           65224 | 99.62%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| mom_4m                        | core_momentum     |             223 | 0.34%          |           65247 | 99.66%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| core_mom_456_avg              | core_momentum     |             223 | 0.34%          |           65247 | 99.66%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| core_mom_456_min              | core_momentum     |             223 | 0.34%          |           65247 | 99.66%          | 2016-01-31          | 2026-09-30         | False     |           nan |
| core_mom_456_max              | core_momentum     |             223 | 0.34%          |           65247 | 99.66%          | 2016-01-31          | 2026-09-30         | False     |           nan |

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
| yearly_top_future_return_examples | 2016-02-29 | DVN      |    13.4278  | -56.94%  | -53.27%  | -50.87%            |            2.13355e+08 | 44.44%               | 7.14%                 | 88.70%             | 85.36%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-04-30 | AMD      |     3.55    | 61.36%   | 67.45%   | 47.19%             |            4.55973e+07 | 46.83%               | 12.70%                | 70.98%             | 93.24%                   |                  1 |                         1 |                        1 |                    0 |
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
| yearly_top_future_return_examples | 2018-03-31 | TKO      |    32.457   | 18.14%   | 53.98%   | 39.32%             |            2.72076e+07 | 7.94%                | 1.59%                 | 56.33%             | 102.62%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-04-30 | TKO      |    35.8641  | 12.92%   | 51.03%   | 40.74%             |            2.85679e+07 | 7.14%                | 0.79%                 | 47.37%             | 99.21%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-05-31 | CVNA     |     5.77    | 43.96%   | 77.98%   | 60.00%             |            2.393e+07   | 38.89%               | 11.11%                | 66.54%             | 124.40%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-06-30 | AMD      |    14.99    | 49.15%   | 45.82%   | 26.23%             |            7.8752e+08  | 28.57%               | 3.97%                 | 96.73%             | 106.07%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-12-31 | ENPH     |     4.73    | -2.47%   | -29.72%  | -17.83%            |            8.59184e+06 | 44.44%               | 9.52%                 | 64.89%             | 95.14%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | PLUG     |     1.24    | -35.42%  | -38.61%  | -37.89%            |            4.00456e+06 | 20.63%               | 3.17%                 | 61.27%             | 93.55%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | SE       |    11.32    | -18.15%  | -24.53%  | -21.60%            |            1.70236e+07 | 33.33%               | 7.14%                 | 64.08%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-04-30 | ENPH     |    10.04    | 38.87%   | 121.15%  | 106.44%            |            1.86016e+07 | 39.68%               | 11.11%                | 64.98%             | 180.38%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-09-30 | BE       |     3.25    | -73.51%  | -74.85%  | -73.63%            |            1.35115e+07 | 44.44%               | 9.52%                 | 65.40%             | 129.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | BE       |     3.06    | -70.72%  | -77.53%  | -74.75%            |            1.11875e+07 | 43.65%               | 8.73%                 | 65.43%             | 157.52%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | PCG      |     6.0642  | -65.97%  | -72.60%  | -69.87%            |            1.31638e+08 | 50.00%               | 12.70%                | 81.82%             | 146.52%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-10-31 | TSLA     |    20.9947  | 30.34%   | 31.94%   | 47.65%             |            1.94498e+09 | 23.02%               | 3.17%                 | 96.78%             | 106.58%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | ENPH     |    21.87    | -26.29%  | 44.17%   | 13.94%             |            1.27686e+08 | 43.65%               | 11.90%                | 80.49%             | 123.91%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | PCG      |     7.33207 | -28.61%  | -56.37%  | -60.89%            |            1.33872e+08 | 52.38%               | 16.67%                | 81.69%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | TSLA     |    21.996   | 46.24%   | 78.19%   | 54.13%             |            2.36702e+09 | 19.84%               | 3.17%                 | 96.20%             | 102.46%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-02-29 | EQT      |     5.46579 | -32.38%  | -41.79%  | -43.68%            |            5.55426e+07 | 42.86%               | 8.73%                 | 67.53%             | 148.55%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | APA      |     3.55084 | -83.54%  | -83.36%  | -81.67%            |            1.30037e+08 | 31.75%               | 6.35%                 | 72.92%             | 223.92%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | CELH     |     1.40333 | -12.84%  | 20.98%   | 9.13%              |            2.39728e+06 | 38.10%               | 11.11%                | 63.68%             | 179.57%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | TRGP     |     6.04267 | -82.66%  | -81.97%  | -81.46%            |            7.26848e+07 | 21.43%               | 5.56%                 | 60.87%             | 192.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-04-30 | CELH     |     1.67333 | -7.04%   | 42.61%   | 16.68%             |            1.90872e+06 | 40.48%               | 12.70%                | 62.85%             | 192.23%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-05-31 | PLUG     |     4.21    | -3.00%   | 7.95%    | 16.65%             |            4.86118e+07 | 42.86%               | 13.49%                | 62.57%             | 208.31%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-05-31 | TSLA     |    55.6667  | 25.00%   | 153.08%  | 93.68%             |            1.11066e+10 | 40.48%               | 17.46%                | 96.62%             | 198.40%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-09-30 | LEU      |     8.37    | -16.63%  | 65.09%   | 29.24%             |            1.80603e+06 | 55.56%               | 19.84%                | 64.35%             | 176.34%                  |                  1 |                         1 |                        1 |                    1 |

## Latest clean panel sample
| month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |
|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|--------------------------:|-------------------------:|
| 2026-09-30 | A        |      156.47 | 17.80%   | 37.54%   | 29.63%             |            315,203,396 | 11.90%               | 0.79%                 | 45.82%             |                          |                         0 |                        0 |
| 2026-09-30 | AAPL     |      336.13 | 16.26%   | 32.68%   | 21.53%             |         16,704,327,747 | 7.14%                | 0.00%                 | 50.54%             |                          |                         0 |                        0 |
| 2026-09-30 | ABBV     |      263.96 | 5.64%    | 23.24%   | 23.71%             |          1,585,644,399 | 7.14%                | 0.79%                 | 50.41%             |                          |                         0 |                        0 |
| 2026-09-30 | ABNB     |      166.22 | 16.16%   | 31.63%   | 24.91%             |            733,070,710 | 11.90%               | 2.38%                 | 64.14%             |                          |                         0 |                        0 |
| 2026-09-30 | ABT      |      102.61 | 13.89%   | 1.29%    | 11.95%             |          1,049,289,625 | 7.94%                | 0.79%                 | 52.27%             |                          |                         0 |                        0 |
| 2026-09-30 | ACGL     |       96.89 | -0.18%   | 0.94%    | 3.99%              |            233,097,913 | 5.56%                | 0.00%                 | 18.95%             |                          |                         0 |                        0 |
| 2026-09-30 | ACN      |      181.29 | 47.44%   | -6.69%   | -1.98%             |          1,193,363,599 | 26.98%               | 7.94%                 | 83.50%             |                          |                         0 |                        0 |
| 2026-09-30 | ADBE     |      248.92 | 21.41%   | 2.40%    | -0.14%             |          1,346,891,927 | 28.57%               | 6.35%                 | 82.75%             |                          |                         0 |                        0 |
| 2026-09-30 | ADI      |      375.72 | -5.11%   | 18.78%   | 1.35%              |          1,562,265,624 | 23.02%               | 3.97%                 | 78.29%             |                          |                         0 |                        0 |
| 2026-09-30 | ADM      |       85.18 | 12.20%   | 18.70%   | 13.97%             |            307,660,881 | 10.32%               | 1.59%                 | 40.56%             |                          |                         0 |                        0 |
| 2026-09-30 | ADP      |      271.22 | 21.88%   | 35.36%   | 29.70%             |            628,913,785 | 13.49%               | 2.38%                 | 58.12%             |                          |                         0 |                        0 |
| 2026-09-30 | ADSK     |      216.95 | 11.59%   | -9.38%   | -8.02%             |            525,000,585 | 25.40%               | 3.97%                 | 71.37%             |                          |                         0 |                        0 |
| 2026-09-30 | AEE      |      102.23 | -8.92%   | -5.68%   | -6.14%             |            176,818,567 | 2.38%                | 0.00%                 | 10.15%             |                          |                         0 |                        0 |
| 2026-09-30 | AEP      |      120    | -11.62%  | -7.09%   | -7.60%             |            546,825,718 | 2.38%                | 0.00%                 | 27.91%             |                          |                         0 |                        0 |
| 2026-09-30 | AES      |       14.83 | 2.37%    | 7.83%    | 5.09%              |            112,249,682 | 0.00%                | 0.00%                 | 4.14%              |                          |                         0 |                        0 |
| 2026-09-30 | AFL      |      116.33 | -0.28%   | 7.12%    | 4.84%              |            260,018,144 | 0.79%                | 0.00%                 | 13.99%             |                          |                         0 |                        0 |
| 2026-09-30 | AIG      |       75.33 | 1.74%    | 1.44%    | 2.11%              |            297,100,012 | 3.17%                | 0.79%                 | 24.72%             |                          |                         0 |                        0 |
| 2026-09-30 | AIZ      |      282.23 | 5.43%    | 30.42%   | 21.60%             |            101,405,780 | 2.38%                | 0.79%                 | 11.63%             |                          |                         0 |                        0 |
| 2026-09-30 | AJG      |      239.48 | 4.60%    | 11.24%   | 15.92%             |            372,865,125 | 13.49%               | 1.59%                 | 49.49%             |                          |                         0 |                        0 |
| 2026-09-30 | AKAM     |      104.52 | -11.58%  | -8.99%   | -12.53%            |            408,358,426 | 35.71%               | 6.35%                 | 74.76%             |                          |                         0 |                        0 |
| 2026-09-30 | ALAB     |      303.25 | -37.22%  | 176.69%  | 73.62%             |          1,490,892,102 | 61.11%               | 23.02%                | 95.10%             |                          |                         0 |                        0 |
| 2026-09-30 | ALB      |      110.91 | -17.59%  | -37.86%  | -39.30%            |            299,191,165 | 31.75%               | 7.94%                 | 68.19%             |                          |                         0 |                        0 |
| 2026-09-30 | ALGN     |      147.61 | -12.48%  | -13.89%  | -15.22%            |            160,476,174 | 22.22%               | 3.17%                 | 49.58%             |                          |                         0 |                        0 |
| 2026-09-30 | ALL      |      249.83 | 5.43%    | 21.63%   | 20.03%             |            436,698,424 | 7.14%                | 0.00%                 | 33.76%             |                          |                         0 |                        0 |
| 2026-09-30 | ALLE     |      152.28 | 8.78%    | 5.62%    | 11.74%             |            203,487,252 | 7.94%                | 0.79%                 | 30.88%             |                          |                         0 |                        0 |
| 2026-09-30 | AMAT     |      444.57 | -38.44%  | 30.37%   | 14.07%             |          4,711,458,999 | 46.03%               | 11.11%                | 93.57%             |                          |                         0 |                        0 |
| 2026-09-30 | AMCR     |       41.9  | -1.96%   | 8.70%    | 10.59%             |            158,395,821 | 13.49%               | 1.59%                 | 38.21%             |                          |                         0 |                        0 |
| 2026-09-30 | AMD      |      559.82 | -3.63%   | 175.19%  | 80.53%             |         12,662,714,729 | 53.17%               | 16.67%                | 96.09%             |                          |                         0 |                        0 |
| 2026-09-30 | AME      |      237.64 | -1.63%   | 11.19%   | 5.98%              |            302,021,443 | 6.35%                | 0.79%                 | 30.83%             |                          |                         0 |                        0 |
| 2026-09-30 | AMGN     |      385.65 | 7.12%    | 11.08%   | 13.04%             |          1,030,411,773 | 7.14%                | 0.00%                 | 45.49%             |                          |                         0 |                        0 |

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