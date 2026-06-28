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
| raw_rows           | 51516               |
| clean_rows         | 51516               |
| raw_columns        | 137                 |
| clean_columns      | 126                 |
| raw_tickers        | 424                 |
| clean_tickers      | 424                 |
| months             | 126                 |
| first_month        | 2016-01-31 00:00:00 |
| last_month         | 2026-06-30 00:00:00 |
| candidate_features | 110                 |
| kept_features      | 110                 |
| dropped_features   | 0                   |

## Tail-label summary
| label                   |   positive_rows |   valid_future_rows | positive_rate   |   months_with_positive |   avg_positives_per_month |   min_positives_per_month |   max_positives_per_month |
|:------------------------|----------------:|--------------------:|:----------------|-----------------------:|--------------------------:|--------------------------:|--------------------------:|
| label_top10_1_3m        |            5173 |               51092 | 10.12%          |                    125 |                   41.0556 |                         0 |                        43 |
| label_top5_1_3m         |            2614 |               51092 | 5.12%           |                    125 |                   20.746  |                         0 |                        22 |
| label_boom30_top10_1_3m |            2517 |               51092 | 4.93%           |                    124 |                   19.9762 |                         0 |                        43 |
| label_boom40_top10_1_3m |            1357 |               51092 | 2.66%           |                    121 |                   10.7698 |                         0 |                        43 |
| label_boom50_top5_1_3m  |             751 |               51092 | 1.47%           |                    116 |                    5.9603 |                         0 |                        22 |
| label_mega100_1_3m      |             151 |               51092 | 0.30%           |                     52 |                    1.1984 |                         0 |                        13 |

## Recent monthly label distribution
| month      |   rows |   tickers | future_max_return_1_3m_mean   | future_max_return_1_3m_p90   | future_max_return_1_3m_p95   | future_max_return_1_3m_max   |   label_top10_1_3m_count |   label_top5_1_3m_count |   label_boom30_top10_1_3m_count |   label_boom40_top10_1_3m_count |   label_boom50_top5_1_3m_count |   label_mega100_1_3m_count |
|:-----------|-------:|----------:|:------------------------------|:-----------------------------|:-----------------------------|:-----------------------------|-------------------------:|------------------------:|--------------------------------:|--------------------------------:|-------------------------------:|---------------------------:|
| 2025-01-31 |    422 |       422 | 1.63%                         | 13.78%                       | 17.73%                       | 45.37%                       |                       43 |                      22 |                               4 |                               2 |                              0 |                          0 |
| 2025-02-28 |    422 |       422 | 2.91%                         | 15.47%                       | 22.56%                       | 55.18%                       |                       43 |                      22 |                              14 |                               8 |                              2 |                          0 |
| 2025-03-31 |    422 |       422 | 10.62%                        | 33.43%                       | 48.19%                       | 194.45%                      |                       43 |                      22 |                              43 |                              31 |                             20 |                          3 |
| 2025-04-30 |    422 |       422 | 16.50%                        | 40.91%                       | 55.77%                       | 210.87%                      |                       43 |                      22 |                              43 |                              43 |                             22 |                          5 |
| 2025-05-31 |    422 |       422 | 13.34%                        | 30.02%                       | 40.63%                       | 248.51%                      |                       43 |                      22 |                              43 |                              22 |                             15 |                          3 |
| 2025-06-30 |    422 |       422 | 10.33%                        | 25.43%                       | 37.35%                       | 175.67%                      |                       43 |                      22 |                              31 |                              17 |                             12 |                          4 |
| 2025-07-31 |    422 |       422 | 10.69%                        | 25.59%                       | 41.55%                       | 134.31%                      |                       43 |                      22 |                              35 |                              23 |                             14 |                          5 |
| 2025-08-31 |    422 |       422 | 8.23%                         | 25.01%                       | 38.13%                       | 117.31%                      |                       43 |                      22 |                              30 |                              18 |                             14 |                          1 |
| 2025-09-30 |    422 |       422 | 5.87%                         | 21.08%                       | 28.22%                       | 71.34%                       |                       43 |                      22 |                              18 |                               8 |                              4 |                          0 |
| 2025-10-31 |    423 |       423 | 8.90%                         | 23.19%                       | 29.36%                       | 85.48%                       |                       43 |                      22 |                              20 |                               8 |                              4 |                          0 |
| 2025-11-30 |    423 |       423 | 12.43%                        | 29.97%                       | 43.23%                       | 90.01%                       |                       43 |                      22 |                              42 |                              26 |                             13 |                          0 |
| 2025-12-31 |    423 |       423 | 11.45%                        | 31.87%                       | 42.09%                       | 88.31%                       |                       43 |                      22 |                              43 |                              24 |                             16 |                          0 |
| 2026-01-31 |    423 |       423 | 9.62%                         | 27.12%                       | 43.79%                       | 109.52%                      |                       43 |                      22 |                              35 |                              28 |                             15 |                          3 |
| 2026-02-28 |    423 |       423 | 8.87%                         | 28.60%                       | 55.25%                       | 188.52%                      |                       43 |                      22 |                              39 |                              32 |                             22 |                         13 |
| 2026-03-31 |    423 |       423 | 18.25%                        | 40.74%                       | 74.21%                       | 257.43%                      |                       43 |                      22 |                              43 |                              43 |                             22 |                         13 |
| 2026-04-30 |    423 |       423 | 8.82%                         | 29.09%                       | 44.91%                       | 118.95%                      |                       43 |                      22 |                              38 |                              24 |                             18 |                          4 |
| 2026-05-31 |    424 |       424 | 1.62%                         | 13.09%                       | 15.99%                       | 39.28%                       |                       43 |                      22 |                               3 |                               0 |                              0 |                          0 |
| 2026-06-30 |    424 |       424 |                               |                              |                              |                              |                        0 |                       0 |                               0 |                               0 |                              0 |                          0 |

