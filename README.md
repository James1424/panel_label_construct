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
| raw_rows           | 64506               |
| clean_rows         | 64506               |
| raw_columns        | 136                 |
| clean_columns      | 125                 |
| raw_tickers        | 531                 |
| clean_tickers      | 531                 |
| months             | 127                 |
| first_month        | 2016-01-31 00:00:00 |
| last_month         | 2026-07-31 00:00:00 |
| candidate_features | 109                 |
| kept_features      | 109                 |
| dropped_features   | 0                   |

## Tail-label summary
| label                   |   positive_rows |   valid_future_rows | positive_rate   |   months_with_positive |   avg_positives_per_month |   min_positives_per_month |   max_positives_per_month |
|:------------------------|----------------:|--------------------:|:----------------|-----------------------:|--------------------------:|--------------------------:|--------------------------:|
| label_top10_1_3m        |            6456 |               63975 | 10.09%          |                    126 |                   50.8346 |                         0 |                        54 |
| label_top5_1_3m         |            3267 |               63975 | 5.11%           |                    126 |                   25.7244 |                         0 |                        27 |
| label_boom30_top10_1_3m |            3267 |               63975 | 5.11%           |                    124 |                   25.7244 |                         0 |                        53 |
| label_boom40_top10_1_3m |            1874 |               63975 | 2.93%           |                    123 |                   14.7559 |                         0 |                        53 |
| label_boom50_top5_1_3m  |            1077 |               63975 | 1.68%           |                    121 |                    8.4803 |                         0 |                        27 |
| label_mega100_1_3m      |             266 |               63975 | 0.42%           |                     69 |                    2.0945 |                         0 |                        22 |

## Recent monthly label distribution
| month      |   rows |   tickers | future_max_return_1_3m_mean   | future_max_return_1_3m_p90   | future_max_return_1_3m_p95   | future_max_return_1_3m_max   |   label_top10_1_3m_count |   label_top5_1_3m_count |   label_boom30_top10_1_3m_count |   label_boom40_top10_1_3m_count |   label_boom50_top5_1_3m_count |   label_mega100_1_3m_count |
|:-----------|-------:|----------:|:------------------------------|:-----------------------------|:-----------------------------|:-----------------------------|-------------------------:|------------------------:|--------------------------------:|--------------------------------:|-------------------------------:|---------------------------:|
| 2025-02-28 |    528 |       528 | 3.48%                         | 17.36%                       | 24.67%                       | 197.99%                      |                       53 |                      27 |                              21 |                              13 |                              5 |                          1 |
| 2025-03-31 |    528 |       528 | 12.02%                        | 35.02%                       | 53.03%                       | 194.45%                      |                       53 |                      27 |                              53 |                              46 |                             27 |                          7 |
| 2025-04-30 |    528 |       528 | 18.14%                        | 44.18%                       | 62.97%                       | 222.62%                      |                       53 |                      27 |                              53 |                              53 |                             27 |                         10 |
| 2025-05-31 |    528 |       528 | 14.27%                        | 32.88%                       | 43.49%                       | 248.51%                      |                       53 |                      27 |                              53 |                              33 |                             22 |                          5 |
| 2025-06-30 |    528 |       528 | 12.16%                        | 29.07%                       | 44.47%                       | 253.55%                      |                       53 |                      27 |                              51 |                              29 |                             22 |                          7 |
| 2025-07-31 |    528 |       528 | 13.11%                        | 29.93%                       | 49.93%                       | 364.42%                      |                       53 |                      27 |                              53 |                              38 |                             27 |                          9 |
| 2025-08-31 |    528 |       528 | 10.44%                        | 28.53%                       | 49.75%                       | 325.54%                      |                       53 |                      27 |                              49 |                              33 |                             27 |                          8 |
| 2025-09-30 |    528 |       528 | 6.70%                         | 21.89%                       | 31.61%                       | 126.53%                      |                       53 |                      27 |                              30 |                              18 |                              9 |                          2 |
| 2025-10-31 |    529 |       529 | 9.22%                         | 23.31%                       | 31.15%                       | 189.09%                      |                       53 |                      27 |                              28 |                              14 |                             10 |                          1 |
| 2025-11-30 |    529 |       529 | 12.80%                        | 30.82%                       | 43.50%                       | 184.56%                      |                       53 |                      27 |                              53 |                              36 |                             19 |                          3 |
| 2025-12-31 |    529 |       529 | 11.41%                        | 31.83%                       | 44.57%                       | 167.66%                      |                       53 |                      27 |                              53 |                              33 |                             24 |                          1 |
| 2026-01-31 |    529 |       529 | 9.78%                         | 27.41%                       | 45.89%                       | 130.28%                      |                       53 |                      27 |                              45 |                              36 |                             23 |                          4 |
| 2026-02-28 |    529 |       529 | 9.71%                         | 35.20%                       | 61.48%                       | 188.52%                      |                       53 |                      27 |                              53 |                              48 |                             27 |                         15 |
| 2026-03-31 |    529 |       529 | 20.23%                        | 47.67%                       | 89.27%                       | 340.71%                      |                       53 |                      27 |                              53 |                              53 |                             27 |                         22 |
| 2026-04-30 |    529 |       529 | 11.53%                        | 33.35%                       | 53.05%                       | 148.03%                      |                       53 |                      27 |                              53 |                              41 |                             27 |                          6 |
| 2026-05-31 |    530 |       530 | 4.44%                         | 16.43%                       | 20.27%                       | 60.65%                       |                       54 |                      27 |                              11 |                               7 |                              2 |                          0 |
| 2026-06-30 |    531 |       531 | 0.11%                         | 8.83%                        | 12.01%                       | 28.58%                       |                       54 |                      27 |                               0 |                               0 |                              0 |                          0 |
| 2026-07-31 |    531 |       531 |                               |                              |                              |                              |                        0 |                       0 |                               0 |                               0 |                              0 |                          0 |

