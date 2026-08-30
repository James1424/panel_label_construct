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
| raw_rows           | 56213               |
| clean_rows         | 56213               |
| raw_columns        | 136                 |
| clean_columns      | 125                 |
| raw_tickers        | 451                 |
| clean_tickers      | 451                 |
| months             | 128                 |
| first_month        | 2016-01-31 00:00:00 |
| last_month         | 2026-08-31 00:00:00 |
| candidate_features | 109                 |
| kept_features      | 109                 |
| dropped_features   | 0                   |

## Tail-label summary
| label                   |   positive_rows |   valid_future_rows | positive_rate   |   months_with_positive |   avg_positives_per_month |   min_positives_per_month |   max_positives_per_month |
|:------------------------|----------------:|--------------------:|:----------------|-----------------------:|--------------------------:|--------------------------:|--------------------------:|
| label_top10_1_3m        |            5651 |               55762 | 10.13%          |                    127 |                   44.1484 |                         0 |                        46 |
| label_top5_1_3m         |            2870 |               55762 | 5.15%           |                    127 |                   22.4219 |                         0 |                        23 |
| label_boom30_top10_1_3m |            2340 |               55762 | 4.20%           |                    125 |                   18.2812 |                         0 |                        45 |
| label_boom40_top10_1_3m |            1171 |               55762 | 2.10%           |                    119 |                    9.1484 |                         0 |                        45 |
| label_boom50_top5_1_3m  |             640 |               55762 | 1.15%           |                    114 |                    5      |                         0 |                        23 |
| label_mega100_1_3m      |             122 |               55762 | 0.22%           |                     53 |                    0.9531 |                         0 |                         9 |

## Recent monthly label distribution
| month      |   rows |   tickers | future_max_return_1_3m_mean   | future_max_return_1_3m_p90   | future_max_return_1_3m_p95   | future_max_return_1_3m_max   |   label_top10_1_3m_count |   label_top5_1_3m_count |   label_boom30_top10_1_3m_count |   label_boom40_top10_1_3m_count |   label_boom50_top5_1_3m_count |   label_mega100_1_3m_count |
|:-----------|-------:|----------:|:------------------------------|:-----------------------------|:-----------------------------|:-----------------------------|-------------------------:|------------------------:|--------------------------------:|--------------------------------:|-------------------------------:|---------------------------:|
| 2025-03-31 |    448 |       448 | 8.14%                         | 26.11%                       | 36.23%                       | 194.45%                      |                       45 |                      23 |                              34 |                              20 |                             14 |                          1 |
| 2025-04-30 |    448 |       448 | 14.61%                        | 38.04%                       | 52.66%                       | 210.87%                      |                       45 |                      23 |                              45 |                              37 |                             23 |                          4 |
| 2025-05-31 |    448 |       448 | 12.82%                        | 29.42%                       | 38.29%                       | 248.51%                      |                       45 |                      23 |                              43 |                              20 |                             11 |                          4 |
| 2025-06-30 |    448 |       448 | 10.52%                        | 23.42%                       | 34.04%                       | 253.55%                      |                       45 |                      23 |                              28 |                              19 |                             15 |                          4 |
| 2025-07-31 |    448 |       448 | 10.58%                        | 20.90%                       | 30.83%                       | 364.42%                      |                       45 |                      23 |                              25 |                              16 |                             13 |                          6 |
| 2025-08-31 |    448 |       448 | 7.75%                         | 20.68%                       | 29.42%                       | 325.54%                      |                       45 |                      23 |                              22 |                              14 |                             12 |                          6 |
| 2025-09-30 |    448 |       448 | 5.58%                         | 20.40%                       | 27.40%                       | 126.53%                      |                       45 |                      23 |                              18 |                              10 |                              5 |                          2 |
| 2025-10-31 |    449 |       449 | 10.39%                        | 22.67%                       | 29.13%                       | 189.09%                      |                       45 |                      23 |                              20 |                              11 |                              8 |                          1 |
| 2025-11-30 |    449 |       449 | 13.23%                        | 30.10%                       | 42.66%                       | 184.56%                      |                       45 |                      23 |                              45 |                              28 |                             14 |                          3 |
| 2025-12-31 |    449 |       449 | 12.32%                        | 30.78%                       | 43.75%                       | 167.66%                      |                       45 |                      23 |                              45 |                              28 |                             21 |                          1 |
| 2026-01-31 |    449 |       449 | 9.74%                         | 26.88%                       | 43.51%                       | 130.28%                      |                       45 |                      23 |                              37 |                              28 |                             19 |                          3 |
| 2026-02-28 |    449 |       449 | 5.69%                         | 24.36%                       | 40.68%                       | 166.77%                      |                       45 |                      23 |                              32 |                              23 |                             17 |                          7 |
| 2026-03-31 |    449 |       449 | 15.28%                        | 37.73%                       | 52.06%                       | 257.88%                      |                       45 |                      23 |                              45 |                              42 |                             23 |                          7 |
| 2026-04-30 |    449 |       449 | 9.89%                         | 27.06%                       | 39.42%                       | 107.40%                      |                       45 |                      23 |                              36 |                              21 |                             12 |                          2 |
| 2026-05-31 |    450 |       450 | 10.84%                        | 24.48%                       | 29.60%                       | 192.41%                      |                       46 |                      23 |                              22 |                              13 |                              3 |                          1 |
| 2026-06-30 |    451 |       451 | 6.16%                         | 24.10%                       | 31.06%                       | 97.04%                       |                       46 |                      23 |                              26 |                               7 |                              5 |                          0 |
| 2026-07-31 |    451 |       451 | 2.27%                         | 12.61%                       | 16.62%                       | 151.71%                      |                       46 |                      23 |                               5 |                               1 |                              1 |                          1 |
| 2026-08-31 |    451 |       451 |                               |                              |                              |                              |                        0 |                       0 |                               0 |                               0 |                              0 |                          0 |