## Feature missingness report
A feature is dropped if `missing_rate > 35%` or `non_null_rows < 1000`.

### Highest-missing candidate features
| feature                       | feature_group     |   missing_count | missing_rate   |   non_null_rows | non_null_rate   | first_valid_month   | last_valid_month   | dropped   |   drop_reason |
|:------------------------------|:------------------|----------------:|:---------------|----------------:|:----------------|:--------------------|:-------------------|:----------|--------------:|
| rel_mom_12m_vs_qqq            | relative_strength |             446 | 0.87%          |           51070 | 99.13%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_12m                       | other_momentum    |             446 | 0.87%          |           51070 | 99.13%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| up_day_volume_ratio_3m        | volume_flow       |             380 | 0.74%          |           51136 | 99.26%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| up_day_dollar_volume_ratio_3m | volume_flow       |             380 | 0.74%          |           51136 | 99.26%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_9m                        | other_momentum    |             331 | 0.64%          |           51185 | 99.36%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_7m                        | other_momentum    |             256 | 0.50%          |           51260 | 99.50%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_6m                        | core_momentum     |             219 | 0.43%          |           51297 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_4m_vs_6m                  | core_momentum     |             219 | 0.43%          |           51297 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_5m_vs_6m                  | core_momentum     |             219 | 0.43%          |           51297 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_6m_first3m                | core_momentum     |             219 | 0.43%          |           51297 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_6m_acceleration           | core_momentum     |             219 | 0.43%          |           51297 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| ret_lag_6m                    | sequence_path     |             219 | 0.43%          |           51297 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| rel_mom_6m_vs_qqq             | relative_strength |             219 | 0.43%          |           51297 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_3m_vs_6m                  | other_momentum    |             219 | 0.43%          |           51297 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| return_vol_ratio_6m           | risk_drawdown     |             219 | 0.43%          |           51297 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| drawdown_12m                  | risk_drawdown     |             218 | 0.42%          |           51298 | 99.58%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| drawdown_12m_abs              | risk_drawdown     |             218 | 0.42%          |           51298 | 99.58%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| ma100_slope_1m                | trend             |             210 | 0.41%          |           51306 | 99.59%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_5m                        | core_momentum     |             182 | 0.35%          |           51334 | 99.65%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| core_mom_456_std              | core_momentum     |             182 | 0.35%          |           51334 | 99.65%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| ret_lag_5m                    | sequence_path     |             182 | 0.35%          |           51334 | 99.65%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| volume_ma3_to_12m             | volume_flow       |             182 | 0.35%          |           51334 | 99.65%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| price_ma100_ratio             | trend             |             174 | 0.34%          |           51342 | 99.66%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| volume_change_3m              | volume_flow       |             171 | 0.33%          |           51345 | 99.67%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| dollar_volume_change_3m       | volume_flow       |             171 | 0.33%          |           51345 | 99.67%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| drawdown_change_3m            | drawdown_recovery |             160 | 0.31%          |           51356 | 99.69%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_4m                        | core_momentum     |             145 | 0.28%          |           51371 | 99.72%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| core_mom_456_avg              | core_momentum     |             145 | 0.28%          |           51371 | 99.72%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| core_mom_456_min              | core_momentum     |             145 | 0.28%          |           51371 | 99.72%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| core_mom_456_max              | core_momentum     |             145 | 0.28%          |           51371 | 99.72%          | 2016-01-31          | 2026-06-30         | False     |           nan |