## Feature missingness report
A feature is dropped if `missing_rate > 35%` or `non_null_rows < 1000`.

### Highest-missing candidate features
| feature                       | feature_group     |   missing_count | missing_rate   |   non_null_rows | non_null_rate   | first_valid_month   | last_valid_month   | dropped   |   drop_reason |
|:------------------------------|:------------------|----------------:|:---------------|----------------:|:----------------|:--------------------|:-------------------|:----------|--------------:|
| rel_mom_12m_vs_qqq            | relative_strength |             672 | 1.04%          |           63834 | 98.96%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_12m                       | other_momentum    |             672 | 1.04%          |           63834 | 98.96%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| up_day_volume_ratio_3m        | volume_flow       |             554 | 0.86%          |           63952 | 99.14%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| up_day_dollar_volume_ratio_3m | volume_flow       |             554 | 0.86%          |           63952 | 99.14%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_9m                        | other_momentum    |             496 | 0.77%          |           64010 | 99.23%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_7m                        | other_momentum    |             381 | 0.59%          |           64125 | 99.41%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_6m                        | core_momentum     |             324 | 0.50%          |           64182 | 99.50%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_4m_vs_6m                  | core_momentum     |             324 | 0.50%          |           64182 | 99.50%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_5m_vs_6m                  | core_momentum     |             324 | 0.50%          |           64182 | 99.50%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_6m_first3m                | core_momentum     |             324 | 0.50%          |           64182 | 99.50%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_6m_acceleration           | core_momentum     |             324 | 0.50%          |           64182 | 99.50%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| ret_lag_6m                    | sequence_path     |             324 | 0.50%          |           64182 | 99.50%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| rel_mom_6m_vs_qqq             | relative_strength |             324 | 0.50%          |           64182 | 99.50%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_3m_vs_6m                  | other_momentum    |             324 | 0.50%          |           64182 | 99.50%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| return_vol_ratio_6m           | risk_drawdown     |             324 | 0.50%          |           64182 | 99.50%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| drawdown_12m                  | risk_drawdown     |             323 | 0.50%          |           64183 | 99.50%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| drawdown_12m_abs              | risk_drawdown     |             323 | 0.50%          |           64183 | 99.50%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| ma100_slope_1m                | trend             |             311 | 0.48%          |           64195 | 99.52%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| volume_ma3_to_12m             | volume_flow       |             275 | 0.43%          |           64231 | 99.57%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| volume_change_3m              | volume_flow       |             273 | 0.42%          |           64233 | 99.58%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| dollar_volume_change_3m       | volume_flow       |             273 | 0.42%          |           64233 | 99.58%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_5m                        | core_momentum     |             270 | 0.42%          |           64236 | 99.58%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| core_mom_456_std              | core_momentum     |             270 | 0.42%          |           64236 | 99.58%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| ret_lag_5m                    | sequence_path     |             270 | 0.42%          |           64236 | 99.58%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| price_ma100_ratio             | trend             |             258 | 0.40%          |           64248 | 99.60%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| drawdown_change_3m            | drawdown_recovery |             237 | 0.37%          |           64269 | 99.63%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| mom_4m                        | core_momentum     |             216 | 0.33%          |           64290 | 99.67%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| core_mom_456_avg              | core_momentum     |             216 | 0.33%          |           64290 | 99.67%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| core_mom_456_min              | core_momentum     |             216 | 0.33%          |           64290 | 99.67%          | 2016-01-31          | 2026-07-31         | False     |           nan |
| core_mom_456_max              | core_momentum     |             216 | 0.33%          |           64290 | 99.67%          | 2016-01-31          | 2026-07-31         | False     |           nan |

