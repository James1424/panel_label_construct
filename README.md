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
| raw_rows           | 66388               |
| clean_rows         | 66388               |
| raw_columns        | 136                 |
| clean_columns      | 125                 |
| raw_tickers        | 530                 |
| clean_tickers      | 530                 |
| months             | 131                 |
| first_month        | 2016-01-31 00:00:00 |
| last_month         | 2026-11-30 00:00:00 |
| candidate_features | 109                 |
| kept_features      | 109                 |
| dropped_features   | 0                   |

## Tail-label summary
| label                   |   positive_rows |   valid_future_rows | positive_rate   |   months_with_positive |   avg_positives_per_month |   min_positives_per_month |   max_positives_per_month |
|:------------------------|----------------:|--------------------:|:----------------|-----------------------:|--------------------------:|--------------------------:|--------------------------:|
| label_top10_1_3m        |            6651 |               65858 | 10.10%          |                    130 |                   50.771  |                         0 |                        54 |
| label_top5_1_3m         |            3362 |               65858 | 5.10%           |                    130 |                   25.6641 |                         0 |                        27 |
| label_boom30_top10_1_3m |            3403 |               65858 | 5.17%           |                    129 |                   25.9771 |                         0 |                        53 |
| label_boom40_top10_1_3m |            1947 |               65858 | 2.96%           |                    128 |                   14.8626 |                         0 |                        53 |
| label_boom50_top5_1_3m  |            1103 |               65858 | 1.67%           |                    125 |                    8.4198 |                         0 |                        27 |
| label_mega100_1_3m      |             272 |               65858 | 0.41%           |                     72 |                    2.0763 |                         0 |                        22 |

## Recent monthly label distribution
| month      |   rows |   tickers | future_max_return_1_3m_mean   | future_max_return_1_3m_p90   | future_max_return_1_3m_p95   | future_max_return_1_3m_max   |   label_top10_1_3m_count |   label_top5_1_3m_count |   label_boom30_top10_1_3m_count |   label_boom40_top10_1_3m_count |   label_boom50_top5_1_3m_count |   label_mega100_1_3m_count |
|:-----------|-------:|----------:|:------------------------------|:-----------------------------|:-----------------------------|:-----------------------------|-------------------------:|------------------------:|--------------------------------:|--------------------------------:|-------------------------------:|---------------------------:|
| 2025-06-30 |    526 |       526 | 12.16%                        | 29.53%                       | 45.46%                       | 253.55%                      |                       53 |                      27 |                              52 |                              30 |                             22 |                          7 |
| 2025-07-31 |    526 |       526 | 13.27%                        | 29.98%                       | 50.22%                       | 364.42%                      |                       53 |                      27 |                              53 |                              39 |                             27 |                          9 |
| 2025-08-31 |    526 |       526 | 10.54%                        | 28.57%                       | 48.66%                       | 325.54%                      |                       53 |                      27 |                              49 |                              32 |                             26 |                          7 |
| 2025-09-30 |    526 |       526 | 6.83%                         | 22.02%                       | 32.50%                       | 126.53%                      |                       53 |                      27 |                              31 |                              18 |                              9 |                          2 |
| 2025-10-31 |    527 |       527 | 9.17%                         | 23.06%                       | 31.15%                       | 189.09%                      |                       53 |                      27 |                              28 |                              14 |                             10 |                          1 |
| 2025-11-30 |    527 |       527 | 12.77%                        | 30.84%                       | 43.53%                       | 184.56%                      |                       53 |                      27 |                              53 |                              36 |                             19 |                          3 |
| 2025-12-31 |    527 |       527 | 11.39%                        | 31.84%                       | 44.69%                       | 167.66%                      |                       53 |                      27 |                              53 |                              33 |                             24 |                          1 |
| 2026-01-31 |    527 |       527 | 9.81%                         | 27.46%                       | 46.01%                       | 130.28%                      |                       53 |                      27 |                              45 |                              36 |                             23 |                          4 |
| 2026-02-28 |    527 |       527 | 10.19%                        | 36.76%                       | 65.00%                       | 188.52%                      |                       53 |                      27 |                              53 |                              50 |                             27 |                         15 |
| 2026-03-31 |    527 |       527 | 20.72%                        | 48.49%                       | 89.45%                       | 340.71%                      |                       53 |                      27 |                              53 |                              53 |                             27 |                         22 |
| 2026-04-30 |    527 |       527 | 13.25%                        | 37.79%                       | 55.46%                       | 148.03%                      |                       53 |                      27 |                              53 |                              46 |                             27 |                          7 |
| 2026-05-31 |    528 |       528 | 10.52%                        | 26.20%                       | 34.58%                       | 197.39%                      |                       53 |                      27 |                              35 |                              17 |                              6 |                          1 |
| 2026-06-30 |    529 |       529 | 7.63%                         | 28.71%                       | 38.07%                       | 174.98%                      |                       53 |                      27 |                              46 |                              24 |                             14 |                          1 |
| 2026-07-31 |    529 |       529 | 8.21%                         | 24.56%                       | 34.40%                       | 304.45%                      |                       53 |                      27 |                              37 |                              19 |                              9 |                          1 |
| 2026-08-31 |    529 |       529 | 4.36%                         | 16.27%                       | 21.25%                       | 81.12%                       |                       53 |                      27 |                               6 |                               2 |                              1 |                          0 |
| 2026-09-30 |    529 |       529 | 6.36%                         | 20.68%                       | 24.21%                       | 43.20%                       |                       53 |                      27 |                              12 |                               1 |                              0 |                          0 |
| 2026-10-31 |    530 |       530 | -1.26%                        | 6.48%                        | 10.61%                       | 71.21%                       |                       54 |                      27 |                               2 |                               1 |                              1 |                          0 |
| 2026-11-30 |    530 |       530 |                               |                              |                              |                              |                        0 |                       0 |                               0 |                               0 |                              0 |                          0 |