## Feature missingness report
A feature is dropped if `missing_rate > 35%` or `non_null_rows < 1000`.

### Highest-missing candidate features
| feature                       | feature_group     |   missing_count | missing_rate   |   non_null_rows | non_null_rate   | first_valid_month   | last_valid_month   | dropped   |   drop_reason |
|:------------------------------|:------------------|----------------:|:---------------|----------------:|:----------------|:--------------------|:-------------------|:----------|--------------:|
| up_day_volume_ratio_3m        | volume_flow       |             491 | 0.87%          |           55722 | 99.13%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| up_day_dollar_volume_ratio_3m | volume_flow       |             491 | 0.87%          |           55722 | 99.13%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| rel_mom_12m_vs_qqq            | relative_strength |             359 | 0.64%          |           55854 | 99.36%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_12m                       | other_momentum    |             359 | 0.64%          |           55854 | 99.36%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_9m                        | other_momentum    |             263 | 0.47%          |           55950 | 99.53%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| volume_change_3m              | volume_flow       |             227 | 0.40%          |           55986 | 99.60%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| dollar_volume_change_3m       | volume_flow       |             227 | 0.40%          |           55986 | 99.60%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_7m                        | other_momentum    |             201 | 0.36%          |           56012 | 99.64%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_6m                        | core_momentum     |             170 | 0.30%          |           56043 | 99.70%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_4m_vs_6m                  | core_momentum     |             170 | 0.30%          |           56043 | 99.70%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_5m_vs_6m                  | core_momentum     |             170 | 0.30%          |           56043 | 99.70%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_6m_first3m                | core_momentum     |             170 | 0.30%          |           56043 | 99.70%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_6m_acceleration           | core_momentum     |             170 | 0.30%          |           56043 | 99.70%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| ret_lag_6m                    | sequence_path     |             170 | 0.30%          |           56043 | 99.70%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| rel_mom_6m_vs_qqq             | relative_strength |             170 | 0.30%          |           56043 | 99.70%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_3m_vs_6m                  | other_momentum    |             170 | 0.30%          |           56043 | 99.70%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| return_vol_ratio_6m           | risk_drawdown     |             170 | 0.30%          |           56043 | 99.70%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| drawdown_12m                  | risk_drawdown     |             169 | 0.30%          |           56044 | 99.70%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| drawdown_12m_abs              | risk_drawdown     |             169 | 0.30%          |           56044 | 99.70%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| volume_change_1m              | volume_flow       |             164 | 0.29%          |           56049 | 99.71%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| dollar_volume_change_1m       | volume_flow       |             164 | 0.29%          |           56049 | 99.71%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| ma100_slope_1m                | trend             |             161 | 0.29%          |           56052 | 99.71%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| volume_ma3_to_12m             | volume_flow       |             147 | 0.26%          |           56066 | 99.74%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_5m                        | core_momentum     |             142 | 0.25%          |           56071 | 99.75%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| core_mom_456_std              | core_momentum     |             142 | 0.25%          |           56071 | 99.75%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| ret_lag_5m                    | sequence_path     |             142 | 0.25%          |           56071 | 99.75%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| price_ma100_ratio             | trend             |             135 | 0.24%          |           56078 | 99.76%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| drawdown_change_3m            | drawdown_recovery |             126 | 0.22%          |           56087 | 99.78%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| mom_4m                        | core_momentum     |             114 | 0.20%          |           56099 | 99.80%          | 2016-01-31          | 2026-08-31         | False     |           nan |
| core_mom_456_avg              | core_momentum     |             114 | 0.20%          |           56099 | 99.80%          | 2016-01-31          | 2026-08-31         | False     |           nan |