### Dropped high-missing features
_No features dropped by missingness filter._

## Committed first-20k panel slice
`outputs/panel_head_20000.csv` contains the first 20,000 rows of the cleaned panel. It is committed for quick inspection and future model-design reference; the full panel remains in the GitHub Actions artifact.
Columns in slice: 126

## Model-design panel sample
This small committed sample contains historical labeled rows and recent examples for model-design inspection. The full panel is uploaded as a GitHub Actions artifact.
| sample_source                     | month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_top10_1_3m |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |   label_mega100_1_3m |
|:----------------------------------|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|-------------------:|--------------------------:|-------------------------:|---------------------:|
| historical_mega100_examples       | 2016-01-31 | FCX      |     4.15298 | -60.92%  | -60.70%  | -56.55%            |            2.92186e+08 | 53.97%               | 11.90%                | 93.57%             | 204.35%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2016-01-31 | LEU      |     1.37    | -49.26%  | -65.23%  | -61.39%            |        74400.9         | 46.83%               | 10.32%                | 64.39%             | 229.20%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-01-31 | TRGP     |    14.1947  | -59.11%  | -73.14%  | -63.68%            |            3.69201e+07 | 43.65%               | 9.52%                 | 69.30%             | 84.40%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2016-02-29 | AMD      |     2.14    | -9.32%   | 18.23%   | 14.53%             |            3.01533e+07 | 40.48%               | 7.94%                 | 66.65%             | 113.55%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2016-02-29 | LEU      |     1.32    | -21.43%  | -65.17%  | -57.67%            |        58517.2         | 51.59%               | 11.11%                | 64.43%             | 241.67%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-02-29 | DVN      |    13.5148  | -56.94%  | -53.27%  | -50.87%            |            2.14737e+08 | 44.44%               | 7.14%                 | 88.44%             | 85.36%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-04-30 | AMD      |     3.55    | 61.36%   | 67.45%   | 47.19%             |            4.55973e+07 | 46.83%               | 12.70%                | 70.73%             | 93.24%                   |                  1 |                         1 |                        1 |                    0 |
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
| yearly_top_future_return_examples | 2018-03-31 | TKO      |    32.5899  | 18.14%   | 53.98%   | 39.32%             |            2.7319e+07  | 7.94%                | 1.59%                 | 57.42%             | 102.62%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-04-30 | TKO      |    36.0109  | 12.92%   | 51.03%   | 40.74%             |            2.86848e+07 | 7.14%                | 0.79%                 | 48.55%             | 99.21%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2018-05-31 | CVNA     |     5.77    | 43.96%   | 77.98%   | 60.00%             |            2.393e+07   | 38.89%               | 11.11%                | 66.33%             | 124.40%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-06-30 | AMD      |    14.99    | 49.15%   | 45.82%   | 26.23%             |            7.8752e+08  | 28.57%               | 3.97%                 | 96.66%             | 106.07%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-12-31 | ENPH     |     4.73    | -2.47%   | -29.72%  | -17.83%            |            8.59184e+06 | 44.44%               | 9.52%                 | 64.80%             | 95.14%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | LEU      |     1.69    | -37.17%  | -50.87%  | -40.69%            |        57707           | 47.62%               | 11.90%                | 65.05%             | 84.02%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | PLUG     |     1.24    | -35.42%  | -38.61%  | -37.89%            |            4.00456e+06 | 20.63%               | 3.17%                 | 61.34%             | 93.55%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2019-03-31 | ENPH     |     9.23    | 95.14%   | 90.31%   | 88.18%             |            1.57355e+07 | 40.48%               | 11.11%                | 64.62%             | 97.51%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2019-04-30 | ENPH     |    10.04    | 38.87%   | 121.15%  | 106.44%            |            1.86016e+07 | 39.68%               | 11.11%                | 65.01%             | 180.38%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-05-31 | ENPH     |    15.17    | 67.25%   | 180.93%  | 170.49%            |            3.08737e+07 | 39.68%               | 10.32%                | 66.27%             | 95.58%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2019-10-31 | PCG      |     6.08183 | -65.97%  | -72.60%  | -69.87%            |            1.32021e+08 | 50.00%               | 12.70%                | 81.53%             | 146.52%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | TSLA     |    20.9947  | 30.34%   | 31.94%   | 47.65%             |            1.94498e+09 | 23.02%               | 3.17%                 | 97.17%             | 106.58%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-11-30 | ENPH     |    21.87    | -26.29%  | 44.17%   | 13.94%             |            1.27686e+08 | 43.65%               | 11.90%                | 80.05%             | 123.91%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-11-30 | PCG      |     7.3534  | -28.61%  | -56.37%  | -60.89%            |            1.34261e+08 | 52.38%               | 16.67%                | 81.28%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | TSLA     |    21.996   | 46.24%   | 78.19%   | 54.13%             |            2.36702e+09 | 19.84%               | 3.17%                 | 96.63%             | 102.46%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-01-31 | EQT      |     5.61896 | -43.51%  | -59.75%  | -47.69%            |            5.80267e+07 | 39.68%               | 7.14%                 | 68.32%             | 142.54%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-02-29 | EQT      |     5.48294 | -32.38%  | -41.79%  | -43.68%            |            5.57168e+07 | 42.86%               | 8.73%                 | 67.63%             | 148.55%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | CVNA     |    11.018   | -40.15%  | -16.53%  | -30.26%            |            1.95395e+08 | 42.06%               | 11.11%                | 81.58%             | 118.19%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | DDOG     |    35.98    | -4.76%   | 6.10%    | 0.49%              |            1.42601e+08 | 42.86%               | 11.90%                | 75.51%             | 141.66%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | PLUG     |     3.54    | 12.03%   | 34.60%   | 19.65%             |            7.59733e+07 | 46.83%               | 15.87%                | 68.25%             | 131.92%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | SHOP     |    41.693   | 4.87%    | 33.78%   | 30.18%             |            1.16644e+09 | 33.33%               | 9.52%                 | 91.79%             | 127.66%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | TRGP     |     6.07095 | -82.66%  | -81.97%  | -81.46%            |            7.3025e+07  | 21.43%               | 5.56%                 | 60.91%             | 192.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-04-30 | DDOG     |    45.12    | -2.36%   | 34.33%   | 21.47%             |            1.4381e+08  | 33.33%               | 6.35%                 | 60.10%             | 108.02%                  |                  1 |                         1 |                        1 |                    1 |

