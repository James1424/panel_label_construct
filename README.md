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
| raw_rows           | 51391               |
| clean_rows         | 51391               |
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
| label_top10_1_3m        |            5171 |               50967 | 10.15%          |                    125 |                   41.0397 |                         0 |                        43 |
| label_top5_1_3m         |            2614 |               50967 | 5.13%           |                    125 |                   20.746  |                         0 |                        22 |
| label_boom30_top10_1_3m |            2513 |               50967 | 4.93%           |                    124 |                   19.9444 |                         0 |                        43 |
| label_boom40_top10_1_3m |            1353 |               50967 | 2.65%           |                    122 |                   10.7381 |                         0 |                        43 |
| label_boom50_top5_1_3m  |             749 |               50967 | 1.47%           |                    117 |                    5.9444 |                         0 |                        22 |
| label_mega100_1_3m      |             150 |               50967 | 0.29%           |                     53 |                    1.1905 |                         0 |                        13 |

## Recent monthly label distribution
| month      |   rows |   tickers | future_max_return_1_3m_mean   | future_max_return_1_3m_p90   | future_max_return_1_3m_p95   | future_max_return_1_3m_max   |   label_top10_1_3m_count |   label_top5_1_3m_count |   label_boom30_top10_1_3m_count |   label_boom40_top10_1_3m_count |   label_boom50_top5_1_3m_count |   label_mega100_1_3m_count |
|:-----------|-------:|----------:|:------------------------------|:-----------------------------|:-----------------------------|:-----------------------------|-------------------------:|------------------------:|--------------------------------:|--------------------------------:|-------------------------------:|---------------------------:|
| 2025-01-31 |    421 |       421 | 1.60%                         | 13.78%                       | 17.73%                       | 45.37%                       |                       43 |                      22 |                               4 |                               2 |                              0 |                          0 |
| 2025-02-28 |    421 |       421 | 2.97%                         | 15.47%                       | 22.59%                       | 55.18%                       |                       43 |                      22 |                              14 |                               8 |                              2 |                          0 |
| 2025-03-31 |    421 |       421 | 10.63%                        | 33.50%                       | 48.32%                       | 194.45%                      |                       43 |                      22 |                              43 |                              31 |                             20 |                          3 |
| 2025-04-30 |    421 |       421 | 16.43%                        | 40.17%                       | 55.89%                       | 210.87%                      |                       43 |                      22 |                              43 |                              43 |                             22 |                          5 |
| 2025-05-31 |    421 |       421 | 12.78%                        | 29.87%                       | 39.66%                       | 136.40%                      |                       43 |                      22 |                              42 |                              21 |                             14 |                          2 |
| 2025-06-30 |    421 |       421 | 9.94%                         | 24.84%                       | 35.95%                       | 166.96%                      |                       43 |                      22 |                              30 |                              16 |                             11 |                          3 |
| 2025-07-31 |    421 |       421 | 10.39%                        | 25.37%                       | 41.43%                       | 125.63%                      |                       43 |                      22 |                              34 |                              22 |                             13 |                          4 |
| 2025-08-31 |    421 |       421 | 8.20%                         | 25.48%                       | 38.15%                       | 117.31%                      |                       43 |                      22 |                              30 |                              18 |                             14 |                          1 |
| 2025-09-30 |    421 |       421 | 5.78%                         | 20.89%                       | 28.05%                       | 71.34%                       |                       43 |                      22 |                              17 |                               7 |                              4 |                          0 |
| 2025-10-31 |    422 |       422 | 8.80%                         | 22.90%                       | 29.36%                       | 85.48%                       |                       43 |                      22 |                              20 |                               7 |                              3 |                          0 |
| 2025-11-30 |    422 |       422 | 12.33%                        | 29.81%                       | 42.73%                       | 90.01%                       |                       43 |                      22 |                              41 |                              25 |                             12 |                          0 |
| 2025-12-31 |    422 |       422 | 11.46%                        | 31.88%                       | 42.10%                       | 88.31%                       |                       43 |                      22 |                              43 |                              24 |                             16 |                          0 |
| 2026-01-31 |    422 |       422 | 9.62%                         | 27.16%                       | 43.84%                       | 109.52%                      |                       43 |                      22 |                              35 |                              28 |                             15 |                          3 |
| 2026-02-28 |    422 |       422 | 8.86%                         | 28.71%                       | 55.41%                       | 188.52%                      |                       43 |                      22 |                              39 |                              32 |                             22 |                         13 |
| 2026-03-31 |    422 |       422 | 18.73%                        | 45.15%                       | 80.56%                       | 263.14%                      |                       43 |                      22 |                              43 |                              43 |                             22 |                         13 |
| 2026-04-30 |    422 |       422 | 9.10%                         | 29.47%                       | 47.95%                       | 205.42%                      |                       43 |                      22 |                              41 |                              26 |                             21 |                          5 |
| 2026-05-31 |    423 |       423 | 1.58%                         | 12.92%                       | 16.06%                       | 184.59%                      |                       43 |                      22 |                               5 |                               2 |                              1 |                          1 |
| 2026-06-30 |    424 |       424 |                               |                              |                              |                              |                        0 |                       0 |                               0 |                               0 |                              0 |                          0 |