### Dropped high-missing features
_No features dropped by missingness filter._

## Committed first-20k panel slice
`outputs/panel_head_20000.csv` contains the first 20,000 rows of the cleaned panel. It is committed for quick inspection and future model-design reference; the full panel remains in the GitHub Actions artifact.
Columns in slice: 125

## Model-design panel sample
This small committed sample contains historical labeled rows and recent examples for model-design inspection. The full panel is uploaded as a GitHub Actions artifact.
| sample_source                     | month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_top10_1_3m |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |   label_mega100_1_3m |
|:----------------------------------|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|-------------------:|--------------------------:|-------------------------:|---------------------:|
| historical_mega100_examples       | 2016-01-31 | FCX      |     4.15298 | -60.92%  | -60.70%  | -56.55%            |            2.92186e+08 | 53.97%               | 11.90%                | 93.96%             | 204.35%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2016-01-31 | LEU      |     1.37    | -49.26%  | -65.23%  | -61.39%            |        74400.9         | 46.83%               | 10.32%                | 64.61%             | 229.20%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-01-31 | TRGP     |    14.1947  | -59.11%  | -73.14%  | -63.68%            |            3.69201e+07 | 43.65%               | 9.52%                 | 69.19%             | 84.40%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2016-02-29 | LEU      |     1.32    | -21.43%  | -65.17%  | -57.67%            |        58517.2         | 51.59%               | 11.11%                | 64.69%             | 241.67%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-02-29 | AMD      |     2.14    | -9.32%   | 18.23%   | 14.53%             |            3.01533e+07 | 40.48%               | 7.94%                 | 66.49%             | 113.55%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-02-29 | DVN      |    13.5148  | -56.94%  | -53.27%  | -50.87%            |            2.14737e+08 | 44.44%               | 7.14%                 | 88.72%             | 85.36%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-04-30 | AMD      |     3.55    | 61.36%   | 67.45%   | 47.19%             |            4.55973e+07 | 46.83%               | 12.70%                | 70.82%             | 93.24%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-08-31 | LEU      |     3.46    | 14.19%   | 162.12%  | 49.10%             |       150004           | 42.86%               | 11.90%                | 65.13%             | 88.15%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-01-31 | PLUG     |     1.06    | -30.72%  | -40.78%  | -36.80%            |            4.82764e+06 | 25.40%               | 3.97%                 | 64.07%             | 111.32%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2017-02-28 | PLUG     |     1.08    | -21.17%  | -30.32%  | -32.19%            |            7.26119e+06 | 32.54%               | 5.56%                 | 65.31%             | 107.41%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2017-04-30 | CVNA     |     2.22    |          |          |                    |                        |                      |                       | 0.00%              | 84.41%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-05-31 | CVNA     |     2.01    |          |          |                    |                        |                      |                       | 0.00%              | 103.68%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2017-08-31 | ENPH     |     0.92    | 21.05%   | -48.60%  | -34.71%            |       600677           | 44.44%               | 7.14%                 | 65.10%             | 215.22%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2017-09-30 | ENPH     |     1.52    | 74.71%   | 10.95%   | 46.23%             |       821362           | 43.65%               | 10.32%                | 65.21%             | 90.79%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-10-31 | ENPH     |     1.53    | 62.77%   | 28.57%   | 68.58%             |       845932           | 46.03%               | 11.90%                | 65.30%             | 89.54%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-12-31 | ENPH     |     2.41    | 58.55%   | 177.01%  | 165.12%            |            2.1306e+06  | 50.00%               | 15.08%                | 65.48%             | 89.63%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-01-31 | ENPH     |     2.2     | 43.79%   | 134.04%  | 105.97%            |            2.52291e+06 | 52.38%               | 16.67%                | 65.50%             | 107.73%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-03-31 | TKO      |    32.5899  | 18.14%   | 53.98%   | 39.32%             |            2.7319e+07  | 7.94%                | 1.59%                 | 56.28%             | 102.62%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-04-30 | TKO      |    36.0109  | 12.92%   | 51.03%   | 40.74%             |            2.86848e+07 | 7.14%                | 0.79%                 | 47.24%             | 99.21%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-05-31 | CVNA     |     5.77    | 43.96%   | 77.98%   | 60.00%             |            2.393e+07   | 38.89%               | 11.11%                | 66.46%             | 124.40%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-06-30 | AMD      |    14.99    | 49.15%   | 45.82%   | 26.23%             |            7.8752e+08  | 28.57%               | 3.97%                 | 96.74%             | 106.07%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-12-31 | ENPH     |     4.73    | -2.47%   | -29.72%  | -17.83%            |            8.59184e+06 | 44.44%               | 9.52%                 | 64.82%             | 95.14%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | PLUG     |     1.24    | -35.42%  | -38.61%  | -37.89%            |            4.00456e+06 | 20.63%               | 3.17%                 | 61.20%             | 93.55%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | SE       |    11.32    | -18.15%  | -24.53%  | -21.60%            |            1.70236e+07 | 33.33%               | 7.14%                 | 64.01%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-04-30 | ENPH     |    10.04    | 38.87%   | 121.15%  | 106.44%            |            1.86016e+07 | 39.68%               | 11.11%                | 64.84%             | 180.38%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-09-30 | BE       |     3.25    | -73.51%  | -74.85%  | -73.63%            |            1.35115e+07 | 44.44%               | 9.52%                 | 65.33%             | 129.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | BE       |     3.06    | -70.72%  | -77.53%  | -74.75%            |            1.11875e+07 | 43.65%               | 8.73%                 | 65.36%             | 157.52%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | PCG      |     6.0642  | -65.97%  | -72.60%  | -69.87%            |            1.31638e+08 | 50.00%               | 12.70%                | 81.65%             | 146.52%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-10-31 | TSLA     |    20.9947  | 30.34%   | 31.94%   | 47.65%             |            1.94498e+09 | 23.02%               | 3.17%                 | 96.81%             | 106.58%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | ENPH     |    21.87    | -26.29%  | 44.17%   | 13.94%             |            1.27686e+08 | 43.65%               | 11.90%                | 80.32%             | 123.91%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | PCG      |     7.33208 | -28.61%  | -56.37%  | -60.89%            |            1.33872e+08 | 52.38%               | 16.67%                | 81.59%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | TSLA     |    21.996   | 46.24%   | 78.19%   | 54.13%             |            2.36702e+09 | 19.84%               | 3.17%                 | 96.23%             | 102.46%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-01-31 | EQT      |     5.61896 | -43.51%  | -59.75%  | -47.69%            |            5.80267e+07 | 39.68%               | 7.14%                 | 68.27%             | 142.54%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-02-29 | EQT      |     5.48294 | -32.38%  | -41.79%  | -43.68%            |            5.57168e+07 | 42.86%               | 8.73%                 | 67.53%             | 148.55%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | APA      |     3.57584 | -83.54%  | -83.36%  | -81.67%            |            1.30953e+08 | 31.75%               | 6.35%                 | 72.91%             | 223.92%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | CELH     |     1.40333 | -12.84%  | 20.98%   | 9.13%              |            2.39728e+06 | 38.10%               | 11.11%                | 63.62%             | 179.57%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | SE       |    44.31    | 10.17%   | 43.17%   | 37.23%             |            2.19988e+08 | 23.02%               | 6.35%                 | 70.67%             | 142.02%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | TRGP     |     6.07095 | -82.66%  | -81.97%  | -81.46%            |            7.3025e+07  | 21.43%               | 5.56%                 | 60.72%             | 192.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-04-30 | CELH     |     1.67333 | -7.04%   | 42.61%   | 16.68%             |            1.90872e+06 | 40.48%               | 12.70%                | 62.79%             | 192.23%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-05-31 | PLUG     |     4.21    | -3.00%   | 7.95%    | 16.65%             |            4.86118e+07 | 42.86%               | 13.49%                | 62.50%             | 208.31%                  |                  1 |                         1 |                        1 |                    1 |