### Dropped high-missing features
_No features dropped by missingness filter._

## Committed first-20k panel slice
`outputs/panel_head_20000.csv` contains the first 20,000 rows of the cleaned panel. It is committed for quick inspection and future model-design reference; the full panel remains in the GitHub Actions artifact.
Columns in slice: 125

## Model-design panel sample
This small committed sample contains historical labeled rows and recent examples for model-design inspection. The full panel is uploaded as a GitHub Actions artifact.
| sample_source                     | month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_top10_1_3m |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |   label_mega100_1_3m |
|:----------------------------------|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|-------------------:|--------------------------:|-------------------------:|---------------------:|
| historical_mega100_examples       | 2016-01-31 | FCX      |     4.14292 | -60.92%  | -60.70%  | -56.55%            |            2.91478e+08 | 53.97%               | 11.90%                | 94.51%             | 204.35%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2016-01-31 | LEU      |     1.37    | -49.26%  | -65.23%  | -61.39%            |        74400.9         | 46.83%               | 10.32%                | 64.56%             | 229.20%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-01-31 | TRGP     |    14.1286  | -59.11%  | -73.14%  | -63.68%            |            3.67481e+07 | 43.65%               | 9.52%                 | 69.06%             | 84.40%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2016-02-29 | LEU      |     1.32    | -21.43%  | -65.17%  | -57.67%            |        58517.2         | 51.59%               | 11.11%                | 64.65%             | 241.67%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2016-02-29 | DVN      |    13.5148  | -56.94%  | -53.27%  | -50.87%            |            2.14737e+08 | 44.44%               | 7.14%                 | 89.26%             | 85.36%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-02-29 | FCX      |     6.87185 | -6.72%   | -28.01%  | -28.05%            |            3.03139e+08 | 57.14%               | 15.08%                | 94.47%             | 83.49%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-02-29 | OKE      |    12.7296  | -16.37%  | -30.26%  | -26.52%            |            5.35763e+07 | 42.86%               | 9.52%                 | 71.43%             | 83.25%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2016-08-31 | LEU      |     3.46    | 14.19%   | 162.12%  | 49.10%             |       150004           | 42.86%               | 11.90%                | 65.19%             | 88.15%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2017-01-31 | PLUG     |     1.06    | -30.72%  | -40.78%  | -36.80%            |            4.82764e+06 | 25.40%               | 3.97%                 | 64.43%             | 111.32%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2017-02-28 | PLUG     |     1.08    | -21.17%  | -30.32%  | -32.19%            |            7.26119e+06 | 32.54%               | 5.56%                 | 65.44%             | 107.41%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2017-04-30 | CVNA     |     2.22    |          |          |                    |                        |                      |                       | 0.00%              | 84.41%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2017-05-31 | CVNA     |     2.01    |          |          |                    |                        |                      |                       | 0.00%              | 103.68%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2017-08-31 | ENPH     |     0.92    | 21.05%   | -48.60%  | -34.71%            |       600677           | 44.44%               | 7.14%                 | 65.16%             | 215.22%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2017-09-30 | ENPH     |     1.52    | 74.71%   | 10.95%   | 46.23%             |       821362           | 43.65%               | 10.32%                | 65.26%             | 90.79%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-10-31 | ENPH     |     1.53    | 62.77%   | 28.57%   | 68.58%             |       845932           | 46.03%               | 11.90%                | 65.34%             | 89.54%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2017-12-31 | ENPH     |     2.41    | 58.55%   | 177.01%  | 165.12%            |            2.1306e+06  | 50.00%               | 15.08%                | 65.55%             | 89.63%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2018-01-31 | ENPH     |     2.2     | 43.79%   | 134.04%  | 105.97%            |            2.52291e+06 | 52.38%               | 16.67%                | 65.57%             | 107.73%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2018-03-31 | TKO      |    32.5899  | 18.14%   | 53.98%   | 39.32%             |            2.7319e+07  | 7.94%                | 1.59%                 | 58.23%             | 102.62%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-03-31 | TTD      |     4.962   | 8.51%    | -19.33%  | -14.36%            |            5.03591e+07 | 23.81%               | 3.17%                 | 68.40%             | 89.04%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-04-30 | TKO      |    36.0109  | 12.92%   | 51.03%   | 40.74%             |            2.86848e+07 | 7.14%                | 0.79%                 | 49.44%             | 99.21%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2018-05-31 | CVNA     |     5.77    | 43.96%   | 77.98%   | 60.00%             |            2.393e+07   | 38.89%               | 11.11%                | 66.42%             | 124.40%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2018-12-31 | ENPH     |     4.73    | -2.47%   | -29.72%  | -17.83%            |            8.59184e+06 | 44.44%               | 9.52%                 | 65.00%             | 95.14%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | LEU      |     1.69    | -37.17%  | -50.87%  | -40.69%            |        57707           | 47.62%               | 11.90%                | 65.10%             | 84.02%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2018-12-31 | PLUG     |     1.24    | -35.42%  | -38.61%  | -37.89%            |            4.00456e+06 | 20.63%               | 3.17%                 | 62.48%             | 93.55%                   |                  1 |                         1 |                        1 |                    0 |
| yearly_top_future_return_examples | 2019-03-31 | ENPH     |     9.23    | 95.14%   | 90.31%   | 88.18%             |            1.57355e+07 | 40.48%               | 11.11%                | 65.18%             | 97.51%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2019-04-30 | ENPH     |    10.04    | 38.87%   | 121.15%  | 106.44%            |            1.86016e+07 | 39.68%               | 11.11%                | 65.26%             | 180.38%                  |                  1 |                         1 |                        1 |                    1 |
| yearly_top_future_return_examples | 2019-05-31 | ENPH     |    15.17    | 67.25%   | 180.93%  | 170.49%            |            3.08737e+07 | 39.68%               | 10.32%                | 66.27%             | 95.58%                   |                  1 |                         1 |                        1 |                    0 |
| historical_mega100_examples       | 2019-09-30 | BE       |     3.25    | -73.51%  | -74.85%  | -73.63%            |            1.35115e+07 | 44.44%               | 9.52%                 | 65.37%             | 129.85%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | BE       |     3.06    | -70.72%  | -77.53%  | -74.75%            |            1.11875e+07 | 43.65%               | 8.73%                 | 65.31%             | 157.52%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-10-31 | PCG      |     6.0642  | -65.97%  | -72.60%  | -69.87%            |            1.31638e+08 | 50.00%               | 12.70%                | 82.61%             | 146.52%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-11-30 | ENPH     |    21.87    | -26.29%  | 44.17%   | 13.94%             |            1.27686e+08 | 43.65%               | 11.90%                | 81.39%             | 123.91%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2019-11-30 | PCG      |     7.33208 | -28.61%  | -56.37%  | -60.89%            |            1.33872e+08 | 52.38%               | 16.67%                | 82.50%             | 107.77%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-01-31 | EQT      |     5.60139 | -43.51%  | -59.75%  | -47.69%            |            5.78453e+07 | 39.68%               | 7.14%                 | 68.38%             | 142.54%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-01-31 | MRNA     |    20.51    | 22.45%   | 56.56%   | 38.59%             |            4.69805e+07 | 30.16%               | 7.94%                 | 66.24%             | 124.23%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-02-29 | EQT      |     5.46579 | -32.38%  | -41.79%  | -43.68%            |            5.55426e+07 | 42.86%               | 8.73%                 | 67.49%             | 148.55%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-02-29 | MRNA     |    25.93    | 27.36%   | 64.84%   | 60.84%             |            1.65444e+08 | 30.16%               | 8.73%                 | 83.16%             | 137.18%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | APA      |     3.55084 | -83.54%  | -83.36%  | -81.67%            |            1.30037e+08 | 31.75%               | 6.35%                 | 74.10%             | 223.92%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | BE       |     5.23    | -29.99%  | 60.92%   | 37.35%             |            3.02464e+07 | 56.35%               | 19.84%                | 65.87%             | 108.03%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | CVNA     |    11.018   | -40.15%  | -16.53%  | -30.26%            |            1.95395e+08 | 42.06%               | 11.11%                | 82.20%             | 118.19%                  |                  1 |                         1 |                        1 |                    1 |
| historical_mega100_examples       | 2020-03-31 | EQT      |     6.58316 | -34.77%  | -32.99%  | -28.38%            |            6.99179e+07 | 46.03%               | 10.32%                | 67.10%             | 106.36%                  |                  1 |                         1 |                        1 |                    1 |