## Latest clean panel sample
| month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |
|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|--------------------------:|-------------------------:|
| 2026-06-30 | AAPL     |      283.78 | 11.92%   | 4.58%    | 7.22%              |         14,914,657,258 | 7.14%                | 0.00%                 | 49.60%             |                          |                         0 |                        0 |
| 2026-06-30 | ABNB     |      145.56 | 15.27%   | 7.25%    | 9.17%              |            513,278,244 | 12.70%               | 2.38%                 | 57.59%             |                          |                         0 |                        0 |
| 2026-06-30 | ADBE     |      202.73 | -16.60%  | -42.08%  | -31.90%            |          1,432,538,309 | 20.63%               | 2.38%                 | 76.75%             |                          |                         0 |                        0 |
| 2026-06-30 | ADI      |      386.91 | 21.95%   | 43.50%   | 26.03%             |          1,745,335,267 | 20.63%               | 3.97%                 | 79.11%             |                          |                         0 |                        0 |
| 2026-06-30 | ADP      |      223.55 | 10.86%   | -11.71%  | -4.58%             |            635,636,227 | 10.32%               | 1.59%                 | 53.95%             |                          |                         0 |                        0 |
| 2026-06-30 | AEP      |      138.69 | 6.57%    | 22.11%   | 14.68%             |            561,148,455 | 2.38%                | 0.00%                 | 28.45%             |                          |                         0 |                        0 |
| 2026-06-30 | AKAM     |      113.29 | -1.36%   | 29.85%   | 20.53%             |            685,755,044 | 33.33%               | 4.76%                 | 82.74%             |                          |                         0 |                        0 |
| 2026-06-30 | ALAB     |      391.74 | 257.43%  | 135.48%  | 175.08%            |          1,600,754,405 | 55.56%               | 21.43%                | 95.24%             |                          |                         0 |                        0 |
| 2026-06-30 | ALGN     |      178.43 | 4.08%    | 14.27%   | 5.86%              |            180,181,624 | 26.19%               | 3.97%                 | 55.66%             |                          |                         0 |                        0 |
| 2026-06-30 | AMAT     |      626.84 | 83.63%   | 144.52%  | 102.69%            |          3,912,761,555 | 38.10%               | 10.32%                | 94.17%             |                          |                         0 |                        0 |
| 2026-06-30 | AMD      |      521.58 | 156.39%  | 143.55%  | 141.46%            |         14,586,629,753 | 45.24%               | 14.29%                | 96.47%             |                          |                         0 |                        0 |
| 2026-06-30 | AMZN     |      232.69 | 11.73%   | 0.81%    | 2.95%              |         12,362,016,281 | 13.49%               | 0.79%                 | 65.12%             |                          |                         0 |                        0 |
| 2026-06-30 | ANET     |      157.6  | 28.36%   | 20.28%   | 16.51%             |          1,443,465,624 | 41.27%               | 8.73%                 | 90.14%             |                          |                         0 |                        0 |
| 2026-06-30 | APP      |      477.08 | 19.87%   | -29.20%  | -6.21%             |          2,332,012,706 | 46.83%               | 15.08%                | 94.65%             |                          |                         0 |                        0 |
| 2026-06-30 | ARM      |      334.27 | 120.96%  | 205.80%  | 195.11%            |          3,095,245,880 | 43.65%               | 16.67%                | 96.38%             |                          |                         0 |                        0 |
| 2026-06-30 | ASML     |     1794.62 | 36.17%   | 68.33%   | 39.63%             |          2,998,870,817 | 30.16%               | 7.94%                 | 89.81%             |                          |                         0 |                        0 |
| 2026-06-30 | AVGO     |      365.02 | 18.12%   | 5.86%    | 10.36%             |         10,431,655,669 | 30.16%               | 3.97%                 | 87.26%             |                          |                         0 |                        0 |
| 2026-06-30 | AXON     |      464.83 | 9.45%    | -18.15%  | -12.11%            |            488,797,309 | 34.13%               | 10.32%                | 80.48%             |                          |                         0 |                        0 |
| 2026-06-30 | BEN      |       33.21 | 40.60%   | 41.04%   | 31.53%             |            142,721,833 | 11.11%               | 1.59%                 | 34.82%             |                          |                         0 |                        0 |
| 2026-06-30 | BF-B     |       27.96 | 6.67%    | 9.23%    | 3.95%              |            112,386,110 | 17.46%               | 3.17%                 | 47.93%             |                          |                         0 |                        0 |
| 2026-06-30 | BG       |      110.54 | -12.57%  | 25.55%   | 5.31%              |            208,234,892 | 10.32%               | 1.59%                 | 36.44%             |                          |                         0 |                        0 |
| 2026-06-30 | BIIB     |      216.03 | 17.84%   | 22.75%   | 18.49%             |            232,609,583 | 12.70%               | 2.38%                 | 47.97%             |                          |                         0 |                        0 |
| 2026-06-30 | BKNG     |      181.46 | 8.02%    | -14.88%  | -5.41%             |          1,351,095,165 | 17.46%               | 3.97%                 | 76.64%             |                          |                         0 |                        0 |
| 2026-06-30 | BKR      |       56.56 | -7.04%   | 25.08%   | 4.56%              |            516,747,275 | 19.05%               | 1.59%                 | 61.22%             |                          |                         0 |                        0 |
| 2026-06-30 | BLDR     |       89.14 | 8.27%    | -13.36%  | -16.66%            |            205,378,705 | 36.51%               | 7.94%                 | 65.20%             |                          |                         0 |                        0 |
| 2026-06-30 | BLK      |      964.71 | 0.88%    | -8.86%   | -9.97%             |            748,605,190 | 10.32%               | 0.79%                 | 51.96%             |                          |                         0 |                        0 |
| 2026-06-30 | BMY      |       57.52 | -4.18%   | 9.01%    | 2.58%              |            661,422,357 | 6.35%                | 0.79%                 | 43.94%             |                          |                         0 |                        0 |
| 2026-06-30 | BNY      |      143.56 | 21.50%   | 24.70%   | 21.97%             |            534,630,070 | 3.97%                | 0.00%                 | 31.57%             |                          |                         0 |                        0 |
| 2026-06-30 | BR       |      137.93 | -14.53%  | -37.43%  | -30.49%            |            238,863,808 | 14.29%               | 0.00%                 | 35.85%             |                          |                         0 |                        0 |
| 2026-06-30 | BRK-B    |      498.66 | 4.06%    | -0.79%   | 0.58%              |          2,444,723,889 | 0.79%                | 0.00%                 | 35.74%             |                          |                         0 |                        0 |

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