## Latest clean panel sample
| month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |
|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|--------------------------:|-------------------------:|
| 2026-07-31 | A        |      134.71 | 16.81%   | 1.07%    | 10.31%             |            293,677,386 | 11.11%               | 0.79%                 | 43.14%             |                          |                         0 |                        0 |
| 2026-07-31 | AAPL     |      327.5  | 20.80%   | 26.45%   | 26.56%             |         15,959,618,286 | 8.73%                | 0.00%                 | 50.75%             |                          |                         0 |                        0 |
| 2026-07-31 | ABBV     |      244.11 | 15.52%   | 10.37%   | 9.87%              |          1,598,937,364 | 7.94%                | 0.79%                 | 50.24%             |                          |                         0 |                        0 |
| 2026-07-31 | ABNB     |      148.38 | 5.71%    | 14.69%   | 14.01%             |            526,857,924 | 13.49%               | 2.38%                 | 57.12%             |                          |                         0 |                        0 |
| 2026-07-31 | ABT      |       89.27 | -1.67%   | -17.81%  | -17.70%            |          1,197,056,848 | 8.73%                | 0.00%                 | 47.14%             |                          |                         0 |                        0 |
| 2026-07-31 | ACGL     |       98.54 | 4.32%    | 2.60%    | 1.22%              |            218,602,017 | 5.56%                | 0.00%                 | 16.66%             |                          |                         0 |                        0 |
| 2026-07-31 | ACN      |      137.02 | -22.41%  | -46.96%  | -36.48%            |          1,196,498,187 | 26.19%               | 3.97%                 | 80.45%             |                          |                         0 |                        0 |
| 2026-07-31 | ADBE     |      224.56 | -8.75%   | -23.42%  | -15.16%            |          1,458,609,926 | 22.22%               | 2.38%                 | 75.58%             |                          |                         0 |                        0 |
| 2026-07-31 | ADI      |      390.96 | -2.54%   | 26.50%   | 20.09%             |          1,866,970,064 | 21.43%               | 3.17%                 | 76.40%             |                          |                         0 |                        0 |
| 2026-07-31 | ADM      |       82.3  | 11.14%   | 24.00%   | 19.32%             |            283,960,973 | 5.56%                | 0.79%                 | 28.14%             |                          |                         0 |                        0 |
| 2026-07-31 | ADP      |      247.47 | 17.65%   | 1.86%    | 13.95%             |            626,201,749 | 11.90%               | 2.38%                 | 55.81%             |                          |                         0 |                        0 |
| 2026-07-31 | ADSK     |      208.98 | -11.82%  | -17.36%  | -15.02%            |            553,230,050 | 23.02%               | 1.59%                 | 64.10%             |                          |                         0 |                        0 |
| 2026-07-31 | AEE      |      111.38 | -1.31%   | 9.34%    | 3.69%              |            199,657,105 | 3.17%                | 0.00%                 | 12.26%             |                          |                         0 |                        0 |
| 2026-07-31 | AEP      |      132.5  | -2.66%   | 12.30%   | 4.62%              |            629,467,650 | 2.38%                | 0.00%                 | 28.74%             |                          |                         0 |                        0 |
| 2026-07-31 | AES      |       14.81 | 3.76%    | 2.34%    | -1.50%             |            144,357,935 | 3.97%                | 1.59%                 | 27.51%             |                          |                         0 |                        0 |
| 2026-07-31 | AFL      |      121.01 | 7.01%    | 10.21%   | 9.60%              |            285,288,001 | 1.59%                | 0.00%                 | 15.22%             |                          |                         0 |                        0 |
| 2026-07-31 | AIG      |       76.78 | 3.33%    | 3.83%    | 1.04%              |            335,563,201 | 4.76%                | 0.79%                 | 27.67%             |                          |                         0 |                        0 |
| 2026-07-31 | AIZ      |      273.92 | 16.33%   | 15.89%   | 20.60%             |            107,099,081 | 3.17%                | 0.00%                 | 9.74%              |                          |                         0 |                        0 |
| 2026-07-31 | AJG      |      247.77 | 20.44%   | -0.01%   | 8.02%              |            394,009,724 | 11.90%               | 0.79%                 | 46.30%             |                          |                         0 |                        0 |
| 2026-07-31 | AKAM     |      120.01 | 16.54%   | 23.53%   | 16.67%             |            660,390,642 | 34.92%               | 5.56%                 | 81.07%             |                          |                         0 |                        0 |
| 2026-07-31 | ALAB     |      350.62 | 80.05%   | 132.78%  | 182.58%            |          1,844,874,017 | 57.94%               | 23.02%                | 95.18%             |                          |                         0 |                        0 |
| 2026-07-31 | ALB      |      124.74 | -36.42%  | -26.53%  | -28.90%            |            386,584,111 | 38.10%               | 7.94%                 | 73.77%             |                          |                         0 |                        0 |
| 2026-07-31 | ALGN     |      181.26 | 2.98%    | 11.18%   | 4.09%              |            182,312,691 | 26.98%               | 4.76%                 | 54.95%             |                          |                         0 |                        0 |
| 2026-07-31 | ALL      |      239.48 | 10.81%   | 21.59%   | 16.83%             |            387,089,923 | 7.14%                | 0.00%                 | 29.82%             |                          |                         0 |                        0 |
| 2026-07-31 | ALLE     |      135.82 | -0.80%   | -17.23%  | -12.80%            |            151,628,271 | 8.73%                | 0.00%                 | 20.88%             |                          |                         0 |                        0 |
| 2026-07-31 | AMAT     |      579.43 | 47.06%   | 80.22%   | 68.59%             |          4,836,632,050 | 40.48%               | 9.52%                 | 92.83%             |                          |                         0 |                        0 |
| 2026-07-31 | AMCR     |       43.4  | 15.99%   | 1.02%    | 1.04%              |            151,779,341 | 15.87%               | 2.38%                 | 43.24%             |                          |                         0 |                        0 |
| 2026-07-31 | AMD      |      529.14 | 49.27%   | 123.52%  | 149.31%            |         15,944,167,291 | 50.79%               | 16.67%                | 96.39%             |                          |                         0 |                        0 |
| 2026-07-31 | AME      |      233.52 | -0.69%   | 4.58%    | 3.87%              |            277,597,575 | 5.56%                | 0.79%                 | 26.85%             |                          |                         0 |                        0 |
| 2026-07-31 | AMGN     |      358.32 | 4.27%    | 6.33%    | 0.65%              |            922,786,986 | 6.35%                | 0.79%                 | 45.57%             |                          |                         0 |                        0 |

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