## Feature missingness report
A feature is dropped if `missing_rate > 35%` or `non_null_rows < 1000`.

### Highest-missing candidate features
| feature                       | feature_group     |   missing_count | missing_rate   |   non_null_rows | non_null_rate   | first_valid_month   | last_valid_month   | dropped   |   drop_reason |
|:------------------------------|:------------------|----------------:|:---------------|----------------:|:----------------|:--------------------|:-------------------|:----------|--------------:|
| rel_mom_12m_vs_qqq            | relative_strength |             693 | 1.04%          |           65695 | 98.96%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| mom_12m                       | other_momentum    |             693 | 1.04%          |           65695 | 98.96%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| up_day_volume_ratio_3m        | volume_flow       |             612 | 0.92%          |           65776 | 99.08%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| up_day_dollar_volume_ratio_3m | volume_flow       |             612 | 0.92%          |           65776 | 99.08%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| mom_9m                        | other_momentum    |             512 | 0.77%          |           65876 | 99.23%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| mom_7m                        | other_momentum    |             395 | 0.59%          |           65993 | 99.41%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| mom_6m                        | core_momentum     |             336 | 0.51%          |           66052 | 99.49%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| mom_4m_vs_6m                  | core_momentum     |             336 | 0.51%          |           66052 | 99.49%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| mom_5m_vs_6m                  | core_momentum     |             336 | 0.51%          |           66052 | 99.49%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| mom_6m_first3m                | core_momentum     |             336 | 0.51%          |           66052 | 99.49%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| mom_6m_acceleration           | core_momentum     |             336 | 0.51%          |           66052 | 99.49%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| ret_lag_6m                    | sequence_path     |             336 | 0.51%          |           66052 | 99.49%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| rel_mom_6m_vs_qqq             | relative_strength |             336 | 0.51%          |           66052 | 99.49%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| mom_3m_vs_6m                  | other_momentum    |             336 | 0.51%          |           66052 | 99.49%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| drawdown_12m                  | risk_drawdown     |             336 | 0.51%          |           66052 | 99.49%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| drawdown_12m_abs              | risk_drawdown     |             336 | 0.51%          |           66052 | 99.49%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| return_vol_ratio_6m           | risk_drawdown     |             336 | 0.51%          |           66052 | 99.49%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| ma100_slope_1m                | trend             |             323 | 0.49%          |           66065 | 99.51%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| volume_change_3m              | volume_flow       |             319 | 0.48%          |           66069 | 99.52%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| dollar_volume_change_3m       | volume_flow       |             319 | 0.48%          |           66069 | 99.52%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| volume_ma3_to_12m             | volume_flow       |             284 | 0.43%          |           66104 | 99.57%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| mom_5m                        | core_momentum     |             279 | 0.42%          |           66109 | 99.58%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| core_mom_456_std              | core_momentum     |             279 | 0.42%          |           66109 | 99.58%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| ret_lag_5m                    | sequence_path     |             279 | 0.42%          |           66109 | 99.58%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| price_ma100_ratio             | trend             |             266 | 0.40%          |           66122 | 99.60%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| drawdown_change_3m            | drawdown_recovery |             244 | 0.37%          |           66144 | 99.63%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| mom_4m                        | core_momentum     |             222 | 0.33%          |           66166 | 99.67%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| core_mom_456_avg              | core_momentum     |             222 | 0.33%          |           66166 | 99.67%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| core_mom_456_min              | core_momentum     |             222 | 0.33%          |           66166 | 99.67%          | 2016-01-31          | 2026-11-30         | False     |           nan |
| core_mom_456_max              | core_momentum     |             222 | 0.33%          |           66166 | 99.67%          | 2016-01-31          | 2026-11-30         | False     |           nan |

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
| yearly_top_future_return_examples | 2018-03-31 | TKO      |    32.457   | 18.14%   | 53.98%   | 39.32%             |            2.72076e+07 | 7.94%                | 1.59%                 | 56.17%             | 102.62%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-04-30 | TKO      |    35.8641  | 12.92%   | 51.03%   | 40.74%             |            2.85679e+07 | 7.14%                | 0.79%                 | 47.18%             | 99.21%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-05-31 | CVNA     |     5.77    | 43.96%   | 77.98%   | 60.00%             |            2.393e+07   | 38.89%               | 11.11%                | 66.52%             | 124.40%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-06-30 | AMD      |    14.99    | 49.15%   | 45.82%   | 26.23%             |            7.8752e+08  | 28.57%               | 3.97%                 | 96.69%             | 106.07%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-12-31 | ENPH     |     4.73    | -2.47%   | -29.72%  | -17.83%            |            8.59184e+06 | 44.44%               | 9.52%                 | 64.76%             | 95.14%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | PLUG     |     1.24    | -35.42%  | -38.61%  | -37.89%            |            4.00456e+06 | 20.63%               | 3.17%                 | 61.18%             | 93.55%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | SE       |    11.32    | -18.15%  | -24.53%  | -21.60%            |            1.70236e+07 | 33.33%               | 7.14%                 | 63.95%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-04-30 | ENPH     |    10.04    | 38.87%   | 121.15%  | 106.44%            |            1.86016e+07 | 39.68%               | 11.11%                | 64.86%             | 180.38%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-09-30 | BE       |     3.25    | -73.51%  | -74.85%  | -73.63%            |            1.35115e+07 | 44.44%               | 9.52%                 | 65.40%             | 129.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | BE       |     3.06    | -70.72%  | -77.53%  | -74.75%            |            1.11875e+07 | 43.65%               | 8.73%                 | 65.43%             | 157.52%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | PCG      |     6.0393  | -65.97%  | -72.60%  | -69.87%            |            1.31098e+08 | 50.00%               | 12.70%                | 81.50%             | 146.52%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-10-31 | TSLA     |    20.9947  | 30.34%   | 31.94%   | 47.65%             |            1.94498e+09 | 23.02%               | 3.17%                 | 96.80%             | 106.58%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | ENPH     |    21.87    | -26.29%  | 44.17%   | 13.94%             |            1.27686e+08 | 43.65%               | 11.90%                | 80.38%             | 123.91%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | PCG      |     7.30198 | -28.61%  | -56.37%  | -60.89%            |            1.33322e+08 | 52.38%               | 16.67%                | 81.51%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | TSLA     |    21.996   | 46.24%   | 78.19%   | 54.13%             |            2.36702e+09 | 19.84%               | 3.17%                 | 96.30%             | 102.46%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-02-29 | EQT      |     5.44867 | -32.38%  | -41.79%  | -43.68%            |            5.53685e+07 | 42.86%               | 8.73%                 | 67.54%             | 148.55%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | APA      |     3.53296 | -83.54%  | -83.36%  | -81.67%            |            1.29382e+08 | 31.75%               | 6.35%                 | 73.02%             | 223.92%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | CELH     |     1.40333 | -12.84%  | 20.98%   | 9.13%              |            2.39728e+06 | 38.10%               | 11.11%                | 63.68%             | 179.57%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | TRGP     |     6.01849 | -82.66%  | -81.97%  | -81.46%            |            7.2394e+07  | 21.43%               | 5.56%                 | 60.94%             | 192.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-04-30 | CELH     |     1.67333 | -7.04%   | 42.61%   | 16.68%             |            1.90872e+06 | 40.48%               | 12.70%                | 62.87%             | 192.23%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-04-30 | TWLO     |   112.3     | -9.68%   | 16.30%   | 13.10%             |            3.57971e+08 | 30.95%               | 5.56%                 | 60.43%             | 147.03%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-05-31 | PLUG     |     4.21    | -3.00%   | 7.95%    | 16.65%             |            4.86118e+07 | 42.86%               | 13.49%                | 62.62%             | 208.31%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-05-31 | TSLA     |    55.6667  | 25.00%   | 153.08%  | 93.68%             |            1.11066e+10 | 40.48%               | 17.46%                | 96.70%             | 198.40%                  |                  1 |                         1 |                        1 |                    1 |