## Latest clean panel sample
| month      | ticker   |   adj_close | mom_3m   | mom_6m   | core_mom_456_avg   |   avg_dollar_volume_3m | large_move_freq_6m   | up_big_move_freq_6m   | liquid_vol_score   | future_max_return_1_3m   |   label_boom30_top10_1_3m |   label_boom50_top5_1_3m |
|:-----------|:---------|------------:|:---------|:---------|:-------------------|-----------------------:|:---------------------|:----------------------|:-------------------|:-------------------------|--------------------------:|-------------------------:|
| 2026-08-31 | AMCR     |       46.67 | 20.22%   | -2.03%   | 14.02%             |            158,400,550 | 15.08%               | 1.59%                 | 44.41%             |                          |                         0 |                        0 |
| 2026-08-31 | AME      |      236.25 | 4.76%    | -0.94%   | 3.30%              |            289,325,933 | 6.35%                | 0.79%                 | 32.90%             |                          |                         0 |                        0 |
| 2026-08-31 | AMGN     |      432.42 | 29.14%   | 12.90%   | 21.34%             |          1,005,883,326 | 7.14%                | 0.00%                 | 46.35%             |                          |                         0 |                        0 |
| 2026-08-31 | AMP      |      559.32 | 25.88%   | 19.78%   | 21.70%             |            294,900,023 | 4.76%                | 0.00%                 | 24.95%             |                          |                         0 |                        0 |
| 2026-08-31 | AMT      |      176.23 | -4.84%   | -6.34%   | -1.62%             |            525,137,859 | 9.52%                | 0.79%                 | 49.11%             |                          |                         0 |                        0 |
| 2026-08-31 | AON      |      355.4  | 12.70%   | 6.46%    | 10.57%             |            470,514,151 | 8.73%                | 0.00%                 | 39.96%             |                          |                         0 |                        0 |
| 2026-08-31 | AOS      |       60.38 | 7.10%    | -21.68%  | -10.27%            |            101,448,884 | 11.90%               | 0.00%                 | 25.45%             |                          |                         0 |                        0 |
| 2026-08-31 | APA      |       42.54 | 17.59%   | 42.00%   | 16.27%             |            203,435,893 | 30.95%               | 3.17%                 | 61.63%             |                          |                         0 |                        0 |
| 2026-08-31 | APD      |      308.09 | 11.26%   | 13.16%   | 7.95%              |            363,495,148 | 3.17%                | 1.59%                 | 35.77%             |                          |                         0 |                        0 |
| 2026-08-31 | APH      |      157.74 | 6.20%    | 8.37%    | 13.56%             |          1,193,345,822 | 31.75%               | 6.35%                 | 89.06%             |                          |                         0 |                        0 |
| 2026-08-31 | APO      |      135.04 | 5.36%    | 30.19%   | 19.40%             |            511,721,827 | 19.84%               | 3.17%                 | 69.88%             |                          |                         0 |                        0 |
| 2026-08-31 | APTV     |       45.75 | -32.66%  | -37.79%  | -31.99%            |            207,605,765 | 24.60%               | 3.97%                 | 62.67%             |                          |                         0 |                        0 |
| 2026-08-31 | ARE      |       51.57 | 5.17%    | -1.79%   | 13.24%             |            100,400,021 | 24.60%               | 3.97%                 | 54.98%             |                          |                         0 |                        0 |
| 2026-08-31 | ARES     |      142.53 | 12.04%   | 30.28%   | 28.29%             |            298,026,290 | 27.78%               | 6.35%                 | 69.33%             |                          |                         0 |                        0 |
| 2026-08-31 | ATO      |      166.65 | -0.87%   | -9.74%   | -9.90%             |            209,851,807 | 0.00%                | 0.00%                 | 11.36%             |                          |                         0 |                        0 |
| 2026-08-31 | AVY      |      177.75 | 12.46%   | -8.44%   | 1.43%              |            128,630,956 | 8.73%                | 0.00%                 | 20.05%             |                          |                         0 |                        0 |
| 2026-08-31 | AWK      |      138.3  | 12.94%   | 3.08%    | 5.10%              |            300,950,391 | 3.17%                | 0.00%                 | 22.95%             |                          |                         0 |                        0 |
| 2026-08-31 | AXON     |      600.73 | 33.88%   | 10.75%   | 33.91%             |            529,671,981 | 40.48%               | 13.49%                | 85.74%             |                          |                         0 |                        0 |
| 2026-08-31 | AXP      |      333.2  | 5.57%    | 8.50%    | 7.58%              |            976,338,052 | 7.14%                | 0.00%                 | 44.25%             |                          |                         0 |                        0 |
| 2026-08-31 | AZO      |     2961.96 | 0.91%    | -21.13%  | -17.83%            |            987,008,297 | 11.11%               | 0.79%                 | 62.55%             |                          |                         0 |                        0 |
| 2026-08-31 | BA       |      209.82 | -9.23%   | -7.78%   | -3.58%             |          1,271,700,418 | 19.05%               | 3.17%                 | 79.17%             |                          |                         0 |                        0 |
| 2026-08-31 | BAC      |       62.32 | 21.40%   | 26.43%   | 24.03%             |          1,981,400,953 | 2.38%                | 0.00%                 | 39.51%             |                          |                         0 |                        0 |
| 2026-08-31 | BALL     |       63.77 | 17.07%   | -4.37%   | 2.90%              |            141,336,299 | 7.94%                | 0.00%                 | 19.66%             |                          |                         0 |                        0 |
| 2026-08-31 | BAX      |       26.13 | 39.19%   | 28.39%   | 44.28%             |            156,507,017 | 28.57%               | 3.17%                 | 56.34%             |                          |                         0 |                        0 |
| 2026-08-31 | BBY      |       82.44 | 7.17%    | 36.85%   | 35.03%             |            307,343,880 | 15.08%               | 1.59%                 | 57.09%             |                          |                         0 |                        0 |
| 2026-08-31 | BDX      |      189.52 | 29.73%   | 8.84%    | 19.43%             |            344,805,789 | 7.94%                | 0.79%                 | 39.01%             |                          |                         0 |                        0 |
| 2026-08-31 | BE       |      210.77 | -26.05%  | 35.40%   | 21.78%             |          3,478,462,750 | 57.94%               | 21.43%                | 99.11%             |                          |                         0 |                        0 |
| 2026-08-31 | BEN      |       34.65 | 12.82%   | 33.80%   | 32.91%             |            143,531,995 | 8.73%                | 1.59%                 | 33.07%             |                          |                         0 |                        0 |
| 2026-08-31 | BF-B     |       27.22 | 6.75%    | -3.98%   | 2.14%              |             69,193,041 | 20.63%               | 4.76%                 | 53.40%             |                          |                         0 |                        0 |
| 2026-08-31 | BG       |      115.48 | -5.75%   | -3.10%   | -6.40%             |            176,249,872 | 11.11%               | 0.79%                 | 35.95%             |                          |                         0 |                        0 |

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