## Feature missingness report
A feature is dropped if `missing_rate > 35%` or `non_null_rows < 1000`.

### Highest-missing candidate features
| feature                       | feature_group     |   missing_count | missing_rate   |   non_null_rows | non_null_rate   | first_valid_month   | last_valid_month   | dropped   |   drop_reason |
|:------------------------------|:------------------|----------------:|:---------------|----------------:|:----------------|:--------------------|:-------------------|:----------|--------------:|
| rel_mom_12m_vs_qqq            | relative_strength |             447 | 0.87%          |           50944 | 99.13%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_12m                       | other_momentum    |             447 | 0.87%          |           50944 | 99.13%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| up_day_volume_ratio_3m        | volume_flow       |             380 | 0.74%          |           51011 | 99.26%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| up_day_dollar_volume_ratio_3m | volume_flow       |             380 | 0.74%          |           51011 | 99.26%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_9m                        | other_momentum    |             332 | 0.65%          |           51059 | 99.35%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_7m                        | other_momentum    |             257 | 0.50%          |           51134 | 99.50%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_6m                        | core_momentum     |             220 | 0.43%          |           51171 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_4m_vs_6m                  | core_momentum     |             220 | 0.43%          |           51171 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_5m_vs_6m                  | core_momentum     |             220 | 0.43%          |           51171 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_6m_first3m                | core_momentum     |             220 | 0.43%          |           51171 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_6m_acceleration           | core_momentum     |             220 | 0.43%          |           51171 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| ret_lag_6m                    | sequence_path     |             220 | 0.43%          |           51171 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| rel_mom_6m_vs_qqq             | relative_strength |             220 | 0.43%          |           51171 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_3m_vs_6m                  | other_momentum    |             220 | 0.43%          |           51171 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| return_vol_ratio_6m           | risk_drawdown     |             220 | 0.43%          |           51171 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| drawdown_12m                  | risk_drawdown     |             219 | 0.43%          |           51172 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| drawdown_12m_abs              | risk_drawdown     |             219 | 0.43%          |           51172 | 99.57%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| ma100_slope_1m                | trend             |             211 | 0.41%          |           51180 | 99.59%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_5m                        | core_momentum     |             183 | 0.36%          |           51208 | 99.64%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| core_mom_456_std              | core_momentum     |             183 | 0.36%          |           51208 | 99.64%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| ret_lag_5m                    | sequence_path     |             183 | 0.36%          |           51208 | 99.64%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| volume_ma3_to_12m             | volume_flow       |             183 | 0.36%          |           51208 | 99.64%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| price_ma100_ratio             | trend             |             175 | 0.34%          |           51216 | 99.66%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| volume_change_3m              | volume_flow       |             172 | 0.33%          |           51219 | 99.67%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| dollar_volume_change_3m       | volume_flow       |             172 | 0.33%          |           51219 | 99.67%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| drawdown_change_3m            | drawdown_recovery |             161 | 0.31%          |           51230 | 99.69%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| mom_4m                        | core_momentum     |             146 | 0.28%          |           51245 | 99.72%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| core_mom_456_avg              | core_momentum     |             146 | 0.28%          |           51245 | 99.72%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| core_mom_456_min              | core_momentum     |             146 | 0.28%          |           51245 | 99.72%          | 2016-01-31          | 2026-06-30         | False     |           nan |
| core_mom_456_max              | core_momentum     |             146 | 0.28%          |           51245 | 99.72%          | 2016-01-31          | 2026-06-30         | False     |           nan |