## Latest clean panel sample
| month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |
|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|--------------------------:|-------------------------:|
| 2026-11-30 | A        |      174.76 | 13.98%   | 29.39%   | 29.21%             |            373,327,784 | 12.70%               | 0.79%                 | 49.41%             |                          |                         0 |                        0 |
| 2026-11-30 | AAPL     |      342.37 | 8.05%    | 9.81%    | 13.05%             |         14,192,823,603 | 7.14%                | 0.79%                 | 54.19%             |                          |                         0 |                        0 |
| 2026-11-30 | ABBV     |      291.31 | 14.30%   | 35.58%   | 23.23%             |          1,297,995,218 | 7.14%                | 0.79%                 | 48.90%             |                          |                         0 |                        0 |
| 2026-11-30 | ABNB     |      189.99 | 3.70%    | 42.52%   | 33.56%             |            799,869,568 | 15.87%               | 3.17%                 | 71.06%             |                          |                         0 |                        0 |
| 2026-11-30 | ABT      |      109.93 | 0.22%    | 30.14%   | 19.18%             |            934,007,892 | 7.94%                | 1.59%                 | 54.05%             |                          |                         0 |                        0 |
| 2026-11-30 | ACGL     |      107.28 | 9.39%    | 20.08%   | 12.44%             |            286,708,768 | 4.76%                | 0.00%                 | 21.77%             |                          |                         0 |                        0 |
| 2026-11-30 | ACN      |      260.5  | 38.38%   | 42.06%   | 71.29%             |          1,295,909,854 | 32.54%               | 9.52%                 | 86.77%             |                          |                         0 |                        0 |
| 2026-11-30 | ADBE     |      239.3  | -18.27%  | -7.68%   | 1.53%              |          1,192,771,603 | 28.57%               | 6.35%                 | 81.78%             |                          |                         0 |                        0 |
| 2026-11-30 | ADI      |      363.56 | 0.70%    | -11.64%  | -6.86%             |          1,465,610,792 | 23.81%               | 2.38%                 | 76.38%             |                          |                         0 |                        0 |
| 2026-11-30 | ADM      |       69.97 | -13.93%  | -11.74%  | -10.25%            |            278,145,013 | 9.52%                | 0.79%                 | 33.86%             |                          |                         0 |                        0 |
| 2026-11-30 | ADP      |      303.35 | 6.69%    | 38.66%   | 29.85%             |            612,160,867 | 11.11%               | 1.59%                 | 52.13%             |                          |                         0 |                        0 |
| 2026-11-30 | ADSK     |      261.72 | 1.23%    | 13.15%   | 19.84%             |            491,955,846 | 24.60%               | 5.56%                 | 71.37%             |                          |                         0 |                        0 |
| 2026-11-30 | AEE      |      112.85 | 7.21%    | 6.00%    | 3.41%              |            184,999,784 | 1.59%                | 0.00%                 | 10.19%             |                          |                         0 |                        0 |
| 2026-11-30 | AEP      |      126.53 | 3.35%    | 0.65%    | -2.15%             |            455,099,304 | 1.59%                | 0.00%                 | 24.53%             |                          |                         0 |                        0 |
| 2026-11-30 | AES      |       14.87 | 2.08%    | 3.79%    | 3.38%              |            125,505,668 | 0.00%                | 0.00%                 | 4.74%              |                          |                         0 |                        0 |
| 2026-11-30 | AFL      |      124.06 | 7.09%    | 10.91%   | 5.02%              |            226,589,550 | 0.79%                | 0.00%                 | 11.84%             |                          |                         0 |                        0 |
| 2026-11-30 | AIG      |       77.75 | 2.49%    | 6.14%    | 3.58%              |            323,474,857 | 3.97%                | 0.00%                 | 22.04%             |                          |                         0 |                        0 |
| 2026-11-30 | AIZ      |      307    | 8.92%    | 24.16%   | 16.38%             |            104,076,228 | 2.38%                | 0.79%                 | 12.57%             |                          |                         0 |                        0 |
| 2026-11-30 | AJG      |      281.61 | 7.71%    | 40.87%   | 25.69%             |            391,144,315 | 14.29%               | 3.17%                 | 55.67%             |                          |                         0 |                        0 |
| 2026-11-30 | AKAM     |       83.09 | -23.50%  | -44.44%  | -34.00%            |            489,236,531 | 35.71%               | 7.14%                 | 76.94%             |                          |                         0 |                        0 |
| 2026-11-30 | ALAB     |      190.71 | -35.78%  | -44.38%  | -47.87%            |          1,235,202,737 | 60.32%               | 19.05%                | 94.32%             |                          |                         0 |                        0 |
| 2026-11-30 | ALB      |       99.25 | -26.22%  | -43.41%  | -28.34%            |            271,210,049 | 29.37%               | 5.56%                 | 62.50%             |                          |                         0 |                        0 |
| 2026-11-30 | ALGN     |      166    | 3.89%    | -5.12%   | -2.85%             |            146,443,127 | 19.84%               | 3.17%                 | 47.75%             |                          |                         0 |                        0 |
| 2026-11-30 | ALL      |      254.81 | -1.16%   | 24.81%   | 9.75%              |            475,910,923 | 10.32%               | 0.00%                 | 40.29%             |                          |                         0 |                        0 |
| 2026-11-30 | ALLE     |      185.39 | 19.84%   | 43.63%   | 31.42%             |            198,643,168 | 7.94%                | 1.59%                 | 34.66%             |                          |                         0 |                        0 |
| 2026-11-30 | AMAT     |      332.72 | -27.42%  | -25.99%  | -38.11%            |          3,256,137,471 | 46.03%               | 10.32%                | 93.15%             |                          |                         0 |                        0 |
| 2026-11-30 | AMCR     |       44.87 | -0.82%   | 17.25%   | 7.88%              |            160,588,949 | 12.70%               | 0.00%                 | 26.64%             |                          |                         0 |                        0 |
| 2026-11-30 | AMD      |      449.04 | -4.61%   | -12.99%  | -13.80%            |         11,819,980,571 | 47.62%               | 13.49%                | 95.57%             |                          |                         0 |                        0 |
| 2026-11-30 | AME      |      228.67 | -2.62%   | 1.55%    | -3.02%             |            356,376,364 | 7.94%                | 0.00%                 | 31.51%             |                          |                         0 |                        0 |
| 2026-11-30 | AMGN     |      460.42 | 7.10%    | 37.51%   | 28.54%             |          1,184,655,533 | 11.11%               | 0.00%                 | 50.67%             |                          |                         0 |                        0 |

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