### Dropped high-missing features
_No features dropped by missingness filter._

## Committed first-20k panel slice
`outputs/panel_head_20000.csv` contains the first 20,000 rows of the cleaned panel. It is committed for quick inspection and future model-design reference; the full panel remains in the GitHub Actions artifact.
Columns in slice: 126

## Model-design panel sample
This small committed sample contains historical labeled rows and recent examples for model-design inspection. The full panel is uploaded as a GitHub Actions artifact.
| sample_source                     | month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_top10_1_3m |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |   label_mega100_1_3m |
|:----------------------------------|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|-------------------:|--------------------------:|-------------------------:|---------------------:|
| historical_mega100_examples       | 2016-01-31 | FCX      |     4.15298 | -60.92%  | -60.70%  | -56.55%            |            2.92186e+08 | 53.97%               | 11.90%                | 93.64%             | 204.35%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2016-01-31 | LEU      |     1.37    | -49.26%  | -65.23%  | -61.39%            |        74400.9         | 46.83%               | 10.32%                | 64.39%             | 229.20%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-01-31 | TRGP     |    14.1947  | -59.11%  | -73.14%  | -63.68%            |            3.69201e+07 | 43.65%               | 9.52%                 | 69.22%             | 84.40%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2016-02-29 | AMD      |     2.14    | -9.32%   | 18.23%   | 14.53%             |            3.01533e+07 | 40.48%               | 7.94%                 | 66.56%             | 113.55%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2016-02-29 | LEU      |     1.32    | -21.43%  | -65.17%  | -57.67%            |        58517.2         | 51.59%               | 11.11%                | 64.43%             | 241.67%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-02-29 | DVN      |    13.5148  | -56.94%  | -53.27%  | -50.87%            |            2.14737e+08 | 44.44%               | 7.14%                 | 88.41%             | 85.36%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-04-30 | AMD      |     3.55    | 61.36%   | 67.45%   | 47.19%             |            4.55973e+07 | 46.83%               | 12.70%                | 70.66%             | 93.24%                   |                  1 |                         1 |                        1 |                    0 |
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
| yearly_top_future_return_examples | 2018-03-31 | TKO      |    32.5899  | 18.14%   | 53.98%   | 39.32%             |            2.7319e+07  | 7.94%                | 1.59%                 | 57.34%             | 102.62%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-04-30 | TKO      |    36.0109  | 12.92%   | 51.03%   | 40.74%             |            2.86848e+07 | 7.14%                | 0.79%                 | 48.47%             | 99.21%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2018-05-31 | CVNA     |     5.77    | 43.96%   | 77.98%   | 60.00%             |            2.393e+07   | 38.89%               | 11.11%                | 66.25%             | 124.40%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-06-30 | AMD      |    14.99    | 49.15%   | 45.82%   | 26.23%             |            7.8752e+08  | 28.57%               | 3.97%                 | 96.65%             | 106.07%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-12-31 | ENPH     |     4.73    | -2.47%   | -29.72%  | -17.83%            |            8.59184e+06 | 44.44%               | 9.52%                 | 64.80%             | 95.14%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | LEU      |     1.69    | -37.17%  | -50.87%  | -40.69%            |        57707           | 47.62%               | 11.90%                | 65.05%             | 84.02%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | PLUG     |     1.24    | -35.42%  | -38.61%  | -37.89%            |            4.00456e+06 | 20.63%               | 3.17%                 | 61.34%             | 93.55%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2019-03-31 | ENPH     |     9.23    | 95.14%   | 90.31%   | 88.18%             |            1.57355e+07 | 40.48%               | 11.11%                | 64.53%             | 97.51%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2019-04-30 | ENPH     |    10.04    | 38.87%   | 121.15%  | 106.44%            |            1.86016e+07 | 39.68%               | 11.11%                | 64.92%             | 180.38%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-05-31 | ENPH     |    15.17    | 67.25%   | 180.93%  | 170.49%            |            3.08737e+07 | 39.68%               | 10.32%                | 66.18%             | 95.58%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2019-10-31 | PCG      |     6.08184 | -65.97%  | -72.60%  | -69.87%            |            1.32021e+08 | 50.00%               | 12.70%                | 81.48%             | 146.52%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | TSLA     |    20.9947  | 30.34%   | 31.94%   | 47.65%             |            1.94498e+09 | 23.02%               | 3.17%                 | 97.16%             | 106.58%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-11-30 | ENPH     |    21.87    | -26.29%  | 44.17%   | 13.94%             |            1.27686e+08 | 43.65%               | 11.90%                | 80.00%             | 123.91%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-11-30 | PCG      |     7.3534  | -28.61%  | -56.37%  | -60.89%            |            1.34261e+08 | 52.38%               | 16.67%                | 81.24%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-11-30 | TSLA     |    21.996   | 46.24%   | 78.19%   | 54.13%             |            2.36702e+09 | 19.84%               | 3.17%                 | 96.63%             | 102.46%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-01-31 | EQT      |     5.61896 | -43.51%  | -59.75%  | -47.69%            |            5.80267e+07 | 39.68%               | 7.14%                 | 68.24%             | 142.54%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-02-29 | EQT      |     5.48294 | -32.38%  | -41.79%  | -43.68%            |            5.57168e+07 | 42.86%               | 8.73%                 | 67.55%             | 148.55%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | CVNA     |    11.018   | -40.15%  | -16.53%  | -30.26%            |            1.95395e+08 | 42.06%               | 11.11%                | 81.53%             | 118.19%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | DDOG     |    35.98    | -4.76%   | 6.10%    | 0.49%              |            1.42601e+08 | 42.86%               | 11.90%                | 75.45%             | 141.66%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | PLUG     |     3.54    | 12.03%   | 34.60%   | 19.65%             |            7.59733e+07 | 46.83%               | 15.87%                | 68.17%             | 131.92%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | SHOP     |    41.693   | 4.87%    | 33.78%   | 30.18%             |            1.16644e+09 | 33.33%               | 9.52%                 | 91.77%             | 127.66%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | TRGP     |     6.07095 | -82.66%  | -81.97%  | -81.46%            |            7.3025e+07  | 21.43%               | 5.56%                 | 60.84%             | 192.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-04-30 | DDOG     |    45.12    | -2.36%   | 34.33%   | 21.47%             |            1.4381e+08  | 33.33%               | 6.35%                 | 60.00%             | 108.02%                  |                  1 |                         1 |                        1 |                    1 |

## Latest clean panel sample
| month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |
|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|--------------------------:|-------------------------:|
| 2026-06-30 | AAPL     |      275.15 | 8.52%    | 1.40%    | 3.96%              |         13,903,495,810 | 6.35%                | 0.00%                 | 48.60%             |                          |                         0 |                        0 |
| 2026-06-30 | ABNB     |      141.88 | 12.35%   | 4.54%    | 6.41%              |            506,194,255 | 12.70%               | 2.38%                 | 58.01%             |                          |                         0 |                        0 |
| 2026-06-30 | ADBE     |      193.41 | -20.43%  | -44.74%  | -35.03%            |          1,421,129,217 | 19.84%               | 2.38%                 | 76.69%             |                          |                         0 |                        0 |
| 2026-06-30 | ADI      |      417.93 | 31.73%   | 55.01%   | 36.13%             |          1,688,169,793 | 19.84%               | 3.97%                 | 78.14%             |                          |                         0 |                        0 |
| 2026-06-30 | ADP      |      216.31 | 7.27%    | -14.57%  | -7.67%             |            614,957,293 | 9.52%                | 1.59%                 | 53.20%             |                          |                         0 |                        0 |
| 2026-06-30 | AEP      |      137    | 5.28%    | 20.62%   | 13.29%             |            550,554,451 | 2.38%                | 0.00%                 | 28.72%             |                          |                         0 |                        0 |
| 2026-06-30 | AKAM     |      112.89 | -1.71%   | 29.39%   | 20.11%             |            687,744,791 | 33.33%               | 4.76%                 | 83.09%             |                          |                         0 |                        0 |
| 2026-06-30 | ALAB     |      398    | 263.14%  | 139.24%  | 179.47%            |          1,565,552,781 | 55.56%               | 21.43%                | 95.00%             |                          |                         0 |                        0 |
| 2026-06-30 | ALGN     |      175.71 | 2.50%    | 12.53%   | 4.24%              |            177,291,002 | 26.19%               | 3.97%                 | 55.73%             |                          |                         0 |                        0 |
| 2026-06-30 | AMAT     |      668    | 95.68%   | 160.58%  | 116.00%            |          3,682,602,440 | 37.30%               | 10.32%                | 94.09%             |                          |                         0 |                        0 |
| 2026-06-30 | AMD      |      532.57 | 161.80%  | 148.68%  | 146.55%            |         14,309,816,907 | 45.24%               | 14.29%                | 96.50%             |                          |                         0 |                        0 |
| 2026-06-30 | AMZN     |      227.01 | 9.00%    | -1.65%   | 0.44%              |         11,598,949,001 | 13.49%               | 0.79%                 | 65.49%             |                          |                         0 |                        0 |
| 2026-06-30 | ANET     |      165.45 | 34.75%   | 26.27%   | 22.31%             |          1,428,492,373 | 40.48%               | 8.73%                 | 90.11%             |                          |                         0 |                        0 |
| 2026-06-30 | APP      |      445.93 | 12.04%   | -33.82%  | -12.33%            |          2,345,173,299 | 46.03%               | 14.29%                | 94.48%             |                          |                         0 |                        0 |
| 2026-06-30 | ARM      |      347.71 | 129.85%  | 218.10%  | 206.98%            |          3,092,647,872 | 42.86%               | 16.67%                | 96.40%             |                          |                         0 |                        0 |
| 2026-06-30 | ASML     |     1841.18 | 39.70%   | 72.70%   | 43.25%             |          2,954,243,336 | 30.16%               | 7.94%                 | 90.04%             |                          |                         0 |                        0 |
| 2026-06-30 | AVGO     |      378.91 | 22.62%   | 9.88%    | 14.56%             |         10,329,953,507 | 29.37%               | 3.97%                 | 87.23%             |                          |                         0 |                        0 |
| 2026-06-30 | AXON     |      444.73 | 4.72%    | -21.69%  | -15.91%            |            483,192,498 | 33.33%               | 10.32%                | 80.79%             |                          |                         0 |                        0 |
| 2026-06-30 | BEN      |       32.65 | 38.23%   | 38.67%   | 29.31%             |            142,361,326 | 11.11%               | 1.59%                 | 35.37%             |                          |                         0 |                        0 |
| 2026-06-30 | BF-B     |       27.68 | 5.60%    | 8.13%    | 2.91%              |            122,418,525 | 18.25%               | 3.17%                 | 48.98%             |                          |                         0 |                        0 |
| 2026-06-30 | BG       |      111.55 | -11.78%  | 26.70%   | 6.27%              |            208,122,761 | 10.32%               | 1.59%                 | 37.45%             |                          |                         0 |                        0 |
| 2026-06-30 | BIIB     |      201.96 | 10.16%   | 14.76%   | 10.77%             |            227,133,698 | 11.90%               | 1.59%                 | 44.66%             |                          |                         0 |                        0 |
| 2026-06-30 | BKNG     |      177.05 | 5.39%    | -16.95%  | -7.71%             |          1,336,054,161 | 17.46%               | 3.97%                 | 76.84%             |                          |                         0 |                        0 |
| 2026-06-30 | BKR      |       56.94 | -6.42%   | 25.92%   | 5.27%              |            516,267,304 | 19.05%               | 1.59%                 | 62.24%             |                          |                         0 |                        0 |
| 2026-06-30 | BLDR     |       88.72 | 7.76%    | -13.77%  | -17.05%            |            202,721,574 | 36.51%               | 7.94%                 | 65.37%             |                          |                         0 |                        0 |
| 2026-06-30 | BLK      |      971.92 | 1.63%    | -8.18%   | -9.30%             |            736,837,480 | 10.32%               | 0.79%                 | 52.44%             |                          |                         0 |                        0 |
| 2026-06-30 | BMY      |       55.39 | -7.73%   | 4.97%    | -1.22%             |            645,555,620 | 5.56%                | 0.79%                 | 42.91%             |                          |                         0 |                        0 |
| 2026-06-30 | BNY      |      145.43 | 23.08%   | 26.33%   | 23.56%             |            503,320,250 | 3.97%                | 0.00%                 | 30.69%             |                          |                         0 |                        0 |
| 2026-06-30 | BR       |      136.26 | -15.57%  | -38.19%  | -31.33%            |            231,060,106 | 14.29%               | 0.00%                 | 35.56%             |                          |                         0 |                        0 |
| 2026-06-30 | BRK-B    |      487.81 | 1.80%    | -2.95%   | -1.61%             |          2,415,828,122 | 0.79%                | 0.00%                 | 35.96%             |                          |                         0 |                        0 |

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